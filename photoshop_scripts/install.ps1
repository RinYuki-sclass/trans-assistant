param([switch]$Elevated)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# ---------------------------------------------------------------------
# 1. TỰ ĐỘNG XIN QUYỀN ADMIN (UAC) - cần để ghi vào C:\Program Files\Adobe\...
# ---------------------------------------------------------------------
$principal = [Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
$isAdmin = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "Cần quyền Administrator để ghi vào thư mục Photoshop. Đang yêu cầu UAC..." -ForegroundColor Yellow
    try {
        $argList = "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`" -Elevated"
        $proc = Start-Process -FilePath "powershell.exe" -ArgumentList $argList -Verb RunAs -PassThru -Wait
        Write-Host "Cửa sổ cài đặt (Admin) đã đóng. Mã thoát: $($proc.ExitCode)" -ForegroundColor Gray
    } catch {
        Write-Host "  [X] Bạn đã từ chối quyền Admin. Hủy cài đặt." -ForegroundColor Red
        Write-Host "      Cách khác: chuột phải install_to_photoshop.bat -> Run as administrator." -ForegroundColor Yellow
    }
    exit
}

Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "    CÀI ĐẶT BỘ TOOL PHOTOSHOP AI TYPESET (F6: Đơn lẻ | F7: Multi-Batch)" -ForegroundColor Yellow
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
# Đường dẫn repo dạng '/' cho ExtendScript
$jsDir = ($scriptDir -replace '\\', '/')

# Chỉ cài LAUNCHER (.jsx nhỏ) vào Photoshop. Script thật, file .py, file tạm
# và .env vẫn nằm ở repo (thư mục ghi được) => không lỗi quyền khi chạy F6/F7.
$launchers = @("AutoStyleFromSelection.jsx", "BatchStyleFromSelection.jsx")
# File cũ (bản cài trước copy thẳng vào Photoshop) cần dọn
$legacyFiles = @("style_analyzer.py", "batch_analyzer.py", "temp_crop.png", "style_result.json", "batch_result.json")

foreach ($l in $launchers) {
    if (-not (Test-Path (Join-Path $scriptDir $l))) {
        Write-Host "  [X] Thiếu file nguồn: $(Join-Path $scriptDir $l)" -ForegroundColor Red
    }
}

Write-Host "Đang quét các phiên bản Photoshop trên máy tính..." -ForegroundColor Gray
Write-Host ""

$installed = 0
$failed = 0
$scanned = 0
$rawPaths = [System.Collections.Generic.List[string]]::new()

try {
    $regApp = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Photoshop.exe" -ErrorAction SilentlyContinue).Path
    if ($regApp) { $rawPaths.Add($regApp) }
} catch {}

try {
    $regUninst = Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*", "HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" -ErrorAction SilentlyContinue |
        Where-Object { $_.DisplayName -like "*Photoshop*" } |
        ForEach-Object { $_.InstallLocation }
    foreach ($p in $regUninst) { if ($p) { $rawPaths.Add($p) } }
} catch {}

$commonFolders = @(
    "D:\Creative cloud",
    "C:\Program Files\Adobe",
    "D:\Program Files\Adobe",
    "C:\Program Files (x86)\Adobe"
)

foreach ($folder in $commonFolders) {
    if (Test-Path $folder) {
        $subDirs = Get-ChildItem -Path $folder -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -like "*Photoshop*" } |
            ForEach-Object { $_.FullName }
        foreach ($s in $subDirs) { $rawPaths.Add($s) }
    }
}

$uniquePaths = $rawPaths |
    Where-Object { $_ -and (Test-Path $_) } |
    ForEach-Object { [System.IO.Path]::GetFullPath($_).TrimEnd('\', '/') } |
    Select-Object -Unique

$utf8Bom = New-Object System.Text.UTF8Encoding($true)

foreach ($psDir in $uniquePaths) {
    $destDir = Join-Path $psDir "Presets\Scripts"
    if (-not (Test-Path $destDir)) { continue }
    $scanned++
    try {
        foreach ($l in $launchers) {
            $target = "$jsDir/$l"
            $stub = @"
// AI Typeset launcher - được tạo tự động bởi install.ps1. KHÔNG sửa file này.
// Script thật nằm tại: $target
#target photoshop
`$.global.AI_TYPESET_DIR = "$jsDir";
(function () {
    var f = new File("$target");
    if (!f.exists) {
        alert("Không tìm thấy script gốc:\n" + f.fsName + "\nHãy chạy lại install_to_photoshop.bat.");
        return;
    }
    try { `$.evalFile(f); } catch (e) { alert("Lỗi khi chạy $($l):\n" + e.message + " (line " + e.line + ")"); }
})();
"@
            [System.IO.File]::WriteAllText((Join-Path $destDir $l), $stub, $utf8Bom)
        }
        foreach ($old in $legacyFiles) {
            $op = Join-Path $destDir $old
            if (Test-Path $op) { Remove-Item $op -Force -ErrorAction SilentlyContinue }
        }
        Write-Host "  [V] ĐÃ CÀI ĐẶT THÀNH CÔNG VÀO:" -ForegroundColor Green
        Write-Host "      $destDir" -ForegroundColor Cyan
        $installed++
    } catch {
        Write-Host "  [X] Không thể ghi file vào: $destDir" -ForegroundColor Red
        Write-Host "      $($_.Exception.Message)" -ForegroundColor DarkRed
        $failed++
    }
}

Write-Host ""
if ($scanned -eq 0) {
    Write-Host "  [!] Không tìm thấy thư mục Presets\Scripts của Photoshop!" -ForegroundColor Yellow
} elseif ($installed -eq 0) {
    Write-Host "  [!] Tìm thấy $scanned bản Photoshop nhưng KHÔNG ghi được file nào (kiểm tra quyền / tắt Photoshop rồi thử lại)." -ForegroundColor Yellow
} else {
    Write-Host ">> TỔNG CỘNG ĐÃ CÀI ĐẶT THÀNH CÔNG VÀO $installed PHIÊN BẢN PHOTOSHOP! <<" -ForegroundColor Green
    if ($failed -gt 0) { Write-Host "   ($failed thư mục bị lỗi, xem chi tiết phía trên)" -ForegroundColor Yellow }
    Write-Host "   Script gốc + file tạm nằm tại: $scriptDir" -ForegroundColor Gray
}

Write-Host ""
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "HƯỚNG DẪN GÁN PHÍM TẮT TRONG PHOTOSHOP:" -ForegroundColor Yellow
Write-Host "1. Khởi động lại Photoshop (hoặc mở Photoshop lên)."
Write-Host "2. Nhấn Ctrl + Alt + Shift + K (Keyboard Shortcuts)."
Write-Host "3. Mở File -> Scripts:"
Write-Host "   - AutoStyleFromSelection   -> Gán phím: F6 (Khoanh 1 chữ đơn lẻ)"
Write-Host "   - BatchStyleFromSelection  -> Gán phím: F7 (Multi-Select nhiều Text Layer)"
Write-Host "4. Nhấn Accept -> OK."
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""

if ($Elevated) { Read-Host "Nhấn Enter để đóng cửa sổ" | Out-Null }
