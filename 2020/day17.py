f = open("./txt/day17.txt", "r")
text = f.read()
lines = text.split("\n")

empty_line = "."*(len(lines)+12)

pocket = []

for i in range(6+(len(lines)//2)):
  add = []
  for i in range(12+len(lines)):
    add.append(list(empty_line))
  pocket.append(add)
z0 = []
for i in range(6):
  z0.append(list(empty_line))
for line in lines:
  z0.append(list("."*6 + line + "."*6))
for i in range(6):
  z0.append(list(empty_line))
pocket.append(z0)
for i in range(6+(len(lines)//2)):
  add = []
  for i in range(12+len(lines)):
    add.append(list(empty_line))
  pocket.append(add)


def adjacent(pocket, x, y, z):
  counter = 0
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      for k in [-1, 0, 1]:
        if i == j == k == 0: continue
        if x+i not in range(len(pocket)) or y+j not in range(len(pocket[0])) or z+k not in range(len(pocket[0][0])): continue
        # print(x+i, y+j, z+k, sep=",")
        if pocket[x + i][y + j][z + k] == "#":
          counter += 1
  return counter


print("x", len(pocket))
print("y", len(pocket[0]))
print("z", len(pocket[0][0]))

change = []
for _ in range(6):
  for i in range(len(pocket)):
    for j in range(len(pocket[0])):
      for k in range(len(pocket[0][0])):
        count = adjacent(pocket, i, j, k)
        if pocket[i][j][k] == "#" and not (count == 2 or count == 3):
          change.append((i, j, k, "."))
        if pocket[i][j][k] == "." and count == 3:
          change.append((i, j, k, "#"))
  for c in change:
    i, j, k, change_to = c[0], c[1], c[2], c[3]
    pocket[i][j][k] = change_to
print(pocket)

