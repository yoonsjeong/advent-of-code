import re

f = open("./txt/day12.txt", "r")
text = f.read()
instruct = text.split("\n")

GLOBAL_X = 0
GLOBAL_Y = 0
POS = ["E", "S", "W", "N"]
CURR_DIR = 0

def change_dir(movement):
  global CURR_DIR, GLOBAL_X, GLOBAL_Y, POS, CURR_DIR
  word, num = movement[0], int(movement[1])
  index = num//90
  if word == "L":
    CURR_DIR = (CURR_DIR - index) % 4
  elif word == "R":
    CURR_DIR = (CURR_DIR + index) % 4
  else:
    raise "Shouldn't have arrived here."


def move(movement):
  global CURR_DIR, GLOBAL_X, GLOBAL_Y, POS, CURR_DIR
  word, num = movement[0], int(movement[1])
  if word == "N":
    GLOBAL_Y += num
  elif word == "S":
    GLOBAL_Y -= num
  elif word == "E":
    GLOBAL_X += num
  elif word == "W":
    GLOBAL_X -= num
  elif word == "F":
    move([POS[CURR_DIR], num])
  elif word == "L" or word == "R":
    change_dir(movement)


def part1(instruct):
  for i in instruct:
    ii = re.split("(\d+)", i)[:2]
    move(ii)
    print(GLOBAL_X)
    print(GLOBAL_Y)
    print(POS[CURR_DIR])
    print("======")

# E, N +
# W, S -
WAYPT_POS = [10, 1]

def move_ship(moveX, moveY):
  global GLOBAL_X, GLOBAL_Y, WAYPT_POS
  GLOBAL_X += moveX
  GLOBAL_Y += moveY

def change_waypt(val):
  global GLOBAL_X, GLOBAL_Y, WAYPT_POS
  n = val % 4
  for _ in range(n):
    WAYPT_POS = [WAYPT_POS[1], -WAYPT_POS[0]]


def move_waypt(movement):
  global GLOBAL_X, GLOBAL_Y, WAYPT_POS
  word, num = movement[0], int(movement[1])
  if word == "N":
    WAYPT_POS[1] += num
  elif word == "S":
    WAYPT_POS[1] -= num
  elif word == "E":
    WAYPT_POS[0] += num
  elif word == "W":
    WAYPT_POS[0] -= num
  
  elif word == "F":
    move_ship(WAYPT_POS[0]*num, WAYPT_POS[1]*num)
  elif word == "L":
    change_waypt(-num//90)
  elif word == "R":
    change_waypt(num//90)


def part2(instruct):
  for i in instruct:
    ii = re.split("(\d+)", i)[:2]
    move_waypt(ii)
    print(GLOBAL_X)
    print(GLOBAL_Y)
    print(POS[CURR_DIR])
    print("======")



# part1(instruct)
part2(instruct)

# print(GLOBAL_X)
# print(GLOBAL_Y)
# print(POS[CURR_DIR])
