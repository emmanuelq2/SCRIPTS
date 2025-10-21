def remove_plus_start(input_file, output_file=None):
    """
    Removes '+' at the start of each line in a text file.
    Saves cleaned text to output_file (or overwrites input_file if None).
    """
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned = [line.lstrip("+") for line in lines]

    if output_file is None:
        # overwrite the original file
        output_file = input_file

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(cleaned)

    print(f"Cleaned file saved to: {output_file}")


# Example usage:
remove_plus_start(r"C:\Users\USER\dwhelper\test_chatbot.txt")