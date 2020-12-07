f = open("./txt/day7.txt", "r")
text = f.read()
lines = text.replace(".","").split("\n")
# print(lines)

def dictionarify(lines):
  store = {}
  for line in lines:
    key = line.split(" contain ")[0]
    values = line.split(" contain ")[1]
    store[key] = values
  return store

def dictionarify2(bag_list):
  store = {}
  for b in bag_list:
    inside = bag_list[b].split(", ")
    
    total_bags = 0
    for i in inside:
      num = int(inside[:1])
      total_bags += num
    store[b] = total_bags
  return store


def gold_bagify(bag_list, keyword):
  arr = []
  for b in bag_list:
    if keyword in bag_list[b]:
      arr.append(b)
  return arr

bag_list = dictionarify(lines)
print(bag_list)
count = 0
arr = ["shiny gold bags"]
counted = []
while len(arr) != 0:
  a = arr[0][:-1]
  if a in counted: 
    arr.pop(0)
    continue
  else: counted.append(a)
  print(a)

  arr += gold_bagify(bag_list, a) # get rid of the s!!!
  # print(len(gold_bagify(bag_list, a)))
  print(count)
  count += 1
  # print(arr)

print(count - 1)



