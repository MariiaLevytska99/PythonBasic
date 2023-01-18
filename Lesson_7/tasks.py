pos1 = 1
pos2 = 3

if pos2 <= pos1:
    exit()
f = open("test_2.txt", "r+")
lines = f.readlines()
s = lines[pos1]
lines[pos1] = lines[pos2]
lines[pos2] = s
f.seek(0)

for el in lines:
    f.write(el)

f.close()
