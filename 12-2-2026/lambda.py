# fun = lambda : print("Hello World")
# fun()

# fun0 = lambda x, y : x + y
# print(fun0(10, 20))

# fun2 = lambda x,y : x if x > y else y
# print(fun2(5, 3))


# pattern = lambda n : list(map(lambda i: print("*" * i), range(1, n+1)))
# pattern(5)

# pattern = lambda n : list(map(lambda i : print("*" * i), range(n, 0, -1)))
# pattern(5)


# pattern1 = lambda n : list(map(lambda i : print("*" * i), range(0, n)))
# pattern1(5)
# pattern2 = lambda n : list(map(lambda i : print("*" * i), range(n, 0, -1)))
# pattern2(5)



pattern = lambda n: [print("*" * i) for i in list(range(0,n+1)) + list(range(n +1,0,-1))]
pattern(5)


# pattern = lambda n, a=65: list(map(lambda i:print(char(a), end=" "), ))












