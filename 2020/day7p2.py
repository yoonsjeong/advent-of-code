f = open("./txt/day7.txt", "r")
text = f.read()
lines = text.replace(".","").split("\n")

def dictionarify(lines):
  store = {}
  for line in lines:
    bag_type = line.split(" contain ")[0]
    bag_val = line.split(" contain ")[1].split(", ")
    bag_key = "{0} {1}".format(bag_type.split(" ")[0], bag_type.split(" ")[1])
    
    store2 = {}
    for v in bag_val:
      name = "{0} {1}".format(v.split(" ")[1], v.split(" ")[2])
      num = v.split(" ")[0]
      if num == "no": continue
      store2[name] = int(num)
    store[bag_key] = store2
  return store


def rec(key, multiplier=1):
  # print(key)
  # print(multiplier)
  bag_list = dictionarify(lines)
  if len(bag_list[key].keys()) == 0:
    return multiplier
  count = 0
  for k in bag_list[key]:
    mult = bag_list[key][k]
    out = rec(k, mult)
    print(k)
    print(mult)
    print(out)
    count += out
  return (count+1)*multiplier
  


bag_list = dictionarify(lines)

# arr = bag_list["shiny gold"].keys()
# multiply_array = []
# count = 0
# for a in arr:
count = rec("shiny gold", 1) - 1
print(count)
# print(out)

