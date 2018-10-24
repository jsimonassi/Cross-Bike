from PPlay.gameimage import *
from PPlay.window import *

def menu(janela):

    fundo = GameImage("imagens/fundo_menu.jpg")
    opcao = GameImage("imagens/sprite.png")
    mouse = Window.get_mouse()

    while(True):
        if mouse.is_over_area([0,0],[1300,430]):
            opcao.set_position(470, 350)
            if mouse.is_button_pressed(1):
                return 0

        elif mouse.is_over_area([0,431],[1300, 550]):
            opcao.set_position(470, 450)
            if mouse.is_button_pressed(1):
                return 1
        else:
            opcao.set_position(470, 550)
            if mouse.is_button_pressed(1):
                exit()

        fundo.draw()
        opcao.draw()

        janela.update()