import re


def grade(filename):
    result = 0
    with open(filename) as file:
        for line in file:
            arr = line.split("-")
            if len(arr) > 1:
                # print(arr[1], sep="")
                num = 0
                try:
                    num = float(arr[1])
                except ValueError:
                    print("Value error")
                # print("collected num = ", num)
                result += num
                # print(result)
    result = result/10.0
    with open(filename, "a") as file:
        file.write("\nTotal - " + str(result))
    return result


def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])


def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))


def parse3():
    for line in open("log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))


def parse4():
    for line in open("log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))


def parse5():
    for line in open("log.txt"):
        print(re.split("\[|\]", line)[1])


def sqsum4(nums):
    return sum(x ** 2 for x in nums if x > 0)





