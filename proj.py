lista=[]

z = int(input("quantas listas: "))
for _ in range(z):
    y = int(input("digite quantos quadrantes: "))
    for _ in range(y):
        n1, n2, n3 = input("Digite um número: ").split()
        n1, n2, n3 = int(n1), int(n2), int(n3)
        num = n1, n2, n3
        lista.append(num)
    print(lista)
    break


