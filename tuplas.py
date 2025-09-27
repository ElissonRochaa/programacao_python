# lista é mutável
lista = []
# tupla é imutável
tupla = ()

melhores_times_pe = ("SANTA CRUZ", "NAUTICO", "RETRO", "MAGUARY", "SETE")

# list_times = list(melhores_times_pe)
# list_times.append("SPORT")

# melhores_times_pe = tuple(list_times)

# print("SPORT" in melhores_times_pe)
print(melhores_times_pe)



pessoa = ('000.000.000-00', "Beatriz Rosa", 19)
cpf, nome, idade = pessoa

print(cpf, nome, idade)

nome_completo = ("Elisson", "da", "Silva", "Oliveira", "Rocha")
primeiro_nome, *nome_do_meio, ultimo_nome = nome_completo

print(primeiro_nome, nome_do_meio, ultimo_nome)