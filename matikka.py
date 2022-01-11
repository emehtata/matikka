#!/usr/bin/env python3

import logging
import arvo
import laskut
from random import randint as randint

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    luvut = arvo.arvo_luvut()
    tulos = laskut.laske_tulo(luvut)
    summa = laskut.laske_summa(luvut)
    oikein = False

    while oikein == False:
        vastaus = laskut.kysymys(luvut, "x")
        if vastaus == tulos:
            print("Oikein! :)")
            oikein = True
            continue
        elif abs(vastaus-tulos) < 5:
            print("Lähellä")
        else:
            print("Ei :(")

        print("Yritä uudelleen!\n")
