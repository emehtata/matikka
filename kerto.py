#!/usr/bin/env python3

import logging
import arvo
from random import randint as randint

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def kysy_tulo(luvut):
    logging.debug(luvut)

    kysymys = "Paljonko on"
    for a in luvut:
        kysymys += " {} x".format(a)

    kysymys = kysymys[:-1]+"? "
    vast = input(kysymys)
    return int(vast)


def laske_tulo(luvut):
    tulo = 1
    for a in luvut:
        tulo = tulo*a
    return tulo


if __name__ == '__main__':
    luvut = arvo.arvo_luvut()
    tulo = laske_tulo(luvut)

    oikein = False
    
    while oikein == False:
        vastaus = kysy_tulo(luvut)
        if vastaus == tulo:
            print("Oikein! :)")
            oikein = True
            continue
        elif abs(vastaus-tulo) < 5:
            print("Lähellä")
        else:
            print("Ei :(")

        print("Yritä uudelleen!\n")
