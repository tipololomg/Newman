from math import sqrt
def primos():
    a = [2]
    b = []
    c = 0
    for n in range(3,10001):
      for w in range(len(a)):
        if a[w] <= n:
          b.append(a[w])
      for z in b:
        if n % z == 0:
          c = 0
          break
        else:
          c += 1
      if c == len(b):
        a.append(n)
        c = 0
      b = []
    return a
    





