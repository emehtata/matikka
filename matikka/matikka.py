#!/usr/bin/env python3

import logging
from .my_maths import arvo
from .my_maths import laskut

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    MAX_TRY=3
    o_count=0
    laskettu=0
    TOTAL=10
    for i in range(0,TOTAL):
        luvut = arvo.arvo_luvut()
        tulo = laskut.laske_tulo(luvut)
        summa = laskut.laske_summa(luvut)
        oikein = False
        tries = 0
        laskettu+=1

        while oikein == False and tries < MAX_TRY:
            vastaus = laskut.kysymys(luvut, "x")
            if vastaus == tulo:
                print("Oikein! :)\n")
                oikein = True
                o_count+=1
                continue
            elif abs(vastaus-tulo) < 5:
                print("Lähellä")
            else:
                print("Ei :(")
            tries+=1
            print(f"Yrityksiä jäljellä vielä {MAX_TRY-tries}/{MAX_TRY}\n")
        else:
            if oikein == False:
                print(f"Nyt ei tullut oikeaa vastausta {MAX_TRY} yritykselläkään. :((((\n")

        print(f"Oikeat vastaukset: {o_count}/{laskettu}\n")

if __name__ == '__main__':
    matikka()