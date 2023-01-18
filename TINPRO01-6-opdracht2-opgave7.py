# Theoretische Informatica
# TINPRO01-6-opdracht2-opgave7
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Blidt, Thijs Dregmans
# 05-12-2022

'''
7a
Schrijf een functie met parameter n die de volgende berekening uitvoert:
SOM j=n n=1 (1 / (j(j + 1)))

7b
Test je functie met verschillende waarden voor n.

7c
Schrijf een effiëntere versie van deze functie en bewijs dat de efficiëntere versie altijd
hetzelfde antwoord oplevert als de oorspronkelijke versie.

7d
Geef de herhalingsfrequentie en complexiteitsontwikkeling van beide functies

'''

# opgave 7a
def function7a(n):
    som = 0
    for j in range(1, n+1):
        som += 1 / (j * (j + 1))
    return som

# opgave 7b
for x in range(0,10):
    print('function7a(',x,') =', function7a(x))
    
# opgave 7c
def function7c(n):
    return (n)/(n+1)

# check 7c
for x in range(0,10):
    print('function7c(',x,') =', function7c(x))

