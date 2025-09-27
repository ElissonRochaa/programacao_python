
dicionario = {'chave':'valor', 'chave':'valor'}

lista = ["Elisson", 18, 1.78, True]

#Dicionario
## Valor -> Pode ser de qualquer tipo (Até as estruturas de dados que a gente estudou)
## Chave -> Varios tipos -> String(texto) ou Inteiro

alunos_dict = {
    'Elisson': ['Vanthuir', 'Beatriz', 'Kimberlly', 'Eneida'],
    'Ivaldir': ['José', 'Maria']
}

alunos = [
    {"nome": "Vanthuir", "idade": 18, "altura": 1.80, "peso":80},
    {"nome": "Maria", "idade": 20, "altura": 1.60, "peso":50}
]

aluno = {"nome": "Vanthuir", "idade": 18, "altura": 1.80, "peso":80}

print(aluno.get('nome'))
print(aluno['idade'])
print(aluno.get('salario', 0))

aluno['salario'] = 10000.00
print(aluno.get('salario', 0))
aluno['idade'] = 40

print(aluno)

#aluno.clear()
#print(aluno)

print(aluno.keys())
print(aluno.values())
print(aluno.items())

for chave in aluno.keys():
    print(chave, aluno[chave])

for valor in aluno.values():
    print(valor)

for chave, valor in aluno.items():
    print(chave, valor)


