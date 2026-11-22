/**
 * BatchStyleFromSelection.jsx - Multi-Select Batch Auto-Style (ComicText Deep Learning AI)
 * Phím tắt đề xuất: F7
 * Chức năng: Chọn nhiều Text Layer cùng lúc (mỗi cái style khác nhau) ->
 * AI ComicText tự động định vị nét chữ gốc của tác giả và áp đúng style cho từng layer!
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
        if (!rawLayer) {
            alert("Không tìm thấy layer 'raw' (chứa bản scan gốc)!\nVui lòng đặt tên layer tranh gốc là 'raw'.");
            return;
        }

        var group1 = findLayer(doc, "Group 1");
        if (!group1) group1 = findTextGroup(doc);

        // 2. LẤY TẤT CẢ CÁC TEXT LAYER ĐƯỢC CHỌN (MULTI-SELECTION HOẶC TOÀN BỘ BATCH)
        var targetTextLayers = getSelectedTextLayers(doc, group1);

        if (targetTextLayers.length === 0) {
            alert("Không tìm thấy Text Layer nào!\nVui lòng giữ Ctrl click chọn các Text Layer (hoặc chọn thư mục Group 1) trước khi bấm F7.");
            return;
        }

        // 3. Đường dẫn thư mục script
        var scriptFolder = ($.global.AI_TYPESET_DIR) ? new Folder($.global.AI_TYPESET_DIR).fsName : new File($.fileName).parent.fsName;
        var pyPath = scriptFolder + "\\batch_analyzer.py";
        var inputPath = scriptFolder + "\\batch_inputs.json";
        var resultPath = scriptFolder + "\\batch_result.json";

        if (!File(pyPath).exists) {
            alert("Không tìm thấy batch_analyzer.py tại:\n" + scriptFolder + "\nHãy kiểm tra lại thư mục photoshop_scripts.");
            return;
        }

        cleanOldBatchFiles(scriptFolder);

        // 4. TẠM ẨN CÁC TEXT LAYER & LAYER CLEAN ĐỂ CẮT VÙNG RAW CHUẨN XÁC
        var prevRawVisible = rawLayer ? rawLayer.visible : true;
        var prevGroup1Visible = group1 ? group1.visible : true;

        var hiddenLayers = [];
        var cleanKeywords = ["clean", "redraw", "xóa chữ", "sửa nền", "paint", "retouch"];

        // Ẩn tất cả text layer đã chọn để không dính chữ tiếng Việt vào crop
        for (var t = 0; t < targetTextLayers.length; t++) {
            if (targetTextLayers[t].visible) {
                targetTextLayers[t].visible = false;
                hiddenLayers.push(targetTextLayers[t]);
            }
        }

        // Ẩn đệ quy các layer text và layer clean khác
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
        rawLayer.visible = true;
        doc.activeLayer = rawLayer;
        app.refresh();

        var docW = doc.width.as('px');
        var docH = doc.height.as('px');
        var inputItems = [];

        var pngSaveOpts = new PNGSaveOptions();
        pngSaveOpts.compression = 0;
        pngSaveOpts.interlaced = false;

        // 5. CẮT VÙNG NGỮ CẢNH RAW XUNG QUANH TỪNG TEXT LAYER ĐỂ AI COMIC-TEXT ĐỊNH VỊ
        for (var i = 0; i < targetTextLayers.length; i++) {
            var lyr = targetTextLayers[i];
            var b = lyr.bounds;
            var lx1 = b[0].as('px');
            var ly1 = b[1].as('px');
            var lx2 = b[2].as('px');
            var ly2 = b[3].as('px');
            var lw = lx2 - lx1;
            var lh = ly2 - ly1;

            // Mở rộng viền ngữ cảnh để bắt trọn khối chữ raw của tác giả
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

            var textLocalCx = Math.round((lx1 + lx2) / 2.0 - cropX1);
            var textLocalCy = Math.round((ly1 + ly2) / 2.0 - cropY1);

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

            var tempDoc = app.documents.add(cw, ch, 72, "TempBatchCrop", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
            tempDoc.paste();
            var cropName = "batch_crop_" + i + ".png";
            var cropFilePath = scriptFolder + "\\" + cropName;
            tempDoc.saveAs(new File(cropFilePath), pngSaveOpts, true, Extension.LOWERCASE);
            tempDoc.close(SaveOptions.DONOTSAVECHANGES);

            app.activeDocument = doc;
            inputItems.push({
                index: i,
                crop_file: cropName,
                text_local_cx: textLocalCx,
                text_local_cy: textLocalCy,
                text_w: lw,
                text_h: lh
            });

            if ((i + 1) % 10 === 0) {
                try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}
            }
        }

        try { doc.selection.deselect(); } catch (e) {}
        try { app.purge(PurgeTarget.CLIPBOARDCACHE); } catch (e) {}

        if (inputItems.length === 0) {
            alert("Không thể trích xuất vùng ảnh nào để phân tích style!");
            restoreVisibility(group1, rawLayer, prevRawVisible, hiddenLayers);
            return;
        }

        // Ghi file batch_inputs.json
        var jsonInputStr = itemsToJSONString(inputItems);
        var inF = new File(inputPath);
        inF.open("w");
        inF.encoding = "UTF-8";
        inF.write(jsonInputStr);
        inF.close();

        // 6. GỌI PYTHON BATCH AI ENGINE ĐỊNH VỊ NÉT CHỮ GỐC & PHÂN TÍCH STYLE
        var cmd = 'cmd /c python "' + pyPath + '" "' + scriptFolder + '"';
        app.system(cmd);

        // 7. ĐỌC KẾT QUẢ TỪ FILE JSON
        var resFile = new File(resultPath);
        if (!resFile.exists) {
            alert("Không tìm thấy kết quả từ Batch AI Engine!\nHãy kiểm tra lại Python và OpenCV.");
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

        // 8. KHÔI PHỤC HIỂN THỊ VÀ LẦN LƯỢT ÁP STYLE CHO TỪNG LAYER
        restoreVisibility(group1, rawLayer, prevRawVisible, hiddenLayers);

        var successCount = 0;
        for (var k = 0; k < results.length; k++) {
            var res = results[k];
            if (res && res.index < targetTextLayers.length) {
                var targetLyr = targetTextLayers[res.index];
                var styleInfo = res.style;

                if (styleInfo && !styleInfo.error) {
                    targetLyr.visible = true;
                    doc.activeLayer = targetLyr;

                    // Chuẩn hóa ký tự Unicode (chống lỗi ô vuông mất glyph tofu trên font Photoshop)
                    if (targetLyr.kind === LayerKind.TEXT) {
                        try {
                            if (targetLyr.textItem.contents && targetLyr.textItem.contents.indexOf("\u2015") !== -1) {
                                targetLyr.textItem.contents = targetLyr.textItem.contents.replace(/\u2015/g, "—");
                            }
                        } catch (eNorm) {}
                    }

                    // Cập nhật màu văn bản cơ bản
                    if (targetLyr.kind === LayerKind.TEXT && styleInfo.fill) {
                        try {
                            var tColor = new SolidColor();
                            var fillHex = (styleInfo.fill.is_gradient ? styleInfo.fill.top_hex : styleInfo.fill.solid_hex) || "#000000";
                            var rgbVal = hexToRGB(fillHex);
                            tColor.rgb.red = rgbVal.red;
                            tColor.rgb.green = rgbVal.green;
                            tColor.rgb.blue = rgbVal.blue;
                            targetLyr.textItem.color = tColor;
                        } catch (e) {}
                    }

                    // Áp dụng đầy đủ VFX Layer Style (Gradient, Stroke, Outer Glow, Drop Shadow)
                    applyExactVFXStyle(styleInfo);
                    successCount++;
                }
            }
        }

        // Dọn dẹp file crop tạm lớn
        cleanTempCropsOnly(scriptFolder);

        // 9. TỰ ĐỘNG XUẤT ẢNH PREVIEW KẾT QUẢ (AUTOMATED VISUAL FEEDBACK PREVIEWS GIỐNG F8)
        // Giúp kiểm tra kết quả thị giác trực tiếp trong thư mục debug_previews
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
                    doc.selection.copy(true); // Copy merged gồm cả nền và chữ đã áp style
                    var pDoc = app.documents.add(pW, pH, 72, "AutoStylePreview", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
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

        alert("Tuyệt vời (F7)! Đã phân tích ComicText AI và áp style chính xác cho " + successCount + " Text Layer!\n(Đã tự động lưu ảnh preview vào debug_previews để kiểm tra kết quả trực tiếp).");

    } catch (e) {
        alert("Lỗi thực thi BatchStyleFromSelection: " + e.message + " (line " + e.line + ")");
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

function cleanTempCropsOnly(folderPath) {
    var f = new Folder(folderPath);
    var files = f.getFiles("batch_crop_*.png");
    for (var i = 0; i < files.length; i++) {
        try { files[i].remove(); } catch (e) {}
    }
}

function cleanOldBatchFiles(folderPath) {
    var f = new Folder(folderPath);
    var files = f.getFiles("batch_crop_*.png");
    for (var i = 0; i < files.length; i++) {
        try { files[i].remove(); } catch (e) {}
    }
    var tightFiles = f.getFiles("tight_crop_*.png");
    for (var j = 0; j < tightFiles.length; j++) {
        try { tightFiles[j].remove(); } catch (e) {}
    }
    var oldCrop = f.getFiles("crop_*.png");
    for (var c = 0; c < oldCrop.length; c++) {
        try { oldCrop[c].remove(); } catch (e) {}
    }
    var oldIn = new File(folderPath + "\\batch_inputs.json");
    if (oldIn.exists) oldIn.remove();
    var oldRes = new File(folderPath + "\\batch_result.json");
    if (oldRes.exists) oldRes.remove();
    var prevF = new Folder(folderPath + "\\debug_previews");
    if (prevF.exists) {
        var pFiles = prevF.getFiles("preview_*.png");
        for (var p = 0; p < pFiles.length; p++) {
            try { pFiles[p].remove(); } catch (e) {}
        }
    }
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

function getSelectedTextLayers(doc, group1) {
    var selectedLayers = [];
    var isMultiSelection = false;

    // 1. Kiểm tra targetLayersIDs (các layer được user giữ Ctrl/Shift click trực tiếp trên panel)
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
            "• Bấm [OK] (Enter): Tự động lấy & áp style HÀNG LOẠT cho TOÀN BỘ " + allDocTextLayers.length + " layer.\n" +
            "• Bấm [Cancel] (Esc): Chỉ áp style duy nhất cho 1 layer đang chọn ('" + singleName + "').";

        if (confirm(promptMsg)) {
            return sortLayersByTopToBottom(allDocTextLayers);
        } else {
            return (selectedLayers.length > 0) ? selectedLayers : [singleLyr];
        }
    }

    if (allDocTextLayers.length === 1) {
        return allDocTextLayers;
    }

    if (selectedLayers.length > 0) {
        return selectedLayers;
    }

    if (doc.activeLayer && doc.activeLayer.typename === "ArtLayer" && doc.activeLayer.kind === LayerKind.TEXT) {
        return [doc.activeLayer];
    }

    return [];
}

function sortLayersByTopToBottom(layers) {
    layers.sort(function (a, b) {
        var ya = 0;
        var yb = 0;
        try { ya = a.bounds[1].as('px'); } catch (e) {}
        try { yb = b.bounds[1].as('px'); } catch (e) {}
        return ya - yb;
    });
    return layers;
}

function getAllTextLayers(container, outList) {
    for (var i = 0; i < container.layers.length; i++) {
        var lyr = container.layers[i];
        if (lyr.typename === "ArtLayer" && lyr.kind === LayerKind.TEXT) {
            outList.push(lyr);
        } else if (lyr.typename === "LayerSet") {
            getAllTextLayers(lyr, outList);
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

function hexToRGB(hex) {
    if (!hex || hex === "#RRGGBB") return { red: 0, green: 0, blue: 0 };
    hex = hex.replace("#", "");
    if (hex.length === 3) {
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
    }
    var num = parseInt(hex, 16);
    return {
        red: (num >> 16) & 255,
        green: (num >> 8) & 255,
        blue: num & 255
    };
}

function itemsToJSONString(items) {
    var parts = [];
    for (var i = 0; i < items.length; i++) {
        var it = items[i];
        var p = '{"index":' + it.index + ',"crop_file":"' + it.crop_file.replace(/\\/g, '\\\\') + '"' +
                ',"text_local_cx":' + it.text_local_cx + ',"text_local_cy":' + it.text_local_cy +
                ',"text_w":' + it.text_w + ',"text_h":' + it.text_h + '}';
        parts.push(p);
    }
    return '[' + parts.join(',') + ']';
}

function clearLayerStyle() {
    var s2t = function (s) { return stringIDToTypeID(s); };
    try {
        var desc = new ActionDescriptor();
        var ref = new ActionReference();
        ref.putEnumerated(s2t("layer"), s2t("ordinal"), s2t("targetEnum"));
        desc.putReference(s2t("null"), ref);
        executeAction(s2t("disableLayerStyle"), desc, DialogModes.NO);
    } catch (e) {}
}

function applyExactVFXStyle(data) {
    try {
        // 1. Luôn quét sạch 100% layer effects cũ trước để triệt tiêu mọi hiệu ứng dư thừa
        clearLayerStyle();

        var fillInfo = data.fill || {};
        var isGradient = (fillInfo.is_gradient === true);
        var strokeInfo = data.stroke || {};
        var hasStroke = (strokeInfo.enabled === true);
        var glowInfo = data.outer_glow || {};
        var hasGlow = (glowInfo.enabled === true);
        var inGlowInfo = data.inner_glow || {};
        var hasInGlow = (inGlowInfo.enabled === true);
        var inShadowInfo = data.inner_shadow || {};
        var hasInShadow = (inShadowInfo.enabled === true);
        var shadowInfo = data.drop_shadow || {};
        var hasShadow = (shadowInfo.enabled === true);

        var s2t = function (s) { return stringIDToTypeID(s); };
        var lfxDesc = new ActionDescriptor();
        lfxDesc.putUnitDouble(s2t("scale"), s2t("percentUnit"), 100);

        var effectCount = 0;

        // --- 1. RUỘT CHỮ: GRADIENT OVERLAY HOẶC COLOR OVERLAY ---
        if (isGradient) {
            // Chỉ thêm DUY NHẤT Gradient Overlay (không dính Color Overlay hay effect thừa nào)
            var gradDesc = new ActionDescriptor();
            gradDesc.putBoolean(s2t("enabled"), true);
            gradDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t("normal"));
            gradDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), 100);
            gradDesc.putUnitDouble(s2t("angle"), s2t("angleUnit"), fillInfo.angle || 90);
            gradDesc.putEnumerated(s2t("type"), s2t("gradientType"), s2t("linear"));
            gradDesc.putBoolean(s2t("reverse"), false);
            gradDesc.putBoolean(s2t("align"), true);
            gradDesc.putUnitDouble(s2t("scale"), s2t("percentUnit"), 100);

            var topColor = hexToRGB(fillInfo.top_hex || "#FFF600");
            var botColor = hexToRGB(fillInfo.bottom_hex || "#FF8000");

            var grad = new ActionDescriptor();
            grad.putString(s2t("name"), "AI Gradient");
            grad.putEnumerated(s2t("gradientForm"), s2t("gradientForm"), s2t("customStops"));
            grad.putDouble(s2t("interfaceIconFrameDimmed"), 4096);

            var colors = new ActionList();
            var stop1 = new ActionDescriptor();
            var col1 = new ActionDescriptor();
            col1.putDouble(s2t("red"), botColor.red);
            col1.putDouble(s2t("green"), botColor.green);
            col1.putDouble(s2t("blue"), botColor.blue);
            stop1.putObject(s2t("color"), s2t("RGBColor"), col1);
            stop1.putEnumerated(s2t("type"), s2t("colorStopType"), s2t("userStop"));
            stop1.putInteger(s2t("location"), 0);
            stop1.putInteger(s2t("midpoint"), 50);
            colors.putObject(s2t("colorStop"), stop1);

            var stop2 = new ActionDescriptor();
            var col2 = new ActionDescriptor();
            col2.putDouble(s2t("red"), topColor.red);
            col2.putDouble(s2t("green"), topColor.green);
            col2.putDouble(s2t("blue"), topColor.blue);
            stop2.putObject(s2t("color"), s2t("RGBColor"), col2);
            stop2.putEnumerated(s2t("type"), s2t("colorStopType"), s2t("userStop"));
            stop2.putInteger(s2t("location"), 4096);
            stop2.putInteger(s2t("midpoint"), 50);
            colors.putObject(s2t("colorStop"), stop2);

            grad.putList(s2t("colors"), colors);

            var trans = new ActionList();
            var tr1 = new ActionDescriptor();
            tr1.putUnitDouble(s2t("opacity"), s2t("percentUnit"), 100);
            tr1.putInteger(s2t("location"), 0);
            tr1.putInteger(s2t("midpoint"), 50);
            trans.putObject(s2t("transferSpec"), tr1);

            var tr2 = new ActionDescriptor();
            tr2.putUnitDouble(s2t("opacity"), s2t("percentUnit"), 100);
            tr2.putInteger(s2t("location"), 4096);
            tr2.putInteger(s2t("midpoint"), 50);
            trans.putObject(s2t("transferSpec"), tr2);

            grad.putList(s2t("transparency"), trans);
            gradDesc.putObject(s2t("gradient"), s2t("gradient"), grad);
            lfxDesc.putObject(s2t("gradientFill"), s2t("gradientFill"), gradDesc);
            effectCount++;

        } else if (fillInfo.solid_hex && fillInfo.solid_hex !== "#000000") {
            // Khi là chữ có màu (tím, đỏ, xanh, cam...), gán Color Overlay:
            // CHỈ THÊM DUY NHẤT solidFill, tuyệt đối không thêm gradient hay effect thừa!
            var solidDesc = new ActionDescriptor();
            solidDesc.putBoolean(s2t("enabled"), true);
            solidDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t("normal"));
            solidDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), 100);

            var sSolidCol = hexToRGB(fillInfo.solid_hex);
            var colSolid = new ActionDescriptor();
            colSolid.putDouble(s2t("red"), sSolidCol.red);
            colSolid.putDouble(s2t("green"), sSolidCol.green);
            colSolid.putDouble(s2t("blue"), sSolidCol.blue);
            solidDesc.putObject(s2t("color"), s2t("RGBColor"), colSolid);
            lfxDesc.putObject(s2t("solidFill"), s2t("solidFill"), solidDesc);
            effectCount++;
        }

        // --- 2. STROKE (CHỈ THÊM KHI CÓ VIỀN THỰC SỰ) ---
        if (hasStroke) {
            var strokeDesc = new ActionDescriptor();
            strokeDesc.putBoolean(s2t("enabled"), true);
            strokeDesc.putEnumerated(s2t("style"), s2t("frameStyle"), s2t("outsetFrame"));
            strokeDesc.putEnumerated(s2t("paintType"), s2t("frameFill"), s2t("solidColor"));
            strokeDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t("normal"));
            strokeDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), 100);
            strokeDesc.putUnitDouble(s2t("size"), s2t("pixelsUnit"), strokeInfo.size_px || 2.5);

            var sCol = hexToRGB(strokeInfo.color_hex || "#000000");
            var colStroke = new ActionDescriptor();
            colStroke.putDouble(s2t("red"), sCol.red);
            colStroke.putDouble(s2t("green"), sCol.green);
            colStroke.putDouble(s2t("blue"), sCol.blue);
            strokeDesc.putObject(s2t("color"), s2t("RGBColor"), colStroke);
            lfxDesc.putObject(s2t("frameFX"), s2t("frameFX"), strokeDesc);
            effectCount++;
        }

        // --- 3. OUTER GLOW (CHỈ THÊM KHI CÓ GLOW) ---
        if (hasGlow) {
            var glowDesc = new ActionDescriptor();
            glowDesc.putBoolean(s2t("enabled"), true);
            glowDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t("normal"));
            glowDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), glowInfo.opacity_percent || 80);

            var gCol = hexToRGB(glowInfo.color_hex || "#FFFFFF");
            var colGlow = new ActionDescriptor();
            colGlow.putDouble(s2t("red"), gCol.red);
            colGlow.putDouble(s2t("green"), gCol.green);
            colGlow.putDouble(s2t("blue"), gCol.blue);
            glowDesc.putObject(s2t("color"), s2t("RGBColor"), colGlow);

            glowDesc.putEnumerated(s2t("glowTechnique"), s2t("matteTechnique"), s2t("softMatte"));
            glowDesc.putUnitDouble(s2t("chokeMatte"), s2t("percentUnit"), 10);
            glowDesc.putUnitDouble(s2t("size"), s2t("pixelsUnit"), glowInfo.size_px || 8.0);
            lfxDesc.putObject(s2t("outerGlow"), s2t("outerGlow"), glowDesc);
            effectCount++;
        }

        // --- 4. INNER GLOW (CHỈ THÊM KHI CÓ VẾT MÁU / HORROR) ---
        if (hasInGlow) {
            var inGlowDesc = new ActionDescriptor();
            inGlowDesc.putBoolean(s2t("enabled"), true);
            inGlowDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t(inGlowInfo.blend_mode || "multiply"));
            inGlowDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), inGlowInfo.opacity_percent || 85);

            var igCol = hexToRGB(inGlowInfo.color_hex || "#8E1B1B");
            var colInGlow = new ActionDescriptor();
            colInGlow.putDouble(s2t("red"), igCol.red);
            colInGlow.putDouble(s2t("green"), igCol.green);
            colInGlow.putDouble(s2t("blue"), igCol.blue);
            inGlowDesc.putObject(s2t("color"), s2t("RGBColor"), colInGlow);

            inGlowDesc.putEnumerated(s2t("glowTechnique"), s2t("matteTechnique"), s2t("softMatte"));
            inGlowDesc.putEnumerated(s2t("innerGlowSource"), s2t("innerGlowSource"), s2t("edgeGlow"));
            inGlowDesc.putUnitDouble(s2t("chokeMatte"), s2t("percentUnit"), 0);
            inGlowDesc.putUnitDouble(s2t("size"), s2t("pixelsUnit"), inGlowInfo.size_px || 3.5);
            inGlowDesc.putUnitDouble(s2t("noise"), s2t("percentUnit"), inGlowInfo.noise_percent || 0);
            lfxDesc.putObject(s2t("innerGlow"), s2t("innerGlow"), inGlowDesc);
            effectCount++;
        }

        // --- 5. INNER SHADOW (CHỈ THÊM KHI CÓ INNER SHADOW) ---
        if (hasInShadow) {
            var inShadowDesc = new ActionDescriptor();
            inShadowDesc.putBoolean(s2t("enabled"), true);
            inShadowDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t(inShadowInfo.blend_mode || "multiply"));
            inShadowDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), inShadowInfo.opacity_percent || 80);

            var isCol = hexToRGB(inShadowInfo.color_hex || "#5E1111");
            var colInShadow = new ActionDescriptor();
            colInShadow.putDouble(s2t("red"), isCol.red);
            colInShadow.putDouble(s2t("green"), isCol.green);
            colInShadow.putDouble(s2t("blue"), isCol.blue);
            inShadowDesc.putObject(s2t("color"), s2t("RGBColor"), colInShadow);

            inShadowDesc.putUnitDouble(s2t("angle"), s2t("angleUnit"), 90);
            inShadowDesc.putBoolean(s2t("useGlobalAngle"), false);
            inShadowDesc.putUnitDouble(s2t("distance"), s2t("pixelsUnit"), inShadowInfo.distance_px || 0.0);
            inShadowDesc.putUnitDouble(s2t("chokeMatte"), s2t("percentUnit"), inShadowInfo.choke_percent || 10);
            inShadowDesc.putUnitDouble(s2t("size"), s2t("pixelsUnit"), inShadowInfo.size_px || 4.0);
            inShadowDesc.putUnitDouble(s2t("noise"), s2t("percentUnit"), inShadowInfo.noise_percent || 0);
            lfxDesc.putObject(s2t("innerShadow"), s2t("innerShadow"), inShadowDesc);
            effectCount++;
        }

        // --- 6. DROP SHADOW (CHỈ THÊM KHI CÓ DROP SHADOW) ---
        if (hasShadow) {
            var shadowDesc = new ActionDescriptor();
            shadowDesc.putBoolean(s2t("enabled"), true);
            shadowDesc.putEnumerated(s2t("mode"), s2t("blendMode"), s2t("normal"));
            shadowDesc.putUnitDouble(s2t("opacity"), s2t("percentUnit"), 75);

            var shCol = hexToRGB(shadowInfo.color_hex || "#000000");
            var colShadow = new ActionDescriptor();
            colShadow.putDouble(s2t("red"), shCol.red);
            colShadow.putDouble(s2t("green"), colShadow.green);
            colShadow.putDouble(s2t("blue"), colShadow.blue);
            shadowDesc.putObject(s2t("color"), s2t("RGBColor"), colShadow);

            shadowDesc.putUnitDouble(s2t("angle"), s2t("angleUnit"), 120);
            shadowDesc.putBoolean(s2t("useGlobalAngle"), false);
            shadowDesc.putUnitDouble(s2t("distance"), s2t("pixelsUnit"), shadowInfo.distance_px || 4.0);
            shadowDesc.putUnitDouble(s2t("chokeMatte"), s2t("percentUnit"), 0);
            shadowDesc.putUnitDouble(s2t("size"), s2t("pixelsUnit"), shadowInfo.blur_px || 4.0);
            lfxDesc.putObject(s2t("dropShadow"), s2t("dropShadow"), shadowDesc);
            effectCount++;
        }

        // Nếu không có bất kỳ hiệu ứng nào cần áp (chữ đen thông thường):
        // clearLayerStyle() ở trên đã xóa sạch 100%, layer sạch tinh tươm!
        if (effectCount === 0) {
            return;
        }

        // Áp dụng bộ hiệu ứng (CHỈ CHỨA CÁC EFFECT ĐƯỢC CHỌN, KHÔNG CÓ HIỆU ỨNG TẮT MẮT THỪA)
        var desc = new ActionDescriptor();
        var ref = new ActionReference();
        ref.putProperty(s2t("property"), s2t("layerEffects"));
        ref.putEnumerated(s2t("layer"), s2t("ordinal"), s2t("targetEnum"));
        desc.putReference(s2t("null"), ref);
        desc.putObject(s2t("to"), s2t("layerEffects"), lfxDesc);
        executeAction(s2t("set"), desc, DialogModes.NO);

    } catch (e) {
        // Bỏ qua lỗi nhỏ
    }
}

main();
