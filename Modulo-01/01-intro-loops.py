#primeiro código

print("Hello World!!!")
print(82375639)

#um pouco da sintaxe

# Este é o comentário de uma unica linha usando '#'

"""
este é um comentario
de várias linhas
"""
#2. Noções básicas de Python

"""
Inteiros (int)
Os números inteiros são aqueles que não têm parte decimal.
Em Python, são representados simplesmente escrevendo
o número sem aspas nem pontos decimais. Por exemplo:
"""

idade = 20
quantidade = 200

"""
Flutuantes (float)
Os números flutuantes, também conhecidos como números de ponto flutuante, são aqueles que têm uma parte decimal.
Em Python, são representados utilizando um ponto para separar a parte inteira da parte decimal. Por exemplo:
"""

preço = 9.99
altura = 1.85

"""
Cadeias de texto (strings)
As cadeias de texto, ou simplesmente cadeias, são sequências de caracteres
encerradas entre aspas simples ('...') ou duplas ("..."). São utilizadas
para representar texto em Python. Por exemplo:
"""

nome = "Arthur"
mensagem = "Olá mundo"

print(f"{nome}")

ano = 2028

#3. Estruturas de controle

"""if ano < 2023:
    print("O ana é menor que 2023")
elif ano >= 2023 and ano < 60:
    print("Ano maior ou igual a 2023 e menor que 60")
elif ano > 2025:
    print("O ano é maior que 2025")
elif ano == 2050:
    print("Ano é igual a 2050")
else:
    print("O ano é 2028")"""

#3.1 LOOPS

#For

#fruta = "maçã", "banana", "laranja"
"""
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)"""



#WHILE

"""
contador = 0
while contador < 5:
    print(contador)
    contador += 1
"""
#alguns exemplos:

"""print("Número de 1 a 5 multiplicados por 2 com for")
for numero in range(1,6):
    print(numero * 2)

print("Número de 1 a 5 multiplicados por 2 com while")
contador = 1
while contador <= 5:
    print(contador * 2)
    contador +=1"""


"""
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
"""
