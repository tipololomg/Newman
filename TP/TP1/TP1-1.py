from math import sqrt,pi
def Kepler(l1,v1):
    M = 1.9891 * 10**(30)
    G = 6.6738 * 10**(-11)
    v2 = (((2*G*M)/(v1*l1))-sqrt(((2*G*M)/(v1*l1))**2+(4*(v1**2-(2*G*M)/l1))))/2
    l2 = (l1*v1)/v2
    a = (l1+l2)/2
    b = sqrt(l1*l2)
    T = ((2*pi*a*b)/(l1*v1))/(3600*24*365.25)
    e = (l2-l1)/(l2+l1)
    return v2,l2,T

print(Kepler(1.4710*10**11,3.0287*10**4))
print(Kepler(8.7830*10**10,5.4529*10**4))
