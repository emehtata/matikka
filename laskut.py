#!/usr/bin/env python3

import logging
import arvo
from random import randint as randint

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def kysymys(luvut, merkki):
    logging.debug(luvut)

    kysymys = "Paljonko on"
    for a in luvut:
        kysymys += " {} {}".format(a, merkki)

    kysymys = kysymys[:-1]+"? "
    vast = input(kysymys)
    return int(vast)


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
