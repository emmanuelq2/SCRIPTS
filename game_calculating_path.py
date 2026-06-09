def calculatingPath(board: list[int], obstacle: int) -> list[int]:
    n = len(board)
    moves = [0] * n

    # Compute from right to left because each jump goes strictly to the right.
    for i in range(n - 1, -1, -1): # start = n - 1, stop = - 1, step = -1
        value = board[i]

        if value == obstacle:
            moves[i] = -1
            continue

        next_position = i + value

        # One move directly exits the board.
        if next_position >= n:
            moves[i] = 1
            continue

        # If the landing position cannot finish, current position cannot either.
        if moves[next_position] == -1:
            # The path from next_position eventually lands on obstacle,
            # so starting from i also fails.
            moves[i] = -1
        else:
            # Dynamic programming transition:
            # 1 move to jump from i to next_position,
            # then reuse the already computed moves from next_position.
            # Example on [5, 3, 2, 6, 2, 1, 7] with obstacle=3:
            # moves[5] = 2 and from i=0 we jump to 5,
            # so moves[0] = 1 + moves[5] = 3.  
            # => we know that from position 0, we can jump to position 5 in one move, 
            # and from position 5, it takes 2 moves to exit the board, so total moves 
            # from position 0 is 1 (to jump to 5) + 2 (moves from 5) = 3.  
            moves[i] = 1 + moves[next_position]

    return moves


if __name__ == "__main__":
    print(calculatingPath([5, 3, 2, 6, 2, 1, 7], 3))  # [3, -1, 3, 1, 2, 2, 1]