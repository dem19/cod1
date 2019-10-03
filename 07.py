
tabuada=int(input("Digite um valor: "))

print("(1)Soma ou (2)Multiplicação")
oper=int(input("Digite uma Operação: "))

soma=1
mult=1
for i in range (1,11):
    if oper == 1:
        if tabuada>10:
            break
        soma=i+tabuada
        print(tabuada,'+',i,'=',soma)
    if oper == 2:
        if tabuada>10:
            break
        mult=i*tabuada
        print(tabuada,'x',i,'=',mult)
