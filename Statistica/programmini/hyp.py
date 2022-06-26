import itertools
import math
import scipy.special

print('metti N')
N = int(input())
print('metti n')
n = int(input())
print('metti r')
r = int(input())

m = max(0,n+r-N)
M = min(n,r)

print('formula: P(X=x) = ')

for i in range(m,M+1):
    var = scipy.special.comb(r,i)
    var *=scipy.special.comb(N-r,n-i)
    var /= scipy.special.comb(N,n)
    print('P(x=',i,')= ' ,var) 
print()
media = (n*r/N)
print('E(x)= ',media)
print('Var(x)= ',(((N-n)/(N-1)) * media * (1-(r/N))))
