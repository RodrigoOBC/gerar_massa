import numpy as np
import random as rd
from pip._vendor.msgpack.fallback import xrange


class gerador:

    def __init__(self):
        pass

    def cpf_funcional(self) -> str:
        n = [rd.randrange(10) for i in xrange(9)]

        # calcula digito 1 e acrescenta ao numero
        s = sum(x * y for x, y in zip(n, range(10, 1, -1)))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)

        # calcula digito 2 e acrescenta ao numero
        s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)

        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)

    def cnpj_funcional(self,  punctuation = False) -> str:
        n = [rd.randrange(10) for i in range(8)] + [0, 0, 0, 1]
        v = [i for i in range(2, 10)] + [i for i in range(2, 6)]
        # calcula dígito 1 e acrescenta ao total
        s = sum(x * y for x, y in zip(reversed(n), v))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)
        # idem para o dígito 2
        s = sum(x * y for x, y in zip(reversed(n), v))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)
        if punctuation:
            return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
        else:
            return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


if __name__ == '__main__':
    pass