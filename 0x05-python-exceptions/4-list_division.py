#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                set_1 = my_list_1[i]
                set_2 = my_list_2[i]
                result = 0

                if not isinstance(set_1, (int, float)):
                    print("wrong type")
                if not isinstance(set_2, (int, float)):
                    print("wrong type")
                elif set_2 == 0:
                    print("division by 0")
                else:
                    result = set_1 / set_2

                result_list.append(result)
            except IndexError:
                print("out of range")
    except ZeroDivisionError:
        pass
    finally:
        return result_list
