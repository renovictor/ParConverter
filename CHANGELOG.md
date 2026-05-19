# Changelog

All notable changes to ParConverter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.4] - 2026-05-19

### Fixed (Missing Parameters Bug)
- **Parameters 48 and 49 were missing from General Parameters predefined list**
- **Issue**: Input with param 48 was not appearing in output
- **Root Cause**: SECTION_OUT_ORDER for General Parameters had a gap:
  ```
  47, [missing 48, 49], 50  ← Gap!
  ```
- **Solution**: Added parameters 48 and 49 to both SECTION_OUT_ORDER and gen_src profile list

### Changes
- **General Parameters list**: Added 48, 49 between 47 and 50
- **Profile (gen_src)**: Added 48, 49 to source-based parameters
- Now all General Parameters from 2-72 are included (except the intentionally skipped ones: 1, 5, 12, 36, 49)

### Verification
- Input param 48 → Now outputs correctly ✅
- Input param 49 → Now outputs correctly ✅
- All other parameters unaffected ✅

---

## [1.0.3] - 2026-05-19

### Fixed (Profile Configuration Bug)
- **All hardcoded constants removed - parameters now always use input values**
- **Issue**: Profile defined parameters as hardcoded constants (e.g., param 10="34", param 41="2")
  - Input param 10 = 30, but output showed 34 (constant override)
  - Input param 41 = 5, but output showed 2 (constant override)
- **Solution**: Changed ALL parameters to source-based rules `("src", id)`
  - Profile now reads value directly from input for every parameter
  - No more hardcoded defaults overriding input data

### Changed - Profile Simplification
- **Removed all `("const", value)` rules** from:
  - General Parameters (removed 14 hardcoded values)
  - Match Parameters (removed 5 hardcoded values)
  - Generator Parameters (removed 7 hardcoded values)
  - PIDs (removed 52 hardcoded values)
- Now profile uses ONLY source-based rules: all parameters = `("src", param_id)`
- Multiplication rules retained where applicable (e.g., parameter 127 doubling)

### Behavior Changes
| Parameter | v1.0.2 (Bug) | v1.0.3 (Fixed) |
|-----------|--------------|----------------|
| param 10 with input 30 | Output 34 (const) | Output 30 (input) ✅ |
| param 41 with input 5 | Output 2 (const) | Output 5 (input) ✅ |
| param N in input | Output uses input | Output uses input ✅ |
| param N not in input | Omitted | Omitted ✅ |

### Profile Architecture
Old (v1.0.2):
```python
gen_const = {2: "11001", 10: "34", 11: "2", ...}  # Hardcoded
gen_src = [3,4,6,7,...]                          # From input
```

New (v1.0.3):
```python
gen_src = [2,3,4,6,7,8,9,10,11,...72]  # All from input!
# (NO hardcoded constants dict)
```

### Examples
**Test Case 1**: Parameter in input
```
Input: param 10 = 30
v1.0.2: Output param 10 = 34 (constant override - WRONG)
v1.0.3: Output param 10 = 30 (input value - CORRECT) ✅
```

**Test Case 2**: Parameter not in input
```
Input: param 13 = (absent)
v1.0.2: Output param 13 = 10000 (constant - then omitted by v1.0.2 fix)
v1.0.3: Output param 13 = (omitted) ✅
```

### Compatibility
- ✅ Backward compatible with v1.0.2 code structure
- ⚠️ Output format changed: removes hardcoded constant overrides
- ✅ Input-driven output fully implemented
- ✅ v1.0.1 dynamic parameter detection retained

### Files Changed
- `ParConverter.py`: Profile completely refactored
- `version.py`: Version bumped to 1.0.3

---

## [1.0.2] - 2026-05-19

### Fixed (Critical Bug Fix)
- **Parameters NOT in input are no longer output with constant values** 
  - **Issue**: v1.0.1 was outputting hardcoded constants (e.g., param 13 with value "10000") even when they didn't exist in input data
  - **Root Cause**: Profile-driven approach forced output of all predefined constants regardless of input
  - **Solution**: Implemented input-driven output - only parameters present in input are processed and output

### Changed
- Output logic now checks `if oid not in in_map: continue` before processing each parameter
- This prevents emission of missing parameters entirely (v1.0.1 would output empty or constant values)
- Parameters marked as `("const", value)` in profile are only output if they exist in input

### Behavior Change (Breaking)
- **v1.0.1**: Would output parameter 13 as "10000" even if parameter 13 wasn't in input
- **v1.0.2**: Parameter 13 is completely omitted if not in input
- This is the intended and expected behavior as per user request

### Example Data Fix
```
Input: param 13 NOT present, param 5 = some_value
v1.0.1 output: param 13 → 10000 (wrong - constant force-output)
v1.0.2 output: param 13 → omitted, param 5 → correctly output
```

### Compatibility
- ✅ Backward compatible with v1.0.1 data processing
- ⚠️ Output format changed: missing parameters omitted (as intended)
- ✅ All conversion rules still work: src, const, mul

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

