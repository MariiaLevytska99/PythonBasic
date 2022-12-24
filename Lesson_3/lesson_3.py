import math

print(int(true_bool))
print(int(false_bool))

print(bool(""))
print(bool("abc"))

a = 8
b = 8

print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

print("Enter number: ")
n = input()

if n > 0:
    print(" n is positive")
elif n == 0:
    print("n is null")
else:
    print("n is negative")

if n % 2 == 0:
    print("парне")
else:
    print(" непарне")

if abs(n) < 10:
    print("однозначне")
elif abs(n) >= 10 and abs(n) < 100:
    print("двозначне")
else:
    print("багатозначне")

if len(str(n)) == 1:
    print("однозначне")
else:
    print("двозначне")
