# Changelog

All notable changes to ParConverter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.1] - 2026-05-17

### Added
- **Dynamic Parameter Detection**: Automatically detects and outputs parameters not defined in SECTION_OUT_ORDER
- Parameters beyond the predefined list (e.g., parameter 73+ in General Parameters) are now automatically captured and appended to output
- Unknown parameters are sorted numerically for consistent ordering

### Changed
- Enhanced `compute_converted_text()` function to support hybrid parameter management
- Improved scalability: no longer limited by hardcoded parameter lists
- Better separation of logic: predefined parameters first (maintains order), then auto-detected parameters (sorted by ID)

### How It Works (v1.0.1)
1. **Part 1 - Predefined Parameters**: Outputs parameters from SECTION_OUT_ORDER in their defined order
2. **Part 2 - Auto-Detected Parameters**: Detects any parameters in input that aren't in predefined list
3. **Part 3 - Dynamic Sorting**: Auto-detected parameters are sorted numerically and appended to output

### Benefits
- ✅ Forward compatible: handles new parameters without code changes
- ✅ Backward compatible: existing workflows unchanged
- ✅ No data loss: no parameters from input are discarded
- ✅ Clean output: maintains predefined order while capturing unknowns

### Example
If General Parameters input contains parameter 73 or higher:
- **Before v1.0.1**: Parameter 73+ silently ignored/not in output
- **After v1.0.1**: Parameter 73+ automatically appended after parameter 72

---

## [1.0.0] - 2026-05-17

### Initial Release
- Tlog parameter list parser and converter
- Four output sections: General Parameters, Match Parameters, Generator Parameters, PIDs
- Conversion profile system with three rule types:
  - Source mapping (`src`)
  - Constant values (`const`)
  - Multiplication operations (`mul`)
- Modern dark-themed GUI with neon accents
- Numeric value normalization (hex, floats, leading zeros)
- Sample data for testing
- Build system for creating standalone executable via PyInstaller

