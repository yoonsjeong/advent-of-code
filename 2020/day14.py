f = open("./txt/day14.txt", "r")
text = f.read()
lines = text.split("\n")

def mask_with(mask, bits):
  n = len(mask)
  out = ""
  bits_arr = bin(bits)[2:]
  while len(bits_arr) != 36:
    bits_arr = "0" + bits_arr
  # print(len(bits_arr))
  # print(len(mask))
  for i in range(n):
    if mask[i] == "0":
      out += "0"
    elif mask[i] == "1":
      out += "1"
    else:
      out += bits_arr[i]
  return out

def masker(mask, bits):
  n = len(mask)
  out = ""
  bits_arr = bin(bits)[2:]
  while len(bits_arr) != 36:
    bits_arr = "0" + bits_arr
  # print(len(bits_arr))
  # print(len(mask))
  for i in range(n):
    if mask[i] == "0":
      out += bits_arr[i]
    elif mask[i] == "1":
      out += "1"
    elif mask[i] == "X":
      out += "X"
  print("for", bits, "out", out)
  return out

def generate(n):
  arr = [None] * n
  out = []
  def gen_bitstrings(n, arr, i):
    if i == n:
      # print(arr, n)
      out.append(arr.copy())
      return
    arr[i] = 0
    gen_bitstrings(n, arr, i+1)
    arr[i] = 1
    gen_bitstrings(n, arr, i+1)
  gen_bitstrings(n, arr, 0)
  return out

# print(generate(3))

def store_bits(store, bits, fill):
  n = bits.count("X")
  combs = generate(n)
  for c in combs:
    address = bits
    for i in c:
      address = address.replace("X", str(i), 1)
    #   print(address)
    # print(int(address, 2))
    # print("====")
    store[int(address, 2)] = fill
  return store

def dictionarify(lines, part2 = False):
  out = {}
  n = len(lines)
  i = 0
  while i < n:
    line = lines[i]
    if line.startswith("mask"):
      mask = line.split(" = ")[1]
      i += 1
      if i == n: break
      while lines[i].startswith("mem"):
        mem = int(lines[i].split("]")[0][4:])
        bits = int(lines[i].split(" = ")[1])
        if part2:
          Xstring = masker(mask, mem)
          store = store_bits(out, Xstring, bits)
        else:
          if mem in out: print("replacing...")
          out[mem] = mask_with(mask, bits)
        i += 1
        if i == n: break

  return out



def part1(lines):
  store = dictionarify(lines)
  out = 0
  for mem in store:
    out += int(store[mem],2)
  print("solution:", out)

def part2(lines):
  store = dictionarify(lines, True)
  out = 0
  for mem in store:
    out += store[mem]
  print("solution:", out)
  # print(store)
  # print(len(store))

# print(lines)
part1(lines)
part2(lines)