n = int(input("Enter the length of the sequence: ")) # Do not change this line
c = 4
x = 1

xx = 1 
yy = 2
zz = 3
print(xx,yy,zz, end=' ')

while c <= n:
    sum = xx + yy + zz
    print(sum, end = ' ')
    xx = yy
    yy = zz
    zz = sum
    
    c += 1

    