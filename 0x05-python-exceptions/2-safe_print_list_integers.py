#!/usr/bin/python

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
    except (IndexError, TypeError):
        pass
    else:
        print()
        return count
