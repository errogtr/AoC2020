from itertools import pairwise


def bin2int(string, zero, one):
    return int(string.replace(zero, "0").replace(one, "1"), 2)


with open("data") as f:
    binaries = [(s[:7], s[7:]) for s in f.read().splitlines()]

# ========= PART 1 =========
seat_ids = [
    8 * bin2int(row, "F", "B") + bin2int(col, "L", "R") for row, col in binaries
]
print(max(seat_ids))

# ========= PART 2 =========
print(next(x + 1 for x, y in pairwise(sorted(seat_ids)) if y - x == 2))
