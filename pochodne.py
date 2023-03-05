import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import analiza

class Wykres():
    def __init__(self, funkcja, licz_zmien) -> None:
        plt.style.use('_mpl-gallery')
        if licz_zmien==1:
            self.wykres1(funkcja)
        elif licz_zmien==2:
            self.wykres2(funkcja)

    def wykres1(self, funkcja): ##pochodna jednej zmiennej
        x=np.arange(-50,51,0.1)
        F=self.analiza1(funkcja, x)
        fig, axis= plt.subplots(1,2)
        axis[0].plot(x,F)
        axis[0].set_title("funkcja pierwotna", y=1.0, pad=-10)
        f=[0 for a in range(len(F))]
        for i in range(len(x)-1):
            dx=0.1
            dy=F[i+1]-F[i]
            f[i]=dy/dx
        f[len(F)-1]=(F[len(F)-1]-F[len(F)-2])/dx
        axis[1].plot(x,f)
        axis[1].set_title("pochodna funkcji", y=1.0, pad=-10)
        fig.set_size_inches(9,7)
        plt.show()

    def analiza1(self, funkcja, osX):
        F=[0 for a in range(len(osX))]
        for n in range(len(osX)):
            F[n]=analiza.zamiana(osX[n], 0, funkcja)
        return F

    def wykres2(self, funkcja):
        ## dziedzina
        D=[(-5,5),(-5,5)]
        I=0.1 ## interwal
        x=np.arange(D[0][0],D[0][1],I)
        y=np.arange(D[1][0],D[1][1],I)
        F=self.analiza2(funkcja, x, y)
        fy=[[0 for a in range(len(x))] for b in range(len(y))]
        fx=[[0 for a in range(len(x))] for b in range(len(y))]
        ## pochodna po x
        dx=I
        for i in range(len(y)): 
            for j in range(len(x)-1):
                dz=F[i][j+1]-F[i][j]
                fx[i][j]=dz/dx
        for k in range(len(F[0])):
            fx[k][len(F)-1]=(F[k][len(F)-1]-F[k][len(F)-2])/dx
        fx=np.array(fx)
        ## pochodna po y
        dy=I
        for i in range(len(y)-1): 
            for j in range(len(x)):
                dz=F[i+1][j]-F[i][j]
                fy[i][j]=dz/dy
        for k in range(len(F)):
            fy[len(F)-1][k]=(F[len(F)-1][k]-F[len(F)-2][k])/dy
        fy=np.array(fy)
        ## stworzenie wykresow i nalozenie osi 
        x,y=np.meshgrid(x,y)
        fig, axis = plt.subplots(2,2,subplot_kw={"projection": "3d"})
        axis[0,0].plot_surface(x, y, F, vmin=F.min(), cmap=cm.Blues)
        axis[0,0].set_title("funkcja pierwotna", y=1.0, pad=-6)
        axis[1,0].plot_surface(x, y, fx, vmin=fx.min(), cmap=cm.Reds)
        axis[1,0].set_title("pochodna cząstkowa po X", y=1.0, pad=-6)
        axis[1,1].plot_surface(x, y, fy, vmin=fy.min(), cmap=cm.Reds)
        axis[1,1].set_title("pochodna cząstkowa po Y", y=1.0, pad=-6)
        fig.set_size_inches(9,9)
        plt.show()
    
    def analiza2(self, funkcja, osX, osY):
        F=[[0 for a in range(len(osX))] for b in range(len(osY))]
        for n in range(len(osY)):
            for m in range(len(osX)):
                F[n][m]=analiza.zamiana(osX[m], osY[n], funkcja)
        F=np.array(F)
        return F
    
# Wykres("x^2+y^2", 2)