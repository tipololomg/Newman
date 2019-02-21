from math import sqrt
h=float(input("Altura da Torre: "))
g= 9.806659
t = sqrt(2*h/g)
print("A bola demora",round(t,2),"segundos a atingir o chão.")