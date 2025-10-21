import subprocess
from pathlib import Path

# Correct paths
UNITEX_APP = r"C:\Program Files (x86)\Unitex-GramLab\App"
TOOL = str(Path(UNITEX_APP, "UnitexToolLogger.exe"))

# English resources are NOT in App/, but in the main Unitex-GramLab folder
UNITEX_ROOT = r"C:\Program Files (x86)\Unitex-GramLab"
NORM_TXT = str(Path(UNITEX_ROOT, "English", "Norm.txt"))
ALPHABET_TXT = str(Path(UNITEX_ROOT, "English", "Alphabet.txt"))

# Input/output
in_txt = Path("input.txt")
if not in_txt.exists():
    in_txt.write_text("Hello! I'm testing Unitex with Python.", encoding="utf-8")

snt_file = in_txt.with_suffix(".snt")

def run(cmd):
    print(">>", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.stdout:
        print("STDOUT:\n", res.stdout)
    if res.returncode != 0:
        print("STDERR:\n", res.stderr)
        raise SystemExit(f"Command failed (exit {res.returncode})")

# 1️⃣ Normalize (works fine now)
run([TOOL, "Normalize", str(in_txt), "-r", NORM_TXT, "-qutf8"])

# 2️⃣ Tokenize using correct path for Alphabet.txt
run([TOOL, "Tokenize", str(snt_file), "-a", ALPHABET_TXT])

print("Done: normalized + tokenized successfully.")