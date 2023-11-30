#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""

from sys import argv

num_arg = len(argv) - 1
if num_arg == 0:
    print("0 arguments.")
elif num_arg == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_arg))
for i in range(num_arg):
    print("{}: {}".format(i + 1, argv[i + 1]))
