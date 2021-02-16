from random import randint

new_list = []
n = int(input("введите кол-во элeментов списка "))

my_list = [randint(0, 500) for el in range(n)]

new_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i]]

print("Ваш список ",my_list)
print("Отсортированный список ", new_list)
