agenda = []  # Criando uma lista.

def p_nome():  # Função para pedir o nome.
    return (input("Nome: "))


def p_telefone():  # Função para pedir o telefone.
    return (input("Telefone: "))
#######################################################################################################3

def listar_dados(nome, telefone):  # Função que mostra todos os dados do contato.
    print("Nome: %s\nTelefone: %s" % (nome, telefone))

#######################################################################################################3

def pesquisa(nome):  # Função para pesquisar contatos.
    name = nome.lower()  # Convertendo todas as letras em minúsculas.
    for d, e in enumerate(agenda):  # Executando o loop.
        if e[0].lower() == name:  # Determinando uma condição.
            return d  # Executa caso a condição for verdadeira.
    return None  # Executa caso a condição for falsa.


def novo():  # Função para adicionar novo Contato.
    global agenda  # Definindo variável como Global.
    nome = p_nome()  # Entrada de dados.
    telefone = p_telefone()  # Entrada de dados.
    agenda.append([nome, telefone])  # Adicionando os dados na agenda


def apagar():  # Função para apagar um contato.
    global agenda  # Definindo variável como Global.
    nome = p_nome()  # Entrada de dados.
    p = pesquisa(nome)  # Cria uma variável e chama a função pesquisa.
    if p != None:  # Determinando uma condição.
        del agenda[p]  # Executa caso a condição for verdadeira.
    else:
        print("Nome não encontrado.")  # Executa caso a condição for falsa.
#######################################################################################################3

def editar():  # Função para editar um contato.
    p = pesquisa(p_nome())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = agenda[p][0]  # Procurando os dados na agenda.
        telefone = agenda[p][1]  # Procurando os dados na agenda.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(nome, telefone)  # Mostra os dados.
        nome = p_nome()  # Entrada dos novos dados editados.
        telefone = p_telefone()  # Entrada dos novos dados editados.
        agenda[p] = [nome, telefone]  # Armazenando os novos dados.
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.
#######################################################################################################3

def listar():  # Função para mostrar lista de contatos.
    print("\nAgenda\n\n------")
    for e in agenda:
        listar_dados(e[0], e[1])
    print("------\n")


def pesquisar():  # Função para Pesquisar os contatos.
    p = pesquisa(p_nome())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = agenda[p][0]  # Procurando os dados na agenda.
        telefone = agenda[p][1]  # Procurando os dados na agenda.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(nome, telefone)  # Mostra os dados.
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.


def validar(pergunta, inicio, fim):  # Função para validar numeros inteiros.
    while True:  # Criando um loop infinito.
        try:  # Criando um acordo/condição.
            valor = int(input(pergunta))  # Entrada de dados.
            if inicio <= valor <= fim:  # Deterimando uma condição.
                return (valor)  # Executa caso for verdadeira.
            return
        except ValueError:  # Executa caso for falsa.
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))


def menu():  # Função que exibe o menu de opções.
    print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
""")

    return validar("Escolha uma opção: ", 1, 6)  # Retorna o valor da opção desejada.


while True:  # Criando um loop infinito.
    opção = menu()
    if opção == 6:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        editar()
    elif opção == 3:
        pesquisar()
    elif opção == 4:
        listar()
    elif opção == 5:
        apagar()