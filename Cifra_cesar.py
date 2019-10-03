#Cifra de César.

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

op = int(input(""" 1- Encriptar 
 2- Desncriptar
"""))
print("-="*15)
nome= input('Digite o nome: ')
print("-="*15)
ordem = int(input('Valor do salto: '))
print("-="*15)

if ordem > alfa.__len__():
    print("Digite um valor entre 1 e 26")
    exit()

def encripta(palavra,ordem):
    texto_criptografado=[]
    for letra in palavra:
        posicao=alfa.index(letra)
        texto_criptografado.append(alfa.__getitem__(posicao+ordem))
    print("".join(texto_criptografado))

def descripta(palavra, ordem):
    texto_criptografado = []
    for letra in palavra:
        posicao = alfa.index(letra)
        texto_criptografado.append(alfa.__getitem__(posicao - ordem))
    print("".join(texto_criptografado))

if op == 1:
    encripta(nome,ordem)
elif op == 2:
    descripta(nome,ordem)
else:
    print("ERRO!")


