# Aulas Python - 009 - Estrutura de Decisões I: if e else
# https://www.youtube.com/watch?v=cszay9XqLn0&index=10&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
from builtins import print

idade = int(input("Digite sua idade: "))

"""
resp = idade >= 18
# if resp:
if resp == True:
    print("Voce pode beber a vontade")
if resp == False:
    print("Não PODE Beber!!")
print(resp)
"""

"""
if idade >= 18:
    print("Você pode beber a vontade")
    if idade >= 21:
        print("Você é VIP")
if idade < 18:
    print("VOCE so pode beber REFRI")
"""
if idade >= 18:
    print("Você pode beber a vontade")
    if idade >= 21:
        print("Você é VIP")
else:
    print("VOCE so pode beber REFRI")


area = int(input("Digite a área "))
litros = area // 3
if area % 3 > 0:
    litros = litros + 1

latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1

print("Voce precisará de ", latas, " Latas")
print("Voce vai pagar R$", latas * 80,"reais")





