#!/usr/bin/env python3

import logging
import sys
from .my_maths import arvo
from .my_maths import laskut


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    taulu=0
    if len(sys.argv) > 1:
        taulu=int(sys.argv[1])
    MAX_TRY = 3
    o_count = 0
    laskettu = 0
    TOTAL = 10

    #    summa = laskut.laske_summa(luvut)
    #    erotus = laskut.laske_erotus(luvut)
    #    osamaara = laskut.laske_osamaara(luvut)

    for i in range(0, TOTAL):
        luvut = arvo.arvo_luvut(taulu=taulu)
        tulo = laskut.laske_tulo(luvut)
        oikein = False
        tries = 0
        laskettu += 1

        while oikein == False and tries < MAX_TRY:
            print(f"Kysymys {laskettu}/{TOTAL}")
            vastaus = laskut.kysymys(luvut, "x")
            if vastaus == tulo:
                print("\nOikein! :)")
                oikein = True
                o_count += 1
                continue
            elif abs(vastaus-tulo) < 5:
                print("Lähellä")
            else:
                print("Ei :(")
            tries += 1
            print(f"Yrityksiä jäljellä vielä {MAX_TRY-tries}/{MAX_TRY}\n")
        else:
            if oikein == False:
                print(
                    f"Nyt ei tullut oikeaa vastausta {MAX_TRY} yritykselläkään. :((((")
                print(f"Oikea vastaus olisi ollut {tulo}.\n")

        print(f"Oikeat vastaukset: {o_count}/{laskettu}")
        print("-"*40)

    arvosana = laskut.laske_kouluarvosana(o_count/laskettu*6+4)
    print(f"Tulos: {arvosana}")


if __name__ == '__main__':
    main()
