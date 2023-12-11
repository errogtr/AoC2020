from itertools import combinations


def is_valid(num, previous):
    return any(x + y == num for x, y in combinations(previous, 2))


def rolling(numbers, invalid_num, max_idx):
    for i in range(max_idx - 1):
        for j in range(i + 1):
            window = numbers[j : invalid_idx - i + j]
            if sum(window) == invalid_num:
                return min(window) + max(window)
    return 0


with open("data") as f:
    numbers = [int(x) for x in f.readlines()]

invalid_num, invalid_idx = None, None
for i, num in enumerate(numbers[25:]):
    preamble = numbers[i : 25 + i]
    if not is_valid(num, preamble):
        invalid_num, invalid_idx = num, i + 25
        break

# ========= PART 1 ==========
print(invalid_num)

# ========= PART 2 ==========
print(rolling(numbers, invalid_num, invalid_idx))
