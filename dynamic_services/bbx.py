from ast import Try
import sys

import generarte_bbx


def main(argv):
    '''controla la operacion'''
    try:
        if(argv[0] == 'h'):
            print("es necesario agregar url_servicio, cantidad de la muestra, path de salida")
        else:
            info=generarte_bbx.get_service_info(argv[0])
            generarte_bbx.calculate_bbx(argv[1],info,argv[2])
    except Exception as e:
        print('valide con argumento h para saver si estan vien los parametros necesarios')
        print(e)
    finally:
        print("ejecusion finalizada!!")
    
if __name__ == "__main__":
    main(sys.argv[1:])