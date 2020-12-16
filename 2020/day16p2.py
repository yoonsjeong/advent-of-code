f = open("./txt/day16.txt", "r")
text = f.read()
chunks = text.split("\n\n")

validator = chunks[0].split("\n")
out = {}
for v in validator:
  key = v.split(": ")[0]
  rng1 = v.split(": ")[1].split(" or ")[0]
  rng2 = v.split(": ")[1].split(" or ")[1]
  range1 = list(range(int(rng1.split("-")[0]), int(rng1.split("-")[1])+1))
  range2 = list(range(int(rng2.split("-")[0]), int(rng2.split("-")[1])+1))
  out[key] = range1+range2
validator = out

my_ticket = chunks[1].split("\n")[1].split(",")
my_ticket = list(map(int, my_ticket))
nearby = chunks[2].split("\n")[1:]
nearby = list(map(lambda x: list(map(int,x.split(","))),nearby))

def valid_ticket(validator, ticket):
  for t in ticket:
    for v in validator:
      if t in validator[v]:
        break
    else:
      # print("failed at", t, "for ", validator[v])
      return False
  else:
    return True
    
    
  # filter(lambda x: for v in validator: ,ticket)

nearby = list(filter(lambda x: valid_ticket(validator, x), nearby))
def group_by_index(valid_tickets):
  out = [[] for _ in valid_tickets[0]]
  for v in valid_tickets:
    for i in range(len(valid_tickets[0])):
      out[i].append(v[i])
  return out

nearby.append(my_ticket)
nearby = group_by_index(nearby)

out = {}
for i in range(len(nearby)):
  n = nearby[i]
  valid_for = []
  for v in validator:
    leave = False
    for ticket in n:
      if not ticket in validator[v]:
        leave = True
    if leave:
      continue
    else:
      if v in out:
        out[v].append(i)
      else:
        out[v] = [i]

def remove_from_arr(arr, el):
  if el in arr:
    arr.remove(el)
  return arr

for o in out:
  out[o] = remove_from_arr(out[o], 10) # departure date
  out[o] = remove_from_arr(out[o], 13) # departure platform
  out[o] = remove_from_arr(out[o], 8) # departure location
  out[o] = remove_from_arr(out[o], 18) # departure time
  out[o] = remove_from_arr(out[o], 5) # departure station
  out[o] = remove_from_arr(out[o], 16) # departure track

  out[o] = remove_from_arr(out[o], 1) # arrival platform
  out[o] = remove_from_arr(out[o], 15)
  out[o] = remove_from_arr(out[o], 3)
  out[o] = remove_from_arr(out[o], 6)
  out[o] = remove_from_arr(out[o], 9)
  out[o] = remove_from_arr(out[o], 12)
  out[o] = remove_from_arr(out[o], 17)
print(out)
print(
  my_ticket[10] *
  my_ticket[13] *
  my_ticket[8] *
  my_ticket[18] *
  my_ticket[5] *
  my_ticket[16]
)
# print(validator)
# print(group_by_index(nearby))