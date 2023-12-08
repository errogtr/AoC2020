from itertools import combinations

with open("data") as f:
    report = [int(x) for x in f.readlines()]


# ========= PART 1 =========
print(next(x * y for x, y in combinations(report, 2) if x + y == 2020))


# ========= PART 2 =========
print(next(x * y * z for x, y, z in combinations(report, 3) if x + y + z == 2020))
