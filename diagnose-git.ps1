# Diagnostic Script - Check Git Status and History
# Run this to diagnose the current state

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Git Status Diagnostic" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Current branch:" -ForegroundColor Yellow
git branch -v

Write-Host ""
Write-Host "Remote tracking:" -ForegroundColor Yellow
git branch -vv

Write-Host ""
Write-Host "Recent commits (local):" -ForegroundColor Yellow
git log --oneline -10

Write-Host ""
Write-Host "Remote commits:" -ForegroundColor Yellow
git log origin/main --oneline -10

Write-Host ""
Write-Host "Git status:" -ForegroundColor Yellow
git status

Write-Host ""
Write-Host "Rebase status (if in progress):" -ForegroundColor Yellow
if (Test-Path ".git/rebase-merge") {
    Write-Host "Rebase is in progress!" -ForegroundColor Red
    Write-Host "Run: git rebase --abort (to cancel)" -ForegroundColor Green
    Write-Host "Or: git rebase --continue (to continue)" -ForegroundColor Green
} else {
    Write-Host "No rebase in progress" -ForegroundColor Green
}

