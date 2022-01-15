import logging
from random import randint as randint

def arvo_luvut(min=1, max=10, n=2, taulu=0):
    luvut=[]
    tulo=1
    for a in range(0,2):
        r=randint(min,max)
        luvut.append(r)

    if taulu != 0:
        luvut[0] = taulu
        
    for a in luvut:        
        logging.debug("{}: {}".format(a, r))
        tulo=tulo*r

    logging.debug("{} = {}".format(luvut, tulo))

    return luvut
