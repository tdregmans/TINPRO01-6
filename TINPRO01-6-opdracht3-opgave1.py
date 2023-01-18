# Theoretische Informatica
# TINPRO01-6-opdracht3-opgave1
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Bildt, Thijs Dregmans
# 19-12-2022

# opgave 1a
def function1a(n):
    steps = 0
    while (n != 1):
        if not(n % 2):
            n = n / 2
        else:
            n = 3 * n + 1
        #print(n)
        steps += 1
    return True, steps

# opgave 1b
def function1b():
    for x in range(1, 1000+1):
        if not function1a(x)[0]:
            return False
    return True

# opgave 1c
def function1c():
    longestRowLen = 0
    longestRowN = 0
    for x in range(1, 1000+1):
        if longestRowLen < function1a(x)[1]:
            longestRowLen = function1a(x)[1]
            longestRowN = x
    return longestRowLen, longestRowN

print(function1c())
