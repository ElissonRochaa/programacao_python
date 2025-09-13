#print() -> imprimir algo na tela
#input() -> Solicitar informacoes
#int() -> float() -> str()

#por padrão o input sempre será texto
nome = input("Digite o nome do usuario: ")

print("Seja bem-vindo", nome)

#################### Forma 1:

# primeiro_numero = input("Digite o primeiro numero: ") #"50"
# segundo_numero = input("Digite o segundo numero: ")

# primeiro_numero_inteiro = int(primeiro_numero)
# segundo_numero_inteiro = int(segundo_numero)

# soma = primeiro_numero_inteiro + segundo_numero_inteiro

#################### Forma 2:
# primeiro_numero = input("Digite o primeiro numero: ") #"50"
# segundo_numero = input("Digite o segundo numero: ")

# primeiro_numero = int(primeiro_numero)
# segundo_numero = int(segundo_numero)

# soma = primeiro_numero + segundo_numero

#################### Forma 3:
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

#soma -> +
soma = primeiro_numero + segundo_numero
#subtracao -> -
subtracao = primeiro_numero - segundo_numero
#multiplicacao -> *
multiplicacao = primeiro_numero * segundo_numero
#divisao -> /
divisao = primeiro_numero / segundo_numero
#divisao inteira -> //
divisao_inteira = primeiro_numero // segundo_numero
#resto -> %
resto = primeiro_numero % segundo_numero
#Exponenciacao -> ** -> 2^3 -> 8 
exp = primeiro_numero ** segundo_numero

print("Olá", nome, "o soma dos numeros digitados é", soma, sep="===")
soma += 5 # soma = soma + 5
print("Olá", nome, "o soma dos numeros digitados é", soma)
print("Olá", nome, "o subtracao dos numeros digitados é", subtracao)
print("Olá", nome, "o multiplicacao dos numeros digitados é", multiplicacao)
print("Olá", nome, "o divisao dos numeros digitados é", divisao)
print("Olá", nome, "o divisao inteira dos numeros digitados é", divisao_inteira)
print("Olá", nome, "o resto div dos numeros digitados é", resto)
print("Olá", nome, "o expon dos numeros digitados é", exp)



