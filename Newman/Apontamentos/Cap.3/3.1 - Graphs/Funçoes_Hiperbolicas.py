from pylab import plot,show,ylim,xlabel,ylabel
from numpy import linspace,cosh,sinh
x = linspace(-5,5,100)
y1 = cosh(x)
y2 = sinh(x)
plot(x,y1,"-")
plot(x,y2,)
ylim(-20,20)
xlabel('x')
ylabel('cosh(x)')
show()