def getRow(code):
  out = 0
  n = len(code)
  for i in range(n):
    if code[i] == "B":
      out += 2 ** (6-i)
    else:
      out += 0
  return out

def getCol(code):
  out = 0
  n = len(code)
  for i in range(n):
    if code[i] == "R":
      out += 2 ** (2-i)
    else:
      out += 0
  return out

def getId(row, col):
  return row*8 + col

def partition(ticket):
  return (ticket[:7], ticket[7:])


f = open("./txt/day5.txt", "r")
text = f.read()
lines = text.split("\n")

seats = []
for line in lines:
  part = partition(line)
  row = getRow(part[0])
  col = getCol(part[1])
  seats.append(getId(row, col))
print("Part 1")
print("The highest plane ticket ID is {}.".format(max(seats)))

seats.sort()
n = len(seats)
for i in range(n-1):
  if seats[i] + 1 != seats[i+1]:
    print("Part 2")
    print("Your seat is at {}.".format(seats[i]+1))
# print(seats)

# print(partition(lines[0]))