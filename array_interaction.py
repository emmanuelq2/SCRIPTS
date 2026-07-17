def simulation_game(balloons):
    # Stores the number of houses/players in
    n = len(balloons)
    # Initializes a counter to track how many simulation rounds are executed.
    steps = 0

    # Starts an infinite loop. The loop will only stop when a break condition is met.
    while True:
        # Increments the round counter at the start of each loop iteration.
        steps += 1
        # Creates a copy of the current state of balloons to calculate the next state.
        new_balloons = balloons.copy()
        for i in range(n):
            # Computes how many balloons house i gives away: half of its current balloons, using integer division.
            share = balloons[i] // 2  # Balloons to share
            new_balloons[i] -= share  # Decrease balloons of current house.
            new_balloons[(i + 1) % n] += share  # Increase balloons of next house. ((i + 1) % n) is used to make the list circular.
        # Checks whether the new state is identical to the previous state (no change happened this round).
        if new_balloons == balloons:
            break
        balloons = new_balloons
    return steps


'''
- Initial balloons: `[5, 1, 0]`
- `n = 3`
- `steps = 0`

Rules per round:
- Each house gives half of its current balloons (`// 2`) to the next house.
- “Next house” wraps around (last gives to first).
- All transfers are based on the old list, and applied to a copied list.

### Round 1
Start:
- `balloons = [5, 1, 0]`
- `steps = 1`
- `new_balloons = [5, 1, 0]` (copy)

Now loop each index:

1. `i = 0`
- `share = 5 // 2 = 2`
- House 0 loses 2: `new_balloons -> [3, 1, 0]`
- House 1 gains 2: `new_balloons -> [3, 3, 0]`

2. `i = 1`
- `share = 1 // 2 = 0`
- No change: `new_balloons -> [3, 3, 0]`

3. `i = 2`
- `share = 0 // 2 = 0`
- No change: `new_balloons -> [3, 3, 0]`

End round:
- Old was `[5, 1, 0]`, new is `[3, 3, 0]` (changed)
- Update: `balloons = [3, 3, 0]`

---

### Round 2
Start:
- `balloons = [3, 3, 0]`
- `steps = 2`
- `new_balloons = [3, 3, 0]`

1. `i = 0`
- `share = 3 // 2 = 1`
- House 0 loses 1: `[2, 3, 0]`
- House 1 gains 1: `[2, 4, 0]`

2. `i = 1`
- `share = 3 // 2 = 1` (important: from old `balloons`, not updated one)
- House 1 loses 1: `[2, 3, 0]`
- House 2 gains 1: `[2, 3, 1]`

3. `i = 2`
- `share = 0 // 2 = 0`
- No change: `[2, 3, 1]`

End round:
- Old was `[3, 3, 0]`, new is `[2, 3, 1]` (changed)
- Update: `balloons = [2, 3, 1]`

---

### Round 3
Start:
- `balloons = [2, 3, 1]`
- `steps = 3`
- `new_balloons = [2, 3, 1]`

1. `i = 0`
- `share = 2 // 2 = 1`
- `[1, 4, 1]`

2. `i = 1`
- `share = 3 // 2 = 1`
- House 1 down, house 2 up: `[1, 3, 2]`

3. `i = 2`
- `share = 1 // 2 = 0`
- No change: `[1, 3, 2]`

End round:
- Old `[2, 3, 1]`, new `[1, 3, 2]` (changed)
- Update.

---

### Round 4
Start:
- `balloons = [1, 3, 2]`
- `steps = 4`
- `new_balloons = [1, 3, 2]`

1. `i = 0` -> `share = 0`  
2. `i = 1` -> `share = 1`: `[1, 2, 3]`  
3. `i = 2` -> `share = 1`: house 2 to house 0 -> `[2, 2, 2]`

End round:
- Old `[1, 3, 2]`, new `[2, 2, 2]` (changed)
- Update.

---

### Round 5
Start:
- `balloons = [2, 2, 2]`
- `steps = 5`
- `new_balloons = [2, 2, 2]`

Each house shares `2 // 2 = 1`, so everyone gives 1 and receives 1.
Result stays `[2, 2, 2]`.

Now:
- `new_balloons == balloons` is true
- loop stops (`break`)
- function returns `steps = 5`

So for input `[5, 1, 0]`, output is `5`.

If you want, I can do one more example where it stabilizes in just 1 or 2 rounds so you can compare patterns.
'''