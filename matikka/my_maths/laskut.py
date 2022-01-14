#!/usr/bin/env python3

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def kysymys(luvut, merkki):
    logging.debug(luvut)
    retval = 0
    vast = 0
    kysymys = "Paljonko on"
    for a in luvut:
        kysymys += f" {a} {merkki}"

    kysymys = kysymys[:-1]+"? "

    tryagain = True
    while tryagain == True:
        try:
            vast = input(kysymys)
            retval = int(vast)
            tryagain = False
        except ValueError:
            print("Syötä luku")
    return retval


def laske_tulo(luvut):
    tulo = 1
    for a in luvut:
        tulo = tulo*a
    return tulo


def laske_erotus(luvut):
    erotus = luvut[0]
    luvut.pop(0)
    for a in luvut:
        erotus = erotus - a
    return erotus


def laske_summa(luvut):
    summa = 0
    for a in luvut:
        summa += a

    return summa

def laske_kouluarvosana(desimaali):
    koko = int(desimaali)
    desi = desimaali-koko
    merkki = ""

    if desi > .75:
        merkki = "-"
        koko +- 1
    elif desi > .5:
        merkki = "½"
    elif desi > .25:
        merkki = "+"

    return f"{koko}{merkki}"