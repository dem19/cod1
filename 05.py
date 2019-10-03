# leia um num e inf a soma e a
# med arit de td par anter a ele.
numero=int(input("Digite um numero: "))
i=2
soma=0
media=0
voltas=0
while(i<numero):
    print(i)
    soma=soma+i
    i+=2
    voltas+=1
print("soma",soma)
media=soma/voltas
print(media)

#programa primo e nao primo
x=int(input("Digite um numero: "))
div=0
for i in range(1,x+1):
    if x%i==0:
        div=div+1
if div>2:
     print(x,"não é primo!")
else:
    print(x,"é primo!")

