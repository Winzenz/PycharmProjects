def my_sum():
    res = 0
    sum_res = 0
    exit = False
    while exit == False:
        num = input("Вводите числа через пробел, как надоест жмакайте ex ").split()
        for el in range(len(num)):
            if num[el] == "ex":
                exit = True
                break
            else:
                res = res + int(num[el])
        sum_res = res
        print("промежуточная сумма равна ", res)
    print("Конечкая сумма равна ", sum_res)
my_sum()

