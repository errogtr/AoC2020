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

jolts_diff = [y - x for x, y in pairwise(sorted(joltage + [0, max(joltage) + 3]))]

# ======== PART 1 =========
print(jolts_diff.count(1) * jolts_diff.count(3))

# ======== PART 2 =========
print(prod(compositions(len(list(g))) for k, g in groupby(jolts_diff) if k == 1))
