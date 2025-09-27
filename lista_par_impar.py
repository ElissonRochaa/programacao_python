
numeros = []

# for i in range(3):
#     valor_digitado = int(input(f"({i+1}) Digite um numero de 1 a 500: "))
#     while valor_digitado < 1 or valor_digitado > 500:
#         print("Numero invalido.")
#         valor_digitado = int(input(f"({i+1}) Digite um numero de 1 a 500: "))
#     numeros.append(valor_digitado)

while len(numeros)<10:
    quant_num = len(numeros)
    valor_digitado = int(input(f"({quant_num+1}) Digite um numero de 1 a 500: "))
    if valor_digitado >= 1 and valor_digitado <= 500:
        numeros.append(valor_digitado)
    else:
        print("Numero Inválido, por favor digite um numero entre 1 a 500")


pares = []
impares = []

#for i in range(len(numeros)):
#i = 0
#while i < len(numeros):
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista total: ", numeros)
print("Lista pares: ", pares)
print("Lista impares: ", impares)








#for i in range(3):
    # print()
    # valor_digitado = int(input(f"({i+1}) Digite um numero de 1 a 500: "))
    # if valor_digitado >= 1 and valor_digitado <= 500:
    #     numeros.append(valor_digitado)
    # else:
    #     print("Numero Inválido, por favor digite um numero entre 1 a 500")