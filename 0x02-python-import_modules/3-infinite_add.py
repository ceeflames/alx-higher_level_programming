#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    n = len(argv) - 1

    add = 0
    if n == 0:
        print(add)
    else:
        for i in range(n):
            add += int(argv[i + 1])
        print("{}".format(add))
