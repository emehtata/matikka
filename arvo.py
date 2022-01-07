import logging
from random import randint as randint

def arvo_luvut(min=1, max=10, n=2):
    luvut=[]
    tulo=1
    for a in range(0,2):
        r=randint(min,max+1)
        logging.debug("{}: {}".format(a, r))
        luvut.append(r)
        tulo=tulo*r

    logging.debug("{} = {}".format(luvut, tulo))

    return luvut    