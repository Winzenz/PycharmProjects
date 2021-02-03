str1 = input("введите строку ")
list = []
num = 1
for el in range(str1.count(' ') + 1):
    list = str1.split()
    if len(str(list)) <= 10:
        print(f" {num} {list [el]}")
        num += 1
    else:
        print(f" {num} {list [el] [0:10]}")
        num += 1
