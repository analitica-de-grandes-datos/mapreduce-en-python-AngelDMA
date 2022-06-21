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

    orden = sorted(orden, key=operator.itemgetter(2))

    for i in range(0, 6):
        sys.stdout.write("{}   {}   {}\n".format(
            orden[i][0], orden[i][1], orden[i][2]))
