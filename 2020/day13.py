f = open("./txt/day13.txt", "r")
text = f.read()

leave_at = int(text.split("\n")[0])
bus_ids = text.split("\n")[1].split(",")

print(leave_at)
print(bus_ids)

def part1(leave_at, bus_ids):
  min_diff = leave_at
  min_id = 0
  for i in bus_ids:
    if i == "x": continue
    else:
      diff = int(i) - (leave_at % int(i))
      if diff < min_diff:
        min_diff = diff
        min_id = int(i)
  print(min_diff)
  print(min_id)
  print("solution", min_diff*min_id)

# found this on stack overflow for mod inverses!
def mod_inv(a, m):
  return pow(a, m-2, m)
      

# takes array of tuples: (dividend, exp_remainder)
def chinese_rem_thm(arr):
  
  product = 1
  for i in arr:
    product *= i[0]
  
  out = 0
  for div, rem in arr:
    out += rem * mod_inv(product//div, div) * (product//div)
  return out % product



def part2(bus_ids):
  n = len(bus_ids)
  arr = []
  for i in range(n):
    if bus_ids[i] == "x": continue
    curr_id = int(bus_ids[i])
    arr.append((curr_id, curr_id-i))
  print(arr)
  print("soln", chinese_rem_thm(arr))
  # just realized this is the chinese remainder theorem!!!
  # glad i took discrete lol



  # timestamp = 100000000000000
  # run = True
  # while run:
  #   print("curr timestamp:", timestamp)
  #   n = len(bus_ids)
  #   for i in range(n):
  #     if bus_ids[i] == "x": continue
  #     curr_id = int(bus_ids[i])
  #     if ((timestamp+i)%curr_id) != 0:
  #       print("broke at", curr_id)
  #       timestamp += curr_id - ((timestamp+i)%curr_id)
  #       break
  #   else:
  #     run = False
  #     print("timestamp:", timestamp)
  #     break
  #   # return

      

part1(leave_at, bus_ids)
part2(bus_ids)
