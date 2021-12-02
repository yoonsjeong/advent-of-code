def calculate_pos(lines):
    depth = 0
    hpos = 0

    for cmd in lines:
        act, num = cmd.split(" ")
        num = int(num)
        if act == "forward":
            hpos += num
        elif act == "down":
            depth += num
        elif act == "up":
            depth -= num
        else:
            print(f"Unknown command {act} {num}")
    return depth*hpos


def calculate_pos2(lines):
    depth = 0
    hpos = 0
    aim = 0

    for cmd in lines:
        act, num = cmd.split(" ")
        num = int(num)
        if act == "forward":
            hpos += num
            depth += aim*num
        elif act == "down":
            aim += num
        elif act == "up":
            aim -= num
        else:
            print(f"Unknown command {act} {num}")
    return depth*hpos

if __name__ == '__main__':
    ## INPUT STUFF
    f = open(__file__.replace(".py", ".txt"), "r")
    text = f.read()
    lines = text.split("\n")
    # lines = list(map(lambda x: int(x), lines))

    ans1 = calculate_pos(lines)
    print(f"Part 1 answer is: {ans1}")

    ans2 = calculate_pos2(lines)
    print(f"Part 2 answer is: {ans2}")
