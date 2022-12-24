import random
# list
first_list = [1, 2, 3, 'a', 1.2, 3,  [1, 2, 3]]
second_list = list([1, 2, 4])

print(type(first_list))
print(type(second_list))

print(len(first_list))
print(first_list[0])
print(first_list[-1])

# index()
print(first_list.index(3))

# append(elem)
first_list.append(7)
print(first_list)

# insert(index, value)
first_list.insert(0, 0)
print(first_list)

# del
del first_list[1]
print(first_list)

# pop(index)
first_list.pop(2)
print(first_list)

# remove(value)
first_list.remove(7)
print(first_list)

index_to_remove = first_list.index([1, 2, 3])
first_list[index_to_remove].remove(2)

# clear()
first_list.clear()
print(first_list)

# del list
del first_list
print(first_list)  # return error

first_list[1] = 1
print(first_list)

# list[start: end]
print(first_list[0:4])
print(first_list[:3])
print(first_list[3:])

first_list[:3] = [1, 1, 1]
print(first_list)

# extend
second_list = ['a', 'b', 'c']
first_list = [1, 2, 3, 'a', 1.2, 3,  [1, 2, 3], 'a', 'b', 'c']
for i in range(len(second_list)):
    first_list.append(second_list[i])

first_list.extend(second_list)
first_list = first_list + second_list
print(first_list)

# copy , list()
new_list = list(second_list)
print(new_list)
new_list = second_list.copy()
print(new_list)


# count(value)
print(first_list.count(1))

first_list.reverse()
# reverse()
print(first_list)

# sorted(), sort()

before_sorting_list = ['b', 'c', 'a', 'd', '1', '2']
before_sorting_list.sort()
print(before_sorting_list)


# tuple()
demo_tuple = tuple([1])
print(type(demo_tuple))
second_tuple = (1,)
print(type(second_tuple))

empty_list = []
i = 0

while i < 3:
    num = random.randint(0, 5)
    empty_list.append(num)
    i = i+1

print(empty_list)
generated_tuple = tuple(empty_list)
print(generated_tuple)
second_tuple = (2, 4, 5)
print(generated_tuple + second_tuple)


# tuple * count
a = (1, 2, 3)
b = a * 3
print(b)

# in
print(b.index(2))
print(b.count(2))


demo_string = 'hello world'
for i in demo_string:
    print(i)

# continue
for i in demo_string:
    if i == 'l':
        continue
    if i == 'd':
        break
    print(i)
print("end")

# break
for i in demo_string:
    if i == 'w':
        break
    print(i)

print("end")

# else

for i in demo_string:
    if i == 'a':
        break
    print(i)
else:
    print("exit without break")

