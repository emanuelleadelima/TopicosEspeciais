c = 0
q = 0
l = []

while c<6:
    a = float(input("digite um numero(até completar 6): \n"))
    c+=1
    if a>0:
        q = q+a
        l.append(a)
print(l)
tam = len(l)
print("a quantidade de numeros positivos digitados é: %d" %(tam))
media = q/tam
print("media dos valores positivos digitados: %.1f" %(media))
