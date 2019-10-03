
#abre um arquivo chamado numero.txt
arquivo = open("numero.txt","w")
#itera sobre os numeros de 1 a 100 armazena na variavel linha
q = int(input("numero inicial: "))
w = int(input("numero final: "))
for linha in range(q,w):
    #escolher no arquivo cada numero de variavel linha em uma linha
    arquivo.write('%d\n' %linha)
#fecha o arquivo
arquivo.close()

# open	    open(nome_arquivo,'r')	Abre um arquivo chamado nome_arquivo e o usa para - leitura -. Retorna uma referëncia para um objeto file.
# open	    open(nome_arquivo,'w')	Abre um arquivo chamado nome_arquivo e o usa para - escrita -. Retorna uma referëncia para um objeto file.
# close 	ref_arquivo.close()	Utilização do arquivo referenciado pela variável ref_arquivo terminou.




