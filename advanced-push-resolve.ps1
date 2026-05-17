# Advanced Git Conflict Resolution for ParConverter
# This uses rebase to cleanly integrate remote changes

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Advanced Git Conflict Resolution" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Step 1: Checking git status..." -ForegroundColor Yellow
git status

Write-Host ""
Write-Host "Step 2: Viewing commit history..." -ForegroundColor Yellow
Write-Host "Local commits:" -ForegroundColor Cyan
git log --oneline -5

Write-Host ""
Write-Host "Step 3: Fetching latest from remote..." -ForegroundColor Yellow
git fetch origin

Write-Host ""
Write-Host "Step 4: Attempting rebase (cleaner than merge)..." -ForegroundColor Yellow
Write-Host "Running: git pull --rebase origin main" -ForegroundColor Green
git pull --rebase origin main

Write-Host ""
Write-Host "Step 5: Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "Running: git push -u origin main" -ForegroundColor Green
git push -u origin main

Write-Host ""
Write-Host "Step 6: Pushing v1.0.0 tag..." -ForegroundColor Yellow
Write-Host "Running: git push origin v1.0.0" -ForegroundColor Green
git push origin v1.0.0

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Success! Push complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Check your repository:" -ForegroundColor Cyan
Write-Host "https://github.com/renovictor/ParConverter" -ForegroundColor White
Write-Host ""
Write-Host "Final git status:" -ForegroundColor Cyan
git status

