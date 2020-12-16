f = open("./txt/day15.txt", "r")
text = f.read()
start = text.split(",")
start = list(map(int, start))

from collections import defaultdict

def generate_count(nums, turns):
  if turns <= len(nums):
    return nums[:turns]

  n = len(nums)
  seen = {}
  out = nums
  for i in range(n-1):
    seen[nums[i]] = i
  for i in range(n, turns):
    prev = nums[i-1]
    if not prev in seen: 
      num = 0
    else: 
      num = i - seen[prev] -1
    seen[prev] = i-1
    out.append(num)
  return out

def get_pos(nums, pos = 2020):
  return generate_count(nums, pos)[-1]

out = get_pos(start, 30000000)
print(out)
# def part1(start):
