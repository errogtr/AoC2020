from math import prod


def trees(slope_x, slope_y, height, width, trees_map):
    trees_count = 0
    x, y = [0, 0]
    while y < height:
        if trees_map[(x % width, y)] == "#":
            trees_count += 1
        x += slope_x
        y += slope_y
    return trees_count


with open("data") as f:
    lines = f.read().splitlines()


trees_map = {(x, y): v for y, l in enumerate(lines) for x, v in enumerate(l)}
height = len(lines)
width = len(lines[0])

# ========= PART 1 =========
print(trees(3, 1, height, width, trees_map))

# ========= PART 2 =========
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(
    prod(
        trees(slope_x, slope_y, height, width, trees_map) for slope_x, slope_y in slopes
    )
)
