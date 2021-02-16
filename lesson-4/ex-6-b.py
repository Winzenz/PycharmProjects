import itertools

my_list = ["rfrg", 454, 56565]
i = 0
for el in itertools.cycle(my_list):
    print(el)
    i += 1
    if i >= 100:
        break