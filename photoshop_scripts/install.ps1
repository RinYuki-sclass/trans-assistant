[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "    CÀI ĐẶT BỘ TOOL PHOTOSHOP AI TYPESET (F6: Đơn lẻ | F7: Multi-Batch)" -ForegroundColor Yellow
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$filesToDeploy = @(
    "AutoStyleFromSelection.jsx",
    "BatchStyleFromSelection.jsx",
    "style_analyzer.py",
    "batch_analyzer.py"
)

Write-Host "Đang quét các phiên bản Photoshop trên máy tính..." -ForegroundColor Gray
Write-Host ""

$found = 0
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

foreach ($psDir in $uniquePaths) {
    $destDir = Join-Path $psDir "Presets\Scripts"
    if (Test-Path $destDir) {
        try {
            foreach ($f in $filesToDeploy) {
                $src = Join-Path $scriptDir $f
                if (Test-Path $src) {
                    $dst = Join-Path $destDir $f
                    Copy-Item -Path $src -Destination $dst -Force
                }
            }
            Write-Host "  [V] ĐÃ CÀI ĐẶT THÀNH CÔNG VÀO:" -ForegroundColor Green
            Write-Host "      $destDir" -ForegroundColor Cyan
            $found++
        } catch {
            Write-Host "  [X] Không thể ghi file vào: $destDir" -ForegroundColor Red
        }
    }
}

Write-Host ""
if ($found -eq 0) {
    Write-Host "  [!] Không tìm thấy thư mục Presets\Scripts của Photoshop!" -ForegroundColor Yellow
} else {
    Write-Host ">> TỔNG CỘNG ĐÃ CÀI ĐẶT THÀNH CÔNG VÀO $found PHIÊN BẢN PHOTOSHOP! <<" -ForegroundColor Green
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
