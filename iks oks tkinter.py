from tkinter import *
import tkinter.font as font

iks_oks = Tk()
iks_oks.title('Iks oks')
iks_oks.minsize(width=283, height=277)
iks_oks.maxsize(width=283, height=277)
iks_oks.configure(bg="#000000")
iks_oks.iconbitmap("C:\\Users\\Korisnik\\Desktop\\tiho\\developers lab\\GUI\\ikonice, slike\\Tic tac toe.ico")
Font_XO = font.Font(size=15, weight='bold')


global turn
turn = 'X'
global turns_num
turns_num = 0


def check_winner():
    winner_is = ''
    winner_exists = False
    if buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] !='' or \
        buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] !='' or \
            buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] !='' or \
                buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] !='' or \
                    buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] !='' or \
                        buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] !='' or \
                            buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] !=''or \
                                buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] !='':

        winner_is=buttons[0]['text']
        winner_exists = True
        results = tuple((winner_exists, winner_is))
        return results
    
    else:
        return FALSE
        
def clicked(potez, n):
    buttons[n]['text'] = potez
    buttons[n].config(state="disabled")
    
    if potez == 'X':
        buttons[n]['bg'] = "#EE3C3C"
        global turn
        turn = 'O'
    else:
        buttons[n]['bg'] = "#45a7ed"
        turn = 'X'
    
    global  turns_num
    turns_num += 1
    
    pobjednik_postoji, pobjednik_je = check_winner()
    if pobjednik_postoji == True:
        print('Winner is', pobjednik_je)
    


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
