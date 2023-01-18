# Theoretische Informatica
# TINPRO01-6-opdracht2-opgave6
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Blidt, Thijs Dregmans
# 05-11-2022

'''
6
Leidt een recurrente betrekking af voor de
berekening van x^p, waarbij x een reëel getal
en p een natuurlijk getal is van n bits.
Maak hiervan een recursief algoritme.

'''

def opgave6(x, p):
    if p >= 1:
        return x * opgave6(x, p-1)
    else:
        return 1


print(opgave6(3,3))

