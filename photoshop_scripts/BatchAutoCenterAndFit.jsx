/**
 * BatchAutoCenterAndFit.jsx - Tự động căn giữa & canh chỉnh cỡ chữ hàng loạt (AI/CV Layout Engine)
 * Tối ưu hóa đặc biệt cho Webtoon/Manhwa dài (trang 15,000px - 40,000px+, 30-80 layer text).
 * Phím tắt đề xuất: F8
 */

#target photoshop

function main() {
    if (app.documents.length === 0) {
        alert("Chưa mở file PSD nào!");
        return;
    }

    var doc = app.activeDocument;
    var origDialogMode = app.displayDialogs;
    app.displayDialogs = DialogModes.NO;

    try {
        // 1. Tìm Layer 'raw' và 'Group 1'
        var rawLayer = findRawLayer(doc);
        var group1 = findLayer(doc, "Group 1");

        // 2. LẤY TẤT CẢ CÁC TEXT LAYER ĐƯỢC CHỌN (MULTI-SELECTION)
        var targetTextLayers = getSelectedTextLayers(doc, group1);

        if (targetTextLayers.length === 0) {
            alert("Vui lòng giữ phím Ctrl click chọn các Text Layer (hoặc chọn thư mục Group 1) trước khi bấm F8!");
            return;
        }

        // 3. Đường dẫn thư mục script
        var scriptFolder = ($.global.AI_TYPESET_DIR) ? new Folder($.global.AI_TYPESET_DIR).fsName : new File($.fileName).parent.fsName;
        var pyPath = scriptFolder + "\\layout_analyzer.py";
        var inputPath = scriptFolder + "\\layout_inputs.json";
        var resultPath = scriptFolder + "\\layout_results.json";

        if (!File(pyPath).exists) {
            alert("Không tìm thấy layout_analyzer.py tại:\n" + scriptFolder + "\nHãy kiểm tra lại thư mục photoshop_scripts.");
            return;
        }

        // Dọn dẹp các file crop cũ
        cleanOldLayoutFiles(scriptFolder);

        // 4. TẠM ẨN GROUP 1 & LAYER CLEAN, BẬT LAYER RAW ĐỂ CHỤP VÙNG THOẠI GỐC
        var prevRawVisible = rawLayer ? rawLayer.visible : true;
        var prevGroup1Visible = group1 ? group1.visible : true;

        var hiddenCleanLayers = [];
        var cleanKeywords = ["clean", "redraw", "xóa chữ", "sửa nền", "paint", "retouch"];
        for (var i = 0; i < doc.layers.length; i++) {
            var lyr = doc.layers[i];
            if (lyr !== rawLayer && lyr !== group1 && lyr.visible) {
                var lName = lyr.name.toLowerCase();
                for (var k = 0; k < cleanKeywords.length; k++) {
                    if (lName.indexOf(cleanKeywords[k]) !== -1) {
                        lyr.visible = false;
                        hiddenCleanLayers.push(lyr);
                        break;
                    }
                }
            }
        }

        if (group1) group1.visible = false;
        if (rawLayer) {
            rawLayer.visible = true;
            doc.activeLayer = rawLayer;
        }
        app.refresh();

        var docW = doc.width.as('px');
        var docH = doc.height.as('px');

        var inputItems = [];

        // Cấu hình lưu PNG siêu tốc (không nén, không interlaced để ghi đĩa tức thì)
        var pngSaveOpts = new PNGSaveOptions();
        pngSaveOpts.compression = 0;
        pngSaveOpts.interlaced = false;

        // 5. CẮT ẢNH VÙNG THOẠI RAW XUNG QUANH TỪNG TEXT LAYER (TỐI ƯU CHO TRANG DÀI)
        for (var i = 0; i < targetTextLayers.length; i++) {
            var lyr = targetTextLayers[i];
            var b = lyr.bounds;
            var lx1 = b[0].as('px');
            var ly1 = b[1].as('px');
            var lx2 = b[2].as('px');
            var ly2 = b[3].as('px');
            var lw = lx2 - lx1;
            var lh = ly2 - ly1;

            // Mở rộng viền xung quanh để chụp trọn vẹn 100% bóng thoại (tránh bị cắt cụt đầu/đáy)
            var padX = Math.round(Math.max(lw * 0.6, 120));
            var padY = Math.round(Math.max(lh * 1.2, 160));
            if (padX > 280) padX = 280;
            if (padY > 300) padY = 300;

            var cropX1 = Math.max(0, lx1 - padX);
            var cropY1 = Math.max(0, ly1 - padY);
            var cropX2 = Math.min(docW, lx2 + padX);
            var cropY2 = Math.min(docH, ly2 + padY);

            var cw = Math.round(cropX2 - cropX1);
            var ch = Math.round(cropY2 - cropY1);

            if (cw < 4 || ch < 4) continue;

            // Chọn vùng trên bản raw
            var selRegion = [
                [cropX1, cropY1],
                [cropX2, cropY1],
                [cropX2, cropY2],
                [cropX1, cropY2]
            ];
            doc.selection.select(selRegion);

            // TỐI ƯU CỐT LÕI: Chỉ copy trực tiếp trên layer raw (nhẹ gấp 10 lần so với copy merged trên trang 30,000px)
            try {
                doc.selection.copy();
            } catch (e) {
                try { doc.selection.copy(true); } catch (e2) {}
            }

            // Tạo temp document ở 72 DPI cố định (tránh tính toán DPI nặng nề)
            var tempDoc = app.documents.add(cw, ch, 72, "TempLayoutCrop", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
            tempDoc.paste();
            var cropName = "layout_crop_" + i + ".png";
            var cropFilePath = scriptFolder + "\\" + cropName;
            var cropFile = new File(cropFilePath);
            tempDoc.saveAs(cropFile, pngSaveOpts, true, Extension.LOWERCASE);
            tempDoc.close(SaveOptions.DONOTSAVECHANGES);

            app.activeDocument = doc;

            var curSize = 20.0;
            try { curSize = lyr.textItem.size.as('px'); } catch (e) {}

            inputItems.push({
                index: i,
                crop_file: cropName,
                crop_x1: cropX1,
                crop_y1: cropY1,
                crop_w: cw,
                crop_h: ch,
                text_bounds: [lx1, ly1, lx2, ly2],
                text_size: curSize,
                current_w: lw,
                current_h: lh
            });

            // Định kỳ dọn bộ nhớ đệm clipboard mỗi 10 layer để Photoshop không bị tràn RAM
            if ((i + 1) % 10 === 0) {
                try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}
            }
        }

        try { doc.selection.deselect(); } catch (e) {}
        try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}

        // Ghi file layout_inputs.json
        var jsonInputStr = itemsToJSONString(inputItems);
        var inF = new File(inputPath);
        inF.open("w");
        inF.encoding = "UTF-8";
        inF.write(jsonInputStr);
        inF.close();

        // 6. GỌI PYTHON LAYOUT ENGINE PHÂN TÍCH ĐA LUỒNG
        var cmd = 'cmd /c python "' + pyPath + '" "' + scriptFolder + '"';
        app.system(cmd);

        // 7. ĐỌC KẾT QUẢ TỪ FILE JSON
        var resFile = new File(resultPath);
        if (!resFile.exists) {
            alert("Không tìm thấy kết quả từ Layout AI Engine!\nHãy kiểm tra lại Python và thư viện (pillow, numpy).");
            if (group1) group1.visible = true;
            if (rawLayer) rawLayer.visible = prevRawVisible;
            return;
        }

        resFile.open("r");
        var jsonText = resFile.read();
        resFile.close();

        var results;
        try {
            results = eval("(" + jsonText + ")");
        } catch (e) {
            alert("Lỗi đọc kết quả JSON!");
            if (group1) group1.visible = true;
            if (rawLayer) rawLayer.visible = prevRawVisible;
            return;
        }

        // 8. KHÔI PHỤC HIỂN THỊ VÀ CĂN CHỈNH TỪNG TEXT LAYER
        if (group1) group1.visible = true;
        if (rawLayer) rawLayer.visible = prevRawVisible;
        for (var c = 0; c < hiddenCleanLayers.length; c++) {
            hiddenCleanLayers[c].visible = true;
        }

        var successCount = 0;
        for (var k = 0; k < results.length; k++) {
            var res = results[k];
            if (res && res.index < targetTextLayers.length) {
                var targetLyr = targetTextLayers[res.index];
                targetLyr.visible = true;
                doc.activeLayer = targetLyr;

                var tItem = targetLyr.textItem;

                // Bật căn giữa từng dòng văn bản (Center Justification)
                try {
                    tItem.justification = Justification.CENTER;
                } catch (e) {}

                // Cập nhật cỡ chữ mới (Auto-fit font size, tự động làm tròn lên thành số nguyên)
                if (res.recommended_font_size && res.recommended_font_size > 6) {
                    try {
                        var finalFontSize = Math.ceil(Number(res.recommended_font_size));
                        tItem.size = new UnitValue(finalFontSize, "px");
                    } catch (e) {}
                }

                // Đo lại toạ độ sau khi đổi size & justification để dịch chuyển vào tâm đích
                var updatedBounds = targetLyr.bounds;
                var curCenterX = (updatedBounds[0].as('px') + updatedBounds[2].as('px')) / 2.0;
                var curCenterY = (updatedBounds[1].as('px') + updatedBounds[3].as('px')) / 2.0;

                var deltaX = res.target_center_x - curCenterX;
                var deltaY = res.target_center_y - curCenterY;

                // Dịch chuyển layer chuẩn xác từng pixel
                targetLyr.translate(new UnitValue(deltaX, "px"), new UnitValue(deltaY, "px"));

                successCount++;
            }
        }

        alert("Hoàn tất! Đã tự động căn giữa & căn cỡ chữ thành công cho " + successCount + " Text Layer!");

    } finally {
        app.displayDialogs = origDialogMode;
    }
}

function itemsToJSONString(items) {
    var parts = [];
    for (var i = 0; i < items.length; i++) {
        var it = items[i];
        var s = '{"index":' + it.index +
            ',"crop_file":"' + it.crop_file + '"' +
            ',"crop_x1":' + it.crop_x1 +
            ',"crop_y1":' + it.crop_y1 +
            ',"crop_w":' + it.crop_w +
            ',"crop_h":' + it.crop_h +
            ',"text_bounds":[' + it.text_bounds.join(",") + ']' +
            ',"text_size":' + it.text_size +
            ',"current_w":' + it.current_w +
            ',"current_h":' + it.current_h + '}';
        parts.push(s);
    }
    return "[" + parts.join(",") + "]";
}

function cleanOldLayoutFiles(folderPath) {
    var f = new Folder(folderPath);
    var files = f.getFiles("layout_crop_*.png");
    for (var i = 0; i < files.length; i++) {
        files[i].remove();
    }
    var oldIn = new File(folderPath + "\\layout_inputs.json");
    if (oldIn.exists) oldIn.remove();
    var oldRes = new File(folderPath + "\\layout_results.json");
    if (oldRes.exists) oldRes.remove();
}

function getSelectedTextLayers(doc, group1) {
    var layers = [];
    try {
        var ref = new ActionReference();
        ref.putProperty(charIDToTypeID("Prpr"), stringIDToTypeID("targetLayersIDs"));
        ref.putEnumerated(charIDToTypeID("Dcmn"), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
        var desc = executeActionGet(ref);

        if (desc.hasKey(stringIDToTypeID("targetLayersIDs"))) {
            var list = desc.getList(stringIDToTypeID("targetLayersIDs"));
            for (var i = 0; i < list.count; i++) {
                var id = list.getReference(i).getIdentifier();
                var lyr = getLayerByID(doc, id);
                if (lyr) {
                    if (lyr.typename === "ArtLayer" && lyr.kind === LayerKind.TEXT) {
                        layers.push(lyr);
                    } else if (lyr.typename === "LayerSet") {
                        getAllTextLayers(lyr, layers);
                    }
                }
            }
        }
    } catch (e) {}

    if (layers.length === 0) {
        if (doc.activeLayer) {
            if (doc.activeLayer.typename === "ArtLayer" && doc.activeLayer.kind === LayerKind.TEXT) {
                layers.push(doc.activeLayer);
            } else if (doc.activeLayer.typename === "LayerSet") {
                getAllTextLayers(doc.activeLayer, layers);
            }
        }
        if (layers.length === 0 && group1 && group1.typename === "LayerSet") {
            getAllTextLayers(group1, layers);
        }
    }

    return layers;
}

function getLayerByID(doc, id) {
    return findLayerInContainerByID(doc, id);
}

function findLayerInContainerByID(container, id) {
    for (var i = 0; i < container.layers.length; i++) {
        var item = container.layers[i];
        if (item.id === id) return item;
        if (item.typename === "LayerSet") {
            var sub = findLayerInContainerByID(item, id);
            if (sub) return sub;
        }
    }
    return null;
}

function getAllTextLayers(container, list) {
    for (var i = 0; i < container.layers.length; i++) {
        var item = container.layers[i];
        if (item.typename === "ArtLayer" && item.kind === LayerKind.TEXT) {
            list.push(item);
        } else if (item.typename === "LayerSet") {
            getAllTextLayers(item, list);
        }
    }
}

function findRawLayer(doc) {
    var names = ["raw", "background", "ảnh gốc", "layer 0", "raw_image", "bg", "gốc"];
    for (var k = 0; k < names.length; k++) {
        var lyr = findLayer(doc, names[k]);
        if (lyr) return lyr;
    }
    for (var i = doc.layers.length - 1; i >= 0; i--) {
        var l = doc.layers[i];
        if (l.typename === "ArtLayer" && l.kind !== LayerKind.TEXT) {
            return l;
        }
    }
    return null;
}

function findLayer(doc, name) {
    var lower = name.toLowerCase();
    for (var i = 0; i < doc.layers.length; i++) {
        if (doc.layers[i].name.toLowerCase() === lower) {
            return doc.layers[i];
        }
    }
    return null;
}

app.activeDocument.suspendHistory("Auto Center and Fit Text Batch", "main()");
