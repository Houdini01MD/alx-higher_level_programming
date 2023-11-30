#!/usr/bin/python3

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

for i in range(num_arg):
    print("{}: {}".format(i + 1, argv[i + 1]))
