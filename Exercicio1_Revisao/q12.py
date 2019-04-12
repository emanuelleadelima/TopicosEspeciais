valorPrestacao = float(input("informe o valor da prestacao *caso nao haja, digite 0*\n"))
li = list()
qtd = len(li)
valorTotal = sum(li)
while (valorPrestacao!=0):
    diasAtraso = int(input("informe a quantidade de dias em atraso *se nao houver, digite 0*\n"))
    if (diasAtraso==0):
        li.append(valorPrestacao)
    else:
        calc = valorPrestacao+(valorPrestacao*0.03)+(valorPrestacao*0.1)
        li.append(calc)
    valorPrestacao = float(input("informe o valor da prestacao *caso nao haja, digite 0*\n"))
print("relatório do dia:\n quantidade de prestacoes pagas no dia: %d\n valor total de prestacoes pagas no dia: %.2f" %(qtd, valorTotal))
