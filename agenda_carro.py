
from aluguel_functions import *

print('###############################################')
print('#     MENU - SISTEMA DE LOCAÇÃO DE CARROS     #')
print('# 1 - Ver Carros Disponíveis                  #')
print('# 2 - Ver Carros Alugados                     #')
print('# 3 - Verificar Valor de Carro                #')
print('# 4 - Ver Histórico de Locação                #')
print('# 5 - Ver Fatura Total                        #')
print('# 6 - Ver Quantidade de Alugueis por Carro    #')
print('# 7 - Alugar Carro                            #')
print('# 8 - Devolver Carro                          #')
print('# 0 - Sair                                    #')
print('###############################################')

op = 9
while op != 0:
    op = int(input('Opção: '))
    if op == 1:
        c_disponivel()
    elif op == 2:
        c_alugado()
    elif op == 3:
        ver_carros()
    elif op == 4:
        exibe_historico()

    elif op == 5:
        pass

    elif op == 6:
        pass

    elif op == 7:
        alugar_carros()

    elif op == 8:
        D_carro()

    elif op == 0:
        print("SAIR")

    else:
        print('Opção inválida!')

