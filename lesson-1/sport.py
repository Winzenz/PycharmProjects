a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
res_d = 1
while a <= b:
    a = a * 0.1 + a
    res_d += 1
print("через ", res_d, "вы достигнете результата ")