from math import sqrt
M = 0
L = int(input('L: '))
for x in range(-L,L+1):
    for y in range(-L,L+1):
        for z in range(-L,L+1):
            if x==0 and y==0 and z==0:
                True
            else:
                if (x+y+z)%2 == 0:
                    M -= 1/sqrt(x**2+y**2+z**2)
                else:
                    M += 1/sqrt(x**2+y**2+z**2)        
print(M)