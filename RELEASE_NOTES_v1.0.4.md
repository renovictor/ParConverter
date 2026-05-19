# ParConverter v1.0.4 Release Notes

**Release Date**: May 19, 2026  
**Type**: Bug Fix  
**Previous Version**: v1.0.3  

---

## 🐛 Bug Fixed

### The Problem
Input parameters 48 and 49 were not appearing in the output.

```
Input Data:
  param 48 = 100
  param 49 = 200

v1.0.3 Output (WRONG):
  (param 48 and 49 missing from output)
  
v1.0.4 Output (CORRECT):
  param 48 = 100 ✅
  param 49 = 200 ✅
```

### Root Cause
The predefined output list `SECTION_OUT_ORDER` for **General Parameters** had a gap:

```python
# v1.0.3 (WRONG):
General Parameters = [
    2,3,4,6,7,8,9,10,11,13,...40,41,42,43,44,45,46,47,
    50,51,52,53,...  # ← JUMPS from 47 to 50! (48, 49 missing)
]

Profile gen_src = [
    2,3,4,6,7,8,9,10,11,13,...40,41,42,43,44,45,46,47,
    50,51,52,53,...  # ← SAME GAP in profile!
]
```

### Solution
Added parameters 48 and 49 to both lists:

```python
# v1.0.4 (FIXED):
General Parameters = [
    2,3,4,6,7,8,9,10,11,13,...40,41,42,43,44,45,46,47,
    48,49,50,51,52,53,...  # ✅ Now includes 48, 49
]

Profile gen_src = [
    2,3,4,6,7,8,9,10,11,13,...40,41,42,43,44,45,46,47,
    48,49,50,51,52,53,...  # ✅ Now includes 48, 49
]
```

---

## 📊 Changes

### Files Modified
- `ParConverter.py`:
  - SECTION_OUT_ORDER: Added 48, 49 to General Parameters list
  - Profile gen_src: Added 48, 49 to source-based parameters
  
- `version.py`: Bumped to v1.0.4

- `CHANGELOG.md`: Added v1.0.4 entry

### General Parameters List Comparison

| Version | Status | List |
|---------|--------|------|
| v1.0.3 | ❌ Bug | 47 → 50 (gap) |
| v1.0.4 | ✅ Fixed | 47 → 48 → 49 → 50 |

---

## ✅ Test Results

| Parameter | v1.0.3 | v1.0.4 | Status |
|-----------|--------|--------|--------|
| 47 | ✅ Output | ✅ Output | ✅ Unchanged |
| 48 | ❌ Missing | ✅ Output | **Fixed** |
| 49 | ❌ Missing | ✅ Output | **Fixed** |
| 50 | ✅ Output | ✅ Output | ✅ Unchanged |

---

## 🔍 Impact Analysis

### What Remains Unchanged
✅ All other parameters still work correctly  
✅ v1.0.1 dynamic parameter detection still works  
✅ v1.0.2 input-driven output still works  
✅ v1.0.3 no hardcoded constants still works  

### What's Fixed
✅ General Parameters now includes 48 and 49  
✅ Complete coverage from 2-72 (with documented gaps)  
✅ No data loss for these parameters  

---

## 📋 General Parameters - Complete List

### v1.0.4 (Complete)
```
2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 
53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 
69, 70, 71, 72
```

### Intentional Gaps (Not included)
- 1, 5, 12, 36 (documented as not part of General Parameters section)

---

## 🎯 Why This Bug Existed

The original profile was based on a specific sample output that didn't include parameters 48 and 49. When transitioning to a fully input-driven approach in v1.0.3, these gaps were not caught because:

1. The sample input didn't have params 48, 49
2. v1.0.1 dynamic detection should have caught them, but they weren't being output in the designated "General Parameters" section

**This is now fixed in v1.0.4.**

---

## 🔄 Migration

No action needed. v1.0.4 is fully backward compatible. Parameter 48 and 49 will now correctly appear in output if present in input.

---

## ✨ Summary

- ✅ Parameters 48, 49 now included in General Parameters
- ✅ Bug fixed: Input parameters no longer skipped
- ✅ Backward compatible
- ✅ Ready for production

**All General Parameters from 2-72 (with documented gaps) are now supported!** 🎉

