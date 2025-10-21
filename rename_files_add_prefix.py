import os

def rename_files_add_prefix(folder_path, extension, word, recursive=False, dry_run=False):
    """
    Rename files by adding a prefix to filenames.

    Args:
        folder_path (str): Folder to scan.
        extension (str): Target extension, e.g. ".mp4" or "mp4".
        word (str): Prefix to add (e.g., "Holiday2025").
        recursive (bool): If True, process subfolders too.
        dry_run (bool): If True, only show what would happen.
    """
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"{folder_path} is not a valid folder.")

    if not extension.startswith("."):
        extension = "." + extension

    def prefixed(name: str) -> bool:
        return name.startswith(f"{word}_")

    def unique_path(dirpath: str, filename: str) -> str:
        # If the target exists, add (_1), (_2), ...
        base, ext = os.path.splitext(filename)
        candidate = os.path.join(dirpath, filename)
        n = 1
        while os.path.exists(candidate):
            candidate = os.path.join(dirpath, f"{base}(_{n}){ext}")
            n += 1
        return candidate

    updated = 0

    def handle_dir(dirpath: str, filenames: list):
        nonlocal updated
        for fname in filenames:
            if not fname.endswith(extension):
                continue
            if prefixed(fname):
                print(f"Skip (already prefixed): {os.path.join(dirpath, fname)}")
                continue

            old_path = os.path.join(dirpath, fname)
            new_fname = f"{word}_{fname}"
            new_path = unique_path(dirpath, new_fname)

            if dry_run:
                print(f"Would rename: {old_path}")
                print(f"To         : {new_path}")
            else:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path}")
                print(f"To     : {new_path}")
                updated += 1

    if recursive:
        for dirpath, _dirs, files in os.walk(folder_path):
            handle_dir(dirpath, files)
    else:
        handle_dir(folder_path, os.listdir(folder_path))

    if dry_run:
        print("\nDry run complete. No files were changed.")
    else:
        print(f"\nDone. Renamed {updated} file(s) with extension {extension}.")

# Examples:
# rename_files_add_prefix("C:/Users/You/Videos", ".mp4", "Holiday2025")
# rename_files_add_prefix("C:/Users/You/Videos", ".mp4", "Holiday2025", recursive=True)
# rename_files_add_prefix("C:/Users/You/Videos", ".mp4", "Holiday2025", dry_run=True)

rename_files_add_prefix("C:/Users/USER/dwhelper", ".mp4", "Swedish ")
