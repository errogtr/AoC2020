with open("data") as f:
    groups = f.read().split("\n\n")

# ========= PART 1 =========
print(sum(len(set.union(*map(set, group.split()))) for group in groups))

# ========= PART 2 =========
print(sum(len(set.intersection(*map(set, group.split()))) for group in groups))
