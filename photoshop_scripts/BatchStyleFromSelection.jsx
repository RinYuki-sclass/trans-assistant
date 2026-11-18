/**
 * BatchStyleFromSelection.jsx - Multi-Select Batch Auto-Style (Gemini Vision)
 * Phím tắt đề xuất: F7
 * Chức năng: Chọn nhiều Text Layer cùng lúc (mỗi cái style khác nhau) -> AI tự động phân tích và áp style riêng cho từng layer!
 */

#target photoshop

function main() {
    if (app.documents.length === 0) {
        alert("Chưa mở file PSD nào!");
        return;
    }

    var doc = app.activeDocument;

    // 1. Tìm Layer 'raw' và 'Group 1'
    var rawLayer = findLayer(doc, "raw");
    var group1 = findLayer(doc, "Group 1");

    // 2. LẤY TẤT CẢ CÁC TEXT LAYER ĐƯỢC CHỌN (MULTI-SELECTION)
    var targetTextLayers = getSelectedTextLayers(doc, group1);

    if (targetTextLayers.length === 0) {
        alert("Vui lòng giữ phím Ctrl click chọn các Text Layer (hoặc chọn thư mục Group 1) trước khi bấm F7!");
        return;
    }

    // 3. Đường dẫn thư mục script
    var thisFile = new File($.fileName);
    var scriptFolder = thisFile.parent.fsName;
    var pyPath = scriptFolder + "\\batch_analyzer.py";
    var resultPath = scriptFolder + "\\batch_result.json";

    if (!File(pyPath).exists) {
        scriptFolder = "d:\\Nhung\\RIDI\\trans-assistant\\photoshop_scripts";
        pyPath = scriptFolder + "\\batch_analyzer.py";
        resultPath = scriptFolder + "\\batch_result.json";
    }

    // Xóa các file crop cũ và kết quả cũ
    cleanOldCropFiles(scriptFolder);

    // 4. TẠM ẨN GROUP 1 & BẬT RAW ĐỂ CẮT CÁC VÙNG ẢNH TƯƠNG ỨNG
    var prevRawVisible = rawLayer ? rawLayer.visible : true;
    var prevGroup1Visible = group1 ? group1.visible : true;

    if (group1) group1.visible = false;
    if (rawLayer) {
        rawLayer.visible = true;
        doc.activeLayer = rawLayer;
    }
    app.refresh();

    var docW = doc.width.as('px');
    var docH = doc.height.as('px');

    // 5. DUYỆT TỪNG TEXT LAYER ĐỂ CẮT ẢNH RAW VÀ LƯU RA crop_0.png, crop_1.png...
    for (var i = 0; i < targetTextLayers.length; i++) {
        var lyr = targetTextLayers[i];
        var b = lyr.bounds;
        var lx1 = b[0].as('px');
        var ly1 = b[1].as('px');
        var lx2 = b[2].as('px');
        var ly2 = b[3].as('px');

        // Mở rộng viền 18px để bắt trọn viền và quầng sáng glow của bản gốc
        var pad = 18;
        var cropX1 = Math.max(0, lx1 - pad);
        var cropY1 = Math.max(0, ly1 - pad);
        var cropX2 = Math.min(docW, lx2 + pad);
        var cropY2 = Math.min(docH, ly2 + pad);

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

        try {
            doc.selection.copy(true); // Copy merged
        } catch (e) {
            doc.selection.copy();
        }

        // Tạo temp document và lưu PNG
        var tempDoc = app.documents.add(cw, ch, doc.resolution, "TempBatchCrop", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
        tempDoc.paste();
        var cropName = "crop_" + i + ".png";
        var cropFilePath = scriptFolder + "\\" + cropName;
        var cropFile = new File(cropFilePath);
        var pngSaveOpts = new PNGSaveOptions();
        tempDoc.saveAs(cropFile, pngSaveOpts, true, Extension.LOWERCASE);
        tempDoc.close(SaveOptions.DONOTSAVECHANGES);

        app.activeDocument = doc;
    }

    try { doc.selection.deselect(); } catch (e) {}

    // 6. GỌI PYTHON BATCH AI ENGINE PHÂN TÍCH SONG SONG
    var cmd = 'cmd /c python "' + pyPath + '" "' + scriptFolder + '"';
    app.system(cmd);

    // 7. ĐỌC KẾT QUẢ TỪ FILE JSON
    var resFile = new File(resultPath);
    if (!resFile.exists) {
        alert("Không tìm thấy kết quả từ Batch AI Engine!");
        if (group1) group1.visible = true;
        if (rawLayer) rawLayer.visible = prevRawVisible;
        return;
    }

    resFile.open("r");
    var jsonText = resFile.read();
    resFile.close();

    var batchData;
    try {
        batchData = eval("(" + jsonText + ")");
    } catch (e) {
        alert("Lỗi đọc kết quả JSON!");
        if (group1) group1.visible = true;
        if (rawLayer) rawLayer.visible = prevRawVisible;
        return;
    }

    // 8. KHÔI PHỤC HIỂN THỊ VÀ LẦN LƯỢT ÁP STYLE CHO TỪNG LAYER
    if (group1) group1.visible = true;
    if (rawLayer) rawLayer.visible = prevRawVisible;

    var successCount = 0;
    for (var k = 0; k < targetTextLayers.length; k++) {
        var targetLyr = targetTextLayers[k];
        var key = "crop_" + k + ".png";
        var styleInfo = batchData[key];

        if (styleInfo && !styleInfo.error) {
            targetLyr.visible = true;
            doc.activeLayer = targetLyr;
            applyExactVFXStyle(styleInfo);
            successCount++;
        }
    }

    alert("Tuyệt vời! Đã hoàn thành phân tích và áp style riêng biệt cho " + successCount + " Text Layer!");
}

function cleanOldCropFiles(folderPath) {
    var f = new Folder(folderPath);
    var files = f.getFiles("crop_*.png");
    for (var i = 0; i < files.length; i++) {
        files[i].remove();
    }
    var oldRes = new File(folderPath + "\\batch_result.json");
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

    // Fallback nếu ActionManager không trả về danh sách multi-select
    if (layers.length === 0) {
        if (doc.activeLayer) {
            if (doc.activeLayer.typename === "ArtLayer" && doc.activeLayer.kind === LayerKind.TEXT) {
                layers.push(doc.activeLayer);
            } else if (doc.activeLayer.typename === "LayerSet") {
                getAllTextLayers(doc.activeLayer, layers);
            }
        }
        // Nếu đang đứng ngoài, lấy toàn bộ text layer trong Group 1
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

function findLayer(doc, name) {
    var lower = name.toLowerCase();
    for (var i = 0; i < doc.layers.length; i++) {
        if (doc.layers[i].name.toLowerCase() === lower) {
            return doc.layers[i];
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

function applyExactVFXStyle(data) {
    try {
        var desc = new ActionDescriptor();
        var ref = new ActionReference();
        ref.putProperty(stringIDToTypeID("property"), stringIDToTypeID("layerEffects"));
        ref.putEnumerated(stringIDToTypeID("layer"), stringIDToTypeID("ordinal"), stringIDToTypeID("targetEnum"));
        desc.putReference(stringIDToTypeID("null"), ref);

        var lfxDesc = new ActionDescriptor();
        lfxDesc.putUnitDouble(stringIDToTypeID("scale"), stringIDToTypeID("percentUnit"), 100);

        var fillInfo = data.fill || {};
        var isGradient = (fillInfo.is_gradient === true);

        // --- 1. RUỘT CHỮ: SOLID COLOR ---
        var solidDesc = new ActionDescriptor();
        solidDesc.putBoolean(stringIDToTypeID("enabled"), !isGradient);
        solidDesc.putEnumerated(stringIDToTypeID("mode"), stringIDToTypeID("blendMode"), stringIDToTypeID("normal"));
        solidDesc.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), 100);

        var sSolidCol = hexToRGB(fillInfo.solid_hex || "#000000");
        var colSolid = new ActionDescriptor();
        colSolid.putDouble(stringIDToTypeID("red"), sSolidCol.red);
        colSolid.putDouble(stringIDToTypeID("green"), sSolidCol.green);
        colSolid.putDouble(stringIDToTypeID("blue"), sSolidCol.blue);
        solidDesc.putObject(stringIDToTypeID("color"), stringIDToTypeID("RGBColor"), colSolid);
        lfxDesc.putObject(stringIDToTypeID("solidFill"), stringIDToTypeID("solidFill"), solidDesc);

        // --- 2. RUỘT CHỮ: GRADIENT OVERLAY ---
        var gradDesc = new ActionDescriptor();
        gradDesc.putBoolean(stringIDToTypeID("enabled"), isGradient);
        gradDesc.putEnumerated(stringIDToTypeID("mode"), stringIDToTypeID("blendMode"), stringIDToTypeID("normal"));
        gradDesc.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), 100);
        gradDesc.putUnitDouble(stringIDToTypeID("angle"), stringIDToTypeID("angleUnit"), fillInfo.angle || 90);
        gradDesc.putEnumerated(stringIDToTypeID("type"), stringIDToTypeID("gradientType"), stringIDToTypeID("linear"));
        gradDesc.putBoolean(stringIDToTypeID("reverse"), false);
        gradDesc.putBoolean(stringIDToTypeID("align"), true);
        gradDesc.putUnitDouble(stringIDToTypeID("scale"), stringIDToTypeID("percentUnit"), 100);

        var topColor = hexToRGB(fillInfo.top_hex || "#FFF600");
        var botColor = hexToRGB(fillInfo.bottom_hex || "#FF8000");

        var grad = new ActionDescriptor();
        grad.putString(stringIDToTypeID("name"), "AI Gradient");
        grad.putEnumerated(stringIDToTypeID("gradientForm"), stringIDToTypeID("gradientForm"), stringIDToTypeID("customStops"));
        grad.putDouble(stringIDToTypeID("interfaceIconFrameDimmed"), 4096);

        var colors = new ActionList();
        var stop1 = new ActionDescriptor();
        var col1 = new ActionDescriptor();
        col1.putDouble(stringIDToTypeID("red"), botColor.red);
        col1.putDouble(stringIDToTypeID("green"), botColor.green);
        col1.putDouble(stringIDToTypeID("blue"), botColor.blue);
        stop1.putObject(stringIDToTypeID("color"), stringIDToTypeID("RGBColor"), col1);
        stop1.putEnumerated(stringIDToTypeID("type"), stringIDToTypeID("colorStopType"), stringIDToTypeID("userStop"));
        stop1.putInteger(stringIDToTypeID("location"), 0);
        stop1.putInteger(stringIDToTypeID("midpoint"), 50);
        colors.putObject(stringIDToTypeID("colorStop"), stop1);

        var stop2 = new ActionDescriptor();
        var col2 = new ActionDescriptor();
        col2.putDouble(stringIDToTypeID("red"), topColor.red);
        col2.putDouble(stringIDToTypeID("green"), topColor.green);
        col2.putDouble(stringIDToTypeID("blue"), topColor.blue);
        stop2.putObject(stringIDToTypeID("color"), stringIDToTypeID("RGBColor"), col2);
        stop2.putEnumerated(stringIDToTypeID("type"), stringIDToTypeID("colorStopType"), stringIDToTypeID("userStop"));
        stop2.putInteger(stringIDToTypeID("location"), 4096);
        stop2.putInteger(stringIDToTypeID("midpoint"), 50);
        colors.putObject(stringIDToTypeID("colorStop"), stop2);

        grad.putList(stringIDToTypeID("colors"), colors);

        var trans = new ActionList();
        var tr1 = new ActionDescriptor();
        tr1.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), 100);
        tr1.putInteger(stringIDToTypeID("location"), 0);
        tr1.putInteger(stringIDToTypeID("midpoint"), 50);
        trans.putObject(stringIDToTypeID("transferSpec"), tr1);

        var tr2 = new ActionDescriptor();
        tr2.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), 100);
        tr2.putInteger(stringIDToTypeID("location"), 4096);
        tr2.putInteger(stringIDToTypeID("midpoint"), 50);
        trans.putObject(stringIDToTypeID("transferSpec"), tr2);

        grad.putList(stringIDToTypeID("transparency"), trans);
        gradDesc.putObject(stringIDToTypeID("gradient"), stringIDToTypeID("gradient"), grad);
        lfxDesc.putObject(stringIDToTypeID("gradientFill"), stringIDToTypeID("gradientFill"), gradDesc);

        // --- 3. STROKE ---
        var strokeInfo = data.stroke || {};
        var hasStroke = (strokeInfo.enabled === true);

        var strokeDesc = new ActionDescriptor();
        strokeDesc.putBoolean(stringIDToTypeID("enabled"), hasStroke);
        strokeDesc.putEnumerated(stringIDToTypeID("style"), stringIDToTypeID("frameStyle"), stringIDToTypeID("outsetFrame"));
        strokeDesc.putEnumerated(stringIDToTypeID("paintType"), stringIDToTypeID("frameFill"), stringIDToTypeID("solidColor"));
        strokeDesc.putEnumerated(stringIDToTypeID("mode"), stringIDToTypeID("blendMode"), stringIDToTypeID("normal"));
        strokeDesc.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), 100);
        strokeDesc.putUnitDouble(stringIDToTypeID("size"), stringIDToTypeID("pixelsUnit"), strokeInfo.size_px || 2.5);

        var sCol = hexToRGB(strokeInfo.color_hex || "#000000");
        var colStroke = new ActionDescriptor();
        colStroke.putDouble(stringIDToTypeID("red"), sCol.red);
        colStroke.putDouble(stringIDToTypeID("green"), sCol.green);
        colStroke.putDouble(stringIDToTypeID("blue"), sCol.blue);
        strokeDesc.putObject(stringIDToTypeID("color"), stringIDToTypeID("RGBColor"), colStroke);
        lfxDesc.putObject(stringIDToTypeID("frameFX"), stringIDToTypeID("frameFX"), strokeDesc);

        // --- 4. OUTER GLOW ---
        var glowInfo = data.outer_glow || {};
        var hasGlow = (glowInfo.enabled === true);

        var glowDesc = new ActionDescriptor();
        glowDesc.putBoolean(stringIDToTypeID("enabled"), hasGlow);
        glowDesc.putEnumerated(stringIDToTypeID("mode"), stringIDToTypeID("blendMode"), stringIDToTypeID("normal"));
        glowDesc.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), glowInfo.opacity_percent || 80);

        var gCol = hexToRGB(glowInfo.color_hex || "#FFB300");
        var colGlow = new ActionDescriptor();
        colGlow.putDouble(stringIDToTypeID("red"), gCol.red);
        colGlow.putDouble(stringIDToTypeID("green"), gCol.green);
        colGlow.putDouble(stringIDToTypeID("blue"), gCol.blue);
        glowDesc.putObject(stringIDToTypeID("color"), stringIDToTypeID("RGBColor"), colGlow);

        glowDesc.putEnumerated(stringIDToTypeID("glowTechnique"), stringIDToTypeID("matteTechnique"), stringIDToTypeID("softMatte"));
        glowDesc.putUnitDouble(stringIDToTypeID("chokeMatte"), stringIDToTypeID("percentUnit"), 10);
        glowDesc.putUnitDouble(stringIDToTypeID("size"), stringIDToTypeID("pixelsUnit"), glowInfo.size_px || 8.0);
        lfxDesc.putObject(stringIDToTypeID("outerGlow"), stringIDToTypeID("outerGlow"), glowDesc);

        // --- 5. DROP SHADOW ---
        var shadowInfo = data.drop_shadow || {};
        var hasShadow = (shadowInfo.enabled === true);

        var shadowDesc = new ActionDescriptor();
        shadowDesc.putBoolean(stringIDToTypeID("enabled"), hasShadow);
        shadowDesc.putEnumerated(stringIDToTypeID("mode"), stringIDToTypeID("blendMode"), stringIDToTypeID("multiply"));

        var dCol = hexToRGB(shadowInfo.color_hex || "#000000");
        var colShadow = new ActionDescriptor();
        colShadow.putDouble(stringIDToTypeID("red"), dCol.red);
        colShadow.putDouble(stringIDToTypeID("green"), dCol.green);
        colShadow.putDouble(stringIDToTypeID("blue"), dCol.blue);
        shadowDesc.putObject(stringIDToTypeID("color"), stringIDToTypeID("RGBColor"), colShadow);

        shadowDesc.putUnitDouble(stringIDToTypeID("opacity"), stringIDToTypeID("percentUnit"), 60);
        shadowDesc.putBoolean(stringIDToTypeID("useGlobalAngle"), true);
        shadowDesc.putUnitDouble(stringIDToTypeID("localLightingAngle"), stringIDToTypeID("angleUnit"), 120);
        shadowDesc.putUnitDouble(stringIDToTypeID("distance"), stringIDToTypeID("pixelsUnit"), shadowInfo.distance_px || 4.0);
        shadowDesc.putUnitDouble(stringIDToTypeID("blur"), stringIDToTypeID("pixelsUnit"), shadowInfo.blur_px || 4.0);
        lfxDesc.putObject(stringIDToTypeID("dropShadow"), stringIDToTypeID("dropShadow"), shadowDesc);

        desc.putObject(stringIDToTypeID("to"), stringIDToTypeID("layerEffects"), lfxDesc);
        executeAction(stringIDToTypeID("set"), desc, DialogModes.NO);
    } catch (e) {
        alert("Lỗi khi áp VFX Layer Style: " + e.message);
    }
}

main();
