import os

def add_extension_except_txt(folder_path, new_extension, recursive=False, dry_run=False):
    """
    Adds a new extension to all files in a folder except those ending with .txt.

    Args:
        folder_path (str): Folder to process.
        new_extension (str): Extension to add (e.g., ".log" or "log").
        recursive (bool): If True, process subfolders too.
        dry_run (bool): If True, only show what would happen.
    """
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"{folder_path} is not a valid folder.")

    if not new_extension.startswith("."):
        new_extension = "." + new_extension

    updated = 0

    def process_files(dirpath, filenames):
        nonlocal updated
        for fname in filenames:
            # Skip if already .txt or already has the new extension
            if fname.lower().endswith(".txt") or fname.lower().endswith(new_extension.lower()):
                continue

            old_path = os.path.join(dirpath, fname)
            new_path = old_path + new_extension

            if dry_run:
                print(f"Would rename: {old_path} -> {new_path}")
            else:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
                updated += 1

    # if recursive:
    #     for dirpath, _dirs, files in os.walk(folder_path):
    #         process_files(dirpath, files)
    # else:
    #     process_files(folder_path, os.listdir(folder_path))

    if not dry_run:
        print(f"\nDone. Renamed {updated} file(s) by adding {new_extension} (excluding .txt).")

# Example usage:
# add_extension_except_txt("C:/Users/You/Documents", ".log")
# add_extension_except_txt("C:/Users/You/Documents", ".log", recursive=True)
# add_extension_except_txt("C:/Users/You/Documents", ".log", dry_run=True)
add_extension_except_txt("C:/Users/USER/dwhelper", ".mp4")
