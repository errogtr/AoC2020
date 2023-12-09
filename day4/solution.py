import re

MANDATORY_FIELDS = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x.strip("cm")) <= 193)
    or (x.endswith("in") and 59 <= int(x.strip("in")) <= 76),
    "hcl": lambda x: re.match(r"^#[a-f0-9]{6}$", x) is not None,
    "ecl": lambda x: x in "amb blu brn gry grn hzl oth".split(),
    "pid": lambda x: re.match(r"\d{9}$", x) is not None,
}


def passport_fields(passport):
    return dict(field.split(":") for field in passport.split())


def is_valid(passport):
    for field in MANDATORY_FIELDS:
        if field not in passport_fields(passport):
            return False
    return True


def fields_valid(passport):
    if not is_valid(passport):
        return False

    for field, value in passport_fields(passport).items():
        if field == "cid":
            continue
        if not MANDATORY_FIELDS[field](value):
            return False
    return True


with open("data") as f:
    passports = f.read().split("\n\n")

# ========= PART 1 =========
print(sum(is_valid(passport) for passport in passports))

# ========= PART 2 =========
print(sum(fields_valid(passport) for passport in passports))
