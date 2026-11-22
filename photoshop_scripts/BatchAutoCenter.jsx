/**
 * BatchAutoCenter.jsx - Tự động căn giữa hàng loạt (AI/CV Layout Engine)
 * Tối ưu hóa đặc biệt cho Webtoon/Manhwa dài (trang 15,000px - 40,000px+, 30-80 layer text).
 * Giữ nguyên 100% cỡ chữ (Font Size) gốc của người dùng, chỉ căn giữa vị trí và dàn dòng.
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
        // 1. Tìm Layer 'raw' và 'Group 1' (hoặc group text bất kỳ)
        var rawLayer = findRawLayer(doc);
        var group1 = findLayer(doc, "Group 1");
        if (!group1) group1 = findTextGroup(doc);

        // 2. LẤY TẤT CẢ CÁC TEXT LAYER (MULTI-SELECTION HOẶC TOÀN BỘ BATCH CỦA FILE)
        var targetTextLayers = getSelectedTextLayers(doc, group1);

        if (targetTextLayers.length === 0) {
            alert("Không tìm thấy Text Layer nào trong tài liệu!\nVui lòng tạo hoặc hiển thị các Text Layer trước khi chạy script.");
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

        // 4. TẠM ẨN TOÀN BỘ CÁC TEXT LAYER & LAYER CLEAN ĐỂ CHỤP VÙNG THOẠI RAW SẠCH 100%
        var prevRawVisible = rawLayer ? rawLayer.visible : true;
        var prevGroup1Visible = group1 ? group1.visible : true;

        var hiddenLayers = [];
        var cleanKeywords = ["clean", "redraw", "xóa chữ", "sửa nền", "paint", "retouch"];

        // Ẩn tất cả text layer đã chọn để không bao giờ bị chụp dính chữ tiếng Việt vào ảnh crop
        for (var t = 0; t < targetTextLayers.length; t++) {
            if (targetTextLayers[t].visible) {
                targetTextLayers[t].visible = false;
                hiddenLayers.push(targetTextLayers[t]);
            }
        }

        // Đệ quy ẩn tất cả các Text Layer khác và Clean layer trong document
        function hideAllTextAndClean(container) {
            for (var i = 0; i < container.layers.length; i++) {
                var lyr = container.layers[i];
                if (lyr === rawLayer) continue;
                if (lyr.typename === "ArtLayer") {
                    if (lyr.kind === LayerKind.TEXT && lyr.visible) {
                        lyr.visible = false;
                        hiddenLayers.push(lyr);
                    } else if (lyr.visible) {
                        var lName = lyr.name.toLowerCase();
                        for (var k = 0; k < cleanKeywords.length; k++) {
                            if (lName.indexOf(cleanKeywords[k]) !== -1) {
                                lyr.visible = false;
                                hiddenLayers.push(lyr);
                                break;
                            }
                        }
                    }
                } else if (lyr.typename === "LayerSet") {
                    hideAllTextAndClean(lyr);
                }
            }
        }
        hideAllTextAndClean(doc);

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
            var padX = Math.round(Math.max(lw * 0.7, 160));
            var padY = Math.round(Math.max(lh * 1.3, 180));
            if (padX > 550) padX = 550;
            if (padY > 550) padY = 550;

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

            var curContents = "";
            try { curContents = lyr.textItem.contents; } catch (e) {}

            inputItems.push({
                index: i,
                crop_file: cropName,
                crop_x1: cropX1,
                crop_y1: cropY1,
                crop_w: cw,
                crop_h: ch,
                text_bounds: [lx1, ly1, lx2, ly2],
                text_size: curSize,
                text_content: curContents,
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
        for (var c = 0; c < hiddenLayers.length; c++) {
            hiddenLayers[c].visible = true;
        }

        var successCount = 0;
        for (var k = 0; k < results.length; k++) {
            var res = results[k];
            if (res && res.index < targetTextLayers.length) {
                var targetLyr = targetTextLayers[res.index];
                targetLyr.visible = true;
                doc.activeLayer = targetLyr;

                var tItem = targetLyr.textItem;

                // 0. BẮT BUỘC: Chuyển layer sang POINT TEXT nếu đang là PARAGRAPH TEXT (Area Text)
                // Giúp triệt tiêu vĩnh viễn lỗi bị bounding box paragraph ép ngắt dòng bừa bãi và lỗi mất chữ cuối
                convertToPointText(targetLyr);

                // 1. Cập nhật ngắt dòng mới theo form quả trứng (Egg/Oval Typeset Wrap)
                if (res.reformatted_text && typeof res.reformatted_text === "string" && res.reformatted_text.length > 0) {
                    try {
                        tItem.contents = res.reformatted_text.replace(/\u2015/g, "—");
                    } catch (e) {}
                } else {
                    try {
                        if (tItem.contents && tItem.contents.indexOf("\u2015") !== -1) {
                            tItem.contents = tItem.contents.replace(/\u2015/g, "—");
                        }
                    } catch (e) {}
                }

                // 2. Bật căn giữa từng dòng văn bản (Center Justification)
                try {
                    tItem.justification = Justification.CENTER;
                } catch (e) {}

                // 3. BỎ QUA CẬP NHẬT CỠ CHỮ: Giữ nguyên 100% cỡ chữ ban đầu của người dùng (No Auto Font Size)

                // 4. Đo lại toạ độ CHUẨN XÁC sau khi đổi text & justification để dịch chuyển vào tâm đích
                var updatedBounds = getLayerExactBounds(targetLyr);
                var curCenterX = (updatedBounds[0] + updatedBounds[2]) / 2.0;
                var curCenterY = (updatedBounds[1] + updatedBounds[3]) / 2.0;

                var deltaX = res.target_center_x - curCenterX;
                var deltaY = res.target_center_y - curCenterY;

                // Dịch chuyển layer chuẩn xác từng pixel
                targetLyr.translate(new UnitValue(deltaX, "px"), new UnitValue(deltaY, "px"));

                successCount++;
            }
        }

        // 9. TỰ ĐỘNG XUẤT ẢNH PREVIEW KẾT QUẢ (AUTOMATED VISUAL FEEDBACK PREVIEWS)
        try {
            var previewFolder = new Folder(scriptFolder + "\\debug_previews");
            if (!previewFolder.exists) previewFolder.create();

            for (var p = 0; p < targetTextLayers.length; p++) {
                var pLyr = targetTextLayers[p];
                var pb = getLayerExactBounds(pLyr);
                var padX = 220;
                var padY = 180;
                var px1 = Math.max(0, Math.round(pb[0] - padX));
                var py1 = Math.max(0, Math.round(pb[1] - padY));
                var px2 = Math.min(docW, Math.round(pb[2] + padX));
                var py2 = Math.min(docH, Math.round(pb[3] + padY));

                var pW = px2 - px1;
                var pH = py2 - py1;
                if (pW < 10 || pH < 10) continue;

                var pSelRegion = [
                    [px1, py1],
                    [px2, py1],
                    [px2, py2],
                    [px1, py2]
                ];
                doc.selection.select(pSelRegion);
                try {
                    doc.selection.copy(true); // Copy merged gồm cả nền và chữ đã typeset
                    var pDoc = app.documents.add(pW, pH, 72, "AutoPreview", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
                    pDoc.paste();
                    var pFile = new File(previewFolder.fsName + "\\preview_" + p + ".png");
                    pDoc.saveAs(pFile, pngSaveOpts, true, Extension.LOWERCASE);
                    pDoc.close(SaveOptions.DONOTSAVECHANGES);
                    app.activeDocument = doc;
                } catch (eCopy) {}

                // Định kỳ dọn bộ nhớ đệm clipboard mỗi 5 layer để tránh tràn RAM trên trang dài
                if ((p + 1) % 5 === 0) {
                    try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (ePurge) {}
                }
            }
            try { doc.selection.deselect(); } catch (eDesel) {}
        } catch (ePrev) {}

        alert("Hoàn tất! Đã tự động căn giữa thành công cho " + successCount + " Text Layer (giữ nguyên cỡ chữ)!\n(Đã tự động lưu ảnh preview vào debug_previews).");

    } finally {
        app.displayDialogs = origDialogMode;
    }
}

function itemsToJSONString(items) {
    var parts = [];
    for (var i = 0; i < items.length; i++) {
        var it = items[i];
        var escapedContent = escapeJSONString(it.text_content || "");
        var s = '{"index":' + it.index +
            ',"crop_file":"' + it.crop_file + '"' +
            ',"crop_x1":' + it.crop_x1 +
            ',"crop_y1":' + it.crop_y1 +
            ',"crop_w":' + it.crop_w +
            ',"crop_h":' + it.crop_h +
            ',"text_bounds":[' + it.text_bounds.join(",") + ']' +
            ',"text_size":' + it.text_size +
            ',"text_content":"' + escapedContent + '"' +
            ',"current_w":' + it.current_w +
            ',"current_h":' + it.current_h + '}';
        parts.push(s);
    }
    return "[" + parts.join(",") + "]";
}

function escapeJSONString(str) {
    if (!str) return "";
    return str.replace(/\\/g, "\\\\")
              .replace(/"/g, '\\"')
              .replace(/\r/g, "\\r")
              .replace(/\n/g, "\\n")
              .replace(/\t/g, "\\t");
}

function getLayerExactBounds(layer) {
    try {
        var ref = new ActionReference();
        ref.putProperty(charIDToTypeID("Prpr"), stringIDToTypeID("bounds"));
        ref.putIdentifier(charIDToTypeID("Lyr "), layer.id);
        var desc = executeActionGet(ref);
        var boundsDesc = desc.getObjectValue(stringIDToTypeID("bounds"));
        var l = boundsDesc.getUnitDoubleValue(stringIDToTypeID("left"));
        var t = boundsDesc.getUnitDoubleValue(stringIDToTypeID("top"));
        var r = boundsDesc.getUnitDoubleValue(stringIDToTypeID("right"));
        var b = boundsDesc.getUnitDoubleValue(stringIDToTypeID("bottom"));
        return [l, t, r, b];
    } catch (e) {
        var b = layer.bounds;
        return [b[0].as('px'), b[1].as('px'), b[2].as('px'), b[3].as('px')];
    }
}

function cleanOldLayoutFiles(folderPath) {
    var f = new Folder(folderPath);
    var files = f.getFiles("layout_crop_*.png");
    for (var i = 0; i < files.length; i++) {
        files[i].remove();
    }
    var prevF = new Folder(folderPath + "\\debug_previews");
    if (prevF.exists) {
        var pFiles = prevF.getFiles("preview_*.png");
        for (var p = 0; p < pFiles.length; p++) {
            pFiles[p].remove();
        }
    }
    var oldIn = new File(folderPath + "\\layout_inputs.json");
    if (oldIn.exists) oldIn.remove();
    var oldRes = new File(folderPath + "\\layout_results.json");
    if (oldRes.exists) oldRes.remove();
}

function getSelectedTextLayers(doc, group1) {
    var selectedLayers = [];
    var isMultiSelection = false;

    // 1. Kiểm tra targetLayersIDs (các layer được user chọn trực tiếp trên panel)
    try {
        var ref = new ActionReference();
        ref.putProperty(charIDToTypeID("Prpr"), stringIDToTypeID("targetLayersIDs"));
        ref.putEnumerated(charIDToTypeID("Dcmn"), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
        var desc = executeActionGet(ref);

        if (desc.hasKey(stringIDToTypeID("targetLayersIDs"))) {
            var list = desc.getList(stringIDToTypeID("targetLayersIDs"));
            if (list.count > 1) {
                isMultiSelection = true;
            }
            for (var i = 0; i < list.count; i++) {
                var id = list.getReference(i).getIdentifier();
                var lyr = getLayerByID(doc, id);
                if (lyr) {
                    if (lyr.typename === "ArtLayer" && lyr.kind === LayerKind.TEXT) {
                        selectedLayers.push(lyr);
                    } else if (lyr.typename === "LayerSet") {
                        // User đã chủ động click chọn thư mục Group -> lấy trọn vẹn toàn bộ text trong group đó
                        getAllTextLayers(lyr, selectedLayers);
                        if (selectedLayers.length > 0) {
                            return sortLayersByTopToBottom(selectedLayers);
                        }
                    }
                }
            }
        }
    } catch (e) {}

    // Nếu user chủ động giữ Ctrl / Shift click chọn NHIỀU layer (> 1) -> Tôn trọng triệt để lựa chọn đó
    if (isMultiSelection && selectedLayers.length > 1) {
        return sortLayersByTopToBottom(selectedLayers);
    }

    // 2. Thu thập tất cả các Text Layer trong toàn bộ tài liệu (hoặc group text)
    var allDocTextLayers = [];
    if (group1 && group1.typename === "LayerSet") {
        getAllTextLayers(group1, allDocTextLayers);
    }

    if (allDocTextLayers.length === 0) {
        var textGroup = findTextGroup(doc);
        if (textGroup && textGroup.typename === "LayerSet") {
            getAllTextLayers(textGroup, allDocTextLayers);
        }
    }

    if (allDocTextLayers.length === 0) {
        getAllTextLayers(doc, allDocTextLayers);
    }

    // 3. XỬ LÝ KHI PHÁT HIỆN NHIỀU LAYER TRONG TÀI LIỆU
    if (allDocTextLayers.length > 1) {
        var singleLyr = (selectedLayers.length === 1) ? selectedLayers[0] : doc.activeLayer;
        var singleName = (singleLyr && singleLyr.name) ? singleLyr.name : "layer hiện tại";

        var promptMsg = "Phát hiện " + allDocTextLayers.length + " Text Layer trong tài liệu!\n\n" +
            "• Bấm [OK] (Enter): Tự động căn giữa HÀNG LOẠT cho TOÀN BỘ " + allDocTextLayers.length + " layer (giữ nguyên cỡ chữ).\n" +
            "• Bấm [Cancel] (Esc): Chỉ căn chỉnh duy nhất 1 layer đang chọn ('" + singleName + "').";

        if (confirm(promptMsg)) {
            return sortLayersByTopToBottom(allDocTextLayers);
        } else {
            return (selectedLayers.length > 0) ? selectedLayers : [singleLyr];
        }
    }

    if (allDocTextLayers.length === 1) {
        return allDocTextLayers;
    }

    return selectedLayers;
}

function sortLayersByTopToBottom(layers) {
    layers.sort(function(a, b) {
        var ya = 0, yb = 0;
        try { ya = a.bounds[1].as('px'); } catch (e) {}
        try { yb = b.bounds[1].as('px'); } catch (e) {}
        return ya - yb;
    });
    return layers;
}

function findTextGroup(container) {
    var textGroupKeywords = ["group 1", "group", "text", "thoại", "thoai", "type", "typeset", "viet", "dịch", "trans", "sub", "chữ", "dialogue"];
    for (var k = 0; k < textGroupKeywords.length; k++) {
        var grp = findLayerByKeyword(container, textGroupKeywords[k]);
        if (grp && grp.typename === "LayerSet") return grp;
    }
    return null;
}

function findLayerByKeyword(container, keyword) {
    var kw = keyword.toLowerCase();
    for (var i = 0; i < container.layers.length; i++) {
        var lyr = container.layers[i];
        if (lyr.name.toLowerCase().indexOf(kw) !== -1) {
            return lyr;
        }
        if (lyr.typename === "LayerSet") {
            var sub = findLayerByKeyword(lyr, keyword);
            if (sub) return sub;
        }
    }
    return null;
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

function convertToPointText(layer) {
    try {
        if (layer.kind === LayerKind.TEXT) {
            if (layer.textItem.kind === TextType.PARAGRAPHTEXT) {
                layer.textItem.kind = TextType.POINTTEXT;
                return;
            }
        }
    } catch (e) {}

    try {
        var idset = charIDToTypeID("set ");
        var desc = new ActionDescriptor();
        var idnull = charIDToTypeID("null");
        var ref = new ActionReference();
        ref.putProperty(charIDToTypeID("Prpr"), stringIDToTypeID("textType"));
        ref.putIdentifier(charIDToTypeID("Lyr "), layer.id);
        desc.putReference(idnull, ref);
        var idto = charIDToTypeID("to  ");
        desc.putEnumerated(idto, stringIDToTypeID("textType"), stringIDToTypeID("pointText"));
        executeAction(idset, desc, DialogModes.NO);
    } catch (e2) {}
}

app.activeDocument.suspendHistory("Auto Center Text Batch", "main()");
