import re
import unicodedata
import sys
sys.stdout.reconfigure(encoding="utf-8")


# Non-breaking space (U+00A0)
NBSP = "\u00A0"

# Adjust the unit list as needed
UNITS = r"(?:mm|cm|m|km|in|inch(?:es)?|ft|yd|mg|g|kg|oz|lb|lbs|ml|cl|l|L)"

# Normalize full-width digits/spaces first (helps JA/ZH inputs)
def normalize_width(s: str) -> str:
    return unicodedata.normalize("NFKC", s)

def fix_dimensions(text: str) -> str:
    t = normalize_width(text)

    # A) Remove parenthetical alternative units, e.g. " (19.7 in)" or "(19.7in)"
    #    Also handles multiple alts separated by / or , inside the parentheses.
    paren_alt = re.compile(
        rf"""\s*\(\s*        # opening paren
            \d+(?:[.,]\d+)?  # number (with , or . decimals)
            \s*{UNITS}       # unit
            (?:\s*[/,]\s*\d+(?:[.,]\d+)?\s*{UNITS})*  # optional more alts
            \s*\)            # closing paren
        """,
        re.IGNORECASE | re.VERBOSE,
    )
    t = paren_alt.sub("", t)

    # B) Keep left side of "Xunit/Yunit", e.g. "50cm/19.7in" -> "50 cm"
    slash_alt = re.compile(
        rf"""\b
            (\d+(?:[.,]\d+)?)   # number (left)
            \s*({UNITS})        # unit (left)
            \s*/\s*
            \d+(?:[.,]\d+)?\s*(?:{UNITS}) # right side (discarded)
        \b""",
        re.IGNORECASE | re.VERBOSE,
    )
    t = slash_alt.sub(lambda m: f"{m.group(1)}{NBSP}{m.group(2)}", t)

    # C) Enforce non-breaking space between number and unit
    number_unit = re.compile(
        rf"""\b
            (\d+(?:[.,]\d+)?)
            \s*({UNITS})\b
        """,
        re.IGNORECASE | re.VERBOSE,
    )
    t = number_unit.sub(lambda m: f"{m.group(1)}{NBSP}{m.group(2)}", t)

    # Optional: collapse multiple spaces and fix punctuation spacing
    t = re.sub(r"\s{2,}", " ", t).strip()
    return t

# ---- demo ----
s = "Dimensions: 50cm (19.7in). Weight: 3kg."
print(fix_dimensions(s))
# -> "Dimensions: 50 cm. Weight: 3 kg."
