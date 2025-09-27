
def is_par(numero):
    return numero % 2 == 0

def list_par_impar(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if is_par(numero):
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

def solicitar_numeros(quantidade, min=1, max=500):
    numeros = []
    
    while len(numeros)<quantidade:
        quant_num = len(numeros)
        valor_digitado = int(input(f"({quant_num+1}) Digite um numero de {min} a {max}: "))
        if valor_digitado >= min and valor_digitado <= max:
            numeros.append(valor_digitado)
        else:
            print("Numero Inválido, por favor digite um numero entre 1 a 500")
    
    return numeros

numeros = solicitar_numeros(2, 10, 50)

pares, impares = list_par_impar(numeros)

print("Lista total: ", numeros)
print("Lista pares: ", pares)
print("Lista impares: ", impares)


