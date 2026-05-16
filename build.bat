@echo off
REM Build script for ParConverter V1.0.0
REM Creates a single executable file

echo Installing PyInstaller...
python -m pip install pyinstaller --quiet

echo Generating spec file...
pyinstaller --onefile --windowed --name ParConverter ParConverter.py --specpath .

echo Building ParConverter executable...
pyinstaller ParConverter.spec

echo.
echo Build complete!
echo Executable location: dist\ParConverter.exe
echo.
pause

