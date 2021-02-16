def my_func(**kwargs):
    return kwargs
my_dict = my_func(name = input("Введите имя "), surname = input("Введите фамилию "), year = input("Введите год "))
print(f"name: {my_dict.get('name')}, surname: {my_dict.get('surname')}, year: {my_dict.get('year')}")
