def add_days(date: str, n: int) -> str:
    """Return the date obtained by adding n days to YYYY-MM-DD.

        Step-by-step example (forward):
        - Input: date="2024-01-01", n=151
        - 2024 is leap year, so February has 29 days.
        - We consume full months from January:
            Jan 31 -> n becomes 120, date becomes 2024-02-01
            Feb 29 -> n becomes 91,  date becomes 2024-03-01
            Mar 31 -> n becomes 60,  date becomes 2024-04-01
            Apr 30 -> n becomes 30,  date becomes 2024-05-01
        - Remaining n=30 fits in May, so final date is 2024-05-31.

        Step-by-step example (backward):
        - Input: date="2024-03-01", n=-2
        - Move back 1 day -> 2024-02-29 (leap day)
        - Move back 1 day -> 2024-02-28
        - Final date is 2024-02-28.
    """

    def leap_year(year: int) -> bool:
        # Leap year rule in the Gregorian calendar.
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def year_days(year: int) -> int:
        # Number of days in the given year.
        return 366 if leap_year(year) else 365

    def month_length(year: int, month: int) -> int:
        # February depends on leap year status; others are fixed.
        if month == 2:
            return 29 if leap_year(year) else 28
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[month]

    # Parse the input date.
    year, month, day = [int(x) for x in date.split("-")]

    # Move forward while n is positive.
    while n > 0:
        # Optimization: if we are exactly at Jan 1, skip whole years at once.
        if month == 1 and day == 1 and n >= year_days(year):
            n = n - year_days(year)
            year += 1
            continue

        # Days left in the current month from the current day.
        # If date is 2024-02-10 => month_length(2024, 2) = 29 (leap year)
        current_month_days = month_length(year, month)
        remaining_in_month = current_month_days - day # how many days remain before this month ends?

        # If remaining n fits in this month, finish directly.
        # Example:
        # - current date: 2024-05-10
        # - month has 31 days, so remaining_in_month = 31 - 10 = 21
        # - if n=7, then 7 <= 21 -> day becomes 17, n becomes 0 (done)
        if n <= remaining_in_month:
            day += n
            n = 0
        else:
            # Jump to day 1 of next month and consume passed days.
            # Example:
            # - current date: 2024-04-20, n=20
            # - remaining_in_month = 30 - 20 = 10
            # - consume 10 days to month end + 1 day to reach next month start
            # - n becomes 20 - (10 + 1) = 9
            # - new date becomes 2024-05-01, then loop continues with n=9
            n = n - (remaining_in_month + 1)
            day = 1
            if month == 12:  # if we are in December, next month is January of next year
                month = 1
                year += 1
            else:
                month += 1

    # Move backward while n is negative.
    while n < 0:
        # Optimization: if we are exactly at Jan 1, skip full previous years.
        previous_year_days = year_days(year - 1)
        if month == 1 and day == 1 and -n >= previous_year_days:
            year -= 1
            n += previous_year_days
            continue

        # If we stay in the same month when moving backward.
        # Example:
        # - current date: 2024-05-20, n=-6
        # - day + n = 20 - 6 = 14 (> 0), so we stay in May
        # - new date becomes 2024-05-14, n becomes 0
        if day + n > 0:
            day += n
            n = 0
        else:
            # Move to previous month end and continue consuming n.
            # Example:
            # - current date: 2024-05-03, n=-10
            # - day + n = 3 - 10 = -7 (cannot stay in May)
            # - consume current day count: n becomes -10 + 3 = -7
            # - move to previous month end: 2024-04-30
            # - loop continues from there with n=-7
            n += day
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
            day = month_length(year, month)

    # Rebuild YYYY-MM-DD with leading zeros.
    return f"{year:04d}-{month:02d}-{day:02d}"
