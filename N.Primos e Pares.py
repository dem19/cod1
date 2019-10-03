
def ret(z,y):
    return(z*y),(z+y)/2
tot=ret(10,5)
print(tot)

########################################
def primo(x):
    div=0
    for i in range(1,x+1):
        if x%i==0:
            div=div+1
    if div>2:
        print(x,"não é primo!")
    else:
        print(x,"é primo!")
primo(15)

########################################
Nprimo=[]
primo=[]
def inserir(x):
    div = 0
    for i in range(1, x + 1):
        if x % i == 0:
            div = div + 1
    if div > 2:
        Nprimo.append(x)
    else:
        primo.append(x)
for i in range(1,21):
    inserir(i)
print("Numeros não primo:",Nprimo)
print("Numeros primo:",primo)

#########################################
lista_par=[]
lista_impar=[]
def inserir(n):
    if n%2==0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

for i in range(1,11):
    inserir(i)
print("Pares:",lista_par)
print("Impares:",lista_impar)

##############################################
#exibir a quantidade de elementos da lista
#print("Pares:",lista_par,_len_())
#print("Impares:",lista_impar,_len_())
print("-="*15)
Nprimo=[]
primo=[]
def inserir(x):
    div = 0
    for i in range(1, x + 1):
        if x % i == 0:
            div = div + 1
    if div > 2:
        Nprimo.append(x)
    else:
        primo.append(x)
for i in range(1,11):
    inserir(i)
print("Numeros não primo:",Nprimo)
print("Numeros primo:",primo)


lista_par=[]
lista_impar=[]

while True:
    print("Para encerrar digite 0 ")
    numero = int(input("Informe um numero: "))
    if numero % 2 == 0:
        lista_par.append(numero)
    if numero % 2 != 0:
        lista_impar.append(numero)
    if numero == 0:
        print("Voce digitou", len(lista_par),"Numeros pares")
        print("São eles",lista_par)
        print("Voce digitou", len(lista_impar), "Numeros Impares")
        print("São eles", lista_impar)
        break

