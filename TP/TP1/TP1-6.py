def fatorial(n):
    if n >= 0:
        if n == 1 or n == 0:
            return 1
        else:
            return n * fatorial(n-1)
    else:
        True


def Catalan(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return ((4*n-2)/(n+1))*Catalan(n-1)
    else:
        True

def mdc(m,n):
    if m >= 0 and n >= 0:
        a,b = int(m),int(n)
        if b == 0:
            return a
        else:
            return mdc(n,m % n)
    else:
        True
print(mdc(108,192))