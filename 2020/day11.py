f = open("./txt/day11.txt", "r")
text = f.read()
seat_rows = text.split("\n")
seat_arr = list(map(lambda x: [i for i in x], seat_rows))

ROW_NUM = len(seat_arr)
COL_NUM = len(seat_arr[0])

def check_around(seat_arr, i, j):
  count = 0
  # print("Looking at {},{}:".format(i, j), seat_arr[i][j])
  if i-1 >= 0:
    if seat_arr[i-1][j] == "#": count += 1
  if i+1 < ROW_NUM:
    if seat_arr[i+1][j] == "#": count += 1
  if j-1 >= 0:
    if seat_arr[i][j-1] == "#": count += 1
  if j+1 < COL_NUM:
    if seat_arr[i][j+1] == "#": count += 1
  if i-1 >= 0 and j-1 >= 0:
    if seat_arr[i-1][j-1] == "#": count += 1
  if i-1 >= 0 and j+1 < COL_NUM:
    if seat_arr[i-1][j+1] == "#": count += 1
  if i+1 < ROW_NUM and j-1 >= 0:
    if seat_arr[i+1][j-1] == "#": count += 1
  if i+1 < ROW_NUM and j+1 < COL_NUM:
    if seat_arr[i+1][j+1] == "#": count += 1
  # print(count)
  return count

def line_of_sight(seat_arr, i, j):
  print(seat_arr[i][j])
  # print(seat_arr[i-1][j+1])
  count = 0
  for up in range(1, i+1):
    if seat_arr[i-up][j] == "L":
      break
    if seat_arr[i-up][j] == "#":
      count += 1
      print("up")
      break
  for back in range(1, j+1):
    if seat_arr[i][j-back] == "L":
      break
    if seat_arr[i][j-back] == "#":
      count += 1
      print("back")
      break
  for fwd in range(1, COL_NUM-j):
    if seat_arr[i][j+fwd] == "L":
      break
    if seat_arr[i][j+fwd] == "#":
      count += 1
      print("fwd")
      break
  for down in range(1, ROW_NUM-i):
    if seat_arr[i+down][j] == "L":
      break
    if seat_arr[i+down][j] == "#":
      count += 1
      print("down")
      break

  for upbk in range(1, min(i+1,j+1)):
    if seat_arr[i-upbk][j-upbk] == "L":
      break
    if seat_arr[i-upbk][j-upbk] == "#":
      count += 1
      print("upbk")
      break
  for upfd in range(1, min(i+1,COL_NUM-j)):
    print("hey")
    print(seat_arr[i-upfd][j+upfd])
    if seat_arr[i-upfd][j+upfd] == "L":
      break
    if seat_arr[i-upfd][j+upfd] == "#":
      count += 1
      print("upfd")
      break
  for dnfd in range(1, min(COL_NUM-j, ROW_NUM-i)):
    if seat_arr[i+dnfd][j+dnfd] == "L":
      break
    if seat_arr[i+dnfd][j+dnfd] == "#":
      count += 1
      print("dnfd")
      break
  for dnbk in range(1, min(ROW_NUM-i, j+1)):
    if seat_arr[i+dnbk][j-dnbk] == "L":
      break
    if seat_arr[i+dnbk][j-dnbk] == "#":
      count += 1
      print("dnbk")
      break
  print(i, j, count)
  return count

  




def occupy_seats(seat_arr):
  arr_out = [[i for i in j] for j in seat_arr]
  print("s",seat_arr)
  print("a",arr_out)
  for i in range(ROW_NUM):
    for j in range(COL_NUM):
      curr = seat_arr[i][j]
      num = check_around(seat_arr, i, j)
      if curr == ".": 
        continue
      elif curr == "L" and num == 0:
        arr_out[i][j] = "#"
      elif curr == "#" and num >= 4:
        arr_out[i][j] = "L"
  return arr_out

def occupy_seats_2(seat_arr):
  arr_out = [[i for i in j] for j in seat_arr]
  # print("s",seat_arr)
  # print("a",arr_out)
  for i in range(ROW_NUM):
    for j in range(COL_NUM):
      curr = seat_arr[i][j]
      num = line_of_sight(seat_arr, i, j)
      if curr == ".": 
        continue
      elif curr == "L" and num == 0:
        arr_out[i][j] = "#"
      elif curr == "#" and num >= 5:
        arr_out[i][j] = "L"
  return arr_out

def count_occu(seat_arr):
  count = 0
  for i in range(ROW_NUM):
    for j in range(COL_NUM):
      if seat_arr[i][j] == "#":
        count += 1
  return count

def part1(seat_arr):
  prev = []
  curr = seat_arr
  while prev != curr:
    prev = curr
    curr = occupy_seats(curr)
  print(curr)

def part2(seat_arr):
  prev = []
  curr = seat_arr
  while prev != curr:
    prev = curr
    curr = occupy_seats_2(curr)
  print(curr)

# for i in range(ROW_NUM):
#   for j in range(ROW_NUM):
# line_of_sight(seat_arr, 1, 2)

part2(seat_arr)
# out = line_of_sight(seat_arr, 3, 3)
# print(out)
# out = check_around(seat_arr, 0, 0)
# out = occupy_seats(seat_arr)
# print(out)
# print(check_around(seat_arr, 0, 2))
# part1(seat_arr)