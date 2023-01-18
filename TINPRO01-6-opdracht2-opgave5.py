# Theoretische Informatica
# TINPRO01-6-opdracht2-opgave5
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Bildt, Thijs Dregmans
# 10-01-2023

'''
5
Leidt een recurrente betrekking af voor een vermenigvuldiging
van twee n-bit natuurlijke getallen x en y. Maak hiervan een
recursief algoritme.

Bepaal tevens de tijdcomplexiteit van
dit algoritme. Wij mogen veronderstellen dat voor het betrokken
processortype, het vermenigvuldigen en delen O(n^2) instructies
zijn. Daarentegen zijn optellen, aftrekken en 1-bits
schuifacties O(n) instructies. Het testen of een natuurlijk
getal even-of oneven is, is zoals alle overige instructies atomair O(1).
'''

def opgave5(x, y):
    if x >= 1:
        return y + opgave5(x-1, y)
    else:
        return 0


print(opgave5(13,8))
