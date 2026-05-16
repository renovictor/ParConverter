# GitHub Setup Script for ParConverter V1.0.0
# Run this script to initialize git, commit, tag, and prepare for GitHub push

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ParConverter V1.0.0 - GitHub Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Initialize git repository
Write-Host "[1/5] Initializing git repository..." -ForegroundColor Yellow
git init

# Step 2: Configure git (optional - use global if already configured)
Write-Host "[2/5] Configuring git user..." -ForegroundColor Yellow
$userName = Read-Host "Enter your GitHub username (or press Enter to skip)"
if ($userName) {
    git config user.name "$userName"
    $email = Read-Host "Enter your email"
    git config user.email "$email"
}

# Step 3: Add all files
Write-Host "[3/5] Adding all files to git..." -ForegroundColor Yellow
git add .

# Step 4: Create initial commit
Write-Host "[4/5] Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: ParConverter V1.0.0 - Tlog Parameter List Converter

- Main application: ParConverter.py with tkinter GUI
- Dark theme with neon accent colors
- Parse and convert tlog parameter lists
- Support for value normalization (hex, floats, leading zeros)
- Configurable conversion profiles
- Build scripts for creating standalone executable
- Comprehensive documentation and examples"

# Step 5: Create version tag
Write-Host "[5/5] Creating version tag v1.0.0..." -ForegroundColor Yellow
git tag -a v1.0.0 -m "Version 1.0.0: Initial release of ParConverter

## Features
- Parse tlog parameter lists from comma-separated or space-separated format
- Organized output with sections: General Parameters, Match Parameters, Generator Parameters, PIDs
- Support for different conversion rules:
  - Direct mapping (source to output)
  - Constant values
  - Multiplication operations
- Automatic numeric normalization
- Modern GUI with dark theme
- Sample data included
- Standalone executable support via PyInstaller

## Build
Run build.ps1 or build.bat to create ParConverter.exe

## Usage
1. Paste tlog parameter list
2. Click Convert
3. Copy output"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Git setup complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "Current status:" -ForegroundColor Cyan
git status

Write-Host ""
Write-Host "Current tags:" -ForegroundColor Cyan
git tag -l

Write-Host ""
Write-Host "========================================" -ForegroundColor Yellow
Write-Host "Next Steps: Push to GitHub" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Create a new repository on GitHub (https://github.com/new)" -ForegroundColor White
Write-Host "   - Repository name: ParConverter" -ForegroundColor White
Write-Host "   - Description: Tlog Parameter List Converter" -ForegroundColor White
Write-Host ""
Write-Host "2. Run the following commands:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/ParConverter.git" -ForegroundColor Green
Write-Host "   git branch -M main" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host "   git push origin v1.0.0" -ForegroundColor Green
Write-Host ""
Write-Host "OR if using SSH:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin git@github.com:YOUR_USERNAME/ParConverter.git" -ForegroundColor Green
Write-Host "   git branch -M main" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host "   git push origin v1.0.0" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

