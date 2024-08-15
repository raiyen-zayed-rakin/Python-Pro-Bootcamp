# *args -- arguments - unlimited positional arguments
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#
#     return sum


# print(add(1, 2, 3, 4, 54, 5))

# **kwargs -- key word arguments - basically a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)
