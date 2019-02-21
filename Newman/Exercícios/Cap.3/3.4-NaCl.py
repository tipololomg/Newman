from vpython import sphere,vector,color
def NaCl():
    L = 5
    R = 0.3
    for i in range(-L,L+1,2):
        for j in range(-L,L+1,2):
            for k in range(-L,L+1,2):
                sphere(pos=vector(i,j,k),radius=R*2,color=color.red)

    for i in range(-L+1,L,2):
        for j in range(-L+1,L,2):
            for k in range(-L+1,L,2):
                sphere(pos=vector(i,j,k),radius=R,color=color.cyan)

def fcc():
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                sphere(pos=vector(i,j,k),radius=0.1,color=color.red)
    sphere(pos=vector(1/2,0,1/2),radius=0.1,color=color.cyan)
    sphere(pos=vector(0,1/2,1/2),radius=0.1,color=color.cyan)
    sphere(pos=vector(1/2,1/2,0),radius=0.1,color=color.cyan)
    sphere(pos=vector(1,1/2,1/2),radius=0.1,color=color.cyan)
    sphere(pos=vector(1/2,1,1/2),radius=0.1,color=color.cyan)
    sphere(pos=vector(1/2,1/2,1),radius=0.1,color=color.cyan)



def Tfcc():
    L = 2
    R = 0.3
    for i in range(-L,L+1,2):
        for j in range(-L,L+1,2):
            for k in range(-L,L+1,2):
                sphere(pos=vector(i,j,k),radius=R)
                sphere(pos=vector(i+1,j+1,k),radius=R)
                sphere(pos=vector(i,j+1,k+1),radius=R)
                sphere(pos=vector(i+1,j,k+1),radius=R)
