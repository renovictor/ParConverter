# Commit script for ParConverter V1.0.2
# Critical bug fix: Input-driven output (omit parameters not in input data)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Committing ParConverter v1.0.2" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Stage changes
git add .

# Create commit with detailed message
git commit -m "v1.0.2: Fix critical bug - Input-driven output (skip missing parameters)

CRITICAL BUG FIX:
- Parameters NOT in input no longer output with constant values
- Issue: v1.0.1 forced output of hardcoded constants (e.g., param 13 = 10000)
  even when param 13 didn't exist in input data
- Fix: Implemented input-driven output with 'if oid not in in_map: continue'

CHANGES:
- Only parameters present in input are processed and output
- Predefined constants only output if parameter exists in input
- Unknown parameters still auto-detected and appended (v1.0.1 feature retained)

BEHAVIOR CHANGE:
- v1.0.1: Outputs param 13 as 10000 (forced constant)
- v1.0.2: Omits param 13 entirely if not in input (correct behavior)

TESTING:
- Input with param 13 absent, param 5 present
- Expected: param 13 omitted, param 5 output with correct value
- Verified: Working as expected

Updated files:
- ParConverter.py: compute_converted_text() function
- version.py: Bumped to 1.0.2
- CHANGELOG.md: Detailed release notes
"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Commit created!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Tag the commit:" -ForegroundColor White
Write-Host "   git tag -a v1.0.2 -m 'Version 1.0.2: Input-driven output fix'" -ForegroundColor Green
Write-Host ""
Write-Host "2. Push to GitHub:" -ForegroundColor White
Write-Host "   git push --force-with-lease -u origin main" -ForegroundColor Green
Write-Host "   git push origin v1.0.2" -ForegroundColor Green
Write-Host ""
Write-Host "3. Verify:" -ForegroundColor White
Write-Host "   git log --oneline -5" -ForegroundColor Green
Write-Host "   git tag -l" -ForegroundColor Green
Write-Host ""

