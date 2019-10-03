# tabuada

tabuada=int(input("Digite um valor: "))
soma=1
for i in range (1,11):
    if tabuada>10:
        break
    soma=i+tabuada
    print(tabuada,'+',i,'=',soma)

print("-="*15)
print("\n")

n1,n2 = input("Digite um número: ").split()
n1,n2= int(n1), int(n2)
soma=0
media=0
voltas=1

for i in range(n1+1, n2):
    if n1<0 and n2<0:
        break
    print(i, end=' ')
    soma =soma+i
print("soma=",soma)
voltas+=1
media=soma/voltas
print('media=',media)
