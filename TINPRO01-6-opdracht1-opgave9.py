# Theoretische Informatica
# TINPRO01-6-opdracht1-opgave9
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Blidt, Thijs Dregmans
# 26-11-2022

'''
9a
Schrijf een functie met parameter n die de volgende berekening uitvoert:

Som k=n k=1 (2k - 1)

9b
Test je functie met verschillende waarden voor n.

9c
Schrijf een efficiëntere versie van deze functie en bewijs dat de efficiëntere versie
altijd hetzelfde antwoord oplevert als de oorspronkelijke versie.

9d
Geef de herhalingsfrequentie en complexiteitsontwikkeling van beide functies.

'''

# opgave 9a
def function9a(n):
    som = 0
    for k in range(1, n+1):
        som += (2 * k) - 1
    return som

# opgave 9b
for x in range(1,6):
    print('function9a(',x,') =', function9a(x))
    

# opgave 9c
def function9c(n):
    return n ** 2

# check 9c
for x in range(1,6):
    print('function9c(',x,') =', function9c(x))


