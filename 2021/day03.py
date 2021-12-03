def freq_table(lines):
    line_len = len(lines[0])
    freq_dict = {}
    for line in lines:
        for i in range(line_len):
            if i in freq_dict: freq_dict[i] += int(line[i])
            else: freq_dict[i] = int(line[i])
    return freq_dict

def get_bin(lines):
    line_len = len(lines[0])
    list_len = len(lines)
    freq_dict = freq_table(lines)

    result = ""
    for i in range(line_len):
        if freq_dict[i] > list_len//2:
            result += "1"
        else:
            result += "0"
    print(freq_dict)
    return result

def part_1(lines):
    res_1 = get_bin(lines)
    # 3875

    return res_1

def o2_iter(lines, place):
    count = 0
    # count step
    for line in lines:
        count += int(line[place])
    
    out = []
    if count > len(lines)//2: 
        search = "1"
    else: 
        search = "0"

    for line in lines:
        if line[place] == search: out.append(line)
    return out


def majority(lines, place):
    ones, zeros = 0, 0
    for line in lines:
        if "1" == line[place]: ones += 1
        else: zeros += 1
    if ones >= zeros: return "1"
    else: return "0"
def minority(lines, place):
    ones, zeros = 0, 0
    for line in lines:
        if "1" == line[place]: ones += 1
        else: zeros += 1
    if zeros <= ones: return "0"
    else: return "1"

def cull(lines, place):
    search = majority(lines, place)    
    out = []
    for line in lines:
        if line[place] == search:
            out.append(line)
    return out
def cull_co2(lines, place):
    search = minority(lines, place)    
    out = []
    for line in lines:
        if line[place] == search:
            out.append(line)
    return out

def part_2(lines):
    o2_out = lines
    co2_out = lines
    for i in range(len(lines[0])):
        o2_out = cull(o2_out, i)
        if len(o2_out) == 1: break
    for i in range(len(lines[0])):
        co2_out = cull_co2(co2_out, i)
        if len(co2_out) == 1: break
    return o2_out, co2_out
if __name__ == '__main__':
    ## INPUT STUFF
    f = open(__file__.replace(".py", ".txt"), "r")
    text = f.read()
    lines = text.split("\n")
    # lines = list(map(lambda x: int(x), lines))

    ans1 = part_1(lines)
    print(f"Part 1 answer is: {ans1}")

    ans2 = part_2(lines)
    print(f"Part 2 answer is: {ans2}")
