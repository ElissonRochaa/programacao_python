#Preciso converter um valor em grau C para grau F

# 1- Receber o valor em grau C -> Criar uma variavel que contenha esse valor
C = float(input("Digite a temperatura em grau C: "))

# 2- Aplicar a formula de conversão
F = C * 1.8 + 32
#F = ((9/5) * C) + 32

# 3- Mostrar ao usuario o valor calculado
print("A temperatura", C, "em grau Celsius é", F, "em Fahrenheit")