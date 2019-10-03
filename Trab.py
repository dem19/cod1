import sqlite3

BD = 'produtos.db'

def lista_todos():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM produto"
    cursor.execute(sql)
    produtos = cursor.fetchall()
    if produtos.__len__() > 0:
        for produto in produtos:
            print('id:',produto[0],' - descrição:',produto[1],'- preço:',produto[2], ' - Novo:',produto[3],' - Ativos:',produto[4])

    else:
        print("Nenhum produto cadastrado!")

    cursor.close()
    conexao.close()

def cadastrar(descricao,preco,novo):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO produto (descricao,preco,novo) VALUES ('%s','%d', '%s')" %(descricao, preco, novo)

    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print("produto", descricao, 'cadastrado')
    else:
        conexao.rollback()
        print("nao foi possivel cadastrar o prodito")
    cursor.close()
    conexao.close()

cadastrar('computador', 4567, True)
lista_todos()

def buscar_por_id(id):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()

    sql = "SELECT * FROM produto WHERE id='%d" %id
    cursor.execute(sql)
    produtos = cursor.fetchall()

    if produtos:
        conexao.commit()
        print('id:', produto[0], ' - descrição:', produto[1], '- preço:', produto[2], ' - Novo:', produto[3],' - Ativos:', produto[4])

