from math import sqrt, floor

def two_crystal_balls(breaks: list[bool]) -> int:
    jump_amount = floor(sqrt(len(breaks)))

    # 1. Find breaking point
    i = 0
    while i < len(breaks):
        if breaks[i]:
            break
        i += jump_amount

    # 2. Jump back sqrt
    i -= jump_amount

    # 3. Walk forward towards sqrt
    j = 0

    while j <= jump_amount and i < len(breaks):
        if(breaks[i]):
            return i
        i += 1
        j += 1

    return -1

breaks = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
assert two_crystal_balls(breaks) == 7

no_break = [0, 0, 0, 0, 0, 0, 0, 0, 0]
assert two_crystal_balls(no_break) == -1

break_at_first = [1, 0, 0, 0, 0, 0, 0, 0, 0]
assert two_crystal_balls((break_at_first)) == 0

break_at_last = [0, 0, 0, 0, 0, 0, 0, 0, 1]
assert two_crystal_balls(break_at_last) == 8