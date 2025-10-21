# unitex_pipeline_windows.py
# End-to-end Unitex pipeline on Windows:
# Normalize (input.txt) -> Tokenize (.snt) -> Dico (apply dictionary)
# Then read tokens.txt (handles UTF-16) and print top frequencies.

import subprocess
from pathlib import Path
from collections import Counter

# --- Adjust only if your Unitex is in a different place ---
UNITEX_ROOT = r"C:\Program Files (x86)\Unitex-GramLab"
UNITEX_APP  = str(Path(UNITEX_ROOT, "App"))
TOOL        = str(Path(UNITEX_APP, "UnitexToolLogger.exe"))

# Language resources (English)
NORM_TXT     = str(Path(UNITEX_ROOT, "English", "Norm.txt"))
ALPHABET_TXT = str(Path(UNITEX_ROOT, "English", "Alphabet.txt"))
DICO_BIN     = str(Path(UNITEX_ROOT, "English", "Dela", "dela-en-public.bin"))

# Input file (will be created if missing)
in_txt = Path("input.txt")
if not in_txt.exists():
    in_txt.write_text(
        "Hello! I'm testing Unitex with Python. "
        "The Velveteen Rabbit hops happily by the garden.",
        encoding="utf-8"
    )

# Derived paths
snt_file = in_txt.with_suffix(".snt")          # created by Normalize
snt_dir  = Path(f"{in_txt.stem}_snt")          # working dir created by Tokenize/Unitex

def run(cmd, cwd=None, must_succeed=True):
    """Run a command, show stdout/stderr; optionally fail the script on error."""
    pretty = " ".join(f'"{c}"' if " " in c else c for c in cmd)
    print(f">> {pretty}  (cwd={cwd or Path.cwd()})")
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if res.stdout:
        print("STDOUT:\n", res.stdout)
    if res.returncode != 0:
        print("STDERR:\n", res.stderr)
        if must_succeed:
            raise SystemExit(f"Command failed (exit {res.returncode})")
    return res

def read_text_safely(path: Path) -> str:
    """Read a text file trying encodings Unitex uses on Windows."""
    for enc in ("utf-16", "utf-16-le", "utf-8", "latin-1"):
        try:
            return path.read_text(encoding=enc, errors="strict")
        except Exception:
            continue
    # last resort
    return path.read_text(encoding="utf-8", errors="ignore")

# --- Sanity: check resources exist
for p in [TOOL, NORM_TXT, ALPHABET_TXT, DICO_BIN]:
    if not Path(p).exists():
        raise FileNotFoundError(f"Missing required file: {p}")

print("\n=== STEP 1: Normalize (creates .snt) ===")
# Unitex 3.3.x syntax: one positional <text>, optional -r rules file.
# Output is <text>.snt next to the input.
run([TOOL, "Normalize", str(in_txt), "-r", NORM_TXT])

if not snt_file.exists():
    raise SystemExit(f"Normalize finished but {snt_file} was not created.")

print("\n=== STEP 2: Tokenize (.snt + _snt folder) ===")
# Your install accepts Tokenize on the .snt with -a Alphabet
run([TOOL, "Tokenize", str(snt_file), "-a", ALPHABET_TXT])

if not snt_dir.exists():
    print(f" {snt_dir} not found yet; Unitex usually creates it during Tokenize.")

print("\n=== STEP 3: Dico (apply dictionary) ===")
# Your machine requires: Dico -t <absolute .snt> <dic.bin>
run([TOOL, "Dico", "-t", str(snt_file.resolve()), DICO_BIN])

print("\n Done: Normalize -> Tokenize -> Dico\n")

# --- Inspect tokens (UTF-16-safe) ---
tokens_txt = snt_dir / "tokens.txt"
if tokens_txt.exists():
    data = read_text_safely(tokens_txt)
    toks = [ln.strip() for ln in data.splitlines() if ln.strip()]
    cnt = Counter(toks)
    print("Top 20 tokens:")
    for tok, n in cnt.most_common(20):
        print(f"{tok:>20}  {n}")
else:
    print(f" {tokens_txt} not found. Explore {snt_dir} to see Unitex outputs.")


