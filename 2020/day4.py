
def extra_check(passport):
    if not 1920 <= int(passport["byr"]) <= 2002:
        return False
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False


    if not (passport["hgt"].endswith("cm") or passport["hgt"].endswith("in")):
        return False
    if passport["hgt"].endswith("cm"):
        height = passport["hgt"].split("cm")[0]
        if not 150 <= int(height) <= 193:
            return False
    if passport["hgt"].endswith("in"):
        height = passport["hgt"].split("in")[0]
        if not 59 <= int(height) <= 76:
            return False

    if not len(passport["hcl"]) == 7:
        return False
    if not passport["hcl"].startswith("#"):
        return False
    hair_code = passport["hcl"].split("#")[1]
    for hc in hair_code:
        if not hc in "0123456789abcdef":
            return False

    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not passport["ecl"] in valid_ecl:
        return False
    
    if not len(passport["pid"]) == 9:
        return False
    for num in passport["pid"]:
        if not num in "0123456789":
            return False
    return True

def passport_contains(passport, contains):
    for c in contains:
        if not c in passport:
            return False
    return extra_check(passport)


def dictionarify(passport):
    store = {}
    keyvals = passport.split()

    for kv in keyvals:
        kv_arr = kv.split(":")
        store[kv_arr[0]] = kv_arr[1]
    return store


def ans(lines, contains=["byr","iyr","eyr","hgt","hcl","ecl","pid"]):
    count = 0
    for line in lines:
        passport = dictionarify(line)
        if passport_contains(passport, contains):
            count += 1
    return count


f = open("day4.txt", "r")
text = f.read()
# text.replace("\n", " ")
lines = text.split("\n\n")
out = ans(lines)
print(out)
