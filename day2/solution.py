import re

with open("data") as f:
    policies = [
        (*map(int, re.findall(r"\d+", l)), *re.findall(r"[a-z]+", l))
        for l in f.read().splitlines()
    ]

# ========= PART 1 =========
print(sum(m <= pwd.count(c) <= M for m, M, c, pwd in policies))

# ========= PART 2 =========
print(sum((pwd[m - 1] == c) + (pwd[M - 1] == c) == 1 for m, M, c, pwd in policies))
