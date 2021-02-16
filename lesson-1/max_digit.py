num = int(input())
max = num % 10
while num >= 1:
    num = num // 10
    if num % 10 > max:
        max = num % 10
    if num > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break