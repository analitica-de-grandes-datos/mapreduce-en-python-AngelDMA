#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys

orden = []


def takeSecond(elem):
    return elem[1]


#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        orden.append((key, val))

    orden.sort(key=takeSecond)

    for line in orden:
        sys.stdout.write("{}\t{}\n".format(line[0], line[1]))
