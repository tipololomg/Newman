import math
a1=15.67 #a1
a2=17.23 #a2
a3=0.75 #a3
a4=93.2 #a4
maior = 0
amaior = 0
for Z in range(1,101):
    for A in range(Z,3*Z+1):
        if A%2==1:
                a5=0
        elif A%2==0 and Z%2==0:
                a5=12
        elif A%2==0 and Z%2==1:
                a5=-12
        B = (a1*A-a2*(A**(2/3))-a3*((Z**2)/(A**(1/3)))-a4*((A-2*Z)**2/A)+a5/math.sqrt(A))
        C = B/A
        if C > maior:
            maior = C
            amaior = Z
            j = A
print(amaior,j)
