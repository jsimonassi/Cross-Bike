from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sound import *
import personagem
import abertura
import menu
import obstaculos
import score
import Ranking

janela = Window(1300, 700)
janela.set_title("Cross Bike")

musica = Sound("inicio.ogg")
musica.play()

abertura.abertura_producao(janela)
abertura.abertura_jogo(janela)
x = 0
queda = False
primeiraVez = True

def perdeu(janela):
    hold = 0
    fundo = GameImage("imagens/gameover.png")

    while(hold < 5):
        hold += janela.delta_time()
        fundo.draw()
        janela.update()

def prepara(janela):
    fundo = GameImage("imagens/contador.jpg")
    fundo.set_position(380, 130)

    contagem = 3
    hold = 0

    while(contagem > 0):
        hold += janela.delta_time()
        if hold > 1:
            contagem -= 1
            hold = 0

        fundo.draw()
        janela.draw_text(str(contagem), 550, 200, size= 180, color=(255, 255, 0), font_name="Purisa", bold=True, italic=False)
        janela.update()

    return

def game(janela):
    velocidade = -1
    principal = personagem.cria()
    Xp = principal.width + 120
    Yp = principal.height + 440
    flagPulo = False
    minutos = 0
    segundos = 30
    milisegundos = 60
    acabou = False
    global x
    faleceu = False


    #Variáveis do scrolling da tela (NÃO MUDAR PQ DEU MUITO TRABALHO)
    fundo1 = GameImage("imagens/fundo_L.jpg")
    fundo1.x = 327
    fundo2 = GameImage("imagens/fundo_R.jpg")
    fundo2.x = fundo1.x + fundo1.width
    fundo3 = GameImage("imagens/fundo_L.jpg")
    fundo3.x = fundo2.x + fundo2.width
    fundo4 = GameImage("imagens/fundo_R.jpg")
    fundo4.x = fundo3.x + fundo3.width
    aux = GameImage("imagens/fundo_R.jpg")
    aux.x = -646

    rampa, carro, tijolo, rampa2, carro2, tijolo2, espinho, fim = obstaculos.cria_obstaculo()


    def scrolling(velfundo, deltatime):

        #O fundo muda conforme a velocidade do personagem
        #Faz a imagem ir da direita para esquerda
        velfundo = velfundo * 2
        fundo1.x -= velfundo * deltatime
        fundo2.x -= velfundo * deltatime
        fundo3.x -= velfundo * deltatime
        fundo4.x -= velfundo * deltatime

        #Primeiro pedaço de imagem de 327px
        if (aux.x + aux.width) >= 0:
            aux.x -= velfundo * deltatime
            aux.draw()
        #A imagem é menor que a resolução do jogo, então fiz uma composição de 4 imagens para compensar
        if(fundo1.x + fundo1.width) <= 0:
            fundo1.x = fundo4.x + fundo4.width
        if(fundo2.x + fundo2.width) <= 0:
            fundo2.x = fundo1.x + fundo1.width
        if(fundo3.x + fundo3.width) <= 0:
            fundo3.x = fundo2.x + fundo2.width
        if(fundo4.x + fundo4.width) <= 0:
            fundo4.x = fundo3.x + fundo3.width

        #Desenha a porra toda
        fundo1.draw()
        fundo2.draw()
        fundo3.draw()
        fundo4.draw()

    #Game Loop
    while (True):
        global queda
        milisegundos -= 1
        if milisegundos < 0:
            segundos -= 1
            milisegundos = 60
        if segundos <= 0:
            perdeu(janela)
            return

        if faleceu:
            perdeu(janela)
            return


        deltatime = janela.delta_time() #É mais eficiente fazer isso do que chamar a função toda hora

        scrolling(velocidade, deltatime)#Chama a função passando a velocidade do personagem como parâmetro

        velocidade, Xp, Yp, principal, flagPulo = personagem.movimenta(principal, velocidade, deltatime, Xp, Yp, flagPulo)

        rampa, carro, tijolo, rampa2, carro2, tijolo2, espinho, fim = obstaculos.atualiza_posicao(rampa, carro, tijolo, rampa2, carro2, tijolo2, espinho, fim, velocidade, deltatime)

        Xp, Yp, velocidade, principal.x, acabou, faleceu = personagem.colisao(rampa, carro, tijolo, tijolo2, rampa2, carro2, espinho, fim, principal, Xp, Yp, deltatime, velocidade, acabou)

        x = (score.score(rampa.x, carro.x, tijolo.x, rampa2.x, carro2.x, tijolo2.x, principal.x)) * segundos


        janela.draw_text(("Tempo: "), 20, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold = True, italic = False)
        janela.draw_text(str(minutos), 135, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text((":"), 150, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text(str(segundos), 165, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text((":"), 200, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text(str(milisegundos), 210, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold=True, italic=False)
        janela.draw_text(("Score: "), 1100, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold = True, italic = False)
        janela.draw_text((str(x)), 1200, 20, size=26, color=(255, 0, 0), font_name="Purisa", bold=True, italic=False)

        if acabou:
            break

        principal.draw()
        janela.update()

        global primeiraVez
        if primeiraVez:
            primeiraVez = False
            prepara(janela)


while(True):
    opcao = menu.menu(janela)

    if opcao == 0:
        game(janela)
        Ranking.SalvaRanking(x, janela)

    elif opcao == 1:
        Ranking.ExibeRanking(janela)

    janela.update()


