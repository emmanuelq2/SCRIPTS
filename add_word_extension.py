import os

def prepend_word_to_all_files_binary(folder_path, extension, word):
    """
    Prepend a word to all files with a given extension in the folder (non-recursive).
    Works even if files are not UTF-8 encoded.
    """
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"{folder_path} is not a valid folder.")

    # Ensure extension starts with a dot
    if not extension.startswith("."):
        extension = "." + extension

    count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            file_path = os.path.join(folder_path, filename)

            # Read as bytes
            with open(file_path, "rb") as f:
                content = f.read()

            # Prepend the word as bytes (with space after it)
            new_content = word.encode("utf-8") + b" " + content

            # Write back
            with open(file_path, "wb") as f:
                f.write(new_content)

            count += 1
            print(f'Prepended "{word}" to: {filename}')

    print(f"\n Done! Updated {count} file(s) with extension {extension}.")

# Example usage:
# prepend_word_to_all_files_binary("C:/Users/YourName/Documents", ".txt", "HelloWorld")

prepend_word_to_all_files_binary("C:/Users/USER/dwhelper", ".mp4", "Swedish ")