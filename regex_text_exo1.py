import re

# RegEx
# EXAMPLE 1: Convert decimal separators in numbers from a dot (.) to a comma (,) in a list of numbers

# Step 1: Capture the pattern for decimal numbers with a dot
# \b\d+\.\d+\b

""" 
\b → word boundary to ensure we match standalone numbers (not parts of codes/URLs).
\d+ → one or more digits (before the dot).
\. → a literal dot (the decimal separator we want to replace).
\d+ → one or more digits (after the dot).
\b → word boundary again, to stop at the end of the number. 
"""

# Step 2: Replacing the sequence
# 1. re.sub(pattern, replacement, text)
# re.sub = regex substitute function.
# searches text for substrings matching pattern and replaces them with replacement.

# 2. replacement string with backreferences
# r"\1,\2"
# r = raw string notation to avoid escape sequence issues.
# \1 = first captured group (digits before the dot)
# \2 = second captured group (digits after the dot)
# , = the new decimal separator (comma)

values = [37.2, 56.897, 6523.1, 0.0042, 1000000.0, 3.14159, 2.0, 7.25, 0.5, 42, 99.99]

# Only replace the decimal point between digits
converted = [re.sub(r"\b(\d+)\.(\d+)\b", r"\1,\2", f"{v}") for v in values]

print("Original:", values)
print("Converted:", converted)
