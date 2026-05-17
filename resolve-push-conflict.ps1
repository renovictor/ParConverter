# Resolve Git Push Conflict for ParConverter
# This script pulls remote changes and then pushes

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Resolving Git Push Conflict" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "The remote repository has changes that need to be pulled first." -ForegroundColor Yellow
Write-Host ""

# Option 1: Pull and merge
Write-Host "[Option 1] Pull remote changes and merge..." -ForegroundColor Cyan
Write-Host "Running: git pull origin main --allow-unrelated-histories" -ForegroundColor Green
git pull origin main --allow-unrelated-histories

Write-Host ""
Write-Host "Now pushing to GitHub..." -ForegroundColor Cyan
git push -u origin main

Write-Host ""
Write-Host "[Optional] Push the v1.0.0 tag" -ForegroundColor Cyan
git push origin v1.0.0

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Push complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Verify at: https://github.com/renovictor/ParConverter" -ForegroundColor Cyan

