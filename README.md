# Week 6 Python Assignment

This assignment demonstrates Python error handling using `try` and `except` to prevent programs from crashing when errors occur.

## Files

- `safe_tools.py` - Contains three safe functions that handle division by zero, invalid number conversion, and missing dictionary keys.
- `unbreakable.py` - Demonstrates handling invalid user input so that the program does not crash.

## Why can the `if` check not catch `abc` on its own?

An `if` check can check whether a number is acceptable after it has been successfully converted, but `abc` cannot be converted to an integer in the first place. Therefore, `try` and `except` are needed to catch the `ValueError` caused by invalid input such as `abc`.
