#Variavel Local e Variavel Global

def saudacao(nome="Pessoal"):
    print(f"Olá {nome}")


def somar(num1, num2):
    #Variavel Local
    nome = "Elisson"
    idade = 18
    valor = num1 + num2
    return nome, valor

saudacao("Rodrigo")
saudacao("Douglas")
saudacao()


#Variavel Global
nome, soma = somar(5,6)
print(nome)
print(soma)
somar(5,2)
