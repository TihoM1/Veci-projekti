from tkinter import *
import tkinter.font as font

kalkulator = Tk()

kalkulator.title('Kalkulator')#Naslov prozora

Font_za_brojeve = font.Font(size=25)
Font_za_operacije = font.Font(size=15, weight='bold')
kalkulator.minsize(width=338, height=433)#Zakljucana velicina prozora
kalkulator.maxsize(width=338, height=433)

kalkulator.configure(bg="#97C3FF")#pozadinska boja

kalkulator.iconbitmap("C:\\Users\\Korisnik\\Desktop\\tiho\\developers lab\\GUI\\ikonice, slike\\Calc icon.ico")#ikonica

unos = Entry(kalkulator, bd = 5, bg="#4ACBE2")#kreiranje naslova

unos.grid(row=0, column=0, columnspan=4,pady=3, ipadx=103)

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


dugme1 = Button(kalkulator, text="1", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(1))#kreiranje dugmati i dodjela funkcija (brojevi)
dugme2 = Button(kalkulator, text="2", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(2))
dugme3 = Button(kalkulator, text="3", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(3))
dugme4 = Button(kalkulator, text="4", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(4))
dugme5 = Button(kalkulator, text="5", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(5))
dugme6 = Button(kalkulator, text="6", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(6))
dugme7 = Button(kalkulator, text="7", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(7))
dugme8 = Button(kalkulator, text="8", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(8))
dugme9 = Button(kalkulator, text="9", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(9))
dugme0 = Button(kalkulator, text="0", font = Font_za_brojeve, bd=5, bg="#26ADFF", activebackground="#00FFF7", command = lambda : click(0))

    
clear = Button(kalkulator, text="C", font = Font_za_operacije, bd=4, relief="ridge", bg="#035AFE", activebackground="#277E7B", command = Clear)#kreiranje dugmati i dodjela funkcija (operacije)
plus = Button(kalkulator, text="+", font = Font_za_operacije, bd=4, relief="ridge", bg="#D42B2B", activebackground="#277E7B", command = sabiranje)
minus = Button(kalkulator, text="-", font = Font_za_operacije, bd=4, relief="ridge", bg="#035AFE", activebackground="#277E7B",command = oduzimanje)
mnozenje = Button(kalkulator, text="*", font = Font_za_operacije, bd=4, relief="ridge", bg="#035AFE", activebackground="#277E7B", command = mnoziti)
dijeljenje = Button(kalkulator, text="÷", font = Font_za_operacije, bd=4, relief="ridge", bg="#035AFE", activebackground="#277E7B", command = dijeliti)
jednako = Button(kalkulator, text="=", font = Font_za_operacije, bd=4, relief="ridge", bg="#035AFE",activebackground="#277E7B", command = Jednako)

dugme1.grid(row=3, column=0, pady=3, ipadx=14, ipady=10)#Pozicioniranje dugmadi
dugme2.grid(row=3, column=1, ipadx=14, ipady=10)
dugme3.grid(row=3, column=2, ipadx=14, ipady=10)
dugme4.grid(row=4, column=0, pady=3, ipadx=14, ipady=10)
dugme5.grid(row=4, column=1, ipadx=14, ipady=10)
dugme6.grid(row=4, column=2, ipadx=14, ipady=10)
dugme7.grid(row=5, column=0, pady=5, ipadx=14, ipady=10)
dugme8.grid(row=5, column=1, ipadx=14, ipady=10)
dugme9.grid(row=5, column=2, ipadx=14, ipady=10)
dugme0.grid(row=6, column=0, ipadx=14, ipady=10)

mnozenje.grid(row=3, column=3, ipadx=15, ipady=10)
dijeljenje.grid(row=4, column=3, ipadx=14, ipady=11)
plus.grid(row=5, column=3, ipadx=10, ipady=20)
clear.grid(row=6, column=1, ipadx=15, ipady=10)
minus.grid(row=6, column=2, ipadx=17, ipady=10)
jednako.grid(row=6, column=3, ipadx=15, ipady=10)


kalkulator.mainloop()