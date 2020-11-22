from tkinter import *

kalkulator = Tk()

kalkulator.title('Kalkulator')#Naslov prozora

kalkulator.minsize(width=335, height=395)#Zakljucana velicina prozora
kalkulator.maxsize(width=335, height=395)

kalkulator.configure(bg="#B8D8FE")#pozadinska boja

kalkulator.iconbitmap("C:\\Users\\Korisnik\\Desktop\\tiho\\developers lab\\GUI\\ikonice, slike\\Calc icon.ico")#ikonica

unos = Entry(kalkulator, bd = 5, bg="#78C1EB")#kreiranje naslova

unos.grid(row=0, column=0, columnspan=4, ipadx=100)

def click(n):#unos brojeva 
    prethodni_br=unos.get()
    unos.delete(0, END)
    unos.insert(0, str(prethodni_br) + str(n)) 

def Clear():#brisanje brojeva
    unos.delete(0, END)

#funkcije za svaku od operacija: 

def Jednako():
    drugiUnesebiBr = unos.get()
    global DrugiBr
    unos.delete(0, END)
    DrugiBr = drugiUnesebiBr
    if operacija == '+':
        unos.insert(0, int(PrviBr) + int(DrugiBr))
    if operacija == '-':
        unos.insert(0, int(PrviBr) - int(DrugiBr))
    if operacija == '*':
        unos.insert(0, int(PrviBr) * int(DrugiBr))
    if operacija == '/':
        unos.insert(0,  int(PrviBr) / int(DrugiBr))

def sabiranje():
    uneseniBr = unos.get()
    global PrviBr 
    PrviBr = uneseniBr
    unos.delete(0, END)
    
    global operacija
    operacija = '+'
    

def oduzimanje():
    uneseniBr = unos.get()
    global PrviBr 
    PrviBr = uneseniBr
    unos.delete(0, END)

    global operacija
    operacija = '-'

def mnoziti():
    uneseniBr = unos.get()
    global PrviBr 
    PrviBr = uneseniBr
    unos.delete(0, END)
    
    global operacija
    operacija = '*'

def dijeliti():
    uneseniBr = unos.get()
    global PrviBr 
    PrviBr = uneseniBr
    unos.delete(0, END)
    
    global operacija
    operacija = '/' 


dugme1 = Button(kalkulator, text="1", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(1))#kreiranje dugmadi i dodjela funkcija (brojevi)
dugme2 = Button(kalkulator, text="2", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(2))
dugme3 = Button(kalkulator, text="3", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(3))
dugme4 = Button(kalkulator, text="4", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(4))
dugme5 = Button(kalkulator, text="5", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(5))
dugme6 = Button(kalkulator, text="6", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(6))
dugme7 = Button(kalkulator, text="7", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(7))
dugme8 = Button(kalkulator, text="8", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(8))
dugme9 = Button(kalkulator, text="9" ,bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(9))
dugme0 = Button(kalkulator, text="0", bd=5, bg="#3EACEB", activebackground="#00FFF7", command = lambda : click(0))

    
clear = Button(kalkulator, text="C", bd=3, bg="#0378FE", activebackground="#277E7B", command = Clear)#kreiranje dugmadi i dodjela funkcija (operacije)
plus = Button(kalkulator, text="+", bd=3, bg="#F15050", activebackground="#277E7B", command = sabiranje)
minus = Button(kalkulator, text="-", bd=3, bg="#0378FE", activebackground="#277E7B",command = oduzimanje)
mnozenje = Button(kalkulator, text="*", bd=3, bg="#0378FE", activebackground="#277E7B", command = mnoziti)
dijeljenje = Button(kalkulator, text="÷", bd=3, bg="#0378FE", activebackground="#277E7B", command = dijeliti)
jednako = Button(kalkulator, text="=", bd=3, bg="#0378FE",activebackground="#277E7B", command = Jednako)

dugme1.grid(row=3, column=0, ipadx=30, ipady=30)#Pozicioniranje dugmadi
dugme2.grid(row=3, column=1, ipadx=30, ipady=30)
dugme3.grid(row=3, column=2, ipadx=30, ipady=30)
dugme4.grid(row=4, column=0, ipadx=30, ipady=30)
dugme5.grid(row=4, column=1, ipadx=30, ipady=30)
dugme6.grid(row=4, column=2, ipadx=30, ipady=30)
dugme7.grid(row=5, column=0, ipadx=30, ipady=30)
dugme8.grid(row=5, column=1, ipadx=30, ipady=30)
dugme9.grid(row=5, column=2, ipadx=30, ipady=30)
dugme0.grid(row=6, column=0, ipadx=30, ipady=30)

mnozenje.grid(row=3, column=3,  padx=10, ipadx=25,ipady=20)
dijeljenje.grid(row=4, column=3, ipadx=25, ipady=20)
plus.grid(row=5, column=3, ipadx=20, ipady=32)
clear.grid(row=6, column=1, ipadx=25, ipady=20)
minus.grid(row=6, column=2, ipadx=25, ipady=20)
jednako.grid(row=6, column=3, ipadx=20, ipady=20)

kalkulator.mainloop()
