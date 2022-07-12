abc = [letter for letter in "abcdefghijklmnñrstuvwxyz"]

for i in range(len(abc), 0, -1):
    if i % 3 == 0:
        abc.pop(i - 1)

print(abc)