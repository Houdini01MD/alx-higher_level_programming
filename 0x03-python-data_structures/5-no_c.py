#!/usr/bin/python3

def no_c(my_string):
    str = ""
    for char in range(len(my_string)):
        if char != 'C' and 'c':
            str += char
    return str
