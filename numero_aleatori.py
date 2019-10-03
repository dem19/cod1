import random

m = int(input("Numero: "))
for _ in range(m):
    # Cria uma lista com números aleatórios no intervalo [0, m].
    nums1 = [random.randint(0, m) for _ in range(m)]
    print(nums1)

import random
#quantas listas
for i in range(6):
#     # Cria uma lista com números aleatórios no intervalo (0, 100),quantos niumeros vai ter
    nums1 = [random.randint(0, 40) for i in range(3)]
    print(nums1)

