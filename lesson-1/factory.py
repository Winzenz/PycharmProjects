proceeds = int(input("Введите выручку фирмы "))
cost = int(input("Введите издержки "))
if proceeds > cost:
    rent = proceeds - cost
    print("Рентабльность ", rent)
    workers = int(input("Кол-во рабочих"))
    print("прибыль на сотрудника: ", rent / workers)
else:
    print("Фирма убыточна")
