import itertools
import math
import scipy.special

#programma per il numero di modi in cui posso 
#il numero di modi in cui posso 
#dividere  12 amici in due squadre da 5 giocatori e
#un arbitro

n=12
oggetti=range(n)
k=6
arbitri=2

combinazioni_n_k=list(itertools.combinations(oggetti,arbitri))
comb_arb = scipy.special.comb(n,arbitri)
print('comb arb',comb_arb)
comb_sq = scipy.special.comb(10,5)
print('comb sq',comb_sq)
print('tot',comb_sq*comb_arb)
