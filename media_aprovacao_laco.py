for i in range(13):
    print("Estamos no Aluno", i+1)
    carga_horaria_atual = 80

    media = float(input("Digite a sua média(entre 0 e 10): "))
    #while media >= 0 or media <= 10
    while media < 0 or media > 10:
        print("Média inválida. Digite um valor entre 0 e 10.")
        media = float(input("Digite a sua média(entre 0 e 10): "))

    if media >= 7:
        print("Parabens, vc foi aprovado!!!")
        #carga_horaria = carga_horaria + 1
        carga_horaria_atual += 1
        if carga_horaria_atual == 100:
            print("Parabéns, vc concluiu o curso")
        else:
            carga_horaria_faltante = 100 - carga_horaria_atual
            print("Você falta", carga_horaria_faltante,"% para finalizar o curso")
    elif media >= 4 and media < 7:
        print("Vc foi para a final")
    else:
        print("Infelizmente não foi dessa vez, estude um pouco mais")

print("Finalizamos o codigo")
