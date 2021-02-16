my_list_tuples = []
char_dict = ()
name_list = []
price_list = []
amount_list = []
i = 1
n = int(input("Введите кол-во товара "))
for my_dict in range(n) :
    name = input("введите название товара ")
    price = input("введите цену товара ")
    amount = input("введите количество ")
    my_dict = dict(название = name, цена = price, количество = amount)
    my_tuple = (i, my_dict)
    i += 1
    my_list_tuples.append(my_tuple)
    name_list.append(my_dict.get('название'))
    price_list.append(my_dict.get('цена'))
    amount_list.append(my_dict.get('количество'))
char_dict = dict(название = name_list, цена = price_list, количество = amount_list)
print(my_list_tuples)
print(char_dict)
