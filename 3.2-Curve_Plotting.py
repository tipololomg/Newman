from pylab import plot,show
from numpy import sin,cos,linspace,pi,exp
def Deltoid():
    Theta = linspace(0,2*pi,100)
    x = 2 * cos(Theta) + cos(2*Theta)
    y = 2 * sin(Theta) - sin(2*Theta)
    plot(x,y)
    show()

def Galilean_Spiral():
    Theta = linspace(0,10*pi,100)
    r = Theta**2
    x = r * cos(Theta)
    y = r * sin(Theta)
    plot(x,y)
    show()

def Feys_Function():
    Theta = linspace(0,24*pi,5000)
    r = (exp(cos(Theta))) - (2 * cos(4*Theta)) + (sin(Theta/12))**5
    x = r * cos(Theta)
    y = r * sin(Theta)
    plot(x,y)
    show()

Feys_Function()