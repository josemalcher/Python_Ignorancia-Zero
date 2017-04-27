# Aulas Python - 011 - Estrutura de Decisões II: if, elif e else
# https://www.youtube.com/watch?v=kY47B3StnWg&t=1s&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=12

"""
Faça um programa que leia um número e exiva o dia correspondente da semana.
(1-Domingo, 2-Segunda,etc), Se digitar outro valor deve aparecer 'Valor Inválido'.
"""

dia = int(input("Digite o dia da semana:_"))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("Entrada invalida")

### Faça um progama que leia três números e mostre-os em ordem decrescente

a = int(input("Digite o primeiro numero:_"))
b = int(input("Digite o segundo numero:_"))
c = int(input("Digite o terceiro numero:_"))

if a >= b >= c :
    print(a , b, c)
elif a >= c >= b:
    print(a ,c ,b)
elif b >= a >= c:
    print(b ,a ,c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c,b,a)
