#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys
valores = []
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
        #print(",".join(map(str, valores)))

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            valores.append(val)

        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                valores.sort()
                #sys.stdout.write("{}\t{}\n".format(curkey, total))
                sys.stdout.write("{}\t{}\n".format(
                    curkey, ",".join(map(str, valores))))

            curkey = key
            valores.clear()
            valores.append(val)

    #sys.stdout.write("{}\t{}\n".format(curkey, total))
    valores.sort()
    sys.stdout.write("{}\t{}\n".format(curkey, ",".join(map(str, valores))))
