from PPlay.gameimage import *

def abertura_producao(janela):
    cont = 0
    fundo = GameImage("imagens/abertura/abertura100.jpg")


    while(cont <= 300):
        cont += 1
        fundo.draw()
        janela.update()


def abertura_jogo(janela):
    cont = 0
    fundo = GameImage("imagens/abertura/wallpaper100.jpg")
    fundo.draw()

    while(cont <= 300):
        cont += 1
        fundo.draw()
        janela.update()