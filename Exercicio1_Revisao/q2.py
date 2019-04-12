c = 0
l = []

while c<6:
    a = int(input("digite um numero(até completar 6): \n"))
    c+=1
    if a==0:
        print("digite um numero positivo ou negativo")
        c-=1
    elif a>0:
        l.append(a)

print(l)
print("a quantidade de numeros positivos digitados é:")
print(len(l))
