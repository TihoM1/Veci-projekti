grid = {'0':'', '1':'', '2':'', '3':'',#tabela
        '4':'', '5':'', '6':'', '7':'',
        '8':'', '9':'', '10':'', '11':'',
        '12':'', '13':'', '14':'', '15':''}

def stampaj_tabelu(gameboard):#stampanje tabele
    print('---------------')
    print('|',grid['0'],'|', grid['1'],'|', grid['2'],'|', grid['3'],'|')
    print('---------------')
    print('|',grid['4'],'|', grid['5'],'|', grid['6'],'|', grid['7'],'|')
    print('---------------')
    print('|',grid['8'],'|', grid['9'],'|', grid['10'],'|', grid['11'],'|')
    print('---------------')
    print('|',grid['12'],'|', grid['13'],'|', grid['14'],'|', grid['15'],'|')
    print('---------------')

def check_winner(gameboard):
    if grid['0']==grid['1']==grid['2']==grid['3']!='':#redovi
        return True
    elif grid['4']==grid['5']==grid['6']==grid['7']!='':
        return True
    elif grid['8']==grid['9']==grid['10']==grid['11']!='':
        return True
    elif grid['12']==grid['13']==grid['14']==grid['15']!='':
        return True

    elif grid['0']==grid['4']==grid['8']==grid['12']!='':#kolone
        return True
    elif grid['1']==grid['5']==grid['9']==grid['13']!='':
        return True
    elif grid['2']==grid['6']==grid['10']==grid['14']!='':
        return True 
    elif grid['3']==grid['7']==grid['11']==grid['15']!='':
        return True

    

na_potezu='X'
br_poteza=0
game_over=False

while not game_over:
    stampaj_tabelu(grid)
    print('Igrac',na_potezu,'je na potezu, unesite br. polja: ')
    br_igracevog_polja=input()
    while grid[br_igracevog_polja]!='':
        print('Unesite polje ponovo: ')
        br_igracevog_polja=input()
          
    grid[br_igracevog_polja]=na_potezu 
    br_poteza+=1
    
    if br_poteza==15:
        print('Nema pobjednika')
        grid = {'0':'', '1':'', '2':'', '3':'',
                '4':'', '5':'', '6':'', '7':'',
                '8':'', '9':'', '10':'', '11':'',
                '12':'', '13':'', '14':'', '15':''}
    elif check_winner(grid):
        print('Pobjednik je:',na_potezu)
        grid = {'0':'', '1':'', '2':'', '3':'',
                '4':'', '5':'', '6':'', '7':'',
                '8':'', '9':'', '10':'', '11':'',
                '12':'', '13':'', '14':'', '15':''}
    if na_potezu=='X':
        na_potezu='O'
    else:
        na_potezu='X'
    





