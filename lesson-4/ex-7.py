def fact(n):
    if n == 1:
        f = 1
    else:
        a = yield from fact(n - 1)
        f = n * a
    yield f
    return f

n = int(input())
for el in fact(n):
    print(el)