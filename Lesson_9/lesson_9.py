def division(a, b):
    return a/b

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

# arg_from = (input("Write your range from: "))
# arg_to = int(input("Write your range to: "))
#
# if arg_from == "":
#     arg_from = arg_from = (input("Write your range from: "))
# arg_to = int(input("Write your range to: "))
#
# if arg_from == "":
#     arg_from = 0
# number = int(input(f"Write number  from {arg_from} to {arg_to}: "))
# print(range_n(arg_from, arg_to, number))
# number = int(input(f"Write number  from {arg_from} to {arg_to}: "))
# print(range_n(arg_from, arg_to, number))

def range_n(arg_from: int, arg_to: int, number: int) -> bool:
    if  number > arg_from and number < arg_to :
        return True
    else:
        return False





