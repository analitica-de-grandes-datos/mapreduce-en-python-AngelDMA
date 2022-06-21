#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys
import operator

orden = []

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
        key, date, val = line.split("\t")
        val = int(val)
        orden.append((key, date, val))

    orden = sorted(orden, key=operator.itemgetter(0, 2))

    for line in orden:
        sys.stdout.write("{}\t{}\t{}\n".format(line[0], line[1], line[2]))
