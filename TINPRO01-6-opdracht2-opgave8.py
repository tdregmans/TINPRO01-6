# Theoretische Informatica
# TINPRO01-6-opdracht2-opgave8
# Hidde-Jan Daniëls, Eliam Traas, Tobias de Bildt, Thijs Dregmans
# 07-12-2022

global steps
steps = 0

# opgave 8
def Ack(m, n):
    global steps
    steps += 1
    if m == 0 and n >= 0:
        #print("", end='')
        #print("Ack(",m,",",n,") = ", end='')
        #print(n + 1)
        return n + 1
    if m > 0 and n == 0:
        return Ack(m-1, 1)
    if m > 0 and n > 0:
        return Ack(m-1, Ack(m, n-1))



print(Ack(2,3))
print(steps)

'''
# visualiseren
ran = 5
wid = 3
for x in range(0, ran):
    print(x, (3-len(str(x)))*" ", " | ", end='')
print()
print((ran*(wid+5))*"-")
for x in range(0, ran):
    for y in range(0, ran):
        try:
            a = Ack(x, y)          
            print(a, (wid-len(str(a)))*" ", " | ", end='')
        except RecursionError:
            print("N", (wid-len(str("N")))*" ", " | ", end='')
    print()
    
print(steps)

'''