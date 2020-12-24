import numpy as np
from copy import deepcopy

f = open("./txt/day17.txt", "r")
text = f.read()
lines = text.split("\n")

# print(out[6][6][7][7])

pocket = np.full((len(lines)+12, len(lines[0])+12, 15, 15), ".")

# pocket = np.full(())

def count_adjacent(i, j, k, l):
  global pocket

  count = 0
  for i_add in [-1, 0, 1]:
    for j_add in [-1, 0, 1]:
      for k_add in [-1, 0, 1]:
        for l_add in [-1, 0, 1]:
          if i_add == j_add == k_add == l_add == 0:
            continue
          if i+i_add not in range(len(pocket)):
            continue
          if j+j_add not in range(len(pocket[0])):
            continue
          if k+k_add not in range(len(pocket[0][0])):
            continue
          if l+l_add not in range(len(pocket[0][0][0])):
            continue
          
          to_check = pocket[i+i_add][j+j_add][k+k_add][l+l_add]
          if to_check == "#":
            count += 1
  return count

def fill_start(start_arr):
  global pocket
  for i in range(len(start_arr)):
    for j in range(len(start_arr[0])):
      pocket[6+i][6+j][len(pocket[0][0])//2][len(pocket[0][0][0])//2] = start_arr[i][j]

def step():
  global pocket

  pocket_copy = deepcopy(pocket)
  for i in range(len(pocket)):
    for j in range(len(pocket[0])):
      for k in range(len(pocket[0][0])):
        for l in range(len(pocket[0][0][0])):
          curr = pocket[i][j][k][l]
          count = count_adjacent(i, j, k, l)
          if curr == "#": # active
            if count != 2 and count != 3:
              pocket_copy[i][j][k][l] = "."
          elif curr == ".": # inactive
            if count == 3:
              pocket_copy[i][j][k][l] = "#"
  pocket = pocket_copy

def count_hashes():
  global pocket
  count = 0
  for i in range(len(pocket)):
    for j in range(len(pocket[0])):
      for k in range(len(pocket[0][0])):
        for l in range(len(pocket[0][0][0])):
          if pocket[i][j][k][l] == "#":
            count += 1
  return count




start = []
for line in lines:
  start.append(list(line))

fill_start(start)
print("first count:", count_hashes())
for i in range(6):
  step()
  print("count", i, ":", count_hashes())