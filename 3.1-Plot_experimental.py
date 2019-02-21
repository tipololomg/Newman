from pylab import *
from numpy import loadtxt
def a ():
        data = loadtxt("sunspots.txt",float)
        x = data[:,0]
        y = data[:,1]
        plot(x,y)
        show()

def b ():
        data = loadtxt("sunspots.txt",float)
        x = data[:1000,0]
        y = data[:1000,1]
        plot(x,y)
        show()

def c (L,r):
        data = loadtxt("sunspots.txt",float)
        x = data[:L,0]
        y = data[:L,1]
        s = [ sum(y[k-r:k+r]) for k in range(L)]
        a = array(s)/2/r
        plot(x,y,label='Noisy')
        plot(x,a,label='Averaged')
        legend()
        show()
