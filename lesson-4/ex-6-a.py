import itertools

n = int(input("введите начало для итератора целых чисел,введите q для выхода"))
for i in itertools.count(n - 1, 1):
    print(i)
    if i >= 10000:
        break


