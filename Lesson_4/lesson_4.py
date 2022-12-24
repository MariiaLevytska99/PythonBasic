# lesson 4 Functions
from lesson_4_make_user_profile import (
    make_user_profile as user_profile,
    func_1 as f1,
    func_2 as f2
)
import lesson_4_make_user_profile as lesson_4_alias

class Person:
    age: int
    first_name: str
    last_name: str


def add_tree_numbers(a: int, b: int, c: int):
    """
    add two numbers
    a - int
    b - int
    """
    a = 4
    b = 5
    c = 6
    return a + b + c, a + b, a


result_1, result_2, result_3 = add_tree_numbers(b=2, a=4, c=5)
print(result_1)
print(result_2)
print(result_3)


def make_pizza(size, *topings):
    print(topings)



make_pizza('s', 'tomato', 'cheese')
make_pizza('tomato', 'cheese', 'mushrooms')


def make_user_profile(first_name, last_name, **user_info):
    print("another function")


user_profile(first_name="Mariia", last_name="Levytska", age="23")

lesson_4_alias.make_user_profile()

# lambda functions
# lambda argument(s) : expression

def func(x):
    return x*2

result = func(3)
print(result)

# list [elem1, elem2, elem3]
list_1 = [1, 2, 3, 4]
res = (lambda x: x**2)(for x in list_1)
print(res)

f = lambda x: x**2
res = [f(x) for x in list_1]
print(res)