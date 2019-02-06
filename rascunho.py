from random import choice

tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
posicoes = (11, 12, 13, 21, 22, 23, 31, 32, 33)


def bot():
    jogada_bot = choice(posicoes)
    l = jogada_bot // 10 - 1
    c = jogada_bot % 10 - 1
    if tabuleiro[l][c] == 0:
        tabuleiro[l][c] = -1
        print(tabuleiro)
    else:
        bot()


for c in range(9):
    bot()
