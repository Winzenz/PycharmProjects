print("программа выводит тип элемента в списке")
list = [2, 'text', 456, 45.3, None]
print("список такой: ", list)
b=1;
for el in list:
    a = [b, 'Элемент', type(el)]
    b+=1
    print(a)
