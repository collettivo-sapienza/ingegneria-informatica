import itertools
import math
import scipy.special

n=4
oggetti=range(n)
k=5

disposizioni_n_k=list(itertools.permutations(oggetti,k))
print('disposizioni_n_k')
#print(disposizioni_n_k)
print(len(disposizioni_n_k) ,'=', (math.factorial(n)/math.factorial(k)))
combinazioni_n_k=list(itertools.combinations(oggetti,k))
print('combinazioni_n_k')
#print(combinazioni_n_k)
print(len(combinazioni_n_k),'=',scipy.special.comb(n,k))
disposizioni_con_rip_n_k=list(itertools.product(oggetti,repeat=k))
print('disposizioni_con_rip_n_k')
#print(disposizioni_con_rip_n_k)
print(len(disposizioni_con_rip_n_k),'=',n**k)
combinazioni_con_rip_n_k=list(itertools.combinations_with_replacement(oggetti,k))
print('combinazioni_con_rip_n_k')
#print(combinazioni_con_rip_n_k)
print(len(combinazioni_con_rip_n_k),'=',scipy.special.comb(n+k-1,k))
