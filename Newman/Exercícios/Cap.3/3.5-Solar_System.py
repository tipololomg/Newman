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

Periodos = array([88.0,224.7,365.3,687.0,4331.6,10759.2],float)

# Criar o Sol
Sol = sphere(radius = raio_sol/raio_mercurio/5,color=color.yellow)

# Criar Planetas

Planetas = empty(6,sphere)
for i in range(len(raios)):
    Planetas[i] = sphere(pos=vector(orbitas[i]/orbita_mercurio,0,0),radius = raios[i]/raio_mercurio)

# Transladar Planetas
for j in range(6):
    for theta in linspace(0,50*pi,int(50/(Periodos[j]))):    
        rate(40)
        x = (orbitas[j]/orbita_mercurio) * cos(theta)
        y = (orbitas[j]/orbita_mercurio) * sin(theta)
        Planetas[j].pos=vector(x,y,0)







# Transladar Planetas

#for theta in arange(0,50*pi,0.1):
#    range(30)
#    xmercurio = cos(theta)
#    ymercurio = sin(theta)
#    mercurio.pos = vector(xmercurio,ymercurio,0)

#for theta in arange(0,50*pi,0.1):
#    range(int(30/(Torbita_venus/Torbita_mercurio)))
#    xvenus = 20 * ((150 + orbita_venus)/orbita_mercurio) * cos(theta)
#    yvenus = 20 * ((150 + orbita_venus)/orbita_mercurio) * sin(theta)
#    venus.pos = vector(xvenus,yvenus,0)

#for theta in arange(0,50*pi,0.1):
#    range(int(30/(Torbita_terra/Torbita_mercurio)))
#    xterra = 20 * ((150 + orbita_terra)/orbita_mercurio) * cos(theta)
#    yterra = 20 * ((150 + orbita_terra)/orbita_mercurio) * sin(theta)
#    terra.pos = vector(xterra,yterra,0)

#for theta in arange(0,50*pi,0.1):
#    range(int(30/(Torbita_marte/Torbita_mercurio)))
#    xmarte = 20 * ((150 + orbita_marte)/orbita_mercurio) * cos(theta)
#    ymarte = 20 * ((150 + orbita_marte)/orbita_mercurio) * sin(theta)
#    marte.pos = vector(xmarte,ymarte,0)

#for theta in arange(0,50*pi,0.1):
#    range(int(30/(Torbita_jupiter/Torbita_mercurio)))
#    xjupiter = 20 * ((150 + orbita_jupiter)/orbita_mercurio) * cos(theta)
#    yjupiter = 20 * ((150 + orbita_jupiter)/orbita_mercurio) * sin(theta)
#    jupiter.pos = vector(xjupiter,yjupiter,0)

#for theta in arange(0,50*pi,0.1):
#    range(int(30/(Torbita_saturno/Torbita_mercurio)))
#    xsaturno = 20 * ((150 + orbita_saturno)/orbita_mercurio) * cos(theta)
#    ysaturno = 20 * ((150 + orbita_saturno)/orbita_mercurio) * sin(theta)
#    saturno.pos = vector(xsaturno,ysaturno,0)



# Criar Planetas

#mercurio = sphere(pos=vector(1,0,0))
#venus = sphere(pos=vector(orbita_venus/orbita_mercurio,0,0),radius = raio_venus/raio_mercurio)
#terra = sphere(pos=vector(orbita_terra/orbita_mercurio,0,0),radius = raio_terra/raio_mercurio)
#marte = sphere(pos=vector(orbita_marte/orbita_mercurio,0,0),radius = raio_marte/raio_mercurio)
#jupiter = sphere(pos=vector(orbita_jupiter/orbita_mercurio,0,0),radius = raio_jupiter/raio_mercurio)
#saturno = sphere(pos=vector(orbita_saturno/orbita_mercurio,0,0),radius = raio_saturno/raio_mercurio)