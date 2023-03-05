import numpy as np


def zamiana(x,y,f):
    xn=0
    liczba=''
    for i in range(len(f)):
        if f[i]=='(':
            podwzor=''
            t=i+1
            while f[t]!=')':
                podwzor+=f[t]
                t+=1
            if t+1<len(f):
                return zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+2:])
            else:
                return zamiana(x,y,podwzor)
        elif f[i]=='*':
            podwzor=''
            t=i+1
            while t<len(f) and f[t]!='+' and f[t]!='-':
                if f[t]=='(':
                    k=t+1
                    podwzor=''
                    while f[k]!=')':
                        podwzor+=f[k]
                        k+=1
                    if k+1<len(f):
                        return xn*zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+3:])
                    else:
                        return xn*zamiana(x,y,podwzor)
                podwzor+=f[t]
                t+=1
            if t<len(f):
                return xn*zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+2:])
            else:
                return xn*zamiana(x,y,podwzor)
        elif f[i]=='^':
            podwzor=''
            t=i+1
            while t<len(f) and f[t]!='+' and f[t]!='-':
                if f[t]=='(':
                    k=t+1
                    podwzor=''
                    while f[k]!=')':
                        podwzor+=f[k]
                        k+=1
                    if k+1<len(f):
                        return xn**zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+3:])
                    else:
                        return xn**zamiana(x,y,podwzor)
                podwzor+=f[t]
                t+=1
            if t<len(f):
                return xn**zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+2:])
            else:
                return xn**zamiana(x,y,podwzor)
        elif f[i]=='/':
            podwzor=''
            t=i+1
            while t<len(f) and f[t]!='+' and f[t]!='-':
                if f[t]=='(':
                    k=t+1
                    podwzor=''
                    while f[k]!=')':
                        podwzor+=f[k]
                        k+=1
                    if k+1<len(f):
                        return xn/zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+3:])
                    else:
                        return xn/zamiana(x,y,podwzor)
                podwzor+=f[t]
                t+=1
            if t<len(f):
                return xn/zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+2:])
            else:
                return xn/zamiana(x,y,podwzor)
        elif f[i]=='s':
            ##sinus()
            if f[i+1]=='i':
                podwzor=''
                t=i+4
                while f[t]!=')':
                    podwzor+=f[t]
                    t+=1
                if t+1<len(f):
                    return np.sin(zamiana(x,y,podwzor))+zamiana(x,y,f[len(podwzor)+2:])
                else:
                    return np.sin(zamiana(x,y,podwzor))
            else:
                ##sqrt()
                podwzor=''
                t=i+5
                while f[t]!=')':
                    podwzor+=f[t]
                    t+=1
                if t+1<len(f):
                    return np.sqrt(zamiana(x,y,podwzor))+zamiana(x,y,f[len(podwzor)+2:])
                else:
                    return np.sqrt(zamiana(x,y,podwzor))
        elif f[i]=='c':
            ##cosinus()
            podwzor=''
            t=i+4
            while f[t]!=')':
                podwzor+=f[t]
                t+=1
            if t+1<len(f):
                return np.cos(zamiana(x,y,podwzor))+zamiana(x,y,f[len(podwzor)+2:])
            else:
                return np.cos(zamiana(x,y,podwzor))
        elif f[i]=='e':
            ##exp()
            podwzor=''
            t=i+4
            while f[t]!=')':
                podwzor+=f[t]
                t+=1
            if t+1<len(f):
                return np.exp(zamiana(x,y,podwzor))+zamiana(x,y,f[len(podwzor)+2:])
            else:
                return np.exp(zamiana(x,y,podwzor))
        elif f[i]=='+':
            podwzor=''
            t=i+1
            while t<len(f):
                podwzor+=f[t]
                t+=1
            return xn+zamiana(x,y,podwzor)
        elif f[i]=='-':
            podwzor=''
            t=i+1
            while t<len(f) and f[t]!='+' and f[t]!='-':
                if f[t]=='(':
                    k=t+1
                    podwzor=''
                    while f[k]!=')':
                        podwzor+=f[k]
                        k+=1
                    if k+1<len(f):
                        return xn-zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor)+3:])
                    else:
                        return xn-zamiana(x,y,podwzor)
                podwzor+=f[t]
                t+=1
            if t<len(f):
                return xn-zamiana(x,y,podwzor)+zamiana(x,y,f[len(podwzor):])
            else:
                return xn-zamiana(x,y,podwzor)
        else:
            if f[i]=='x':
                xn=x
            elif f[i]=='y':
                xn=y
            elif f[i]=='p' and f[i+1]=='i':
                xn=np.pi
            elif f[i]!='i':
                liczba+=f[i]
        if liczba!='':
            xn=float(liczba)
    return xn

# X=np.arange(-5,5,1)
# Y=np.arange(-5,5,1)
# F=[[0 for a in range(len(X))] for b in range(len(Y))]
# for i in range(len(Y)):
#     for j in range(len(X)):
#         F[i][j]=zamiana(X[j],Y[i],"x^2+2*y")
# F=np.array(F)
# print(F)
        