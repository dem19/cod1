agenda = []
def mostrar_todos():
    if agenda.__len__() > 0:
        for contato in agenda:
            print(agenda.index(contato)," - ",contato)
    else:
        print("Não existem contatos na agenda!")

def n_ome(nome):
    agenda.append(nome)
    print("Contato inserido com sucesso!")

def altera_contato(id):
    if agenda.__len__() > id:
        novo_nome = input("Informe o novo nome do contato : ")
        agenda[id] = novo_nome
        print("Alterado com sucesso!")
    else:
        print("Contato não encontrado")

def busca_id(id):
    if agenda.__len__() > id:
        print(agenda[id])
    else:
        print("Contato não encontrado")
############################################################
def busca_nome(nome):
    if agenda.__contains__(nome):
        print(agenda.index(nome))
    else:
        print("Contato não encontrado")

#############################################################

def excluir_id(id):
    if agenda.__len__() > id:
        agenda.__delitem__(id)
        print('Contato excluido com sucesso!')
    else:
        print("Contato não encontrado")

def excluir_agenda():
    agenda.clear()
    print("Agenda excluida com sucesso!")


print("#"*27)
print("###### MENU - AGENDA ######")
print("#"*27)
print("# 1 - Acessar Agenda      #")
print("# 2 - inserir contato     #")
print("# 3 - Alterar contato     #")
print("# 4 - Busca pelo ID       #")
print("# 5 - Busca pelo Nome     #")
print("# 6 - Excluir pelo ID     #")
print("# 7 - Excluir pela Agenda #")
print("# 8 - Sair                #")
print("#"*27)

op = 0
while op != 8:
    op = int(input("Opção: "))
    if op == 1:
        mostrar_todos()
    elif op == 2:
        nome = input("Informe o nome do contato: ")
        n_ome(nome)
    elif op == 3:
        id = int(input("Informe o id do contato: "))
        altera_contato(id)
    elif op == 4:
        id = int(input("Informe o id do contato: "))
        busca_id(id)
#########################################################################
    elif op == 5:
        nome = input("Informe o nome do contato: ")
        busca_nome(nome)
##########################################################################
    elif op == 6:
        id = int(input("Informe o id do contato: "))
        excluir_id(id)
    elif op == 7:
        excluir_agenda()
    elif op == 8:
        print("SAIR")
        break
    else:
        print("Opção invalida!")