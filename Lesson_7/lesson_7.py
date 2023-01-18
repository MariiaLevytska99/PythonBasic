# r - read
# w - write
# x -  write
# a - append
# t - open in  txt
# b - open in bin
# + read+write
# r+ - read and write
# a+ - read and append some data
# wb
# rb
# rb+
# ra+


# open(file_name, mode)

file_open = open("test.txt", "r")
print(file_open.name)
print(file_open.closed)
print(file_open.mode)
print(file_open.closed)

# read from file
# read(num_of_symbols)
result = file_open.read()
print(result)

# readline(num_of_symbols)
# readlines([])

res = file_open.readline(3)
print(res)

res = file_open.readlines()
print(res)

line_number = 3
current_line = 1
for line in file_open:
    if current_line == line_number:
        print(line)
        break
    current_line = current_line + 1


# write data
file_open.close()
file_open = open("test_2.txt", "w")
file_open.write("Create new file")
# writelines([])
name_list = ["Andrii\n", 'Illia\n', "Oleg\n"]
name_list_2 = ["Ira\n", 'Mariia\n']
file_open.writelines(name_list)
file_open.close()

file_open = open("test_2.txt", "a+")
file_open.writelines(name_list_2)


# tell()
# seek()
print(f"Cursor position {file_open.tell()}")
file_open.seek(0)
# 0 - start file
# 1 - current  file
# 2 -  end of file
for line in file_open:
    print(line)


# rename and delete from os module

from os import rename, remove
# rename(current_name, new_name)
rename("test_2.txt", "renamed_test.txt")
#
# # remove(file_name)
remove("renamed_test.txt")

# windows  Cp1252
# linusutf-8
# mac utf-8/utf-16


# file.encoding
file_open = open("test.txt", "a+", encoding="utf-16")
print(f"current encoding {file_open.encoding}")

# binary files
binary_file = open("binary_file.bin", "wb+")
message = "It's binary file"
# encode(coding)
encoded_message = message.encode("ASCII")
binary_file.write(encoded_message)
binary_file.seek(0)
read_data = binary_file.read()
print(read_data)
decoded_data = read_data.decode("ASCII")
print(decoded_data)
with open("test.txt", "w+") as file:
    file.read()
    file.write("abcd")


# directory  listing
#os.listdir()

import  os
directories = os.listdir("../Lesson_7")
print(directories)

#os.scandir()
dorectories = os.scandir('../Lesson_7')
print(directories)

# pathlib
from pathlib import Path
directories = Path('../Lesson_7')
for dir in directories.iterdir():
    print(dir.name)
