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
    var rawLayer = findRawLayer(doc);
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
    // Ưu tiên thư mục repo do launcher (cài trong Photoshop\Presets\Scripts) truyền vào
    var scriptFolder = ($.global.AI_TYPESET_DIR) ? new Folder($.global.AI_TYPESET_DIR).fsName : new File($.fileName).parent.fsName;
    var cropPath = scriptFolder + "\\temp_crop.png";
    var resultPath = scriptFolder + "\\style_result.json";
    var pyPath = scriptFolder + "\\style_analyzer.py";

    if (!File(pyPath).exists) {
        alert("Không tìm thấy style_analyzer.py tại:\n" + scriptFolder + "\nHãy chạy lại install_to_photoshop.bat.");
        return;
    }

    // 5. TẠM ẨN GROUP 1, CÁC LAYER CLEAN/REDRAW & BẬT RAW ĐỂ LƯU ẢNH CROP NÉT CHỮ GỐC
    var prevRawVisible = rawLayer ? rawLayer.visible : true;
    var prevGroup1Visible = group1 ? group1.visible : true;

    // Tạm ẩn các layer clean/redraw nếu có để copy trọn vẹn nét chữ gốc trên raw
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
    for (var c = 0; c < hiddenCleanLayers.length; c++) {
        hiddenCleanLayers[c].visible = true;
    }

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
    if (targetTextLayer && targetTextLayer.kind === LayerKind.TEXT) {
        try {
            if (targetTextLayer.textItem.contents && targetTextLayer.textItem.contents.indexOf("\u2015") !== -1) {
                targetTextLayer.textItem.contents = targetTextLayer.textItem.contents.replace(/\u2015/g, "—");
            }
        } catch (eNorm) {}
    }

    if (targetTextLayer && targetTextLayer.kind === LayerKind.TEXT && styleData.fill) {
        try {
            var tColor = new SolidColor();
            var fillHex = styleData.fill.solid_hex || (styleData.fill.is_gradient ? styleData.fill.bottom_hex : "#FFFFFF");
            var rgbVal = hexToRGB(fillHex);
            tColor.rgb.red = rgbVal.red;
            tColor.rgb.green = rgbVal.green;
            tColor.rgb.blue = rgbVal.blue;
            targetTextLayer.textItem.color = tColor;
        } catch (e) {}
    }

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
        // 1. Luôn dọn sạch toàn bộ layer effects cũ trước để triệt tiêu mọi hiệu ứng dư thừa
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

        // --- 2. STROKE (CHỈ THÊM KHI CÓ VIỀN) ---
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
            colShadow.putDouble(s2t("green"), shCol.green);
            colShadow.putDouble(s2t("blue"), shCol.blue);
            shadowDesc.putObject(s2t("color"), s2t("RGBColor"), colShadow);

            shadowDesc.putUnitDouble(s2t("angle"), s2t("angleUnit"), 120);
            shadowDesc.putBoolean(s2t("useGlobalAngle"), false);
            shadowDesc.putUnitDouble(s2t("distance"), s2t("pixelsUnit"), shadowInfo.distance_px || 4.0);
            shadowDesc.putUnitDouble(s2t("chokeMatte"), s2t("percentUnit"), 0);
            shadowDesc.putUnitDouble(s2t("size"), s2t("pixelsUnit"), shadowInfo.blur_px || 4.0);
            lfxDesc.putObject(s2t("dropShadow"), s2t("dropShadow"), shadowDesc);
            effectCount++;
        }

        // Nếu không có hiệu ứng nào cần áp (chữ đen phẳng thông thường):
        // clearLayerStyle() ở trên đã xóa sạch 100%, layer sạch tinh tươm!
        if (effectCount === 0) {
            return;
        }

        var desc = new ActionDescriptor();
        var ref = new ActionReference();
        ref.putProperty(s2t("property"), s2t("layerEffects"));
        ref.putEnumerated(s2t("layer"), s2t("ordinal"), s2t("targetEnum"));
        desc.putReference(s2t("null"), ref);
        desc.putObject(s2t("to"), s2t("layerEffects"), lfxDesc);
        executeAction(s2t("set"), desc, DialogModes.NO);
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

function findRawLayer(doc) {
    var names = ["raw", "background", "ảnh gốc", "layer 0", "raw_image", "bg", "gốc"];
    for (var k = 0; k < names.length; k++) {
        var lyr = findLayer(doc, names[k]);
        if (lyr) return lyr;
    }
    // Lấy layer dưới cùng không phải text và không phải group
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

main();
