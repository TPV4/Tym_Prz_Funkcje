import tkinter as tk
from tkinter.ttk import *
import pochodne as po

class Menu():
    def __init__(self) -> None:
        self.okno=tk.Tk()
        self.okno.geometry("600x400")
        self.okno.title("Pochodne")
        self.okno.resizable(False, False)
        self.interface()
        self.okno.mainloop()   

    def interface(self):
        self.napis=Label(self.okno, text="wpisz wzor funkcji").place(x=150,y=100)
        self.notes=Entry(self.okno, width=30)
        self.notes.place(x=150,y=150)
        self.sprawdzenie=Button(self.okno, text="zatwierdz", command=lambda:self.czy_poprawne(self.notes.get())).place(x=400,y=150)
        self.wykres=Button(self.okno, text="utworz wykresy", command=lambda:self.wykresy(self.notes.get()))
        self.wykres.place(x=400, y=200)
        self.wykres["state"]=tk.DISABLED
        self.wyjscie=Button(self.okno, text="wyjdz", command=lambda:self.okno.destroy()).place(x=400, y=250)  

    def czy_poprawne(self, F): ##sprawdza czy wzor funkcji jest poprawny
        self.zmienne=0
        for i in range(len(F)):
            znak=ord(F[i])
            if znak>96 and znak<123:
                if not (i+1>len(F) or i+2>len(F)):
                    slowo=F[i]+F[i+1]+F[i+2]
                    if slowo=="sin" or slowo=="cos" or slowo=="exp":
                        i+=2
                    elif slowo=="pi":
                        i+=1
                    else:
                        self.zmienne+=1
                else:
                    self.zmienne+=1
                if self.zmienne>2:
                    return False
            elif (znak<40 or znak>57) and znak!=94:
                return False
        if self.zmienne!=0:
            self.wykres["state"]=tk.ACTIVE

    def wykresy(self, funkcja):
        po.Wykres(funkcja, self.zmienne)

if __name__=="__main__":
    Menu()