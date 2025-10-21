import os

def remove_prefix_from_mp4(folder_path, dry_run=True):
    """
    Removes any bytes before the 'ftyp' box in MP4 files in the given folder.
    Creates a new file with '.fixed.mp4' suffix.
    """
    for fname in os.listdir(folder_path):
        if not fname.lower().endswith(".mp4"):
            continue  # skip non-MP4 files

        file_path = os.path.join(folder_path, fname)

        with open(file_path, "rb") as f:
            data = f.read()

        # Find the position of 'ftyp'
        pos = data.find(b"ftyp")
        if pos == -1:
            print(f"[SKIP] {fname} → 'ftyp' not found (not a valid MP4?)")
            continue

        # The MP4 box starts 4 bytes before 'ftyp'
        start_index = max(0, pos - 4)

        if start_index == 0:
            print(f"[OK] {fname} → No prefix detected.")
            continue

        new_fname = fname.replace(".mp4", ".fixed.mp4")
        new_path = os.path.join(folder_path, new_fname)

        if dry_run:
            print(f"[DRY RUN] Would remove {start_index} bytes from start of {fname} -> {new_fname}")
        else:
            with open(new_path, "wb") as out:
                out.write(data[start_index:])
            print(f"[FIXED] {fname} → {new_fname}")

# Example usage:
# remove_prefix_from_mp4("C:/path/to/folder", dry_run=True)   # Preview changes
# remove_prefix_from_mp4("C:/path/to/folder", dry_run=False)  # Actually fix

# Example:
# scan_mp4_folder("C:/path/to/folder")
remove_prefix_from_mp4("C:/Users/USER/dwhelper", dry_run=True)