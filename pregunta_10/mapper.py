#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

#! /usr/bin/ python3
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #

        #
        # escribe al flujo estandar de salida
        #
        val = line.split('\t')[0]
        keys = line.split('\t')[1].replace(
            '\n', '').replace('\t', '').replace(' ', '')

        for key in keys.split(','):
            sys.stdout.write("{}\t{}\n".format(key.replace('\n', ''), val))
