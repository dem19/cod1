#A lista
verdade='O palmeiras não tem mundial!'
lista=list(verdade)
print(lista) #(['O', ' ', 'p', 'a', 'l', 'm', 'e', 'i', 'r', 'a', 's', ' ', 'n', 'ã', 'o', ' ', 't', 'e', 'm', ' ', 'm', 'u', 'n', 'd', 'i', 'a', 'l', '!'])
print("-="*15)
#inicializa uma variavel "i" para acumular o numero
# de ocorrencia da letra "p" na frase
i=0
#coverte o texto para minuscula
verdade = verdade.lower()
print(verdade) #(o palmeiras não tem mundial!)
print("-="*15)
#Itera sobre o texto verdade guardando cada caractere na variavel letra
for letra in verdade:
    #verificar se a letra e igual a p
    if letra == 'p':
        #incrementa o valor de "i" em 1
        i+=1
print(i) #(1)

print("-="*15)

ver = "O são paulo não tem copa do brasil!"
#coverte o texto para maiuscula
ver = ver.upper()
print(ver) #(O SÃO PAULO NÃO TEM COPA DO BRASIL!)
print(ver.count("O")) #(o)

print("-="*15)

#mostras as letras iguais dos dois texto
y = "oi"
x = "boi"
for letra in y:
    for z in x:
        if letra == z:
            print(letra.upper())
            #(o)
            #(i)

print("-="*20)

texto = "ola, meu nome é demerson"
texto2 = "...ola como vai vc?..."
#separa o nome por causa do aspaço
lista = texto.split(" ")
print(lista) #(['ola,', 'meu', 'nome', 'é', 'demerson'])
#tirar todos os pontos antes do texto
print(texto2.lstrip(".")) #(ola como vai vc?...)
#tirar todos os pontos depois do texto
print(texto2.rstrip(".")) #(...ola como vai vc?)
#tirar todos os pontos do texto
print(texto2.strip(".")) #(ola como vai vc?)
#subestituir o nome do texto por outo
print(texto.replace("demerson","Dem")) #(ola, meu nome é Dem)
#subestituir a letra determinada do texto por outo
print(texto.replace("e","v")) #(ola, mvu nomv é dvmvrson)

print("-="*15)
# importa texto de outra guia

#from strings3 import revelacao
#converte uma lista em string
#texto=''.join(revelacao())
#print(texto)

#def revelacao():
#    texto = """ O VASCO É O GRANDE CAMPEAO
#  DA SERIE B! """
#    lista=list(texto)
#    return lista
