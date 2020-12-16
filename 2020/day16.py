f = open("./txt/day16.txt", "r")
text = f.read()
chunks = text.split("\n\n")

# print(chunks)
validator = chunks[0].split("\n")
my_ticket = chunks[1].split("\n")[1].split(",")
my_ticket = list(map(int, my_ticket))
nearby = chunks[2].split("\n")[1:]


def rangify(rng):
  start = int(rng.split("-")[0])
  end = int(rng.split("-")[1])
  return range(start, end)

def dictionarify_ranges(validator):
  store = {}
  for v in validator:
    key = v.split(":")[0]
    rng1 = v.split(": ")[1].split(" or ")[0]
    rng2 = v.split(": ")[1].split(" or ")[1]
    val = (rangify(rng1), rangify(rng2))
    store[key] = val
  return store

def check_in_ranges(range_store, ticket):
  for i in ticket:
    for j in range_store:
      vals = range_store[j]
      if i in vals[0] or i in vals[1]:
        break
    else:
      return i
  return 0

def check_in_ranges_bool(range_store, ticket):
  for i in ticket:
    for j in range_store:
      vals = range_store[j]
      if i in vals[0] or i in vals[1]:
        break
    else:
      return False
  return True

def part1(validator, my_ticket, nearby):

  store = dictionarify_ranges(validator)
  print(my_ticket)
  error_rate = 0
  for n in nearby:
    ticket = n.split(",")
    ticket = list(map(int,ticket))
    print("ticket:", ticket)
    error_rate += check_in_ranges(store, ticket)
  print("soln", error_rate)
  # print(keys)

def get_valid_tickets(validator, my_ticket, nearby):
  store = dictionarify_ranges(validator)
  valid_tickets = []
  for n in nearby:
    ticket = n.split(",")
    ticket = list(map(int, ticket))
    if check_in_ranges_bool(store, ticket):
      valid_tickets.append(ticket)
  return valid_tickets

def group_by_index(valid_tickets):
  out = [[] for _ in valid_tickets[0]]
  for v in valid_tickets:
    for i in range(len(valid_tickets[0])):
      out[i].append(v[i])
  return out

def figure_out_range(validator, index_group):
  store = dictionarify_ranges(validator)
  out = {}
  n = len(index_group)
  for s in store:
    # if not "departure" in s: continue
    out[s] = []
    for index in range(n):
      i = index_group[index]
      candidate = True
      for each in i:
        if each in store[s][0] or each in store[s][1]:
          continue
        else:
          candidate = False
          break
      if candidate:
        out[s].append(index)
  return out

#   n = len(valid_tickets)
#   m = len(valid_tickets[0])
#   for i in range(n):
#     out = []
#     for j in range(m):
#       valid_tickets[i][j]

def counter_help(candidates):
  store = {}
  for s in candidates:
    for i in candidates[s]:
      if i in store:
        store[i] += 1
      else:
        store[i] = 1
  return store

# def list_valid_ranges(validator, index_range_single):
#   store = dictionarify_ranges(validator)
#   out = []
#   for s in store:
#     rng1 = list(store[s][0])
#     rng2 = store[s][1]
#     valid = True
#     for i in index_range_single:
#       if i in rng1 or i in rng2:
#         print("checking is", i, "in", store[s][0],"or", store[s][1])
#         continue
#       else:
#         valid = False
#         break
#     if valid:
#       out.append(s)
#   return out

def new_rangify(rng):
  start = int(rng.split("-")[0])
  end = int(rng.split("-")[1])
  return list(range(start, end+1))

def dictionarify(validator):
  store = {}
  for v in validator:
    key = v.split(":")[0]
    rng1 = v.split(": ")[1].split(" or ")[0]
    rng2 = v.split(": ")[1].split(" or ")[1]
    val = new_rangify(rng1)+ new_rangify(rng2)
    store[key] = val
  return store

def check_in_dict(store, index_group):
  for s in store:
    for index in range(len(index_group)):
      i = index_group[index]
      valid = True
      for j in range(len(i)):
        check = i[j]
        if check in store[s]:
          continue
        else:
          print("failed for", check, "on", store[s])
          valid = False
          break
      if valid:
        print("valid for", s, "on index", index)

def part2(validator, my_ticket, nearby):
  valid = get_valid_tickets(validator, my_ticket, nearby)
  out = dictionarify(validator)
  print(out)
  i_group = group_by_index(valid)
  bruh = check_in_dict(out, i_group)
  print(bruh)

    # if i == 16 or i == 5 or i == 3:
    #   continue
    # valid = list(filter(lambda x: "departure station" in x, valid))
    # if len(valid) >= 1:



  # print(out2)
  # out3 =figure_out_range(validator, out2)
  # out3["departure track"] = [] # 16
  # out3["departure station"] = [] # 5
  # out3["departure time"] = [] # 18 or 8
  # out3["departure platform"] = [] # 12 or 13 or 17
  # out3["departure location"] = [] # 3
  # out3["departure date"] = [] # 1 or 6 or 9 or 10 or 15
  # out3["wagon"] = [] # 0 or 19
  # print(out3)
  # print(counter_help(out3))
  # out3 = 
  # print(store)

# part1(validator, my_ticket, nearby)
# part2(validator, my_ticket, nearby)

x = {
  "departure location": [1, 3, 6, 9, 10, 15],
  "departure station": [5, 8, 10, 13, 15, 17, 18],
  "departure platform": [1, 3, 6, 9, 10, 12, 13, 15, 17],
  "departure track": [3, 5, 6, 8, 10, 13, 15, 16, 17],
  "departure date": [1, 6, 9, 10, 15],
  "departure time": [1, 8, 9, 10, 12, 13, 15, 17, 18],
  "arrival location": [3, 4, 5, 6, 7, 9, 10, 13, 14, 17, 18],
  "arrival station": [],
  "arrival platform": [1, 3, 6, 9, 15, 17],
  "arrival track": [12, 17],
  "class": [6, 12, 17],
  "duration": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 17, 18],
  "price": [1, 3, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18],
  "route": [6, 9],
  "row": [6, 17],
  "seat": [1, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18],
  "train": [2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18],
  "type": [3, 6, 12, 15],
  "wagon": [0, 1, 3, 5, 6, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19],
  "zone": [1, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17]
}