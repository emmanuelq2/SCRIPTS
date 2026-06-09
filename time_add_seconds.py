def add_seconds_to_times(timePoints, seconds):
    result = []
    for time_point in timePoints:
        time_parts = [int(part) for part in time_point.split(":")]
        seconds_since_start = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
        total_seconds = (seconds_since_start + seconds) % (24 * 3600)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        result.append(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    return result