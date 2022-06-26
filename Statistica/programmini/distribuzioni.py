import math
import scipy.special
import scipy.integrate

def form(st):
    st = str(st)
    '''
    if(len(st)>8):
        return st[0:8]
    else:
        for i in range(len(st),8):
            st+=' '
    '''
    return st
def hippy():
    print('metti N')
    N = int(input())
    print('metti n')
    n = int(input())
    print('metti r')
    r = int(input())
    m = max(0,n+r-N)
    M = min(n,r)
    print('formula: P(X=x) = ')
    cdf = 0.0
    for i in range(m,M+1):
        var = scipy.special.comb(r,i)
        var *=scipy.special.comb(N-r,n-i)
        var /= scipy.special.comb(N,n)
        cdf+=var
        print('P(x=',i,')= '+form(var),end ='') 
        print('\t cum=',form(cdf))
    print()
    media = (n*r/N)
    print('E(x)= ',form(media))
    print('Var(x)= ',form((((N-n)/(N-1)) * media * (1-(r/N)))))

def bini():
    print('metti p')
    p = float(input())
    print('metti n')
    n = int(input())
    var = 0.0
    cdf = 0.0
    for i in range(0,n+1):
        var =  scipy.special.comb(n,i)
        var*=pow(p,i)
        var*=pow((1-p),n-i)
        cdf+=var
        print('P(x=',i,')= ' ,var,end='')
        print('\t cum=',cdf)
    print()
    media = p*n
    print('E(x)= ',media)
    print('Var(x)= ',media * (1-p))

def geom():
    print('metti p')
    p = float(input())
    print('metti fino a dove vuoi arrivare')
    n = int(input())
    cdf = 0.0
    for i in range(1,n+1):
        var = pow((1-p),i-1) * p
        cdf+=var
        print('P(x=',i,')= ' ,form(var),end=' ')
        print('\t cum=',form(cdf))
    print()
    media = 1/p
    print('E(x)= ',media)
    print('Var(x)= ',(1-p)/(p*p))

def nBin():
    print('metti r')
    r = int(input())
    print('metti fino a dove vuoi arrivare')
    n = int(input())
    print('metti p')
    p = float(input())

    print('formula: P(X=x) = ')
    cdf = 0.0
    for i in range(1,n+1):
        prob = scipy.special.comb(i-1,r-1) * pow((1-p),(i-r)) * pow(p,r)
        cdf+=prob
        print('P(x=',i,')= ' ,form(prob),end=' ') 
        print('\t cum=',form(cdf))
    print()
    media = (r/p)
    print('E(x)= ',media)
    print('Var(x)= ',r*(1-p)/(p*p))
    
def poi():
    print('metti lambda')
    l=float(input())
    print('metti fino a dove vuoi arrivare')
    n = int(input())
    cdf =0.0
    for i in range(0,n+1):
        var=(math.exp(-l)*pow(l,i))/(math.factorial(i))
        cdf+=var
        print('P(x=',i,')= ' ,form(var),end=' ') 
        print('\t cum=',form(cdf))
    print()
    media = l
    print('E(x)= ',media)
    print('Var(x)= ',media)

def mult():
    print('inserisci n trials:')
    n=int(input())
    print('inseri k outcomes')
    k=int(input())
    p=[]
    x=[]
    for j in range(0,k):
        print("inserisci la prob dell'outcome",j,":")
        p.append(float(input()))    
        print("inserisci il numero di successi desiderato per",j,":")
        x.append(float(input()))
    print("ora calcolo")
    d=1.0
    ptot=1.0
    s=''
    for j in range(0,k):
        d*=math.factorial(x[j])
        ptot*=pow(p[j],x[j])
        s+='X'
        s+=str(j)
        s+='='
        s+=str(x[j])
        s+=', '
    #print('d',d,'ptot ',ptot,'n ',n)
    s+=')='
    ciccio=ptot* (math.factorial(n))/d
    print('P(',s,ciccio)
    
    print('medie e varianze:')
    for j in range(0,k):
        print('E(x',j,')=',n*p[j])
        print('Var(x',j,')=',n*p[j]*(1-p[j]))
    print('fatto!!')
    
def unif():
    print('inserisci a')
    a=float(input())
    print('inserisci b')
    b=float(input())
    print('f(x)=',1/(b-a))
    print('F(x)=(x-',a,')/',b-a)
    print('E(x)=',(a+b)/2)
    print('Var(x)=',pow((b-a),2)/12)
    
def esp():
    print('inserisci lambda:')
    l=float(input())
    print('inserisci una x:')
    x=float(input())
    print('f(x)=',l*math.exp(-l*x))
    print('F(x)=',1-math.exp(-l*x))
    print('E(x)=dev st=',1/l)
    print('Var(x)=',1/l*l)

def gammino(x,l,k):
    return pow(l,k)* pow(x,k-1) * math.exp(-l * x) / math.gamma(k)

def gammaDist():
    print('inserisci lambda,kappa,x:')
    stringa = input().strip('\n').split(',')
    l = float(stringa[0])
    k = float(stringa[1])
    x = float(stringa[2])
    y=x
    f = gammino(x,l,k)
    print('f(X=',x,')=',f)
    print('F(X=',x,')=',scipy.integrate.quad(gammino,0,y,args=(l,k))[0])
    print('E(x)=',k/l)
    print('Var(x)=',k/pow(l,2))

def normina(x,m,s):
    return math.exp(-pow((x-m),2) / 2*pow(s,2)) / (s*math.sqrt(2*math.pi))

def norm():
    print('inserisci media, dev std,x:')
    stringa = input().strip('\n').split(',')
    m = float(stringa[0])
    s = float(stringa[1])
    x=float(stringa[2])
    y=(x-m)/s
    f=normina(y,0,1)
    pcf='Fi(Z='
    print('f(Z=',y,')=',f)
    print(pcf,y,')=',scipy.integrate.quad(normina,-math.inf,y,args=(0,1))[0])
    print('E(x)=',m)
    print('Var(x)=',s*s)
   
def chi():
    print('inserisci v, la x che vuoi:')
    stringa=input().strip('\n').split(',')
    v=float(stringa[0])
    x = float(stringa[1])
    f = gammino(x,1/2,v/2)
    print('f(X=',x,')=',f)
    print('F(X=',x,')=',scipy.integrate.quad(gammino,0,x,args=(1/2,v/2))[0])
    print('E(x)=',v)
    print('Var(x)=',2*v)
    
def t_aux(x,v):
    return math.gamma((v+1)/2) / (math.sqrt(math.pi)*math.gamma(v/2)*pow((1+((x*x)/v)),(v+1)/2))
def t():
    print('inserisci x,v:')
    stringa=input().strip('\n').split(',')
    x=float(stringa[0])
    v=float(stringa[1])
    f=t_aux(x,v)
    print('f(X=',x,')=',f)
    #print('F(X=',x,')=',scipy.integrate.quad(t_aux,-math.inf,x,args=(v))[0])
    if v>=2:
        print('E(x)=',0)
    if v>=3:
        print('Var(x)=',v/(v-2))

print('Copyright Minchiasoft 2021')
print('Versione 2.1.0')
print('BuonaSEGA')
while(True): 
    print('Inserisci (discrete: 1,continue: 2,uscire: esci):')
    di = input()
    if di=='1':
        print('Scegli la distribuzione (geom:0,hyp:1,bin:2,nBin:3,poi:4,multi:5):')
        di=input()
        if di=='0': 
            geom()
        elif di=='1':
            hippy()
        elif di=='2':
            bini()
        elif di=='3':
            nBin()
        elif di=='4':
            poi()
        elif di=='5':
            mult()
    elif di=='2':
        print('Scegli la distribuzione (unif: 0,esp: 1,gamma: 2,norm: 3,chi_quadro: 4,t_student: 5) :')
        di=input()
        if di=='0':
            unif()
        elif di=='1':
            esp()
        elif di=='2':
            gammaDist()
        elif di=='3':
            norm()
        elif di=='4':
            chi()
        elif di=='5':
            t()
    elif di=='esci':
        print('Arrivederci!')
        break
    else:
        print("input non valido")

