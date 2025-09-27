#import my_functions
#from my_functions import solicitar_numeros, list_par_impar
from my_functions import *

if __name__ == "__main__":
    numeros = solicitar_numeros(2, 10, 50)

    pares, impares = list_par_impar(numeros)

    print("Lista total: ", numeros)
    print("Lista pares: ", pares)
    print("Lista impares: ", impares)
