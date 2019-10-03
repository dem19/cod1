
urna = ["CIRO GOMES", "HADDAD", "BOLSONARO", "MARINA SILVA", "DACIOLO" ,"NULO"]
d = {urna[0]: 0, urna[1]: 0, urna[2]: 0, urna[3]: 0, urna[4]: 0, urna[5]: 0}
vot=[]
print("######################")
print("##  ELEIÇÔES - 2018 ##")
print("######################")
print("# 12 - CIRO GOMES    #")
print("# 13 - HADDAD        #")
print("# 17 - BOLSONARO     #")
print("# 18 - MARINA SILVA  #")
print("# 51 - DACIOLO       #")
print("######################")

while True:
    voto = int(input('Informe o número do seu candidato: '))
    vot.append(voto)

    if voto == 12:
        d[urna[0]] += 1
    elif voto == 13:
        d[urna[1]] += 1
    elif voto == 17:
        d[urna[2]] += 1
    elif voto == 18:
        d[urna[3]] += 1
    elif voto == 51:
        d[urna[4]] += 1
    elif voto == 0000:
        q = "Contabilizando..."
        for i in range(1, 4):
            from time import sleep
            sleep(1)
            print(q)
            sleep(1)

        print(len(vot) - 1, "PESSOAS VOTARAM")

        maior = 1
        presidente = ''

        for candidato in d:
            x = 0
            for i in range(d[candidato]):
                x += 1

            if d[candidato] > maior:
                maior = d[candidato]
                presidente = candidato
            print("{}: {}".format(candidato,"%d" %x))

        print('O candidato {} é o novo presidente!'.format(presidente))
        break
    else:
        d[urna[5]] += 1
