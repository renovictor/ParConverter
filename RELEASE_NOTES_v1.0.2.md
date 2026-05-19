# ParConverter v1.0.2 Release Notes

**Release Date**: May 19, 2026  
**Type**: Critical Bug Fix  
**Previous Version**: v1.0.1  

---

## 🐛 Critical Bug Fixed

### Problem Statement
When input data **did NOT contain** a particular parameter ID (e.g., parameter 13), but that parameter ID was defined in the profile with a **hardcoded constant value**, the output would **still include that parameter** with its constant value.

**Example Bug Scenario:**
```
Input Data:
  param 3: 100
  param 5: 200
  (param 13: MISSING)
  
v1.0.1 Output (WRONG):
  param 3: 100
  param 5: 200
  param 13: 10000    ← Force-output! (hardcoded constant from profile)
  
v1.0.2 Output (CORRECT):
  param 3: 100
  param 5: 200
  (param 13: completely omitted)
```

### Root Cause
The profile system in v1.0.1 (and earlier) was designed as **profile-driven output**:
- The profile defined ALL parameters that SHOULD be output
- If a parameter was marked as `("const", value)`, it was ALWAYS output
- This caused hardcoded constants to appear even when input didn't have that parameter

### Solution Implemented
Changed to **input-driven output**:
```python
# v1.0.2 Fix (Line 231-233 in compute_converted_text):
for oid in out_ids:
    if oid not in in_map:           # ← NEW: Check if param exists in input
        continue                    # ← NEW: Skip if not present
    
    # Process and output (rest of logic unchanged)
```

**Key Logic**: Only parameters present in the input are processed and output.

---

## ✅ What Changed

### Code Changes
- **File**: `ParConverter.py`
- **Function**: `compute_converted_text()`
- **Lines**: 231-233 (added input existence check)
- **Impact**: Low-risk change, highly localized

### Behavior Changes
| Aspect | v1.0.1 | v1.0.2 |
|--------|--------|--------|
| Parameter not in input | Output as constant (if defined) | Completely omitted |
| Parameter in input | Output with conversion rule | Output with conversion rule |
| Unknown parameters | Auto-detected & appended | Auto-detected & appended ✅ |
| Data loss risk | None → INCORRECT data added | None (only true data) |

---

## 📊 Technical Details

### Conversion Rules Still Work
All three profile rule types continue to work correctly:

1. **Source Rule** `("src", id)`:
   - Gets value from input parameter `id`
   - v1.0.2: Skipped if `id` not in input
   
2. **Constant Rule** `("const", value)`:
   - v1.0.1: Always output this value
   - v1.0.2: Only output if parameter exists in input
   
3. **Multiplication Rule** `("mul", id, factor)`:
   - Gets value from input parameter `id`, multiplies by factor
   - v1.0.2: Skipped if `id` not in input

### v1.0.1 Features Retained
✅ Dynamic parameter detection (Part 2 of output logic unchanged)  
✅ Auto-sorting of unknown parameters  
✅ Backward compatible data processing  

---

## 🔍 Verification

### Test Case
**Input:**
```
// General Parameters
2 000000, 3 00, 4 0, 6 1, 7 0, 8 0.0, 9 0, 10 0
11 0x6aa, 14 0.0, 15 100.0, 16 5, 17 13, 18 20, 19 0
...
(Note: parameter 13 is deliberately omitted)
```

**Expected v1.0.2 Output:**
- Parameters 2-12, 14-20, etc. are output
- **Parameter 13 is completely omitted** (not in input, so not output)

**Previous v1.0.1 Output:**
- Parameters 2-13, 14-20, etc. are output
- **Parameter 13 shows "10000"** (hardcoded from profile)

---

## 📝 Updated Version Information

```python
# version.py
__version__ = "1.0.2"
__description__ = "GUI application for converting tlog parameter lists - Input-driven output with smart parameter detection"
```

```markdown
# CHANGELOG.md
## [1.0.2] - 2026-05-19
### Fixed (Critical Bug Fix)
- Parameters NOT in input are no longer output with constant values
- Implemented input-driven output checking
```

---

## 🚀 Deployment Instructions

### 1. Commit Changes
```powershell
.\commit-v1.0.2.ps1
```

### 2. Create Tag
```bash
git tag -a v1.0.2 -m "Version 1.0.2: Input-driven output fix"
```

### 3. Push to GitHub
```bash
git push --force-with-lease -u origin main
git push origin v1.0.2
```

### 4. Build Executable (Optional)
```powershell
.\build.ps1
```

---

## 📦 Files Modified/Created

### Modified
- ✏️ `ParConverter.py` - Bug fix in `compute_converted_text()`
- ✏️ `version.py` - Version bumped to 1.0.2
- ✏️ `CHANGELOG.md` - Release notes added

### Created
- 📄 `commit-v1.0.2.ps1` - Commit automation script

---

## ⚠️ Breaking Changes

**Behavior will change** for workflows that relied on hardcoded constants being forced into output:

**Before v1.0.2:**
```
If param 13 wasn't in input, it would still appear with value "10000"
```

**After v1.0.2:**
```
If param 13 isn't in input, it won't appear in output at all
```

**This is the correct and intended behavior** as per user requirements.

---

## 🎯 Future Considerations

1. **Profile System Refinement**: Consider separating profile rules for "required vs optional parameters"
2. **Configuration Files**: Support external JSON/YAML configs for different profiles
3. **Validation Layer**: Add pre-processing validation to warn about missing expected parameters
4. **Test Suite**: Add unit tests for various input/output scenarios

---

## ✨ Summary

- ✅ Critical bug fixed
- ✅ Input-driven output implemented
- ✅ v1.0.1 features retained
- ✅ Backward compatible processing
- ✅ Ready for production release

