# ParConverter V1.0.0

**Tlog Parameter List Converter** - A GUI application for converting tlog parameter lists into tab-separated format.

## Features

- **Parse tlog parameter lists** with support for multiple sections
- **Convert parameters** using customizable profiles (source mapping, constants, and multiplication rules)
- **Normalize numeric values** (hex to int, float simplification, leading zero removal)
- **Modern dark UI** with neon accents
- **Sample data** included for testing
- **Real-time feedback** with conversion warnings

## Building the Executable

### Option 1: Using the Batch Script (Windows)
```bash
build.bat
```

### Option 2: Using the PowerShell Script (Windows)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\build.ps1
```

### Option 3: Manual Build
```bash
pip install pyinstaller
pyinstaller build_executable.spec --onefile
```

## Output

The executable will be created at:
```
dist\ParConverter.exe
```

## Running the Application

After building, simply double-click `ParConverter.exe` to launch the GUI.

## Usage

1. **Input**: Paste your tlog parameter list in the left panel
2. **Sample**: Click "Insert Sample" to see an example
3. **Convert**: Click "Convert" to transform the parameters
4. **Output**: Tab-separated result appears in the right panel
5. **Copy**: Click "Copy Output" to copy to clipboard

## Input Format

```
// Section Name
param_id value, param_id value, ...
param_id value, param_id value, ...

// Another Section
param_id value, param_id value, ...
```

## Supported Value Formats

- Hexadecimal: `0x6aa` → `1706`
- Floats: `1.00` → `1`, `3.14159` → `3.14159`
- Leading zeros: `000` → `0`

## Version

- **V1.0.0** - Initial release
- Built with Python 3.x and tkinter

