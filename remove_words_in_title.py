import os
import re

def clean_filenames(directory, words_to_remove):
    """
    Remove certain words from filenames inside a directory.

    Args:
        directory (str): Path to the folder containing files.
        words_to_remove (list[str]): List of words or patterns to remove.
    """
    # Compile regex pattern for unwanted words
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, words_to_remove)) + r")\b", re.IGNORECASE)

    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if not os.path.isfile(old_path):
            continue  # skip folders

        # Separate base and extension
        base, ext = os.path.splitext(filename)

        # Remove unwanted words
        new_base = pattern.sub("", base)

        # Clean up extra spaces, dashes, underscores
        new_base = re.sub(r"[-_ ]+", " ", new_base).strip()

        new_filename = new_base + ext
        new_path = os.path.join(directory, new_filename)

        # Avoid overwriting if name unchanged
        if new_path != old_path:
            print(f"Renaming: {filename} -> {new_filename}")
            os.rename(old_path, new_path)


# Example usage:
if __name__ == "__main__":
    folder = r"C:/Users/USER/dwhelper"   # change to your folder path
    words = ["Porn", "Version Italian Hardco"] # words you want to strip out
    clean_filenames(folder, words)

