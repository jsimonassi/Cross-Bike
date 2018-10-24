import personagem
import abertura
import menu
import obstaculos
from PPlay.window import*
from PPlay.gameimage import *


def score(rampa, carro, tijolo, rampa2, carro2, tijolo2, principal):
    a = 0
    b = 0
    c = 0
    if principal > rampa:
        a += 10
    if principal > carro:
        b += 10
    if principal > tijolo:
        c += 10
    if principal > rampa2:
        a += 10
    if principal > carro2:
        b += 10
    if principal > tijolo2:
        c += 10
    x = a + b + c

    return x
