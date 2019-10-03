#print('numero aleatorio')
#from random import *

#for i in range(1, 4):
#    print(randrange(1, 10))

print("---JO,KEN,PO---\n")
from random import randint
from time import sleep

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("""Suas opções:
[0] pedra
[1] papel
[2] tesoura""")
jogador = int(input("Qual é a sua jogada? "))
print("-=" * 11)
sleep(1)
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po\n")
print("-=" * 11)
print("jogador jogou {}".format(itens[jogador]))
print("Computador jogou {}".format(itens[computador]))
print("-=" * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!\n')

print("##### JOGO DE PAR ou IMPAR #####\n")
acumulador1 = 0
acumulador2 = 0
q = input("Seu nome: ")
for i in range(1, 4):
    a = input("par ou impar: ")
    print("-=" * 15)
    if a == "par" or a == "impar":
        b = int(input("Seu numero: "))
        from random import *

        z = randrange(1, 11)

        print("o computador {}".format(z))
        soma = b + z
        print("o resultado dos numeros foi:{}".format(soma))
        print("-=" * 15)
        if soma % 2 == 0:
            print(" O resultado é Par")
            if a == "par":
                acumulador1 += 1
                print("{} ganhou".format(q))

            else:

                acumulador2 += 1
                print("O computador ganhou")

        if soma % 2 != 0:
            print(" O resultado é impar")
            if a == "impar":
                acumulador1 += 1
                print("{} ganhou".format(q))

            else:
                acumulador2 += 1
                print("O computador ganhou")

    else:
        print("ERRO")

    print("~" * 25)
print(" você fez", acumulador1, "pontos e o computador", acumulador2, "pontos")
if acumulador1 >= 2:
    print(" {} GANHOU!!!".format(q))

if acumulador2 >= 2:
    print(" Computador Ganhou")