#!/bin/python3

from sys import argv

if __name__ == "__main__":
    """print number and value of argument"""

num_arg = len(argv) - 1

if num_arg == 1:
    print("1 argument:")

elif num_arg == 0:
    print("0 arguments.")

else:
    print("{} argument:".format(num_arg))

for i, arg in enumerate(argv[1:], start=1):
    print("{}: {}".format(i, arg))
