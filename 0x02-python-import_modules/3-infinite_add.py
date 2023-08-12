#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    n = len(argv) - 1

    sum = 0
    if n == 0:
        print(sum)
    for i in range(n):
        sum += int(argv[i + 1])
    print("{}".format(sum))
