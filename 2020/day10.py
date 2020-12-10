f = open("./txt/day10.txt", "r")
text = f.read()
adaps = text.split("\n")
adaps = list(map(int, adaps))



def part1(adaps):
  adap_list = sorted(adaps)
  print(adap_list)
  n = len(adap_list)
  ones = 1
  threes = 1 
  for i in range(n-1):
    if adap_list[i] + 1 == adap_list[i+1]:
      ones += 1
    elif adap_list[i] + 3 == adap_list[i+1]:
      threes += 1
  print("ones",ones)
  print("threes",threes)
  print("ans",ones*threes)

from collections import Counter
def part2(adaps):
  n = len(adaps)
  adap_list = sorted(adaps)
  adap_list += [0,0,0]
  print(adap_list[:n])
  poss_list = [0]*(n+3)

  for i in range(n):
    if adap_list[i] + 1 == adap_list[i+1]:
      poss_list[i] += 1
    if adap_list[i] + 2 == adap_list[i+1]:
      poss_list[i] += 1
    if adap_list[i] + 3 == adap_list[i+1]:
      poss_list[i] += 1
    
    if adap_list[i] + 2 == adap_list[i+2]:
      poss_list[i] += 1
    if adap_list[i] + 3 == adap_list[i+2]:
      poss_list[i] += 1

    if adap_list[i] + 3 == adap_list[i+3]:
      poss_list[i] += 1
  
  # poss_list[n = 
  poss_list = poss_list[:n]
  poss_ct = Counter(poss_list)
  return poss_list
  print(poss_list[:n])
  print(poss_ct)


def rec(poss_list, index):
  # n = len(poss_list)
  # poss_list += [0,0]
  # for i in range(n):
  # print(poss_list)
  if poss_list[index] == 0:
    return 1
  if poss_list[index] == 3:
    a = rec(poss_list, index+1)
    b = rec(poss_list, index+2)
    c = rec(poss_list, index+3)
    return a+b+c
  if poss_list[index] == 2:
    a = rec(poss_list, index+1)
    b = rec(poss_list, index+2)
    return a+b
  if poss_list[index] == 1:
    a = rec(poss_list, index+1)
    return a

def rec_2(poss_list):
  rev = list(reversed(poss_list))
  n = len(rev)
  print("rev:", rev)
  out = [0]*n
  for i in range(n):
    thing = rev[i]
    if thing == 0:
      out[i] = 1
    if thing == 1:
      out[i] = out[i-1]
    if thing == 2:
      out[i] = out[i-1] + out[i-2]
    if thing == 3:
      out[i] = out[i-1] + out[i-2] + out[i-3]
  return out
poss_list = part2(adaps)
print(rec_2(poss_list))
out = sum(rec_2(poss_list)[-1] + rec_2(poss_list)[-2])
print(out)