def count_valid(lines, checker):
  count = 0
  for line in lines:
    tup = line.split(": ") # [0-99 c, password]

    rng = tup[0].split(" ")[0].split("-")
    letter = tup[0].split(" ")[1]
    low = int(rng[0])
    high = int(rng[1])
    
    pwd = tup[1]

    cond = checker(low, high, letter, pwd)

    if cond: count += 1
  return count


def check_1(low, high, letter, password):
  count = 0
  for char in password:
    if char == letter:
      count += 1
  return count in range(low, high+1)

def check_2(incl, excl, letter, password):
  cond1 = password[incl-1] == letter
  cond2 = password[excl-1] == letter
  return cond1 != cond2


f = open("day2.txt", "r")
text = f.read()
lines = text.split("\n")
f.close()

out = count_valid(lines, check_1)
print("Of {} passwords, {} are valid.".format(len(lines), out))
out = count_valid(lines, check_2)
print("Of {} passwords, {} are valid.".format(len(lines), out))