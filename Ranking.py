from PPlay.gameimage import *
from PPlay.window import *
import menu

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def ExibeRanking(janela):
    mouse = Window.get_mouse()

    voltaOff = GameImage("imagens/ranking/voltaOff.jpg")
    voltaOff.set_position(1000, 100)

    voltaOn = GameImage("imagens/ranking/voltaOn.jpg")
    voltaOn.set_position(1000, 100)

    while(True):

        fundo = GameImage("imagens/ranking/fundoRanking.jpg")
        fundo.draw()
        dic = {}
        y = 200
        igual = 1

        voltaOff.draw()

        if mouse.is_over_object(voltaOff) or mouse.is_over_object(voltaOn):
            voltaOn.draw()
            if mouse.is_button_pressed(1):
                return

        arq = open('lista_ranking.txt', 'r')
        texto = arq.readlines()

        for linha in texto:
            nome, pontos = linha.split(" ")
            pontos = int(pontos)
            print(type(pontos))
            if (nome in dic):
                nome = nome + str(igual)
                igual += 1

            dic[nome] = pontos

        for item in sorted(dic, key=dic.get, reverse=True):
            print(dic[item])
            janela.draw_text((item), 150, y, size=28, color=(255, 255, 0), font_name="Purisa", bold=True, italic=False)
            janela.draw_text(str(dic[item]), 280, y, size=28, color=(255, 255, 0), font_name="Purisa", bold=True, italic=False)
            y += 40

        arq.close()


        janela.update()


def SalvaRanking(score, janela):
    mouse = Window.get_mouse()
    fundo = GameImage("imagens/ranking/fundo_salvaponto.png")
    fundo.set_position(340, 130)
    global alfabeto

    fundo = GameImage("imagens/ranking/fundo_salvaponto.png")
    fundo.set_position(340, 130)

    upOff0 = GameImage("imagens/ranking/upOff.png")
    upOff0.set_position(400,280)

    upOn0 = GameImage("imagens/ranking/upOn.png")
    upOn0.set_position(400,280)

    upOff1 = GameImage("imagens/ranking/upOff.png")
    upOff1.set_position(485,280)

    upOn1 = GameImage("imagens/ranking/upOn.png")
    upOn1.set_position(485,280)

    upOff2 = GameImage("imagens/ranking/upOff.png")
    upOff2.set_position(570,280)

    upOn2 = GameImage("imagens/ranking/upOn.png")
    upOn2.set_position(570,280)

    downOff0 = GameImage("imagens/ranking/downOff.png")
    downOff0.set_position(400, 410)

    downOn0 = GameImage("imagens/ranking/downOn.png")
    downOn0.set_position(400,410)

    downOff1 = GameImage("imagens/ranking/downOff.png")
    downOff1.set_position(485,410)

    downOn1 = GameImage("imagens/ranking/downOn.png")
    downOn1.set_position(485,410)

    downOff2 = GameImage("imagens/ranking/downOff.png")
    downOff2.set_position(570,410)

    downOn2 = GameImage("imagens/ranking/downOn.png")
    downOn2.set_position(570,410)

    salvarOff = GameImage("imagens/ranking/salvarOff.jpg")
    salvarOff.set_position(800, 480)

    salvarOn = GameImage("imagens/ranking/salvarOn.jpg")
    salvarOn.set_position(800, 480)

    i = 0
    j = 0
    k = 0
    time_hold = 0
    while(True):
        time_hold += 10 * janela.delta_time()

        fundo.draw()

        upOff0.draw()
        upOff1.draw()
        upOff2.draw()
        downOff0.draw()
        downOff1.draw()
        downOff2.draw()
        salvarOff.draw()

        if (mouse.is_over_object(upOn0) or mouse.is_over_object(upOff0)) and time_hold > 2:
            upOn0.draw()
            if mouse.is_button_pressed(1):
                if i > 0:
                    i-=1
                time_hold = 0


        elif (mouse.is_over_object(upOn1) or mouse.is_over_object(upOff1)) and time_hold > 2:
            upOn1.draw()
            if mouse.is_button_pressed(1):
                if j > 0:
                    j -= 1
                time_hold = 0

        elif (mouse.is_over_object(upOn2) or mouse.is_over_object(upOff2)) and time_hold > 2:
            upOn2.draw()
            if mouse.is_button_pressed(1):
                if k > 0:
                    k -= 1
                time_hold = 0

        elif (mouse.is_over_object(downOff0) or mouse.is_over_object(downOn0)) and time_hold > 2:
            downOn0.draw()
            if mouse.is_button_pressed(1):
                i += 1
                if i > 25:
                    i = 0
                time_hold = 0

        elif (mouse.is_over_object(downOff1) or mouse.is_over_object(downOn1)) and time_hold > 2:
            downOn1.draw()
            if mouse.is_button_pressed(1):
                j += 1
                if j > 25:
                    j = 0
                time_hold = 0

        elif (mouse.is_over_object(downOff2) or mouse.is_over_object(downOn2)) and time_hold > 2:
            downOn2.draw()
            if mouse.is_button_pressed(1):
                k += 1
                if k > 25:
                    k = 0
                time_hold = 0

        elif (mouse.is_over_object(salvarOff) or mouse.is_over_object(salvarOn)) and time_hold > 3:
            salvarOn.draw()
            if mouse.is_button_pressed(1):
                arq = open('lista_ranking.txt', 'a')
                texto = alfabeto[i]+alfabeto[j]+alfabeto[k] + " " + str(score) + "\n"
                arq.writelines(texto)
                arq.close()
                menu.menu(janela)
                return



        janela.draw_text((alfabeto[i]), 410, 350, size=35, color=(0, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text((alfabeto[j]), 495, 350, size=35, color=(0, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text((alfabeto[k]), 580, 350, size=35, color=(0, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text((str(score) + " Pontos"), 700, 350, size=32, color=(255, 255, 0), font_name="Purisa", bold=True, italic=False)
        janela.update()


    return