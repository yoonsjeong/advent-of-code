f = open("./txt/day6.txt", "r")
text = f.read()
lines = text.split("\n\n")

def countUnanimous(group):
  store = {}
  for member in group:
    for letter in member:
      if letter in store:
        store[letter] += 1
      else:
        store[letter] = 1
  
  count = 0
  for s in store:
    if store[s] == len(group):
      count += 1
  return count

def countQs(group):
  store = {}
  for member in group:
    for letter in member:
      if letter in store:
        continue
      else:
        store[letter] = True
  return len(store)

count = 0
for line in lines:
  group = line.split("\n")
  # count += countQs(group)
  count += countUnanimous(group)


print(count)