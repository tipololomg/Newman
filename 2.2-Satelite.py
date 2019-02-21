from math import pi
G = 6-67*10**(-11)
M = 5.97*10**(24)
R = 6371*1000
T = float(input("Período: "))
h=((G*M*T**2)/(4*pi**2))**(1/3)-R
print(int(h))
