

""" write a Python function that finds repeating two-character patterns in a string. 
The function should identify when the same pair of characters appear next to each 
other in the string and count how many times each pair repeats consecutively. """

import sys
import unittest
from pathlib import Path

def bigram_counting_chains(chains: str) -> str:
    encoded_results = ""

    current_pair = None
    current_count = 0
    encoded_parts = []

    # Move by 2 to avoid overlapping pairs.
    for j in range(0, len(chains), 2):
        pair = chains[j:j + 2]

        # Skip a trailing incomplete chunk when length is odd.
        if len(pair) < 2:
            continue

        if pair == current_pair:
            current_count += 1
        else:
            if current_pair is not None:
                encoded_parts.append(current_pair + str(current_count))
            current_pair = pair
            current_count = 1

    if current_pair is not None:
        encoded_parts.append(current_pair + str(current_count))

    encoded_results += "".join(encoded_parts)

    return encoded_results


solution = bigram_counting_chains


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="bigram_counting_chains_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        chains = "aaababbababaca"
        print(bigram_counting_chains(chains))