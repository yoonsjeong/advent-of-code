f = open("./txt/day18.txt", "r")
text = f.read()
lines = text.split("\n")
# print(lines)

def eval(line, val, op):
  # print("my line:", line)
  # print("my val:", val)
  if len(line) == 0:
    return val
  
  char = line[0]
  
  if char == " ":
    return eval(line[1:], val, op)
  if char in "123456789":
    if op == None:
      return eval(line[1:], int(char), None)
    elif op == "*":
      return eval(line[1:], val*int(char), None)
    elif op == "+":
      return eval(line[1:], val+int(char), None)
  if char in "*+":
    return eval(line[1:], val, char)
  
  # parens case
  if char == "(":
    n = len(line)
    count = 0
    for i in range(n):
      if line[i] == "(":
        count += 1
      if line[i] == ")":
        count -= 1
      if count == 0:
        break
    value = eval(line[1:i], 0, None)
    if op == None:
      return eval(line[i+1:], value, None)
    if op == "*":
      return eval(line[i+1:], val * value, None)
    if op == "+":
      return eval(line[i+1:], val + value, None)
  if char == ")":
    print("printin value:", val)
    return val
  #   for i in range(n):
  #     if line[i] == ")":
  #       break
  #   return eval(line[i+1], val + eval(line[1:i+1], []))
  # if char == ")":
  #   return val


# out = eval("2 + 3 * 5 + (5 + 5)", None, None)
# print(out)
def part_one():
  global lines
  count = 0
  for line in lines:
    # print(eval(line, None, None))
    count += eval(line, None, None)
  print("final count:", count)
  return count


def add_parens(line, acc):
  if len(line) == 0:
    return acc
  char = line[0]
  if char == " ":
    return add_parens(line[1:], acc)
  

def conv_rpn(line, out, ops):
  if len(line) == 0:
    while len(ops) != 0:
      out += ops.pop()
    return out


  i = line[0]
  if i == " ":
    return conv_rpn(line[1:], out, ops)
  if i in "123456789":
    return conv_rpn(line[1:], out + [i], ops)
  if i == "*":
    if len(ops) == 0 or ops[-1] == "(":
      return conv_rpn(line[1:], out, ops + ["*"])
    else:
      new_out = out
      while len(ops) != 0 and ops[-1] != "(":
        new_out += [ops.pop()]
      return conv_rpn(line[1:], new_out, ops + ["*"])
  if i == "+":
    return conv_rpn(line[1:], out, ops + ["+"])
  if i == "(":
    return conv_rpn(line[1:], out, ops + ["("])
  if i == ")":
    new_out = out
    while ops[-1] != "(":
      new_out += [ops.pop()]
    ops.pop()
    return conv_rpn(line[1:], new_out, ops)




def calc_rpn(rpn):
  stack = []
  for i in rpn:
    if i in "123456789":
      stack.append(int(i))
    if i == "*":
      val1 = stack.pop()
      val2 = stack.pop()
      stack.append(val1 * val2)
    if i == "+":
      val1 = stack.pop()
      val2 = stack.pop()
      stack.append(val1 + val2)
  return stack[0]

# out = conv_rpn("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", [], [])
# print(out)
# out2 = calc_rpn(out)
# print(out2)
# import regex as re
def part_two():
  global lines
  count = 0
  for line in lines:
    # print(eval(line, None, None))
    converted = conv_rpn(line, [], [])
    ans = calc_rpn(converted)
    print("line:", line)
    print("converted:", converted)
    print("ans:", ans)
    count += ans
    print("count:", count)

  return count

#     # print(blah)
#   # print("final count:", count)
#   # return count
count = part_two()
print("final count", count)