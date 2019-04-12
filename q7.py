def fatorial():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    if n==0:
        print("0!=1")
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %n, fat)

fatorial()
