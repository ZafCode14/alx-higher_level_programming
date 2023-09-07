#!/usr/bin/python3
if __name__ == "__main__"
    import sys
    if len(sys.argv) == 2:
        print("1 argument:")
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
