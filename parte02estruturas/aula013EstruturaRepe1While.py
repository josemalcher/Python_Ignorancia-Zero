# Aulas Python - 013 - Estruturas de Repetição I: while
# https://www.youtube.com/watch?v=36uDqv17zdo&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=14


n = 10
cont = 0
while cont < n :
    print(cont)
    cont = cont + 1

"""
Faça um programa que peça dois numero, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função potencia da 
linguagem.
2**3 = 1*2*2*2 = 8 
"""

base = int(input("Digite o valor da base:_"))
expoente = int(input("Digite o valor da expoente:_"))

cont = 0
produto = 1
while cont < expoente:
    produto = produto * base
    cont = cont + 1
print(base, "elevado a", expoente, "=", produto)


"""
Dado um numero inteiro não negativo n, determine n!
5! = 5 * 4 * 3 * 2 * 1 = 120
"""

n = int(input("Digite n:_ "))

prod = n
contador = n-1
while contador > 1:
    prod = prod * contador
    contador = contador - 1
print(n, "! = ", prod)


"""
Dada uma sequencia de números inteiro não-nulos,
seguida por 0, imprimir seus quedrados
"""

n = int(input("Digite o primeiro numero:_"))
while n != 0 :
    print(n , "ao quadrado =", n * n)
    n = int(input("Digite o proximo numero:_"))

