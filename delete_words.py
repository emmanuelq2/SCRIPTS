import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
from typing import Iterable, List


def _normalize_terms(terms: Iterable) -> List[str]:
    """
    Flattens nested lists/tuples/sets into a single list of unique, non-empty strings.
    Removes None and trims whitespace. Case-insensitive de-duplication.
    """
    flat: List[str] = []

    def add_one(x):
        if x is None:
            return
        if isinstance(x, str):
            s = x.strip()
            if s:
                flat.append(s)
        else:
            try:
                iter(x)
                if isinstance(x, (list, tuple, set)):
                    for y in x:
                        add_one(y)
                    return
            except TypeError:
                pass
            s = str(x).strip()
            if s:
                flat.append(s)

    add_one(terms)

    seen = set()
    out = []
    for s in flat:
        key = s.lower()
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out

def _process_name_tokens(name: str, delete_prefixes: List[str], trim_sequences: List[str]) -> str:
    """
    Token-based rename:
      - delete any alnum 'word' that starts with one of delete_prefixes
      - trim any alnum 'word' that starts with one of trim_sequences to just that sequence
    A 'word' here is a run of .isalnum() characters. Everything else is a separator and preserved.
    """
    del_lc = [p.lower() for p in _normalize_terms(delete_prefixes)]
    trim_lc = [t.lower() for t in _normalize_terms(trim_sequences)]

    if not del_lc and not trim_lc:
        return name

    # Split into alternating [word, sep, word, sep, ...] keeping separators
    parts = re.split(r'([^A-Za-z0-9]+)', name)

    for i, tok in enumerate(parts):
        if not tok or not tok.isalnum():   # separators or empty
            continue

        low = tok.lower()

        # 1) Delete rule: remove whole word if it STARTS with any delete prefix
        if any(low.startswith(p) for p in del_lc):
            parts[i] = ""   # drop the word, separators around remain
            continue

        # 2) Trim rule: keep only the sequence if word STARTS with it
        if trim_lc:
            # pick the longest matching trim (more specific wins)
            matches = [t for t in trim_lc if low.startswith(t)]
            if matches:
                keep = max(matches, key=len)
                parts[i] = tok[:len(keep)]  # preserve original casing of kept prefix

    new_name = "".join(parts)

    # Normalize leftover spaces/underscores to a single space
    new_name = re.sub(r'[_\s]+', ' ', new_name).strip()

    # Remove any dashes/underscores/spaces right before the extension dot
    new_name = re.sub(r'[-_\s]+$', '', new_name).strip()

    # Fallback if everything vanished
    if not new_name:
        new_name = "untitled"

    return new_name

def rename_mp4_files(directory: str, delete_prefixes, trim_sequences, batch_size=100, start_index=0, dry_run=True):
    """
    Rename .mp4 files in the given directory only (no subfolders).
      - delete_prefixes: remove whole 'words' that START with any of these (e.g., 'pedal*')
      - trim_sequences:  trim 'words' that START with any of these to just the sequence (e.g., 'bla*' -> 'bla')
    Cleans spaces and removes dash/underscore/space before .mp4.
    """
    delete_prefixes = _normalize_terms(delete_prefixes)
    trim_sequences  = _normalize_terms(trim_sequences)

    # Collect only top-level .mp4 files
    all_files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.lower().endswith(".mp4") and os.path.isfile(os.path.join(directory, f))
    ]
    all_files.sort()

    batch_files = all_files[start_index:start_index + batch_size]
    if not batch_files:
        print(f"No more files to process at start_index={start_index}")
        return False

    for idx, file_path in enumerate(batch_files, start=start_index):
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        name_part, ext = os.path.splitext(base_name)

        new_name_part = _process_name_tokens(name_part, delete_prefixes, trim_sequences)

        # Final safety: collapse spaces again and strip trailing separators
        new_name_part = re.sub(r'[_\s]+', ' ', new_name_part).strip()
        new_name_part = re.sub(r'[-_\s]+$', '', new_name_part).strip()

        new_path = os.path.join(dir_name, new_name_part + ext)

        if dry_run:
            print(f"[DRY RUN] {base_name} -> {os.path.basename(new_path)}")
        else:
            try:
                os.rename(file_path, new_path)
                print(f"[RENAMED] {base_name} -> {os.path.basename(new_path)}")
            except Exception as e:
                print(f"[ERROR] Could not rename {base_name}: {e}")

    print(f"--- Finished batch {start_index} to {start_index + len(batch_files) - 1} ---")
    return True

def run_batches_until_limit(directory, delete_prefixes, trim_sequences, batch_size=100, limit=3000, dry_run=True):
    """
    Runs rename_mp4_files repeatedly in increments until 'limit' or no files remain.
    """
    start = 0
    while start < limit:
        more = rename_mp4_files(
            directory=directory,
            delete_prefixes=delete_prefixes,
            trim_sequences=trim_sequences,
            batch_size=batch_size,
            start_index=start,
            dry_run=dry_run
        )
        if not more:
            break
        start += batch_size
    print(f"--- Processing complete up to {start} ---")

if __name__ == "__main__":
    # Example usage
    run_batches_until_limit(
        # directory=r"D:/xxx",            # Folder with .mp4 files
        directory=r"C:/Users/USER/dwhelper/",
        delete_prefixes=["FapHouse", "by", "Po", "Fap", "Porn","xH","xHam","xHamster", "Amateur"],  # Remove whole words starting with these
        # delete_prefixes=[("by FapHouse", "Amateur Porn by FapHouse xH", " Porn by FapHouse xHamster", "Amateur Porn by FapHouse xHam", "Amateur Porn by FapHouse xHamster", "Amateur Amateur Porn by FapHouse xHamster")],    # Remove whole words starting with these
        trim_sequences=["Euro"],      # 'European' -> 'Euro'
        batch_size=100,
        limit=13000,
        dry_run=False               # set to False to actually rename
    )

        