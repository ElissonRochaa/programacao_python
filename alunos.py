#### Tipos de Dados
## Texto -> String
## Inteiro -> int
## Real -> float double
## Binario -> Booleano

###Estruturas de Dados
##Lista!!!!

quantidade = int(input("Digite quantos alunos vc quer cadastrar: "))

alunos = []
for i in range(quantidade):
    nome = input("Digite o nome do "+ str(i+1) + " aluno: ")
    alunos.append(nome)
    #alunos.append(input("Digite o nome do "+ str(i+1) + " aluno: "))

for i in range(len(alunos)):
    print("Seja bem-vindo", alunos[i])

for aluno in alunos:
    print("Seja bem-vindo", aluno)


## NÃo façam assim!!!!
#primeiro_aluno = input("Digite o nome do 1o aluno: ")
# segundo_aluno = input("Digite o nome do 2o aluno: ")
# terceiro_aluno = input("Digite o nome do 3o aluno: ")
# quarto_aluno = input("Digite o nome do 4o aluno: ")
# quinta_aluno = input("Digite o nome do 5o aluno: ")

# print("Sejam bem-vindos,", primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno, quinta_aluno)