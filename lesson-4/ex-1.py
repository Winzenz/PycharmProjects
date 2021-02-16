from sys import argv

name, s, v, p = argv

v = int(v)
s = int(s)
p = int(p)
f = v * s + p
print("(выработка в часах * ставка в час) + премия равно ", f)
