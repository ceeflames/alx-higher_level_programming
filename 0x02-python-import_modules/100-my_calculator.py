#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1, sys
    
    argv = sys.argv
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ["*", "+", "-", "/"]
    a = argv[1]
    b = argv[2]
    c = argv[3]

    if b not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == "+":
            print("{} {} {} = {}".format(a, b, c, calculator_1.add(int(a), int(c))))
        if argv[2] == "-":
            print("{} {} {} = {}".format(a, b, c, calculator_1.sub(int(a), int(c))))
        if argv[2] == "*":
            print("{} {} {} = {}".format(a, b, c, calculator_1.mul(int(a), int(c))))
