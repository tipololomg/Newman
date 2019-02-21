from pylab import imshow,show,jet,ylim,xlim,xlabel,ylabel
from numpy import loadtxt

data = loadtxt("/Users/tipololomg/Desktop/Python/Newman/stm.txt",float)

imshow(data,origin="lower")
jet()
xlabel("Position")
ylabel("Quantum Tunneling")
xlim(150,550)
ylim(150,500)
show()              