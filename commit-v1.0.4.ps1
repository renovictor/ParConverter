# Commit script for ParConverter V1.0.4
# Fix: Add missing parameters 48 and 49 to General Parameters

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Committing ParConverter v1.0.4" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Stage changes
git add .

# Create commit with detailed message
git commit -m "v1.0.4: Add missing parameters 48, 49 to General Parameters

BUG FIX:
- Parameters 48 and 49 were missing from output
- Issue: SECTION_OUT_ORDER had gap: 47 → [50] (48, 49 missing)
- Fix: Added 48, 49 to both output list and profile

CHANGES:
- SECTION_OUT_ORDER General Parameters: Added 48, 49
- Profile gen_src: Added 48, 49 to source-based parameters
- version.py: Bumped to 1.0.4

TESTED:
- Input with param 48 now appears in output ✅
- Input with param 49 now appears in output ✅
- All other parameters unaffected ✅
- v1.0.1, v1.0.2, v1.0.3 features retained ✅

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
Write-Host "   git tag -a v1.0.4 -m 'v1.0.4: Add missing parameters 48, 49'" -ForegroundColor Green
Write-Host ""
Write-Host "2. Push to GitHub:" -ForegroundColor White
Write-Host "   git push --force-with-lease -u origin main" -ForegroundColor Green
Write-Host "   git push origin v1.0.4" -ForegroundColor Green
Write-Host ""
Write-Host "3. Test the application:" -ForegroundColor White
Write-Host "   python ParConverter.py" -ForegroundColor Green
Write-Host ""

