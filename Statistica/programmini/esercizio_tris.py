import itertools
import math
import scipy.special

def ordine(el):
    st =''
    for e in el:
        st+=str(e)
    if('123') in st:
        return 1
    if('234') in st:
        return 1
    if('345') in st:
        return 1
    return 0
n=5
oggetti=range(n)

disposizioni_con_rip_n_k=list(itertools.permutations(oggetti,5))
cnt =0
for el in disposizioni_con_rip_n_k:
    var = ordine(el)
    cnt+=var
    print()
    print(cnt)
print('disposizioni_con_rip_n_k')
print(cnt)
print(cnt/len(disposizioni_con_rip_n_k))
#print(disposizioni_con_rip_n_k)
#print(len(disposizioni_con_rip_n_k),'=',n**k)
