def fac(x):
    if x == 1:
        return 1
    else:
        a = 1
        for i in range(1,x+1):
            a *= i
        return a



def binomial(n,k):
    if k == 0:
        return int(1)
    else:
        return int(fac(n)/(fac(k)*fac(n-k)))

def Pascal():
    print('1')
    print('')
    for n in range(1,21):
        for k in range(0,n+1):
            print(binomial(n,k),end=' ')
        print('\n')

def prob(n,k):
    return binomial(n,k)/(2**n)

def prob2(n,k):
    p = 0
    for i in range(k,n):
        p += prob(n,k)
    return p

print(prob(100,60)*100,'%')
print(prob2(100,60)*100,'%')