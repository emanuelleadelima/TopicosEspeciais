qtdPizza = int(input("Olá, cliente! Informe aqui a quantidade de pizzas desejada.\n"))
precoPizza = float(input("Agora, informe o valor da pizza, contido no cardápio. \n"))
custoPizzas = precoPizza*qtdPizza
imposto = precoPizza*0.08
valorTotal= custoPizzas+imposto
print("O valor total é de %.2f" %(valorTotal))
