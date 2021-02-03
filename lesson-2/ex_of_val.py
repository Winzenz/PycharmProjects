n = int(input("Введите кол-во элементов списка "))
list = []
for i in range(n):
    list.append(input("Введите элемент "))
for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i - 1]
list_2 = ' '.join([str(i) for i in list])
print("Список с замененными занчиниями ",list_2)
