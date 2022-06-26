#Copyright Minchiasoft 2021

from random import randint

sel = []

f = open('domande.txt','r').readlines()

for i in range(0,10):
    indice = randint(0,len(f)-1)
    while(f[indice] in sel and len(f[indice])<1):
        indice = randint(0,len(f)-1)
    sel.append(f[indice])
fw = open('compito_r.txt','w')
ind = 0
for el in sel:
    ind+=1
    fw.write(str(ind)+'\n')
    fw.write(el)

fw.close()
