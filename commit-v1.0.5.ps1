# Commit script for ParConverter V1.0.5
# Fix: Add Quantum and Tykon as option to convert

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Committing ParConverter v1.0.5" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Stage changes
git add .

# Create commit with detailed message
git commit -m "v1.0.5: Add Quantum and Tykon as conversion options

BUG FIX:
- Add Quantum and Tykon as options to convert to
- Issue1: Quantum par : 1, 70 , 2, 1010; Tykon par : 1, 70 , 2, 1010; were not recognized as valid output formats
- Issue2: Quantum has distinct sections as // HF Match Params and // LF Match Params.
- Fix: Added pull down manu to select output format (Quantum, Tykon, or default)

CHANGES:
- Format option between Quantum and Tykon added to GUI
- Parameter mapping updated to support Quantum and Tykon formats
- version.py: Bumped to 1.0.5

TESTED:
- Input with Tykon now appears in output ✅
- Input with Quantum now appears in output ✅
- All other parameters unaffected ✅
- v1.0.1, v1.0.2, v1.0.3, v1.0.4 features retained ✅

General Parameters now complete: 2-72 (with documented gaps: 1, 5, 12, 36)
"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Commit created!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Tag the commit:" -ForegroundColor White
Write-Host "   git tag -a v1.0.5 -m 'v1.0.5: Add pull down manu to select Quantum and Tykon.'" -ForegroundColor Green
Write-Host ""
Write-Host "2. Push to GitHub:" -ForegroundColor White
Write-Host "   git push --force-with-lease -u origin main" -ForegroundColor Green
Write-Host "   git push origin v1.0.5" -ForegroundColor Green
Write-Host ""
Write-Host "3. Test the application:" -ForegroundColor White
Write-Host "   python ParConverter.py" -ForegroundColor Green
Write-Host ""

