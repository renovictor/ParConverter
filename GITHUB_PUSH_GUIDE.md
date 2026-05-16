# GitHub Push Guide for ParConverter V1.0.0

## Overview
This document provides step-by-step instructions to push your ParConverter project to GitHub.

## Prerequisites
- Git installed on your machine
- GitHub account
- GitHub CLI (optional, but helpful)

---

## Step 1: Local Git Setup

### Option A: Using the Automated Script (Recommended)

**For PowerShell:**
```powershell
.\github-setup.ps1
```

**For Command Prompt (Batch):**
```batch
github-setup.bat
```

These scripts will:
- Initialize the git repository
- Configure your git user (name and email)
- Stage all files
- Create an initial commit
- Create the v1.0.0 tag

### Option B: Manual Setup

If you prefer manual commands, run these in PowerShell or Command Prompt:

```bash
# Initialize git
git init

# Configure git (if not already done globally)
git config user.name "Your GitHub Username"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: ParConverter V1.0.0 - Tlog Parameter List Converter"

# Create version tag
git tag -a v1.0.0 -m "Version 1.0.0: Initial release of ParConverter"
```

---

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in the form:
   - **Repository name:** `ParConverter`
   - **Description:** `Tlog Parameter List Converter`
   - **Public/Private:** Choose your preference
   - **Initialize with README, .gitignore, license:** DO NOT CHECK (you already have these)
3. Click "Create repository"
4. You'll get a repository URL like:
   - HTTPS: `https://github.com/YOUR_USERNAME/ParConverter.git`
   - SSH: `git@github.com:YOUR_USERNAME/ParConverter.git`

---

## Step 3: Push to GitHub

### Option A: Using HTTPS (Recommended for beginners)

```powershell
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/ParConverter.git

# Rename branch to main (if needed)
git branch -M main

# Push main branch
git push -u origin main

# Push the v1.0.0 tag
git push origin v1.0.0

# Push all tags
git push origin --tags
```

### Option B: Using SSH (Recommended for security)

First, set up SSH keys if you haven't already:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Then run:

```bash
# Add remote repository
git remote add origin git@github.com:YOUR_USERNAME/ParConverter.git

# Rename branch to main (if needed)
git branch -M main

# Push main branch
git push -u origin main

# Push the v1.0.0 tag
git push origin v1.0.0

# Push all tags
git push origin --tags
```

---

## Step 4: Verify

After pushing, verify on GitHub:

1. Visit https://github.com/YOUR_USERNAME/ParConverter
2. Check that all files are there
3. Check the commit history
4. Visit the "Releases" tab to confirm v1.0.0 tag is present

---

## Additional Commands

### View git status
```bash
git status
```

### View commit history
```bash
git log --oneline
```

### View all tags
```bash
git tag -l
```

### View remote configuration
```bash
git remote -v
```

### Push future commits
```bash
git push origin main
```

---

## Troubleshooting

### "fatal: not a git repository"
Make sure you're in the ParConverter directory and have run `git init`

### "permission denied" or "authentication failed"
- For HTTPS: Make sure your GitHub credentials are saved in Windows Credential Manager
- For SSH: Make sure your SSH keys are set up correctly

### "origin already exists"
If you accidentally added the remote twice, remove it first:
```bash
git remote remove origin
git remote add origin <your-url>
```

### Tag already exists error
If creating the tag fails because it exists, you can delete it locally:
```bash
git tag -d v1.0.0
```

Then create it again.

---

## Next Steps

After successfully pushing to GitHub:

1. **Create a GitHub Release** for v1.0.0:
   - Go to your repository
   - Click "Releases" tab
   - Click "Draft a new release"
   - Tag version: `v1.0.0`
   - Title: `ParConverter V1.0.0`
   - Add description and release notes
   - Attach the compiled executable if available

2. **Enable GitHub Pages** (optional):
   - Go to Settings > Pages
   - Set source to `main` branch
   - Your README.md will become your project website

3. **Add Topics** (optional):
   - Settings > About
   - Add topics: `python`, `tkinter`, `parameter-converter`, `tlog`

---

## File Structure in GitHub

Your repository will contain:

```
ParConverter/
├── ParConverter.py              # Main application
├── version.py                   # Version information
├── build.ps1                    # PowerShell build script
├── build.bat                    # Batch build script
├── build_executable.spec        # PyInstaller spec file
├── github-setup.ps1             # GitHub setup script (PowerShell)
├── github-setup.bat             # GitHub setup script (batch)
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── LICENSE                      # Project license (if added)
```

---

## Questions?

For more information on git and GitHub:
- Git Documentation: https://git-scm.com/doc
- GitHub Documentation: https://docs.github.com/
- GitHub Guides: https://guides.github.com/

