# Lista de carros disponíveis para locação
carros = [['Ferrari', 1220.00], ['Hilux', 150.00], ['Golf', 80.00], ['Amarok', 150.00], ['Cobalt', 60.00],
          ['Punto', 60.00], ['New Fiesta', 60.00], ['Focus', 100.00], ['S10', 150.00], ['Corolla', 100.00]]

# Lista de carros disponíveis
carros_disponiveis = carros
# Lista de carros alugados
carros_alugados = []
# Histórico de locação
historico = []


def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(carros):
        if e[0].lower() == name:
            return d
    return None


def c_disponivel():
    lista=list(carros_disponiveis)
    print(lista)

# Item 2 resolvido
def c_alugado():
    lista = list(carros_alugados)
    print(lista)


def ver_carros():
    p = pesquisa((input("Nome: ")))
    if p != None:
        lista = list(carros)
        print(lista[p])


def alugar_carros():
    print("Alugar um carro")
    nome = input("Qual é o seu nome: ")
    p = pesquisa((input("Qual é a marca do carro: ")))
    if p != None:
        lista = list(carros)
        print(nome," - Alugol a:",lista[p])
        carros_disponiveis.pop(p)
        carros_alugados.append(lista[p])
        historico.append(lista[p]+[nome])
        print("Carro Alugado")


def D_carro():
        dias = float(input('O carro foi alugado por quantos dias? '))
        km = float(input('Quantos km foram rodados? '))
        preco = float(input('Qual é o preço por dia do carro? '))
        pkl = float(input('Qual é o preço por km do carro? '))

        d = dias * preco
        k = km * pkl
        total = d + k
        print(total, "a pagar!")
        print("Carro devolvido")


def exibe_historico():
    for locacao in historico:
        print('Carro: ', locacao[0], 'Valor: ',
              locacao[1], 'Locatário: ', locacao[2])
