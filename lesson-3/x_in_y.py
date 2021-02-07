"""
лёгкий метод возведения в степень:

def my_func(x, y):
   return x**y
x = int(input("Введите основание "))
y = int(input("Введиет степень "))
print(my_func(x, y))
"""

#способ через цикл
x = int(input("Введите основание "))
y = int(input("Введите степень "))
def my_func(x, y):
    if y == 0:
        mult = 1
    else:
        i = 1
        mult = 1
        while i <= y:
            mult = mult * x
            i += 1
    return mult
print(my_func(x, y))

