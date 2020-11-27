from tkinter import *
import tkinter.font as font
from tkinter import messagebox


iks_oks = Tk() #kreiranje prozora naslov, velicina, ikonica, boja i font
iks_oks.title('Tic tac toe')
iks_oks.minsize(width=283, height=277)
iks_oks.maxsize(width=283, height=277)
iks_oks.configure(bg="#000000")
iks_oks.iconbitmap("C:\\Users\\Korisnik\\Desktop\\tiho\\developers lab\\GUI\\ikonice, slike\\Tic tac toe.ico")
Font_XO = font.Font(size=15, weight='bold')

global turn #varijabla koja odredjuje ciji je potez
turn = 'X'
global turns_num #varijabla koja odredjuje broj poteza
turns_num = 0

def reset_game(gameboard, n): #resetovanje tabele
    gameboard[n]['text'] = '' 
    gameboard[n]['state'] = 'active' 
    gameboard[n]['bg'] = '#ffffff'
    global turns_num
    turns_num = 0
    global turn
    turn = 'X'

def check_winner(broj_poteza): #funkcija koja provjerava da li pobjednik postoji
    winner_is = '' #varijabla koja ce cuvati znak pobjednika
    winner_exists = False 
    if buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] !='': #redovi
        winner_is=buttons[0]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] !='': 
        winner_is=buttons[3]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] !='':
        winner_is=buttons[6]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] !='':#kolone 
        winner_is=buttons[0]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] !='':
        winner_is=buttons[1]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] !='':
        winner_is=buttons[2]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] !='':#dijagonale
        winner_is=buttons[0]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    elif buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] !='':
        winner_is=buttons[2]['text']
        winner_exists = True
        return (winner_exists, winner_is)
    else:
        return False, "none"


def clicked(potez, n):
    buttons[n]['text'] = potez #dugme dobija tekst poteza tj. znak onog koga je pritisnuo (X, O)
    buttons[n].config(state="disabled") #nakon jednog klika dugme se ne moze opet pritisnuti 
    
    if potez == 'X': #mijenja se boja dugmeta i znak koji je na potezu
        buttons[n]['bg'] = "#EE3C3C"
        global turn
        turn = 'O'
    else:
        buttons[n]['bg'] = "#45a7ed"
        turn = 'X'
    
    global  turns_num #povecavamo broj poteza
    turns_num += 1
    
    pobjednik_postoji, pobjednik_je = check_winner(turns_num)
    if pobjednik_postoji == True: #ako postoji pobjednik iskace prozor sa porukom 
        messagebox.showinfo("Game over", "Winner is " + pobjednik_je, )
        new_game = messagebox.askyesno("Game over", "Do you want to play one more game?")#postavlja se pitanje da li igrac zeli da pokrene novu partiju
        if new_game == False: #ako igrac ne zeli da igra opet prozor se zatvara
            iks_oks.destroy()
        else:#ako zeli resetujemo tabelu
            i = 0
            while i != 9: #pozivamo se na funkciju reset_game 9 puta jer ona resetuje dugme zasebno
                reset_game(buttons,i)
                i+=1

    elif pobjednik_postoji == False and turns_num==9: #grana u slucaju kada nema ni pobjednika i tabla je popunjena
        messagebox.showinfo("Game over", "There is no winner.")
        new_game = messagebox.askyesno("Game over", "Do you want to play one more game?")
        if new_game == False:
            iks_oks.destroy()
        else:
            i = 0
            while i != 9:
                reset_game(buttons,i)
                i+=1
            
#kreiranje dugmadi    
buttons = list(range(0, 9))
buttons[0] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 0))
buttons[1] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 1))
buttons[2] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 2))
buttons[3] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 3))
buttons[4] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 4))
buttons[5] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 5))
buttons[6] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 6))
buttons[7] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 7))
buttons[8] = Button(iks_oks, font = Font_XO, relief = "raised", text = '', activebackground = "#C7C7BA", bd = '4', command = lambda : clicked(turn, 8))

#pozicioniranje dugmadi
buttons[0].grid(row = 0, column = 0, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[1].grid(row = 0, column = 1, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[2].grid(row = 0, column = 2, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[3].grid(row = 1, column = 0, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[4].grid(row = 1, column = 1, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[5].grid(row = 1, column = 2, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[6].grid(row = 2, column = 0, padx = 3, pady = 3, ipadx = 25, ipady = 20) 
buttons[7].grid(row = 2, column = 1, padx = 3, pady = 3, ipadx = 25, ipady = 20)
buttons[8].grid(row = 2, column = 2, padx = 3, pady = 3, ipadx = 25, ipady = 20)  


iks_oks.mainloop()
