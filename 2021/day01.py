def count_inc(lines):
    cache = float('inf')
    count = 0
    for curr in lines:
        if curr > cache:
            count += 1
        cache = curr
    return count

def group_threes(lines):
    group = []
    for i in range(len(lines) - 2):
        group.append(lines[i] + lines[i+1] + lines[i+2])
    return group



if __name__ == '__main__':
    ## INPUT STUFF
    f = open(__file__.replace(".py", ".txt"), "r")
    text = f.read()
    lines = text.split("\n")
    lines = list(map(lambda x: int(x), lines))

    ans1 = count_inc(lines)
    print(f"Part 1 answer is: {ans1}")

    ans2 = count_inc(group_threes(lines))
    print(f"Part 2 answer is: {ans2}")
