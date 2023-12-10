import re

BAG_REGEX = re.compile(r"(\d+)\s(.+)\sbags*")


def parse_rule(rule):
    bag, contains = rule.split(" bags contain ", 1)
    bag_matches = [BAG_REGEX.search(x) for x in contains.split(",")]
    return bag, {m.group(2): int(m.group(1)) for m in bag_matches if m}


def contains_shiny_gold(this_color, rules):
    this_bag_rules = rules[this_color]
    if "shiny gold" in this_bag_rules or any(
        contains_shiny_gold(color, rules) for color in this_bag_rules
    ):
        return True
    return False


def contained_in_shiny_gold(this_color, rules):
    return sum(
        n * (contained_in_shiny_gold(color, rules) + 1)
        for color, n in rules[this_color].items()
    )


with open("data") as f:
    rules = dict(parse_rule(rule) for rule in f.read().splitlines())

# ========= PART 1 =========
print(sum(contains_shiny_gold(color, rules) for color in rules))

# ========= PART 2 =========
print(contained_in_shiny_gold("shiny gold", rules))
