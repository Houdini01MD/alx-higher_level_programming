#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0
            resutlt = 0
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("division by 0")
            except (ValueError, TypeError):
                print("wrong type")
            finally:
                new_list.append(result)
    except IndexError:
        print("out of range")
    finally:
        return new_list
