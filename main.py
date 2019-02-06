from tkinter import *
from tkinter import messagebox
# from random import choice

# Largura dos botões: 355px
# Altura dos botões: 261px

FONTE = ('Arial', '60')
FONTE2 = ('Arial', '24')
players = dict()
lScoreP1N = lScoreP2N = None

i = Tk()
i.title('Jogo da Velha')
i.geometry('1800x831')
i.wm_iconbitmap('Imagens/icone.ico')

fBase = Frame(i, width=i.winfo_width(), height=i.winfo_height(), bg='white')
fBase.place(x=0, y=0)

base = PhotoImage(file='Imagens/base.PNG')
lBase = Label(fBase, bd=0, image=base)
# lBase['image'] = base
lBase.image = base
lBase.place(relx=0.0, rely=0.0, x=78, y=5)

fPlayers = Frame(i, width=i.winfo_width(), height=i.winfo_height(), bg='white')
fPlayers.place(x=0, y=0)

lJogadores = Label(fPlayers, font=('Copperplate Gothic Bold', '44'), text='Jogadores', bg='white')
lJogadores.place(x=700, y=100)

lPlayer1 = Label(fPlayers, font=FONTE2, text='Nome do jogador 1: ', bg='white')
lPlayer1.place(x=500, y=200)
ePlayer1 = Entry(fPlayers, font=FONTE2)
i.update()
ePlayer1.place(x=lPlayer1.winfo_width()+500, y=200)

lPlayer2 = Label(fPlayers, font=FONTE2, text='Nome do jogador 2: ', bg='white')
lPlayer2.place(x=500, y=250)
ePlayer2 = Entry(fPlayers, font=FONTE2)
i.update()
ePlayer2.place(x=lPlayer2.winfo_width()+500, y=250)


def nomes():
    global fPlayers, players, lScoreP1N, lScoreP2N
    players['X'] = [ePlayer1.get().title().strip(), 0]
    players['O'] = [ePlayer2.get().title().strip(), 0]

    fPlacar = Frame(fBase, width=400, height=250, bg='light grey')
    fPlacar.place(x=1350, y=10)
    lPlacar = Label(fBase, text='PLACAR', font=('Arial', '28', 'bold'), bg='light grey')
    lPlacar.place(x=1470, y=50)

    lScoreP1 = Label(fBase, text=f'{players["X"][0]}:', font=('Arial', '24'), bg='light grey')
    lScoreP1.place(x=1400, y=130)
    lScoreP1N = Label(fBase, text=players["X"][1], font=('Arial', '24'), bg='light grey')
    i.update()
    lScoreP1N.place(x=lScoreP1.winfo_width()+1400, y=130)

    lScoreP2 = Label(fBase, text=f'{players["O"][0]}:', font=('Arial', '24'), bg='light grey')
    lScoreP2.place(x=1400, y=180)
    lScoreP2N = Label(fBase, text=players["O"][1], font=('Arial', '24'), bg='light grey')
    i.update()
    lScoreP2N.place(x=lScoreP2.winfo_width()+1400, y=180)

    fPlayers.destroy()


def restart():
    global vez, flag, tabuleiro, posicoes, lScoreP1N
    btn1['text'] = ''
    btn1['state'] = NORMAL
    btn2['text'] = ''
    btn2['state'] = NORMAL
    btn3['text'] = ''
    btn3['state'] = NORMAL
    btn4['text'] = ''
    btn4['state'] = NORMAL
    btn5['text'] = ''
    btn5['state'] = NORMAL
    btn6['text'] = ''
    btn6['state'] = NORMAL
    btn7['text'] = ''
    btn7['state'] = NORMAL
    btn8['text'] = ''
    btn8['state'] = NORMAL
    btn9['text'] = ''
    btn9['state'] = NORMAL
    vez = 1
    flag = 0
    tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    lScoreP1N['text'] = players['X'][1]
    lScoreP2N['text'] = players['O'][1]
    # posicoes = (11, 12, 13, 21, 22, 23, 31, 32, 33)


bOk = Button(fPlayers, text='OK', width=10, height=1, command=nomes, font=('Arial', '24'))
bOk.place(x=780, y=320)

tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
posicoes = (11, 12, 13, 21, 22, 23, 31, 32, 33)
botoes = [['btn1', 'btn2', 'btn3'], ['btn4', 'btn5', 'btn6'], ['btn7', 'btn8', 'btn9']]
vez = 1
flag = 0


def jogador(jogada):
    global vez, flag
    l = jogada // 10 - 1
    c = jogada % 10 - 1
    if tabuleiro[l][c] == 0:
        tabuleiro[l][c] = 1
        flag += 1
        if vez == 1:
            vez = 0
        else:
            vez = 1
        fBase.after_idle(resultado)


def resultado():
    if btn1['text'] == btn2['text'] and btn2['text'] == btn3['text'] and btn1['text'] == 'X' or \
    btn1['text'] == btn2['text'] and btn2['text'] == btn3['text'] and btn1['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn1["text"]][0]}')
        players[btn1["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn4['text'] == btn5['text'] and btn5['text'] == btn6['text'] and btn4['text'] == 'X' or \
    btn4['text'] == btn5['text'] and btn5['text'] == btn6['text'] and btn4['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn4["text"]][0]}')
        players[btn4["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn7['text'] == btn8['text'] and btn8['text'] == btn9['text'] and btn7['text'] == 'X' or \
    btn7['text'] == btn8['text'] and btn8['text'] == btn9['text'] and btn7['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn7["text"]][0]}')
        players[btn7["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn1['text'] == btn4['text'] == btn7['text'] and btn1['text'] == 'X' or\
    btn1['text'] == btn4['text'] == btn7['text'] and btn1['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn1["text"]][0]}')
        players[btn1["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn2['text'] == btn5['text'] == btn8['text'] and btn2['text'] == 'X' or\
    btn2['text'] == btn5['text'] == btn8['text'] and btn2['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn2["text"]][0]}')
        players[btn2["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn3['text'] == btn6['text'] == btn9['text'] and btn3['text'] == 'X' or\
    btn3['text'] == btn6['text'] == btn9['text'] and btn3['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn3["text"]][0]}')
        players[btn3["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn1['text'] == btn5['text'] == btn9['text'] and btn1['text'] == 'X' or\
    btn1['text'] == btn5['text'] == btn9['text'] and btn1['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn1["text"]][0]}')
        players[btn1["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif btn3['text'] == btn5['text'] == btn7['text'] and btn3['text'] == 'X' or \
    btn3['text'] == btn5['text'] == btn7['text'] and btn3['text'] == 'O':
        messagebox.showinfo('Fim de jogo!', f'Vencedor: {players[btn3["text"]][0]}')
        players[btn3["text"]][1] += 1
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()

    elif flag == 9:
        messagebox.showinfo('Fim de jogo!', 'Empate!')
        if messagebox.askyesno('Fim de jogo!', 'Gostaria de jogar novamente?'):
            restart()


def btn1():
    jogador(11)
    if vez == 0:
        btn1['text'] = 'X'
    else:
        btn1['text'] = 'O'
    btn1['state'] = DISABLED


def btn2():
    jogador(12)
    if vez == 0:
        btn2['text'] = 'X'
    else:
        btn2['text'] = 'O'
    btn2['state'] = DISABLED


def btn3():
    jogador(13)
    if vez == 0:
        btn3['text'] = 'X'
    else:
        btn3['text'] = 'O'
    btn3['state'] = DISABLED


def btn4():
    jogador(21)
    if vez == 0:
        btn4['text'] = 'X'
    else:
        btn4['text'] = 'O'
    btn4['state'] = DISABLED


def btn5():
    jogador(22)
    if vez == 0:
        btn5['text'] = 'X'
    else:
        btn5['text'] = 'O'
    btn5['state'] = DISABLED


def btn6():
    jogador(23)
    if vez == 0:
        btn6['text'] = 'X'
    else:
        btn6['text'] = 'O'
    btn6['state'] = DISABLED


def btn7():
    jogador(31)
    if vez == 0:
        btn7['text'] = 'X'
    else:
        btn7['text'] = 'O'
    btn7['state'] = DISABLED


def btn8():
    jogador(32)
    if vez == 0:
        btn8['text'] = 'X'
    else:
        btn8['text'] = 'O'
    btn8['state'] = DISABLED


def btn9():
    jogador(33)
    if vez == 0:
        btn9['text'] = 'X'
    else:
        btn9['text'] = 'O'
    btn9['state'] = DISABLED


btn1 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn1)
btn1.place(x=120, y=25)

btn2 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn2)
btn2.place(x=475, y=25)

btn3 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn3)
btn3.place(x=830, y=25)

btn4 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn4)
btn4.place(x=120, y=290)

btn5 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn5)
btn5.place(x=475, y=290)

btn6 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn6)
btn6.place(x=830, y=290)

btn7 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn7)
btn7.place(x=120, y=555)

btn8 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn8)
btn8.place(x=475, y=555)

btn9 = Button(fBase, width=7, height=2, bg='white', text='', bd=0, font=FONTE, command=btn9)
btn9.place(x=830, y=555)


i.mainloop()
