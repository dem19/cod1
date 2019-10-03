import emoji
print(emoji.emojize("Carro  :car:",use_aliases=True))
print(emoji.emojize("Coração\033[1;31m:heart:\033[m",use_aliases=True))
print(emoji.emojize("Cavalo :horse:",use_aliases=True))
print(emoji.emojize("gato :cat_face_with_wry_smile:",use_aliases=True))
print(emoji.emojize("familha :family:",use_aliases=True))
print(emoji.emojize(" :kissing_heart:",use_aliases=True))
print(emoji.emojize("gato coração :heart_eyes_cat:",use_aliases=True))
#print(emoji.emojize(" :Smiling_Cat_Face_With_Heart-Eyes:",use_aliases=True))
#print(emoji.emojize("Cavalo ::",use_aliases=True))



# \033[ - começar e terminar
# ; - separa
# [m - É pra fica o plano de fundo so na letra/numero
print('\033[7mEU\033[m')
#0 - semformato
#1 - negrito
#4 - subliniado
#7 - inverte as cores

# cor da letra/numero
print('\033[97mEU')
#30m - branco
#31m - vermelho
#32m - verde
#33m - amarelo
#34m - azul
#35m - rocho
#36m - ciano
#37m - sinza
#90m -
#95m - rosa
#97m - preto


# cor do plano de fundo
print('\033[0;105mEU,TU\033[m')#vermelho
#40m - branco
#41m - vermelho
#42m - verde
#43m - amarelo
#44m - azul
#45m - rocho
#46m - ciano
#47m - sinza
#101m -
#105m - rosa
#107m -


nome = input("Digite um texto: ")
print("""CORES PARA TEXTO
		 	branco
		 	vermelho
		 	verde
			azul
		 	amarelo
		 	rocho
		 	sinza
		 	pretoebranco""")

cor = input("Digite a cor que voce quer: ")
cores = {'limpa':'\033[m',
        'branco':'\033[1;30m',
        'vermelho':'\033[1;31m',
        'verde':'\033[1;32m',
        'azul':'\033[1;34m',
        'amarelo':'\033[1;33m',
        'rocho':'\033[1;35m',
        'sinza':'\033[1;37m',
        'pretoebranco':'\033[7;30m'}

if cores[cor]:
	print('olá! Muito prazer em te conhecer,{}{}{}!'.format(cores[cor],nome,cores['limpa']))



