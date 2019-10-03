vot=[]
ciro=0
haddad=0
bolsonaro=0
marina=0
daciolo=0
nulo=0


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
         ciro += 1
         print("Voto registrado!")
    elif voto == 13:
        haddad += 1
        print("Voto registrado!")
    elif voto == 17:
        bolsonaro += 1
        print("Voto registrado!")
    elif voto == 18:
        marina += 1
        print("Voto registrado!")
    elif voto == 51:
        daciolo += 1
        print("Voto registrado!")
    elif voto == 0000:
        q = "Contabilizando..."
        for i in range(1, 4):
            from time import sleep
            sleep(1)
            print(q)
            sleep(1)
        print(len(vot) - 1, "- PESOOAS QUE VOTARAM")
        perc = 0
        for perc in vot:
            perc = 100/(ciro+haddad+bolsonaro+marina+daciolo+nulo)
            por1=perc*ciro
            por2=perc*haddad
            por3=perc*bolsonaro
            por4=perc*marina
            por5=perc*daciolo
            print((ciro), "- Pessoas votaram em Ciro Gomes", "%#.2f" %por1,"%")
            print((haddad), "- Pessoas votaram em Haddad","%#.2f" %por2,"%")
            print((bolsonaro), "- Pessoas votaram em Bolsonaro","%#.2f" %por3,"%")
            print((marina), "- Pessoas votaram em Marina Silva","%#.2f" %por4,"%")
            print((daciolo), "- Pessoas votaram em Daciolo","%#.2f" %por5,"%")
            break

    else:
        nulo+=1
        print("Voto registrado!")



