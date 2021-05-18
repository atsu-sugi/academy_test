decimal = int(input('10進数:'))
L = []
while decimal != 0:
    L.insert(0,decimal % 2)
    decimal //= 2
for i in L:
    print(i,end="")