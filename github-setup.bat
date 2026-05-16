@echo off
REM GitHub Setup Script for ParConverter V1.0.0
REM Run this script to initialize git, commit, tag, and prepare for GitHub push

echo.
echo ========================================
echo ParConverter V1.0.0 - GitHub Setup
echo ========================================
echo.

REM Step 1: Initialize git repository
echo [1/5] Initializing git repository...
git init

REM Step 2: Configure git
echo [2/5] Configuring git user...
set /p userName="Enter your GitHub username (or press Enter to skip): "
if not "%userName%"=="" (
    git config user.name "%userName%"
    set /p email="Enter your email: "
    git config user.email "!email!"
)

REM Step 3: Add all files
echo [3/5] Adding all files to git...
git add .

REM Step 4: Create initial commit
echo [4/5] Creating initial commit...
git commit -m "Initial commit: ParConverter V1.0.0 - Tlog Parameter List Converter"

REM Step 5: Create version tag
echo [5/5] Creating version tag v1.0.0...
git tag -a v1.0.0 -m "Version 1.0.0: Initial release of ParConverter"

echo.
echo ========================================
echo Git setup complete!
echo ========================================
echo.

echo Current status:
git status

echo.
echo Current tags:
git tag -l

echo.
echo ========================================
echo Next Steps: Push to GitHub
echo ========================================
echo.
echo 1. Create a new repository on GitHub (https://github.com/new)
echo    - Repository name: ParConverter
echo    - Description: Tlog Parameter List Converter
echo.
echo 2. Run the following commands:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/ParConverter.git
echo    git branch -M main
echo    git push -u origin main
echo    git push origin v1.0.0
echo.
echo ========================================
echo.
pause

