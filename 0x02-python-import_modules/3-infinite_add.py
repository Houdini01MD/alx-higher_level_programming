#!/usr/bin/python3


if __name__ == "__main__":
    """prints the result of the addition of all arguments"""

from sys import argv

num_arg = [int(arg) for arg in argv[1:]]
add_arg = 0

for i in num_arg:
    add_arg = add_arg + i

print(add_arg)
