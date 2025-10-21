import os
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def clean_filenames(directory):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        # skip folders
        if not os.path.isfile(old_path):
            continue

        # new filename: remove undesired symbols
        new_filename = filename.replace("+" " ").replace("_", " ")

        # only rename if changed
        if new_filename != filename:
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Example usage:
# change this to your folder path
clean_filenames(r"C:\Users\USER\Downloads")