def my_func(var1 , var2, var3):
    if var1 >= var3 and var2 >= var3:
        return var1 + var2
    elif var1 > var2 and var1 < var3:
        return var1 + var3
    else:
        return var2 + var3

print(f"результат {my_func(int(input('Введите первый элемент ')), int(input('Введите второй элемент ')), int(input('Введите третий элемент ')))}")
