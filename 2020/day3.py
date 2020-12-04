def tobogganHitsTree(x, field):
  if field[x % len(field)] == "#": return True
  else: return False

def treeEncounter(lines, xMove=3, yMove=1):
  n = len(lines)
  x = 0
  y = 0
  treeCount = 0
  while y < n:
    line = lines[y]
    if tobogganHitsTree(x, line):
      treeCount += 1
    x += xMove
    y += yMove
  return treeCount


f = open("day3.txt", "r")
text = f.read()
lines = text.split("\n")
a = treeEncounter(lines, 1, 1)
b = treeEncounter(lines, 3, 1)
c = treeEncounter(lines, 5, 1)
d = treeEncounter(lines, 7, 1)
e = treeEncounter(lines, 1, 2)
out = a*b*c*d*e



print(out)

f.close()