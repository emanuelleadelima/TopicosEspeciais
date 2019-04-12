l = []
for j in range(15):
    x = int(input("digite um valor: "))
    l.append(x)

print(l)
a = max(l)
print("valor maximo da lista: %d" %(a))
print("posicao: ")
print(l.index(a))
