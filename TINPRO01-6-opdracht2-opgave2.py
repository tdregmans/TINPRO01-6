# Theoretische Informatica
# TINPRO01-6-opdracht2-opgave2
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Blidt, Thijs Dregmans
# 30-11-2022

'''
2
De volgende functie berekent de faculteit van een natuurlijk getal n.
Maak een iteratieve versie van deze functie.

'''

def opgave2(n):
    som = 1
    for i in range(1, n + 1):
        som  = som * i
    return som


print(opgave2(3))
