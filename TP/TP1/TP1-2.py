def Catalan():
    c=1
    n=0
    while c<1000000000:
        c*=(4*n+2)/(n+2)
        n+=1
        print (c)

Catalan()