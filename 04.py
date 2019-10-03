z=5
for i in range(1,6):
    from time import sleep
    sleep(1)
    print(z)
    z=z-1
    sleep(1)
print("\n")

print("███████████████████████████")
print("████████▀░░░░░░░▀██████████")
print("██████▀░░░░░░░░░░░▀████████")
print("████▀░░░░░░░░░░░░░░▀███████")
print("███▀░░░░░░░░░░░░░░░░▀██████")
print("███│░░░░░░░░░░░░░░░░░│██████")
print("██▌│░░░░░░░░░░░░░░░░░░│▐████ ")
print("██░└┐░░░░░░░░░░░░░░░░┌┘░█████")
print("██░░└┐░░░░░░░░░░░░░░┌┘░░█████")
print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░█████")
print("██▌░│██████▌░░░▐██████│░▐█████")
print("██░│▐███▀▀░░▄░░▀▀███▌│░██████")
print("██▀─┘░░░░░░██▌░░░░░░░└▀██████")
print("█▄░░░▄▄▄▓░▀█▀░░▓▄▄▄░░▄█████")
print("████▄─┘██▌░░░░░░░▐█└─▄███████")
print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░██████████")
print("████▌░░░▀ ┬┼┼┼┼┼┼┼┬▀░░░▐████████")
print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████████")
print("█████▄░░░░░░░░░░▄█████████")
print("████████░░░░░░░███████████")
print("███████████████████████████")

#funçoes comparametro ou argumento

def imprime_nome(nome):
    print(nome)
imprime_nome("Demerson")
print("-="*15)

#funçoes sem retorno
def imprime_nome():
    print("Demerson")
print("seu nome é:")
imprime_nome()
print("-="*15)

def somar(a,s):
    print(a+s)
somar(4,6)
print("-="*15)

def par_impar(numero):
    if numero%2==0:
        print("É par",numero)
    else:
        print("É impar",numero)
par_impar(5)