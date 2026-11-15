#target photoshop

/**
 * Script Paste & Replace Text Manhwa cho Photoshop
 * - Mở hộp thoại trực tiếp để bạn Copy & Paste (Ctrl + V) thoại từ Excel, Sheets, Subtitle tool
 * - Tự động nhận diện folder Group 1
 * - Tự động đếm và báo số câu thoại nhận diện được so với số Text Layer
 * - Hỗ trợ lọc bỏ số thứ tự đầu dòng (1., 2., 3...)
 * - Giữ nguyên 100% Font, Size, Warp, Vị trí và Layer Styles (Stroke, Shadow...)
 */

function main() {
    if (app.documents.length === 0) {
        alert("Vui lòng mở file PSD cần thay text trước!");
        return;
    }

    var doc = app.activeDocument;

    // 1. Tìm folder Group 1
    var targetGroup = null;
    try {
        targetGroup = doc.layerSets.getByName("Group 1");
    } catch (e) {
        for (var i = 0; i < doc.layerSets.length; i++) {
            var grp = doc.layerSets[i];
            for (var j = 0; j < grp.artLayers.length; j++) {
                if (grp.artLayers[j].kind === LayerKind.TEXT) {
                    targetGroup = grp;
                    break;
                }
            }
            if (targetGroup) break;
        }
    }

    if (!targetGroup) {
        alert("Không tìm thấy folder 'Group 1' trong file PSD!");
        return;
    }

    // 2. Thu thập Text Layer trong Group
    var textLayers = [];
    for (var i = 0; i < targetGroup.artLayers.length; i++) {
        var lyr = targetGroup.artLayers[i];
        if (lyr.kind === LayerKind.TEXT) {
            textLayers.push(lyr);
        }
    }

    if (textLayers.length === 0) {
        alert("Không có Text Layer nào bên trong folder '" + targetGroup.name + "'!");
        return;
    }

    // Chuẩn bị text mẫu để xem trước thứ tự
    var topSample = textLayers[0].textItem.contents.replace(/\r?\n/g, ' ').substring(0, 24);
    var bottomSample = textLayers[textLayers.length - 1].textItem.contents.replace(/\r?\n/g, ' ').substring(0, 24);

    // 3. Hàm xử lý tách text
    function parseText(rawText, isEachLine, removeNumbers) {
        if (!rawText || rawText.replace(/^\s+|\s+$/g, '').length === 0) {
            return [];
        }

        var list = [];
        if (isEachLine) {
            // Tách theo từng dòng (chuẩn Excel / Google Sheets)
            var lines = rawText.split(/\r?\n/);
            for (var k = 0; k < lines.length; k++) {
                var s = lines[k].replace(/^\s+|\s+$/g, '');
                if (s.length > 0) {
                    // Bỏ dấu ngoặc kép của cell Excel nếu có
                    if (s.charAt(0) === '"' && s.charAt(s.length - 1) === '"') {
                        s = s.substring(1, s.length - 1).replace(/""/g, '"');
                    }
                    if (removeNumbers) {
                        s = s.replace(/^\[?\d+\]?[\.\:\)\-\t\s]+\s*/, '');
                    }
                    if (s.length > 0) list.push(s);
                }
            }
        } else {
            // Tách theo dòng trống hoặc dấu '---'
            var blocks = [];
            if (rawText.indexOf("---") !== -1) {
                blocks = rawText.split(/\r?\n---\r?\n/);
            } else {
                blocks = rawText.split(/\r?\n\s*\r?\n/);
            }
            for (var m = 0; m < blocks.length; m++) {
                var b = blocks[m].replace(/^\s+|\s+$/g, '');
                if (b.length > 0) {
                    if (removeNumbers) {
                        b = b.replace(/^\[?\d+\]?[\.\:\)\-\t\s]+\s*/, '');
                    }
                    list.push(b);
                }
            }
        }
        return list;
    }

    // 4. Tạo giao diện UI hộp thoại
    var dlg = new Window("dialog", "Paste & Replace Text Manhwa");
    dlg.orientation = "column";
    dlg.alignChildren = ["fill", "top"];
    dlg.preferredSize.width = 540;

    // Panel 1: Thứ tự nạp
    var pnlOrder = dlg.add("panel", undefined, "1. Thứ tự khớp Layer trong Group 1 (Tổng: " + textLayers.length + " layer)");
    pnlOrder.orientation = "column";
    pnlOrder.alignChildren = ["left", "top"];
    var rbBottomUp = pnlOrder.add("radiobutton", undefined, "Từ Dưới lên Trên (Bắt đầu từ: \"" + bottomSample + "...\")");
    var rbTopDown = pnlOrder.add("radiobutton", undefined, "Từ Trên xuống Dưới (Bắt đầu từ: \"" + topSample + "...\")");
    rbBottomUp.value = true; // Khuyên dùng

    // Panel 2: Khung Paste Text
    var pnlPaste = dlg.add("panel", undefined, "2. Dán nội dung bản dịch vào đây (Ctrl + V):");
    pnlPaste.orientation = "column";
    pnlPaste.alignChildren = ["fill", "top"];

    var txtInput = pnlPaste.add("edittext", [0, 0, 500, 180], "", {multiline: true, scrollable: true});
    txtInput.active = true;

    // Tùy chọn phân tách
    var grpOptions = pnlPaste.add("group");
    grpOptions.orientation = "row";
    grpOptions.alignChildren = ["left", "center"];
    var rbEachLine = grpOptions.add("radiobutton", undefined, "Mỗi dòng là 1 thoại (Excel / Sheets)");
    var rbBlocks = grpOptions.add("radiobutton", undefined, "Cách nhau bởi dòng trống / '---'");
    rbEachLine.value = true;

    var chkRemoveNum = pnlPaste.add("checkbox", undefined, "Tự động xóa số thứ tự đầu dòng (1., 2., 3... nếu copy cả cột STT)");
    chkRemoveNum.value = true;

    // Label trạng thái đếm số câu
    var lblStatus = dlg.add("statictext", undefined, "💡 Đã nhận diện: 0 câu thoại | Cần thay: " + textLayers.length + " layer");
    lblStatus.graphics.foregroundColor = lblStatus.graphics.newPen(lblStatus.graphics.PenType.SOLID_COLOR, [0, 0.45, 0.9, 1], 1);

    function refreshStatus() {
        var parsed = parseText(txtInput.text, rbEachLine.value, chkRemoveNum.value);
        var matchCount = Math.min(parsed.length, textLayers.length);
        lblStatus.text = "💡 Đã nhận diện: " + parsed.length + " câu thoại | Sẽ thay thế: " + matchCount + "/" + textLayers.length + " layer";
    }

    txtInput.onChanging = refreshStatus;
    rbEachLine.onClick = refreshStatus;
    rbBlocks.onClick = refreshStatus;
    chkRemoveNum.onClick = refreshStatus;

    // Hàng nút bấm
    var grpButtons = dlg.add("group");
    grpButtons.alignment = "right";
    var btnOk = grpButtons.add("button", undefined, "Bắt Đầu Thay Thế", {name: "ok"});
    var btnCancel = grpButtons.add("button", undefined, "Hủy", {name: "cancel"});

    // 5. Khi bấm Thay Thế
    if (dlg.show() === 1) {
        var finalTexts = parseText(txtInput.text, rbEachLine.value, chkRemoveNum.value);

        if (finalTexts.length === 0) {
            alert("Bạn chưa dán nội dung nào vào khung text!");
            return;
        }

        var orderedLayers = [];
        if (rbBottomUp.value) {
            for (var k = textLayers.length - 1; k >= 0; k--) {
                orderedLayers.push(textLayers[k]);
            }
        } else {
            orderedLayers = textLayers;
        }

        var replaceCount = Math.min(orderedLayers.length, finalTexts.length);

        // Gom vào 1 bước History để có thể Ctrl+Z hoàn tác ngay lập tức
        doc.suspendHistory("Batch Paste Comic Text", "applyPastedText()");

        function applyPastedText() {
            for (var m = 0; m < replaceCount; m++) {
                orderedLayers[m].textItem.contents = finalTexts[m];
            }
        }

        var resultMsg = "Đã cập nhật thành công " + replaceCount + " bóng thoại!\n";
        resultMsg += "• Giữ nguyên 100% Font, Size, Warp, Vị trí & Hiệu ứng viền/bóng.\n";
        if (orderedLayers.length !== finalTexts.length) {
            resultMsg += "\n⚠️ Lưu ý: Trong Group có " + orderedLayers.length + " layer, bạn đã dán " + finalTexts.length + " câu thoại.";
        }
        alert(resultMsg);
    }
}

main();
