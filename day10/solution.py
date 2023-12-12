from functools import lru_cache
from itertools import pairwise, groupby
from math import prod


@lru_cache
def compositions(n):
    match n:
        case 0: return 1
        case 1: return 1
        case 2: return 2
    return sum(compositions(n-k) for k in [1, 2, 3])


with open("data") as f:
    joltage = [int(x) for x in f.readlines()]

jolt_diffs = [y - x for x, y in pairwise(sorted(joltage + [0, max(joltage) + 3]))]

# ======== PART 1 =========
print(jolt_diffs.count(1) * jolt_diffs.count(3))

# ======== PART 2 =========
print(prod(compositions(len(list(g))) for k, g in groupby(jolt_diffs) if k == 1))
