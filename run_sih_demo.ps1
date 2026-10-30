# run_sih_demo.ps1
# Script to compile and run the BharatOpt-X engine for SIH Demo

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Building BharatOpt-X Core Engine       " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Setup DevShell Environment (Required for correct VS/CMake paths)
Import-Module "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Microsoft.VisualStudio.DevShell.dll" -ErrorAction SilentlyContinue
Enter-VsDevShell -VsInstallPath "C:\Program Files\Microsoft Visual Studio\2022\Community" -SkipAutomaticLocation -Arch amd64 -ErrorAction SilentlyContinue
$env:PATH = "C:\Users\rohan\AppData\Local\Android\Sdk\cmake\3.22.1\bin;" + $env:PATH

# Build Project
Write-Host "`n[1/3] Running CMake Build..." -ForegroundColor Yellow
if (!(Test-Path -Path "build")) {
    New-Item -ItemType Directory -Path "build" | Out-Null
}
Set-Location -Path "build"
cmake .. 
cmake --build .

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[ERROR] Build Failed!" -ForegroundColor Red
    Set-Location -Path ".."
    exit $LASTEXITCODE
}

Write-Host "`n[2/3] Running Demo Executable..." -ForegroundColor Yellow
Set-Location -Path ".."
# Run from root so data/test_model.mps is found relative to CWD
.\build\Debug\bharatopt_engine.exe

Write-Host "`n[3/3] Running Final System Tests..." -ForegroundColor Yellow
Set-Location -Path "build"
ctest -C Debug --output-on-failure
Set-Location -Path ".."

Write-Host "`n========================================" -ForegroundColor Green
Write-Host " SIH Demo Execution Completed Successfully" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "`nTo start the ML Sidecar, run:"
Write-Host "  pip install -r requirements.txt"
Write-Host "  python services/gnn/inference_service.py"
Write-Host "`nTo view the UI, open:"
Write-Host "  web/index.html in your browser`n"
