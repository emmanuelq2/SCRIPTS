import time
import tracemalloc
from typing import List

def count_peaks(values: List[float]) -> int:
    """
    Args:
        values (List[float]): The radioactivity values measured by the sensor.
                              Length between 0 and 20 inclusive.
                              Each value between 0 and 100 inclusive.
    Returns:
        int: The total number of top peaks and bottom peaks.
    """

    # Constraint 1: Length check
    if not (0 <= len(values) <= 20):
        raise ValueError("Length of values must be between 0 and 20.")

    # Constraint 2: Value range check
    if any(v < 0 or v > 100 for v in values):
        raise ValueError("All values must be between 0 and 100 inclusive.")

    tracemalloc.start()
    start_time = time.time()

    peak_count = 0
    
    # Iterate excluding first and last element
    for i in range(1, len(values) - 1):
        # Top peak
        if values[i] >= values[i - 1] + 5 and values[i] >= values[i + 1] + 5:
            peak_count += 1
        # Bottom peak
        elif values[i] <= values[i - 1] - 5 and values[i] <= values[i + 1] - 5:
            peak_count += 1

        # Constraint 3: Time limit check
        if time.time() - start_time > 1:
            raise TimeoutError("Execution time exceeded 1 second.")

        # Constraint 4: Memory limit check
        current, peak = tracemalloc.get_traced_memory()
        if peak > 512 * 1024 * 1024:  # 512 MB in bytes
            raise MemoryError("Memory usage exceeded 512 MB.")
    
    tracemalloc.stop()
    return peak_count


# Edge case tests for count_peaks
def run_tests():
    # Valid edge cases
    assert count_peaks([]) == 0
    assert count_peaks([50]) == 0
    assert count_peaks([0, 100]) == 0
    assert count_peaks([0, 5, 0]) == 1
    assert count_peaks([10, 5, 10]) == 1
    assert count_peaks([0, 4.999, 0]) == 0
    assert count_peaks([50, 50, 50]) == 0
    assert count_peaks([0, 10, 20, 30]) == 0
    assert count_peaks([30, 20, 10, 0]) == 0
    assert count_peaks([0, 10, 10, 0]) == 0
    assert count_peaks([10, 14.9, 10]) == 0
    assert count_peaks([0, 6, 0, 7, 0]) == 3
    assert count_peaks([100, 95, 100]) == 1
    assert count_peaks([5, 10, 6]) == 0
    assert count_peaks([10, 0, 10, 0, 10]) == 3
    seq20 = ([0, 10] * 10)[:20]
    assert len(seq20) == 20 and count_peaks(seq20) == 18


    # Invalid constraint-violating cases
    try:
        count_peaks([-1, 5, -1])
        assert False, "Expected ValueError for value < 0"
    except ValueError:
        pass

    try:
        count_peaks([0]*21)
        assert False, "Expected ValueError for length > 20"
    except ValueError:
        pass

    try:
        count_peaks([0, 5, 101])
        assert False, "Expected ValueError for value > 100"
    except ValueError:
        pass

    print("All tests passed!")

# Run the test suite
run_tests()