from PPlay.sprite import *
from PPlay.window import *
import math

sobe = False

def cria():
    #principal = Sprite("imagens/empina/empina_animado.png", 17)
    principal = Sprite("imagens/personagem_animado.png", 2)
    principal.set_position(120, 440)
    #principal.set_total_duration(500)
    return principal

#***********************************************************************************************************************
def mede_angulo(Xp,Yp,principal): #Calcula a inclinação da moto em relação ao chão. Tá empinando quanto?

    Xa = 120 #X do canto inferior esquerdo
    Xb = principal.width + 120 #X do canto inferior direito
    Yb = principal.height + 440 #Y do canto inferior direito

    if( Xb != Xa):
        # Tangente = Cat. Oposto / Cat. Adjacente, por isso, vou dividir as duas distâncias
        tangente = math.sqrt(((Xb-Xp)**2) + ((Yb - Yp)**2)) / (Xb - Xa)  #Não preciso fazer pra y, pois as coordenadas serão sempre iguais
        angulo = math.atan(tangente) #Acha o angulo em Rad
        angulo = math.degrees(angulo) #Passa de Rad / Graus


        return angulo

    return 90 #Se Xb == Xa, significa que o angulo é 90


#***********************************************************************************************************************
def alteraSprite(angulo, principal):  #Muda o Sprite em relação ao angulo

    auxX = principal.x
    auxY = principal.y

    if angulo > 2:
        #principal.set_sequence(2, 2, loop=True)
        principal = Sprite("imagens/empina/1.png")
        if angulo > 5:
            #principal.set_sequence(3, 3, loop=True)
            principal = Sprite("imagens/empina/2.png")
            if angulo > 7:
                #principal.set_sequence(4, 4, loop=True)
                principal = Sprite("imagens/empina/3.png")
                if angulo > 10:
                    #principal.set_sequence(5, 5, loop=True)
                    principal = Sprite("imagens/empina/4.png")
                    if angulo > 12:
                        #principal.set_sequence(6, 6, loop=True)
                        principal = Sprite("imagens/empina/5.png")
                        if angulo > 15:
                            #principal.set_sequence(7, 7, loop=True)
                            principal = Sprite("imagens/empina/6.png")
                            if angulo > 17:
                                #principal.set_sequence(8, 8, loop=True)
                                principal = Sprite("imagens/empina/7.png")
                                if angulo > 20:
                                    #principal.set_sequence(9, 9, loop=True)
                                    principal = Sprite("imagens/empina/8.png")
                                    if angulo > 23:
                                        #principal.set_sequence(10, 10, loop=True)
                                        principal = Sprite("imagens/empina/9.png")
                                        if angulo > 25:
                                            #principal.set_sequence(11, 11, loop=True)
                                            principal = Sprite("imagens/empina/10.png")
                                            if angulo > 28:
                                                #principal.set_sequence(12, 12, loop=True)
                                                principal = Sprite("imagens/empina/11.png")
                                                if angulo > 31:
                                                    #principal.set_sequence(13, 13, loop=True)
                                                    principal = Sprite("imagens/empina/11.png")
                                                    if angulo > 33:
                                                        #principal.set_sequence(14, 14, loop=True)
                                                        principal = Sprite("imagens/empina/12.png")
                                                        if angulo > 38:
                                                            #principal.set_sequence(15, 15, loop=True)
                                                            principal = Sprite("imagens/empina/13.png")
                                                            if angulo > 45:
                                                                #principal.set_sequence(16, 16, loop=True)
                                                                principal = Sprite("imagens/empina/14.png")
                                                                if angulo > 50:
                                                                    #principal.set_sequence(16, 16, loop=True)
                                                                    principal = Sprite("imagens/empina/15.png")

                                                                    if angulo > 55:
                                                                        #principal.set_sequence(3, 3, loop=True)
                                                                        principal = Sprite("imagens/empina/16.png")


    else: #MUITO INEFICIENTE
       principal = Sprite("imagens/personagemAnimado.png", 2)
       principal.set_position(auxX, auxY)
       principal.set_total_duration(500)
       #principal.set_sequence(1, 1, loop=True)
       return principal

    principal.set_position(auxX, auxY)

    return principal

#***********************************************************************************************************************
def movimenta(principal, velocidade, deltatime, Xp, Yp, flagPulo):
    teclado = Window.get_keyboard()

    global paraDeVoltar

    if (teclado.key_pressed("RIGHT")) and principal.x < 1000:#Acelera a hornet
        principal.x += velocidade * deltatime
        if velocidade < 300:
            velocidade += 10

    elif (velocidade >= 0): #Negativa bambam!
        velocidade -= 100 * deltatime
        if principal.x > 10: # Pra não passar da tela no lado esquerdo
            principal.x -= 150 * deltatime

    if (teclado.key_pressed("LEFT")) and velocidade > 0: #Freia
        velocidade -= 150 * deltatime
        if principal.x > 10:  #Pra não passar da tela no lado esquerdo
            principal.x -= 200 * deltatime

    if (teclado.key_pressed("SPACE")) and principal.y >= 340:
        flagPulo = True
    if(flagPulo):
        principal.y -= 600 * deltatime
        if(principal.y < 250):
            flagPulo = False

    elif((not flagPulo) and principal.y < 440): #Gravidade
        principal.y += 500 * deltatime


    angulo = mede_angulo(Xp, Yp, principal)

    if (teclado.key_pressed("UP") and velocidade > 0):
        Yp -= 0.1 + (velocidade * deltatime)
        Xp -= 0.1 + (velocidade * deltatime)

    elif(Yp < principal.height + 440): #Yp < Xb
        if(teclado.key_pressed("DOWN")):
            Yp += 5 + (velocidade * deltatime)
            Xp += 5 + (velocidade * deltatime)
        elif(velocidade < 50):
            Yp += 1 + (velocidade + 100 * deltatime)
            Xp += 1 + (velocidade + 100  * deltatime)
        else:
            Yp += 1 + (velocidade * deltatime)
            Xp += 1 + (velocidade * deltatime)

    if angulo!= 0 or principal.y < 400:
        principal = alteraSprite(angulo, principal)
    """
    if velocidade > 0 and angulo == 0: #Roda a roda se a moto estiver andando
        principal.update()
    """

    return velocidade, Xp, Yp, principal, flagPulo


def colisao(rampa, carro, tijolo, tijolo2, rampa2, carro2, espinho, fim, principal, Xp, Yp, deltatime, velocidade, acabou):
    global sobe
    global paraDeVoltar
    faleceu = False

    if 0 < rampa.x < 1300: #Tá na tela
        if (principal.x + principal.width) > rampa.x + 50:
            Xp = principal.width + 50
            Yp = principal.height + 400
            principal.y -= 50 * deltatime
            sobe = True

    if sobe:
        principal.y -= (velocidade * 2) * deltatime
        if principal.y < 250 or velocidade < 90:
            sobe = False
            Xp = principal.width + 120
            Yp = principal.height + 440

    if 0 < carro.x < 1300:
        if principal.y + principal.height > 600:
            if carro.x < (principal.x + principal.width) < carro.x + 100:
                velocidade = -velocidade

    if 0 < tijolo.x < 1300:
        if principal.y + principal.height > 600:
            if tijolo.x < (principal.x + principal.width) < tijolo.x + 20:
                velocidade = -velocidade

    if 0 < tijolo2.x < 1300:
        if principal.y + principal.height > 600:
            if tijolo2.x < (principal.x + principal.width) < tijolo2.x + 20:
                velocidade = -velocidade

    if 0 < rampa2.x < 1300: #Tá na tela
        if (principal.x + principal.width) > rampa2.x + 100:
            Xp = principal.width + 50
            Yp = principal.height + 400
            principal.y -= 50 * deltatime
            sobe = True

        elif (principal.x + principal.width) > rampa2.x + 200:
            principal.y -= 30 * deltatime
            sobe = True

        elif (principal.x + principal.width) > rampa2.x + 300:
            principal.y -= 50 * deltatime
            sobe = True

    if sobe:
        principal.y -= (velocidade * 2) * deltatime
        if principal.y < 250 or velocidade < 90:
            sobe = False
            Xp = principal.width + 120
            Yp = principal.height + 440

    if 0 < carro2.x < 1300:
        if principal.y + principal.height > 600:
            if carro2.x < (principal.x + principal.width) < carro2.x + 100:
                velocidade = -velocidade

    if 0 < espinho.x < 1300: #Tá na tela
        if (principal.x + principal.width) > espinho.x + 50:
            Xp = principal.width + 50
            Yp = principal.height + 400
            principal.y -= 50 * deltatime
            sobe = True

        if((principal.x + principal.width) > espinho.x + 370) and ((principal.x + principal.width) < espinho.x + 900):
            if principal.y + principal.height > 450:
                faleceu = True

    if  principal.x > fim.x:
        acabou = True

    return Xp, Yp, velocidade, principal.x, acabou, faleceu
