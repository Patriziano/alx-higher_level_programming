#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            result = result + (a ** b) / i
        except(ValueError, TypeError):
            result = b + a
            break
    return result