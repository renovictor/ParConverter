# Force Push Solution - Override Remote with Local Changes
# This is safe via --force-with-lease (prevents accidental overwrites)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Force Push Solution for ParConverter" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "WARNING: This will overwrite the remote repository!" -ForegroundColor Red
Write-Host "Your local version will become the source of truth." -ForegroundColor Yellow
Write-Host ""

$confirm = Read-Host "Continue? (yes/no)"
if ($confirm -ne "yes") {
    Write-Host "Cancelled." -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "Step 1: Check for active rebase..." -ForegroundColor Yellow
if (Test-Path ".git/rebase-merge") {
    Write-Host "Rebase in progress - aborting..." -ForegroundColor Yellow
    git rebase --abort
}

Write-Host ""
Write-Host "Step 2: Fetch latest from remote..." -ForegroundColor Yellow
git fetch origin

Write-Host ""
Write-Host "Step 3: Force push with lease (safe force push)..." -ForegroundColor Yellow
Write-Host "Running: git push --force-with-lease -u origin main" -ForegroundColor Green
git push --force-with-lease -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Step 4: Push v1.0.0 tag..." -ForegroundColor Yellow
    Write-Host "Running: git push origin v1.0.0" -ForegroundColor Green
    git push origin v1.0.0

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Success! Repository pushed!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "Push failed - see errors above" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
}

Write-Host ""
Write-Host "Final status:" -ForegroundColor Cyan
git status

