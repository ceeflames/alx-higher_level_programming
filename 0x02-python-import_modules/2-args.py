#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("{} argument:".format(n))
        print("{}: {}".format(n, argv[n]))
    elif n > 1:
        print("{} arguments:".format(n))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
