# d = int(input())

# bus = d * 2
# taxi = d * 5
# electric = d * 10

# print(bus + taxi + electric)


# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1


# n = int(input())

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     while j > 1:
#         print(j - 1, end=' ')
#         j = j - 1
#     print()
    
    
    
#   *
#  ***
# *****
#  ***
#   *


n = int(input())
for i  in range(1, n + 1):
    print(" " * (n - i), "*" * (2 * i - 1))  
    print()
    
for i in range(n-1, 0, -1):
    print(" " * (n - i), "*" * (2 * i - 1))  
    print()

        
