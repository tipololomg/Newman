from vpython import sphere,vector,rate,color
from math import sin,cos,pi,sqrt
from numpy import arange,array,empty,linspace

# Raios dos Planetas

raio_mercurio = 2440
raio_venus = 6052
raio_terra = 6371
raio_marte = 3386
raio_jupiter = 69173
raio_saturno = 57316
raio_sol = 695500

raios = array([2440,6052,6371,3386,69173,57316],float)

# Orbitas dos Planetas

orbita_mercurio = 57.9
orbita_venus = 108.2
orbita_terra = 149.6
orbita_marte = 227.9
orbita_jupiter = 778.5
orbita_saturno = 1433.4

orbitas = 20 * (150 + array([57.9,108.2,149.6,227.9,778.5,1433.4],float))

#Períodos de Orbita

Torbita_mercurio = 88.0
Torbita_venus = 224.7
Torbita_terra = 365.3
Torbita_marte = 687.0
Torbita_jupiter = 4331.6
Torbita_saturno = 10759.2

Periodos = array([88.0*2,224.7,365.3,687.0,4331.6/10,10759.2/10],float) #jupiter e saturno com velocidade 10x maior q a original
#Mercurio com metade da velocidade original

# Criar o Sol 
Sol = sphere(radius = raio_sol/raio_mercurio/5,color=color.yellow)

# Cores dos Planetas

Cores = array([color.red,color.orange,color.blue,color.red,color.white,color.cyan],color)

# Criar Planetas

Planetas = empty(6,sphere)
for i in range(len(raios)):
    Planetas[i] = sphere(pos=vector(orbitas[i]/orbita_mercurio,0,0),radius = raios[i]/raio_mercurio,color=Cores[i],make_trail=True)

# Transladar Planetas
for t in arange(0,100,0.01):   
        for j in range(6):
                rate(90)
                x = (orbitas[j]/orbita_mercurio) * cos(100*t*2*pi/Periodos[j])
                y = (orbitas[j]/orbita_mercurio) * sin(100*t*2*pi/Periodos[j])
                Planetas[j].pos=vector(x,y,0)