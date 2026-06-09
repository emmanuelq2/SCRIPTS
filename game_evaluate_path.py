def evaluatePath(numbers: list[int]) -> tuple[int, int]:
    position = 0
    moves = 0
    direction = 1  # 1: normal mapping, -1: inverted mapping
    reversed_once: bool = False

    while True:
        value = numbers[position]

        # A blockade always ends the game immediately.
        if value == 0:
            return (position, moves)

        next_position = position + direction * value

        # Out-of-bounds means movement in this direction is blocked.
        if next_position < 0 or next_position >= len(numbers):
            # Second boundary encounter ends the game.
            if reversed_once == True:
                return (position, moves)

            # First boundary encounter: reverse directions and try again.
            direction *= -1
            reversed_once = True
            continue

        position = next_position
        moves += 1


# Backward-compatible alias for the previous naming style.
def game_evaluate_path(numbers: list[int]) -> tuple[int, int]:
    return evaluatePath(numbers)


if __name__ == "__main__":
    sample = [3, 4, 1, 1, -3, 1]
    print(evaluatePath(sample))  # (4, 5)
