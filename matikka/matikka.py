#!/usr/bin/env python3

import logging
import sys
import argparse
import random

from .my_maths import arvo, laskut

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

def parse_options():
    parser = argparse.ArgumentParser(description='Laskutehtävien valinnat.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='Käytä aina tätä lukua, esim. kertotaulu.')
    parser.add_argument('--summa', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

def laskukoe():
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

def kertotaulu():
    o_total=0
    k_total=0
    if len(sys.argv) > 1:
        kertoja=int(sys.argv[1])
    else:
        print(f"{sys.argv[0]} kertoja")
        sys.exit(0)

    taulu = arvo.tee_kertotaulu(kertoja)

    while len(taulu) > 0:
        print("-"*40)
        k_total+=1
        print(f"Kysymyksiä jäljellä: {len(taulu)}")
        r=random.randint(0,len(taulu)-1)
        tulo = laskut.laske_tulo(taulu[r])
        vastaus = laskut.kysymys(taulu[r], "x")
        if vastaus == tulo:
            print("\nOikein! :)")
            taulu.pop(r)
            logging.debug(f"{taulu}")
            o_total+=1
            continue
        else:
            print("Ei :(")
    
    print("-"*40)
    print(f"Oikeat vastaukset: {o_total}/{k_total}")
    print("-"*40)

    arvosana = laskut.laske_kouluarvosana(o_total/k_total*6+4)
    print(f"Tulos: {arvosana}")

def main():
    kertotaulu()

if __name__ == '__main__':
    main()
