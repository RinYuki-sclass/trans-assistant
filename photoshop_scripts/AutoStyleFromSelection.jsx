/**
 * AutoStyleFromSelection.jsx - AI Vision VFX Engine (Chỉ bật hiệu ứng THỰC SỰ CÓ)
 * Phím tắt: F6
 */

#target photoshop

function main() {
    if (app.documents.length === 0) {
        alert("Chưa mở file PSD nào!");
        return;
    }

    var doc = app.activeDocument;

    // 1. Kiểm tra vùng chọn
    var hasSelection = false;
    try {
        var bounds = doc.selection.bounds;
        hasSelection = true;
    } catch (e) {
        hasSelection = false;
    }

    if (!hasSelection) {
        alert("Vui lòng dùng Marquee (M) khoanh vùng chữ raw trước khi bấm F6!");
        return;
    }

    // 2. Tìm Layer 'raw' và 'Group 1'
    var rawLayer = findLayer(doc, "raw");
    var group1 = findLayer(doc, "Group 1");

    var selBounds = doc.selection.bounds;
    var x1 = selBounds[0].as('px');
    var y1 = selBounds[1].as('px');
    var x2 = selBounds[2].as('px');
    var y2 = selBounds[3].as('px');
    var w = Math.round(x2 - x1);
    var h = Math.round(y2 - y1);

    if (w < 4 || h < 4) {
        alert("Vùng chọn quá nhỏ!");
        return;
    }

    // 3. Xác định Text Layer mục tiêu trong Group 1
    var targetTextLayer = null;
    if (doc.activeLayer && doc.activeLayer.kind === LayerKind.TEXT) {
        targetTextLayer = doc.activeLayer;
    } else if (group1 && group1.typename === "LayerSet") {
        targetTextLayer = findBestMatchingTextLayer(group1, x1, y1, x2, y2);
    }
    if (!targetTextLayer) targetTextLayer = doc.activeLayer;

    if (!targetTextLayer) {
        alert("Vui lòng click chọn Text Layer cần áp style trước khi bấm F6.");
        return;
    }

    // 4. Đường dẫn thư mục script
    var thisFile = new File($.fileName);
    var scriptFolder = thisFile.parent.fsName;
    var cropPath = scriptFolder + "\\temp_crop.png";
    var resultPath = scriptFolder + "\\style_result.json";
    var pyPath = scriptFolder + "\\style_analyzer.py";

    if (!File(pyPath).exists) {
        pyPath = "d:\\Nhung\\RIDI\\trans-assistant\\photoshop_scripts\\style_analyzer.py";
        cropPath = "d:\\Nhung\\RIDI\\trans-assistant\\photoshop_scripts\\temp_crop.png";
        resultPath = "d:\\Nhung\\RIDI\\trans-assistant\\photoshop_scripts\\style_result.json";
    }

    // 5. TẠM ẨN GROUP 1 & BẬT RAW ĐỂ LƯU ẢNH CROP NÉT CHỮ GỐC
    var prevRawVisible = rawLayer ? rawLayer.visible : true;
    var prevGroup1Visible = group1 ? group1.visible : true;

    if (group1) group1.visible = false;
    if (rawLayer) {
        rawLayer.visible = true;
        doc.activeLayer = rawLayer;
    }
    app.refresh();

    // Copy merged vùng chọn chữ raw
    try {
        doc.selection.copy(true);
    } catch (e) {
        doc.selection.copy();
    }

    // Tạo document tạm để lưu ảnh crop ra PNG
    var tempDoc = app.documents.add(w, h, doc.resolution, "TempCrop", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
    tempDoc.paste();
    var cropFile = new File(cropPath);
    var pngSaveOpts = new PNGSaveOptions();
    tempDoc.saveAs(cropFile, pngSaveOpts, true, Extension.LOWERCASE);
    tempDoc.close(SaveOptions.DONOTSAVECHANGES);

    // Khôi phục hiển thị trên Document chính
    app.activeDocument = doc;
    if (group1) group1.visible = true;
    if (rawLayer) rawLayer.visible = prevRawVisible;

    targetTextLayer.visible = true;
    doc.activeLayer = targetTextLayer;

    // Bỏ vùng chọn
    try { doc.selection.deselect(); } catch (e) {}

    // 6. GỌI GEMINI VISION AI ENGINE
    var cmd = 'cmd /c python "' + pyPath + '" "' + cropPath + '" "' + resultPath + '"';
    app.system(cmd);

    // 7. ĐỌC KẾT QUẢ TỪ FILE JSON CỦA VISION AI
    var resFile = new File(resultPath);
    if (!resFile.exists) {
        alert("Lỗi: Không tìm thấy kết quả từ AI Engine!");
        return;
    }

    resFile.open("r");
    var jsonText = resFile.read();
    resFile.close();

    var styleData;
    try {
        styleData = eval("(" + jsonText + ")");
    } catch (e) {
        alert("Lỗi đọc dữ liệu JSON từ AI!");
        return;
    }

    // 8. ÁP DỤNG ĐÚNG CÁC HIỆU ỨNG (KHÔNG ÉP BUỘC)
    applyExactVFXStyle(styleData);
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

        // --- 1. RUỘT CHỮ: NẾU LÀ MÀU ĐƠN THUẦN (SOLID COLOR) ---
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

        // --- 2. RUỘT CHỮ: NẾU LÀ GRADIENT OVERLAY ---
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

        // --- 3. STROKE (CHỈ BẬT KHI AI BẢO CÓ THỰC SỰ) ---
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

        // --- 5. DROP SHADOW (CHỈ BẬT KHI AI BẢO CÓ THỰC SỰ) ---
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

function findBestMatchingTextLayer(group, selX1, selY1, selX2, selY2) {
    var selCenterX = (selX1 + selX2) / 2;
    var selCenterY = (selY1 + selY2) / 2;
    var bestLayer = null;
    var maxOverlap = 0;
    var minDistance = 999999;

    var textLayers = [];
    getAllTextLayers(group, textLayers);

    for (var i = 0; i < textLayers.length; i++) {
        var lyr = textLayers[i];
        try {
            var b = lyr.bounds;
            var lx1 = b[0].as('px');
            var ly1 = b[1].as('px');
            var lx2 = b[2].as('px');
            var ly2 = b[3].as('px');

            var interX1 = Math.max(selX1, lx1);
            var interY1 = Math.max(selY1, ly1);
            var interX2 = Math.min(selX2, lx2);
            var interY2 = Math.min(selY2, ly2);

            if (interX2 > interX1 && interY2 > interY1) {
                var overlap = (interX2 - interX1) * (interY2 - interY1);
                if (overlap > maxOverlap) {
                    maxOverlap = overlap;
                    bestLayer = lyr;
                }
            }

            var lyrCenterX = (lx1 + lx2) / 2;
            var lyrCenterY = (ly1 + ly2) / 2;
            var dist = Math.sqrt(Math.pow(selCenterX - lyrCenterX, 2) + Math.pow(selCenterY - lyrCenterY, 2));

            if (dist < minDistance) {
                minDistance = dist;
                if (maxOverlap === 0) bestLayer = lyr;
            }
        } catch (e) {}
    }

    if (maxOverlap === 0 && minDistance > 600) return null;
    return bestLayer;
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

main();
