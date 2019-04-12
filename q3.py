num = int(input("digite quantos casos de teste tu queres: "))
c = 0
while c<num:
    l = float(input("digite o primeiro valor: "))
    m = float(input("digite o segundo valor: "))
    n = float(input("digite o terceiro valor: "))
    o = round(l, 1)
    p = round(m, 1)
    q = round(n, 1)
    calc= ((o*2)+(p*3)+(q*5))/10
    print("média ponderada: ")
    print(calc)
    c = c+1
