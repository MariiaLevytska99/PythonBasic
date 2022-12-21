import sys
import math
import random

# operator is, is not

a=3
b=6
print(a is b)
print(a is not b)
a=6
print(a is b)
print(a is not b)
check_equal = a is b
print(check_equal)

# type()
a=True
print(type(a))

# max int value
print(sys.maxsize)

# + - * / ** %
a=2
b=5
print(a+b)
print(a-b)
print(a*2)
print(a/b)

print(a*a)
print(a**3)
print(a%b)

a=8
b=3
print(8 - 5 + 4 /3 * 2 ** 5)

# round()
float_value = 5.67898866
print(round(float_value, 3))

# math
print(dir(math))
print(math.sqrt(4))

# random
print(dir(random))
print(random.randint(2, 7))  # from 2 to 7, includes 7
print(random.randrange(15))  # from 0 to 14, doesn't include 15
print(random.choice(["She loves me", "She doesn't love me"]))

# concatenation
first_name = "maRiia"
print(first_name)
last_name = "levytska"
full_name = first_name + ' ' + last_name
print(full_name)

# string *
double_name = first_name*6
print(double_name)

# methods for work with string
print(full_name.title())
print(full_name.upper())
print((full_name.lower()))

# space symbols \n \t ' '
print("Python")
print("\t\tPython")
print("Python is great\n\tlanguage")
favorite_language="python"
print(favorite_language.strip())
favorite_language=favorite_language.strip()
print(favorite_language)

# methods to check data inside the string
s='123'
print(s.isalnum())

# isalpha()
s=""
print(s.isalpha())
s="a"
print(s.isalpha())

#isdecimal()
a="133"
print(a.isdecimal())
a="f123"
print(a.isdecimal())
a="1.2"
print(a.isdecimal())

# isdigit()
a=" "
print(a.isdigit())
a="133+"
print((a.isdigit()))

# islower()
s = "123"
print(s.islower())

# isspace()
s="\n\t"
print(s.isspace())

# count()
s1 = "abcdbcdebfb"
n  = s1.count('b')
print(n)


# find(), rfind()
# index =  s.find(sub,  [start, end])

s = "ab  fg cde fg"
index= s.find('fg')
print(index)
index = s.rfind('fg')
print(index)

# replace()
# s1 = s2.replace(old, new)

s1 = "1,23 3,4 7,8"
s2 = s1.replace(',', ".")
print(s2)

# in
# s1 = "abcdef"
s2 = "abc"
print(s2 in s1)

# startswith() endswith()
print(s1.startswith(s2))
print(s1.endswith('ef'))

#  split()
s1="abc_defbvg"
s2 = s1.split("_")
print(s2)
name = "Mariia"
last_name= "Levytska"
age = 23

# string formatting
print("My name is " + name + " last name " + last_name  + "age " + str(age))
print("My name is {} last name {} age {} ".format(name, last_name, age))
print(f"My name is {name} last name {last_name} age {age}")

c = name + str(age)
print(age)

# input()
print("enter your name: ")
name = input()
print(f"Your name is {name}")
name = "Mariia 2"
print(f"Your name is {name}")

