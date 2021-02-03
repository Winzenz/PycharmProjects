list = ['winter', 'spring', 'summer', 'autumn']
dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
mon = int(input("Введите месяц от 1 до 12 "))
if mon == 1 or mon == 12 or mon == 2:
        print("через список ",dict.get(1))
        print("через лист ",list[0])
elif mon == 3 or mon == 4 or mon == 5:
    print("через список ",dict.get(2))
    print("через лист ",list[1])
elif mon == 6 or mon == 7 or mon == 8:
    print("через список ",dict.get(3))
    print("через лист ",list[2])
elif mon == 9 or mon == 10 or mon == 11:
    print("через список ",dict.get(4))
    print("через лист ",list[3])
else:
        print("Такого месяца не существует")
