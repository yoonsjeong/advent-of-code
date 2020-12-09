f = open("./txt/day9.txt", "r")
text = f.read()
code = text.split("\n")
PRE_LEN = 25
preamble = code[:5]
cipher = code[5:]
print(preamble)



def part1(init_code):
  global PRE_LEN
  code = init_code.copy()
  while len(code) != PRE_LEN:
    preamble = code[:PRE_LEN]
    cipher = code[PRE_LEN:]

    found = False
    for i in preamble:
      if str(int(cipher[0]) - int(i)) in preamble:
        found = True
      else:
        continue
    if not found:
      print("Not found!")
      print(cipher[0])
      return
    code = code[1:]
      
def part2(init_code):
  code = list(map(int, init_code))
  global PRE_LEN
  target = 105950735
  for i in range(564):
    for j in range(i, 564):
      if sum(code[i:j]) == target:
        print(code[i])
        print(code[j])
        return
# out = part1(code)
out = part2(code)
# print(out)
