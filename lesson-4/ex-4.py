from random import randint

my_list = [randint(0, 10) for el in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print("исходный список ", my_list)
print("отсортированный список ", new_list)
