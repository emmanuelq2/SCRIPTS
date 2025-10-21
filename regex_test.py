import random, re

# RegEx

def generate_numbers(n=10):
    values = []
    for _ in range(n):
        decimals = random.randint(0, 4)  # choose 0 to 4 decimal places
        number = round(random.uniform(0, 1000000), decimals)
        values.append(f"{number:.{decimals}f}")
    return values

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

values = generate_numbers(10)
converted = [re.sub(r"\b(\d+)\.(\d+)\b", r"\1,\2", v) for v in values]

print("Original:", values)
print("Converted:", converted)


# EXAMPLE 2: Convert dates from the MM/DD/YYYY format into the YYYY-MM-DD format

# Step 1: Capture the date pattern
# \b(\d{1,2})/(\d{1,2})/(\d{4})\b

""" 
\b → word boundary to ensure we match standalone dates.
(\d{1,2}) → first capturing group for month (1 or 2 digits).
/ → literal slash separator.
(\d{1,2}) → second capturing group for day (1 or 2 digits).
 / → another literal slash separator.
(\d{4}) → third capturing group for year (exactly 4 digits).    
\b → word boundary again, to stop at the end of the date. 
"""


# Step 2: Replacing the sequence
# r"\3-\1-\2"
# \3 = third captured group (year)
# - = new separator (dash)
# \1 = first captured group (month)
# \2 = second captured group (day)
dates = ["12/31/2023", "1/3/2024", "07/04/2023", "11/3/2024", "6/11/2025"]
text = ", ".join(dates)
converted_dates = re.sub(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", r"\3-\1-\2", text)

print("Original Dates:", dates)
print("Converted Dates:", converted_dates)