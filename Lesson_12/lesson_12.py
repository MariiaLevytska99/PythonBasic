# iterators
# iter()- get iter from object
# next() - get next element

list_1 = ["a", "b", "c"]

# get object iterator
iterator_list = iter(list_1)
print(iterator_list)

# get current and go to next

current_element = next(iterator_list)
print(current_element)

next_element = next(iterator_list)
print(next_element)

while True:
    try:
        item = next(iterator_list)
        print(item)
    except StopIteration:
        break

file = open("test_iterator.txt", "r")

# get iterator

file_iterator = iter(file)

while True:
    try:
        line = next(file_iterator)
        print(line)
    except StopIteration:
        break



# __next__()

list_2 = ["a", "b", "c", "d"]

# get iterator
list_2_iterator = iter(list_2)

current_value = list_2_iterator.__next__()
print(current_value)

next_value = list_2_iterator.__next__()
print(next_value)

next_value = list_2_iterator.__next__()
print(next_value)

next_value = list_2_iterator.__next__()
print(next_value)

next_value = list_2_iterator.__next__()
print(next_value)


# manual and automatic iterations

# automatic - for - iter(), next()
# manual - while - try -> except


list_3 = [1, 2, 3, 4, 5]

# automatic

for el in list_3:
    print(el)

# manual

list_3_iterator = iter(list_3)
while True:
    try:
        el = next(list_3_iterator)
        print(el)
    except StopIteration:
        break


# custom infinity iterator

class InfinitiveIterator:

    def __init__(self):
        self._int = 0

    def __next__(self):
        self._int += 1
        return self._int

    def __iter__(self):
        return InfinitiveIterator()


int_iterator = InfinitiveIterator()
print(next(int_iterator))
print(next(int_iterator))
print(next(int_iterator))


infinitive_iterator = InfinitiveIterator()

for x in infinitive_iterator:
    print(x)


class HundredIter:

    def __init__(self):
        self._int = 0

    def __next__(self):
        if self._int > 99:
            raise StopIteration

        self._int += 1
        return self._int

    def __iter__(self):
        return HundredIteratorator():

hundred_iterator = HundredIterator()

for x in hundred_iterator:
    print(x)

class HundredWithoutIterIterator:

    def __init__(self):
        self._int = 0

    def __next__(self):
        if self._int > 99:
            raise StopIteration

        self._int += 1
        return self._int

without_iter = HundredWithoutIterIterator()

for x in without_iter:
    print(x)

print(2 ^ 4)

str = "Hello world"
str_iterator = iter(str)
print(next(str_iterator))
print(next(str_iterator))


def is_iterable(object) -> bool:
    try:
        iter(object)
        return True
    except TypeError:
        return False


list_4 = [1, [4, 5], "abc", (1, 2), {"a": 1}]

for el in list_4:
    is_iter = is_iterable(el)
    print(f"{el} is iterable: {is_iter}")


class Letters:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return LetterIterator(self.string[:])


class LetterIterator:
    def __init__(self, string):
        self.string = string
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.string == []:
            raise StopIteration
        tmp = self.string[self.n]
        self.n +=1
        return tmp


letter = Letters("demo string")
print(letter.string)
for el in letter:
    print(el)