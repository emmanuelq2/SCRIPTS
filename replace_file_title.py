import os

def bulk_replace_in_filenames(directory, replacements):
    """
    Rename all files in a folder by replacing words in their titles.

    :param directory: Folder where files are located
    :param replacements: Dictionary of {old_word: new_word}
    """
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        if not os.path.isfile(old_path):
            continue  # skip folders

        new_filename = filename
        for old, new in replacements.items():
            new_filename = new_filename.replace(old, new)

        if new_filename != filename:  # only rename if changed
            new_path = os.path.join(directory, new_filename)

            if os.path.exists(new_path):
                print(f" Skipping {filename}, {new_filename} already exists.")
                continue

            os.rename(old_path, new_path)
            print(f" {filename} → {new_filename}")

# Example usage:
# Replace "cat" with "black cat"
# Replace "dog" with "big dog"
replacements = {
    # "Harryr": "Russian Harry" 
    # "Russian Eighteens": "Russian Yam-Yam Eighteens"
    "Danish ": "vintage Danish "
}

bulk_replace_in_filenames(r"E:\P", replacements)