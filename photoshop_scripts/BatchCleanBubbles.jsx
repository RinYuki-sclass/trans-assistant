/**
 * BatchCleanBubbles.jsx - Tự động Clean Bong Bóng Thoại & Loại Trừ 100% SFX
 * Tích hợp ComicTextDetector Deep Learning AI & Computer Vision:
 *   1. Nhận diện và chỉ xóa chữ trong các BONG BÓNG THOẠI (nền trắng / màu trơn).
 *   2. BẢO TỒN NGUYÊN VẸN 100% CÁC CHỮ SFX & TRANH VẼ PHỨC TẠP.
 *   3. Tự động duplicate hoặc cập nhật layer "Background (Clean)".
 * Phím tắt đề xuất: F9
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
        // 1. Tìm Layer 'raw'
        var rawLayer = findRawLayer(doc);
        if (!rawLayer) {
            alert("Không tìm thấy Layer 'raw' (hoặc Background gốc)!\nVui lòng đặt tên layer chứa tranh scan gốc là 'raw'.");
            return;
        }

        var group1 = findLayer(doc, "Group 1");
        if (!group1) group1 = findTextGroup(doc);

        // 2. Kiểm tra chế độ xử lý:
        //    - Chế độ A: Người dùng đang khoanh 1 vùng chọn Marquee (M)
        //    - Chế độ B: Xử lý theo các Text Layer (Multi-selection hoặc Group 1)
        var hasSelection = false;
        var selBounds = null;
        try {
            selBounds = doc.selection.bounds;
            var sw = selBounds[2].as('px') - selBounds[0].as('px');
            var sh = selBounds[3].as('px') - selBounds[1].as('px');
            if (sw >= 8 && sh >= 8) {
                hasSelection = true;
            }
        } catch (e) {
            hasSelection = false;
        }

        var targetTextLayers = [];
        if (!hasSelection) {
            targetTextLayers = getSelectedTextLayers(doc, group1);
            if (targetTextLayers.length === 0) {
                alert("Không tìm thấy Text Layer hoặc vùng chọn nào!\n\nCách dùng:\n1. Chọn các Text Layer cần clean bóng thoại (hoặc để trong Group 1).\n2. HOẶC dùng Marquee (M) khoanh vùng bóng thoại cần clean rồi bấm F9.");
                return;
            }
        }

        // 3. Đường dẫn thư mục script
        var scriptFolder = ($.global.AI_TYPESET_DIR) ? new Folder($.global.AI_TYPESET_DIR).fsName : new File($.fileName).parent.fsName;
        var pyPath = scriptFolder + "\\bubble_cleaner.py";
        var inputPath = scriptFolder + "\\clean_inputs.json";
        var resultPath = scriptFolder + "\\clean_results.json";

        if (!File(pyPath).exists) {
            alert("Không tìm thấy bubble_cleaner.py tại:\n" + scriptFolder + "\nHãy kiểm tra lại thư mục photoshop_scripts.");
            return;
        }

        cleanOldCleanFiles(scriptFolder);

        // 4. Tìm hoặc tạo layer "Background (Clean)"
        var cleanLayer = findCleanLayer(doc);
        if (!cleanLayer) {
            cleanLayer = rawLayer.duplicate(rawLayer, ElementPlacement.PLACEAFTER);
            cleanLayer.name = "Background (Clean)";
        }
        cleanLayer.visible = true;

        var prevRawVisible = rawLayer.visible;
        var prevGroup1Visible = group1 ? group1.visible : true;
        var hiddenLayers = [];

        // Ẩn các text layer để không bị dính chữ tiếng Việt vào crop
        for (var t = 0; t < targetTextLayers.length; t++) {
            if (targetTextLayers[t].visible) {
                targetTextLayers[t].visible = false;
                hiddenLayers.push(targetTextLayers[t]);
            }
        }
        if (group1) group1.visible = false;
        rawLayer.visible = true;
        doc.activeLayer = rawLayer;
        app.refresh();

        var docW = doc.width.as('px');
        var docH = doc.height.as('px');
        var inputItems = [];

        var pngSaveOpts = new PNGSaveOptions();
        pngSaveOpts.compression = 0;
        pngSaveOpts.interlaced = false;

        // 5. CẮT ẢNH VÙNG CẦN CLEAN TỪ RAW LAYER
        if (hasSelection) {
            // Chế độ khoanh vùng Marquee đơn lẻ
            var x1 = Math.max(0, Math.round(selBounds[0].as('px')));
            var y1 = Math.max(0, Math.round(selBounds[1].as('px')));
            var x2 = Math.min(docW, Math.round(selBounds[2].as('px')));
            var y2 = Math.min(docH, Math.round(selBounds[3].as('px')));
            var cw = x2 - x1;
            var ch = y2 - y1;

            if (cw >= 8 && ch >= 8) {
                var cropName = "clean_crop_input_0.png";
                var cropFilePath = scriptFolder + "\\" + cropName;
                try {
                    doc.selection.copy();
                } catch (e) {
                    try { doc.selection.copy(true); } catch (e2) {}
                }
                var tempDoc = app.documents.add(cw, ch, 72, "TempCleanCrop", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
                tempDoc.paste();
                tempDoc.saveAs(new File(cropFilePath), pngSaveOpts, true, Extension.LOWERCASE);
                tempDoc.close(SaveOptions.DONOTSAVECHANGES);

                app.activeDocument = doc;
                inputItems.push({
                    index: 0,
                    crop_file: cropName,
                    crop_x1: x1,
                    crop_y1: y1,
                    crop_w: cw,
                    crop_h: ch
                });
            }
        } else {
            // Chế độ quét theo các Text Layers
            for (var i = 0; i < targetTextLayers.length; i++) {
                var lyr = targetTextLayers[i];
                var b = lyr.bounds;
                var lx1 = b[0].as('px');
                var ly1 = b[1].as('px');
                var lx2 = b[2].as('px');
                var ly2 = b[3].as('px');
                var lw = lx2 - lx1;
                var lh = ly2 - ly1;

                // Mở rộng viền chụp trọn vẹn bóng thoại
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
                if (cw < 8 || ch < 8) continue;

                var selRegion = [
                    [cropX1, cropY1],
                    [cropX2, cropY1],
                    [cropX2, cropY2],
                    [cropX1, cropY2]
                ];
                doc.selection.select(selRegion);

                try {
                    doc.selection.copy();
                } catch (e) {
                    try { doc.selection.copy(true); } catch (e2) {}
                }

                var tempDoc = app.documents.add(cw, ch, 72, "TempCleanCrop", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
                tempDoc.paste();
                var cropName = "clean_crop_input_" + i + ".png";
                var cropFilePath = scriptFolder + "\\" + cropName;
                tempDoc.saveAs(new File(cropFilePath), pngSaveOpts, true, Extension.LOWERCASE);
                tempDoc.close(SaveOptions.DONOTSAVECHANGES);

                app.activeDocument = doc;
                inputItems.push({
                    index: i,
                    crop_file: cropName,
                    crop_x1: cropX1,
                    crop_y1: cropY1,
                    crop_w: cw,
                    crop_h: ch
                });

                if ((i + 1) % 10 === 0) {
                    try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}
                }
            }
        }

        try { doc.selection.deselect(); } catch (e) {}
        try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}

        if (inputItems.length === 0) {
            alert("Không thể trích xuất vùng ảnh nào để clean!");
            restoreVisibility(group1, rawLayer, prevRawVisible, hiddenLayers);
            return;
        }

        // Ghi file clean_inputs.json
        var jsonInputStr = itemsToJSONString(inputItems);
        var inF = new File(inputPath);
        inF.open("w");
        inF.encoding = "UTF-8";
        inF.write(jsonInputStr);
        inF.close();

        // 6. GỌI PYTHON BUBBLE CLEANER
        var cmd = 'cmd /c python "' + pyPath + '" "' + scriptFolder + '"';
        app.system(cmd);

        // 7. ĐỌC KẾT QUẢ TỪ FILE JSON
        var resFile = new File(resultPath);
        if (!resFile.exists) {
            alert("Không tìm thấy kết quả từ Bubble Cleaner AI!\nHãy kiểm tra lại Python và OpenCV.");
            restoreVisibility(group1, rawLayer, prevRawVisible, hiddenLayers);
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
            restoreVisibility(group1, rawLayer, prevRawVisible, hiddenLayers);
            return;
        }

        // 8. DÁN CÁC VÙNG ĐÃ CLEAN VÀO LAYER "Background (Clean)"
        doc.activeLayer = cleanLayer;
        var totalCleaned = 0;
        var totalSkippedSFX = 0;

        for (var k = 0; k < results.length; k++) {
            var res = results[k];
            if (res && res.cleaned && res.clean_file) {
                var cleanFilePath = scriptFolder + "\\" + res.clean_file;
                var cFile = new File(cleanFilePath);
                if (cFile.exists) {
                    var x1 = res.crop_x1;
                    var y1 = res.crop_y1;
                    var x2 = x1 + res.crop_w;
                    var y2 = y1 + res.crop_h;

                    var selRegion = [
                        [x1, y1],
                        [x2, y1],
                        [x2, y2],
                        [x1, y2]
                    ];

                    var cropDoc = app.open(cFile);
                    cropDoc.selection.selectAll();
                    cropDoc.selection.copy();
                    cropDoc.close(SaveOptions.DONOTSAVECHANGES);

                    app.activeDocument = doc;
                    doc.activeLayer = cleanLayer;
                    doc.selection.select(selRegion);
                    doc.paste();

                    // Merge layer vừa dán xuống layer Background (Clean)
                    try {
                        doc.activeLayer.merge();
                    } catch (e) {}

                    totalCleaned += (res.bubbles_cleaned || 1);
                    totalSkippedSFX += (res.sfx_skipped || 0);
                }
            } else if (res) {
                totalSkippedSFX += (res.sfx_skipped || 0);
            }
        }

        try { doc.selection.deselect(); } catch (e) {}
        try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}

        // Dọn file tạm
        cleanOldCleanFiles(scriptFolder);

        // 9. KHÔI PHỤC HIỂN THỊ (ẨN RAW, BẬT CLEAN VÀ TEXT)
        if (group1) group1.visible = true;
        for (var c = 0; c < hiddenLayers.length; c++) {
            hiddenLayers[c].visible = true;
        }
        // Tắt mắt layer raw để hiển thị layer Background (Clean) sạch đẹp bên dưới text
        rawLayer.visible = false;
        cleanLayer.visible = true;

        alert("[V] BATCH CLEAN THÀNH CÔNG (F9)!\n\n" +
              "• Đã clean sạch: " + totalCleaned + " bong bóng thoại\n" +
              "• Đã bỏ qua: " + totalSkippedSFX + " SFX / tranh vẽ (Bảo tồn nguyên bản 100%)\n" +
              "• Kết quả được lưu tại Layer: '" + cleanLayer.name + "'\n" +
              "(Layer 'raw' gốc vẫn được giữ nguyên và tạm ẩn để so sánh)");

    } catch (e) {
        alert("Lỗi thực thi BatchCleanBubbles: " + e.message + " (line " + e.line + ")");
    } finally {
        app.displayDialogs = origDialogMode;
    }
}

function restoreVisibility(group1, rawLayer, prevRawVisible, hiddenLayers) {
    if (group1) group1.visible = true;
    if (rawLayer) rawLayer.visible = prevRawVisible;
    for (var i = 0; i < hiddenLayers.length; i++) {
        hiddenLayers[i].visible = true;
    }
}

function cleanOldCleanFiles(folderPath) {
    var f = new Folder(folderPath);
    var inFiles = f.getFiles("clean_crop_input_*.png");
    for (var i = 0; i < inFiles.length; i++) {
        try { inFiles[i].remove(); } catch (e) {}
    }
    var outFiles = f.getFiles("clean_crop_*.png");
    for (var j = 0; j < outFiles.length; j++) {
        try { outFiles[j].remove(); } catch (e) {}
    }
    var oldIn = new File(folderPath + "\\clean_inputs.json");
    if (oldIn.exists) oldIn.remove();
    var oldRes = new File(folderPath + "\\clean_results.json");
    if (oldRes.exists) oldRes.remove();
}

function findCleanLayer(doc) {
    var names = ["background (clean)", "background clean", "clean", "cleaned", "redraw"];
    for (var i = 0; i < doc.layers.length; i++) {
        var lyr = doc.layers[i];
        if (lyr.typename === "ArtLayer") {
            var lName = lyr.name.toLowerCase();
            for (var k = 0; k < names.length; k++) {
                if (lName === names[k]) return lyr;
            }
        }
    }
    return null;
}

function findRawLayer(doc) {
    for (var i = 0; i < doc.layers.length; i++) {
        var lyr = doc.layers[i];
        if (lyr.name.toLowerCase() === "raw") return lyr;
    }
    for (var j = 0; j < doc.layers.length; j++) {
        var l = doc.layers[j];
        var n = l.name.toLowerCase();
        if (n.indexOf("raw") !== -1 || n.indexOf("scan") !== -1 || n.indexOf("gốc") !== -1) return l;
    }
    for (var k = doc.layers.length - 1; k >= 0; k--) {
        if (doc.layers[k].typename === "ArtLayer" && doc.layers[k].kind !== LayerKind.TEXT) {
            return doc.layers[k];
        }
    }
    return null;
}

function findLayer(container, name) {
    for (var i = 0; i < container.layers.length; i++) {
        if (container.layers[i].name.toLowerCase() === name.toLowerCase()) {
            return container.layers[i];
        }
    }
    return null;
}

function findTextGroup(doc) {
    for (var i = 0; i < doc.layerSets.length; i++) {
        var set = doc.layerSets[i];
        for (var j = 0; j < set.layers.length; j++) {
            if (set.layers[j].typename === "ArtLayer" && set.layers[j].kind === LayerKind.TEXT) {
                return set;
            }
        }
    }
    return null;
}

function getSelectedTextLayers(doc, group1) {
    var selectedLayers = [];
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
                        selectedLayers.push(lyr);
                    } else if (lyr.typename === "LayerSet") {
                        collectTextLayers(lyr, selectedLayers);
                    }
                }
            }
        }
    } catch (e) {}

    if (selectedLayers.length === 0 && doc.activeLayer && doc.activeLayer.kind === LayerKind.TEXT) {
        selectedLayers.push(doc.activeLayer);
    }

    if (selectedLayers.length === 0 && group1 && group1.typename === "LayerSet") {
        collectTextLayers(group1, selectedLayers);
    }

    if (selectedLayers.length === 0) {
        collectTextLayers(doc, selectedLayers);
    }

    return selectedLayers;
}

function collectTextLayers(container, outList) {
    for (var i = 0; i < container.layers.length; i++) {
        var lyr = container.layers[i];
        if (lyr.typename === "ArtLayer" && lyr.kind === LayerKind.TEXT) {
            outList.push(lyr);
        } else if (lyr.typename === "LayerSet") {
            collectTextLayers(lyr, outList);
        }
    }
}

function getLayerByID(doc, id) {
    function search(container) {
        for (var i = 0; i < container.layers.length; i++) {
            var lyr = container.layers[i];
            if (lyr.id === id) return lyr;
            if (lyr.typename === "LayerSet") {
                var found = search(lyr);
                if (found) return found;
            }
        }
        return null;
    }
    return search(doc);
}

function itemsToJSONString(items) {
    var parts = [];
    for (var i = 0; i < items.length; i++) {
        var it = items[i];
        var p = '{"index":' + it.index + ',"crop_file":"' + it.crop_file.replace(/\\/g, '\\\\') + '"' +
                ',"crop_x1":' + it.crop_x1 + ',"crop_y1":' + it.crop_y1 +
                ',"crop_w":' + it.crop_w + ',"crop_h":' + it.crop_h + '}';
        parts.push(p);
    }
    return '[' + parts.join(',') + ']';
}

main();
