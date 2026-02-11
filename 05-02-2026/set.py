a = (1, 2, 3, 4, 5, 6)
b = (True, False)
z = (1.0, 2.0, 3.0, 4.0)

c = set(a).union(set(b))
print(c)

d = set(b).union(set(a))
print(d)

d.update(z)
print(d)