# Build script for ParConverter V1.0.0
# Creates a single executable file

Write-Host "Installing PyInstaller..." -ForegroundColor Cyan
python -m pip install pyinstaller --quiet

Write-Host "Generating spec file..." -ForegroundColor Cyan
pyinstaller --onefile --windowed --name ParConverter ParConverter.py --specpath .

Write-Host "Building ParConverter executable..." -ForegroundColor Cyan
pyinstaller ParConverter.spec

Write-Host ""
Write-Host "Build complete!" -ForegroundColor Green
Write-Host "Executable location: dist\ParConverter.exe" -ForegroundColor Yellow
Write-Host ""

