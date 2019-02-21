from pylab import imshow,show,jet,ylim,xlim
from numpy import loadtxt

data = loadtxt("/Users/tipololomg/Desktop/Python/Newman/Apontamentos/Cap.3/3.3-Density Plots/Fig.3.5/circular.txt",float)
imshow(data,origin="lower",extent=[0,10,0,5],aspect=2.0)
jet()
show()