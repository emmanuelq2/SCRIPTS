def mutual_digit_sum_pairs(l, r):
    # Store each number and the sum of its digits.
    s = {}
    for x in range(l, r+1):
        # Start the digit sum at 0 for the current number.
        digit_sum = 0
        # Use a temporary copy so we can break the number apart digit by digit.
        temp = x
        # Keep looping until there are no digits left in temp.
        while temp > 0:
            # temp % 10 gives the last digit of the number.
            # Example: 27 % 10 is 7.
            digit_sum += temp % 10
            # temp // 10 removes the last digit.
            # Example: 27 // 10 becomes 2.
            temp //= 10
        # Save the final digit sum for this number.
        s[x] = digit_sum

    # Count how many pairs satisfy the rule.
    valid_pairs_count = 0
    for a in range(l, r+1):
        for b in range(a + 1, r + 1):
            # Check whether b is inside a's allowed reach.
            valid_cfs_a = (a - s[a] <= b <= a + s[a])
            # Check whether a is inside b's allowed reach.
            valid_cfs_b = (b - s[b] <= a <= b + s[b])
            # Count the pair only if both numbers reach each other.
            if valid_cfs_a and valid_cfs_b:
                valid_pairs_count += 1

    # Return the number of valid pairs found.
    return valid_pairs_count


# Example for the range 9 to 11:
# 9  -> digit sum is 9,  so its reach is [0, 18]
# 10 -> digit sum is 1,  so its reach is [9, 11]
# 11 -> digit sum is 2,  so its reach is [9, 13]
#
# Pairs checked:
# (9, 10):
# - 10 is inside 9's reach  -> True
# - 9 is inside 10's reach  -> True
# - valid pair
#
# (9, 11):
# - 11 is inside 9's reach  -> True
# - 9 is inside 11's reach  -> True
# - valid pair
#
# (10, 11):
# - 11 is inside 10's reach -> True
# - 10 is inside 11's reach -> True
# - valid pair
#
# Total valid pairs from 9 to 11: 3


""" 
def solution(l, r):
    def digit_sum(x):
        return sum(int(d) for d in str(x))

    count = 0
    for a in range(l, r + 1):
        sa = digit_sum(a)
        for b in range(a + 1, r + 1):
            sb = digit_sum(b)
            if (a - sa <= b <= a + sa) and (b - sb <= a <= b + sb):
                count += 1
    return count """


