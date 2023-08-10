#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

add_value = add(a, b)
substract_value = sub(a, b)
multiply_value = mul(a, b)
divide_value = div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, add_value))
print("{:d} - {:d} = {:d}".format(a, b, substract_value))
print("{:d} * {:d} = {:d}".format(a, b, multiply_value))
print("{:d} / {:d} = {:d}".format(a, b, divide_value))
