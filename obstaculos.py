from PPlay.window import*
from PPlay.gameimage import *


def cria_obstaculo():
    rampa = GameImage("imagens/rampa.png")
    rampa.set_position(1350, 490)
    carro = GameImage("imagens/carro1.png")
    carro.set_position(2500, 500)
    tijolo = GameImage("imagens/tijolo2.png")
    tijolo.set_position(3800, 520)
    tijolo2 = GameImage("imagens/cimento.png")
    tijolo2.set_position(4500, 530)

    rampa2 = GameImage("imagens/morro.png")
    rampa2.set_position(6000, 470)
    carro2 = GameImage("imagens/obstaculo.png") #Ficou como carro2, mas é o sprite do obstaculo
    carro2.set_position(7500, 450)
    espinho = GameImage("imagens/espinho.png")
    espinho.set_position(8500, 450)


    fim = GameImage("imagens/fim.png")
    fim.set_position(10000,470)

    return rampa, carro, tijolo, rampa2, carro2, tijolo2, espinho, fim


def atualiza_posicao(rampa, carro, tijolo, rampa2, carro2, tijolo2, espinho, fim, velocidade, deltatime):

    velocidade = velocidade * 2 #Mesma velocidae do fundo

    rampa.x -= velocidade * deltatime
    carro.x -= velocidade * deltatime
    tijolo.x -= velocidade * deltatime
    rampa2.x -= velocidade * deltatime
    carro2.x -= velocidade * deltatime
    tijolo2.x -= velocidade * deltatime
    espinho.x -= velocidade * deltatime

    fim.x -= velocidade * deltatime

    if -rampa.width < rampa.x < 1300:
        rampa.draw()
    if -carro.width < carro.x < 1300:
        carro.draw()
    if -tijolo.width < tijolo.x < 1300:
        tijolo.draw()
    if -fim.width < fim.x < 1300:
        fim.draw()
    if -rampa2.width < rampa2.x < 1300:
        rampa2.draw()
    if -carro2.width < carro2.x < 1300:
        carro2.draw()
    if -tijolo2.width < tijolo2.x < 1300:
        tijolo2.draw()
    if -espinho.width < espinho.x < 1300:
        espinho.draw()

    return rampa, carro, tijolo, rampa2, carro2, tijolo2, espinho, fim

