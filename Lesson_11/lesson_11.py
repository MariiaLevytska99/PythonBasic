# Exception ->  BaseException
# error type, program state, error description

# FileNotFoundException
# ImportError
# RunTimeError
# NameError
# TypeError


# Error -> syntax, logic


# IndentationError
# syntax error
# print("Hello world")
#     print("Hello world with error")


# if True
#     print("Raise exception")

# logic error
# a = 10
# b = 5
# print(a  + c)

# str_num = "5"
# number = int(str_num)
# print(number)
#
# str_num = "hello"
# number = int(str_num)
# print(number)

# OutofMemoryError

# RecursionError
# def recursion():
#     return recursion()
#
# recursion()


# TypeError
#
# a = 2
# b = "string"
# a+b

# ZeroDivisionError

# print(100/0)


# AssertionError
# AttributeError
# EOFError -> input()
# FloatingPointError
# GenerateExit -> close()
# ImportError
# IndexError
# KeyError -> dict
# KeyboardInterrupt
# MemoryError
# NameError
# OSError


# FileNotFoundError

# file = open("Test.txt", "r")
# if file:
#     print("File open")



# try -> except -> finally
# try:
#   statement in try block
# except:
#   executed when exception occured in try block

# a = 100
# b = 0
# try:
#     c = a/b
# except:
#     print("Can't divide by zero")


# try:
#     a = int(input("enter value a:"))
#     b = int(input("enter value b: "))
#     c = a/b
#     print(f"result {c}")
# except ValueError:
#     print("Entered wrong value")
# except ZeroDivisionError:
#     print("Can't divide by zero")

# try:
#     a = int(input("enter value a:"))
#     b = int(input("enter value b: "))
#     c = a/b
#     print(f"result {c}")
# except(ValueError, ZeroDivisionError):
#     print("Error...")


# finally
# try:
#     # block of code
# finally:
#     # this will always be executed


# try:
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     c = a/b
#     print(f"result {c}")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# finally:
#     print("Inside a finally block")


# try -> else

# try:
#     # block of code
# except:
#     # except block
# else:
#     # this code executes when exceptions not occured


# try:
#     a = int(input("enter value a:"))
#     b = int(input("enter value b: "))
#     c = a/b
#     print(f"result {c}")
# except(ValueError, ZeroDivisionError):
#     print("Error...")
# else:
#     print("This is else block")


# def do_smth():
#     return 100/0
#
#
# try:
#     do_smth()
# except ZeroDivisionError:
#     print("Can't divide by zero")
#     raise


# try:
#     file = open("error.txt")
# except FileNotFoundError as error:
#     print(error)
#     raise


# raise Exception_class, <value>


# def demo_func(amount, year, rate):
#     try:
#         if rate > 100:
#             raise ValueError(rate)
#         result = (amount * year * rate) / 100
#         return result
#     except ValueError:
#         print("Rate is out of range")
#
# print(demo_func(800, 8, 9))
# print(demo_func(800, 7, 120))


# def factorial(n):
#     if n < 0:
#         raise ValueError("factorial n can't be negative")
#     return 1 if n == 0  else  n * factorial(n-1)
#
#
# print(factorial(4))
# try:
#     print(factorial(-4))
# except ValueError as e:
#     print(e)


# class FactorialError(Exception):
#     pass
#
# def factorial(n):
#     if n < 0:
#         raise FactorialError("n can't be negative")
#     return 1 if n ==0 else n*factorial(n-1)
#
# print(factorial(8))
# try:
#     print(factorial(-8))
# except FactorialError as error:
#     print(error)


class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"{self.age} must be in range [ {self.minage} ; {self.maxage} ]"


class Person:

    min_age = 0
    max_age = 100

    def __init__(self, name, age):
        self.__name = name
        if self.min_age < age < self.max_age:
            self.__age = age
        else:
            raise PersonAgeException(age, self.min_age, self.max_age)

    def info(self):
        print(f"Name: {self.__name} age is {self.__age}")


try:
    person =Person("Maria", 23)
    person.info()

    person =Person("Maria", -4)
    person.info()

except PersonAgeException as e:
    print(e)


# raise ... from
#
# try:
#     a = int(input("enter value a:"))
#     b = int(input("enter value b: "))
#     c = a/b
#     print(f"result {c}")
# except ZeroDivisionError as error:
#     raise ValueError("Division failed") from error


# class Error(Exception):
#     """base error class"""
#     pass
#
#
# class ValueTooSmallError(Error):
#     pass
#
#
# class ValueTooLargeError(Error):
#     pass
#
#
# class Person_2:
#
#     min_age = 0
#     max_age = 100
#
#     def __init__(self, name, age):
#         self.__name = name
#         if age < self.min_age:
#             raise ValueTooSmallError
#         elif age > self.max_age:
#             raise ValueTooLargeError
#         else:
#             self.__age = age
#
#     def info(self):
#         print(f"Name: {self.__name} age is {self.__age}")
#
#
# try:
#     person =Person("Maria", 23)
#     person.info()
#
#     person =Person("Maria", -4)
#     person.info()
#
# except (ValueTooLargeError, ValueTooLargeError):
#     print("Error....")


# def sum_of_list(numbers):
#     return sum(numbers)
#
# def average(sum, n):
#     # ZeroDivisionError
#     return sum/n
#
# list = [10, 20, 30, 40]
# list_2 = []
# try:
#     print(average(sum_of_list(list), len(list)))
#
#     print(average(sum_of_list(list_2), len(list_2)))
# except:
#     print("Error")

# warn()
# module warnings -> exception


# import warnings
# print("Hello world")
#
# warnings.warn("Warning message")
#
# print("Hello world")

# warning
# UserWarning -> warn()
# DeprecationWarning - for developers
# SyntaxWarning
# RunTimeWarning
# FutureWarning - for end users
# ImportWarming
# UnicodeWarning
# BytesWarning
# ResourceWarning


# warning filters:
#   bydefault
#   error
#   ignore
#   always
#   module
#   onetime


# warn(messagem category= None, stacklevel=1, source=None)
# filterwarnings(action, message="", catefory=Warning, append=Flase, linelo=0)

# import warnings
# warnings.warn("First warning")
# warnings.filterwarnings('always', "demo message",)
#
#
# # simplefilter(action, category=Warning, linelo=0, append=False)
# warnings.simplefilter('error', SyntaxWarning)
# warnings.warn("This is a warning message")


def divide(a, b):
    return a/b

import pytest

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

dict = {1: "g", }