# Quick Start: Push ParConverter to GitHub

## 1. Run GitHub Setup (Choose One)

### PowerShell:
```powershell
.\github-setup.ps1
```

### Command Prompt (Batch):
```batch
github-setup.bat
```

This will:
✓ Initialize git repository
✓ Create initial commit
✓ Create v1.0.0 tag
✓ Show instructions for next steps

---

## 2. Create Repository on GitHub

Visit: https://github.com/new

- Name: `ParConverter`
- Description: `Tlog Parameter List Converter`
- Public/Private: Your choice
- **DO NOT** initialize with README (you already have one)

Click "Create repository"

---

## 3. Push to GitHub

Copy the repository URL from GitHub, then run one of these commands:

### HTTPS (easiest):
```bash
git remote add origin https://github.com/YOUR_USERNAME/ParConverter.git
git branch -M main
git push -u origin main
git push origin v1.0.0
```

### SSH (more secure):
```bash
git remote add origin git@github.com:YOUR_USERNAME/ParConverter.git
git branch -M main
git push -u origin main
git push origin v1.0.0
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## 4. Verify

Visit: https://github.com/YOUR_USERNAME/ParConverter

You should see:
- All your files
- Commit history
- v1.0.0 tag in the releases

---

## Need Help?

See `GITHUB_PUSH_GUIDE.md` for detailed instructions and troubleshooting.

