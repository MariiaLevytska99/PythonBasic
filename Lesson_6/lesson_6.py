# set - mutable
# frozenset - unmutable

# create set {}
first_set = set([1, 2, 3])
print(type(first_set))
second_set = {1, 2, 3}
print(type(second_set))

fr_set = frozenset([1, 2, 3])

first_set = set([1, 3, 4, 7])
second_set = {1, 2, 3, 4, 8, 9, 10}
print(first_set)

# len()
print(len(first_set))
print((len({})))

# s1.isdisjoint(s2)
print(first_set.isdisjoint(second_set))

# s1.issubset(s2)
print(first_set.issubset(second_set))

# s1.isuperset(s2)
print(first_set.issuperset(second_set))

#  in, not in
print(1 in first_set)
print(9 not in first_set)

# s.union(s1, s2....) -> s  | s1 | s2 | ....
third_set = first_set.union(second_set)
print(third_set)

# s.intersection(s1, s2, s3....) -> s  & s1 & s2 ...
print(first_set.intersection(second_set))

# s.difference(s1,  s2,  s3....) -> s - s1 - s2 - ....
print(first_set.difference(second_set))
print(second_set.difference(first_set))

# s.symetric_difference(s2) -> s ^ s2
print(first_set.symmetric_difference(second_set))

# methods only for SET
# s.update(s1, s2, ...) -> |=
first_set.update(second_set)
print(first_set)

# s.intersection_update(s1, s2 ....) -> &=
first_set.intersection_update(second_set)
print(first_set)

# s.difference_update(s1, s2, s3....) -> -=
first_set.difference_update(second_set)
print(first_set)


# s.add(element)
first_set.add(11)
first_set.add(12)
first_set.add(13)
first_set.add(14)
print(first_set)

# s.remove(element)
first_set.remove(13)
print(first_set)

# s.pop()
first_set.pop()
print(first_set)

# s.clear()
first_set.clear()
print(first_set)


def unique_numbers(list_1, list_2):
    list_1_to_set = set(list_1)
    list_2_to_set = set(list_2)
    print(list_1_to_set)
    print(list_2_to_set)
    print(len(list_1_to_set))
    print(len(list_2_to_set))


unique_numbers([1, 2, 3, 7, 8, 1, 2, 3], [1, 1, 1, 1, 1])


# isuperset() -> > >=
# set1 >= set2

set_1 = {1, 2, 3}
set_2 = {1, 3, 7, 8, 9}
print(set_1 >= set_2)

# issubset() < <=

print(set_1 <= set_2)

# == !=

# s1.copy()
s3 = set_1.copy()
print(s3)



# dictionaries
# {key: value}
# dict() {}
dict_1 = {}
dict_2 = dict()
print(type(dict_1))
print(type(dict_2))


dict_1 = {
    1: [2, 4, 6],
    2: {1: "a", 2: "b"},
    3: "Wednesday"
}
print(dict_1)

# [key]
print(dict_1[2])

dict_2 = dict(Mon=1, tue=2)

# zip()
days = [1, 2, 3]
days_name = ['m', 't', 'w']

dict_days = dict(zip(days, days_name))
print(dict_days)


# add new element
dict_1 = {
    1: [2, 4, 6],
    2: {1: "a", 2: "b"},
    3: "Wednesday",
    4: 'abc'
}

dict_1[5] = 'new value'
print(dict_1)

dict_1[5] = "another one"
print(dict_1)


# del

del dict_1[5]
print(dict_1)

# dict.items()
for key, value in dict_1.items():
    print(key)
    print(value)

# dict.keys()
for key in dict_1.keys():
    print(key)

print(dict_1.values())

lang_dict = {
    'p': 'Python',
    'j': 'Java',
    'c': 'c#',
    'p_': 'pascal'
}

for lang in sorted(lang_dict.values()):
    print(lang)

# in, not in
print('a' in lang_dict)
# clear()
# lang_dict.clear()
# print(lang_dict)
# copy()
# copy_dict = lang_dict.copy()
# get()
# print(copy_dict.get('c'))
# items()
# keys()
# values()
# pop()
# popitem()
print(lang_dict.popitem())
# update()



def movies_info():
    movies = {
        'movie 1': 2019,
        'movie 2': 2014,
        'movie 4': 2007,
        'movie 3': 2022

    }
    print(dict(sorted(movies.items())))
    print(dict(sorted(movies.items(), key=lambda item: item[1])))


movies_info()

# {n: n*2}

def generate_dict(n):
    generated_dict = {x: x*x for x in range(1, n)}
    print(generated_dict)

generate_dict(3)
