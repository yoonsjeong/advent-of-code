def sumTo2(arr, to=2020):
    n = len(arr)
    store = {}
    for i in range(n):
        num = arr[i]
        store[to-num] = i

    for num in arr:
        if num in store:
            print("The numbers are {} and {}.".format(num, to-num))
            return num * (to - num)
    raise Exception("Given array did not contain a solution.")


def sumTo3(arr, to=2020):
    n = len(arr)
    store = {}
    for i in range(n):
        num1 = arr[i]
        for j in range(i, n):
            num2 = arr[j]
            store[to - num1 - num2] = (i, j)

    for num3 in arr:
        if num3 in store:
            tup = store[num3]
            num1 = arr[tup[0]]
            num2 = arr[tup[1]]
            print("The numbers are {}, {}, and {}.".format(num1, num2, num3))
            return num1 * num2 * num3
    raise Exception("Given array did not contain a solution.")


f = open("./txt/day1.txt", "r")
text = f.read()
arr = text.split("\n")
arr = [int(el) for el in arr]
f.close()
# out = sumTo2(arr)
out = sumTo2(arr)
print("Part 1")
print("The product is {}.".format(out))
out = sumTo3(arr)
print("Part 2")
print("The product is {}.".format(out))
