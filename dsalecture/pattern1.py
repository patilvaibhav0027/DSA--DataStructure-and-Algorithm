# 1 2 3 4 5
# 1 2 3 
# 1 2 3
# 1 2
# 1


n=5
for i in range(n, 0, -1): 
    for j in range(i, 0, -1):
        print(j, end =" ")
    print( )