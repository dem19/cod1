for i in range(1, 21, +1):
    print(i)
print("~" * 35)

print("Calcular os numeros ate o que digitar")

x = int(input("Digite um número: "))
soma = 0
for i in range(1, x):
    soma = soma + i
print(soma)
print("~" * 35)


print("**Fatorial**")

x = int(input("Digite um número :"))

fat = 1
for i in range(1, x + 1):
    fat = fat * i
print("O fatorial de", x, "é:", fat)

print("*RAIZ QUADRADA*\n")
x = int(input("Digite um numero: "))
y = x ** (1 / 2)
print('A raiz quadrada de', x, ': %d' % y)
print("†" * 35)

print("*serie de fibonaci*")

x = int(input("Digite um numero: "))
a, b = 0, 1
while (b < x):
    print(b)
    a, b = b, a + b
print("~" * 35)

a = 20
while (a > 8):
    print(a)
    a = a - 1

print("~" * 35)

resposta = " "
while (resposta != "sim"):
    resposta = input("Aceita namorar comigo? ")
print("farei de vc a mulher mais feliz do mundo")
print("  *  *   *  *")
print(" *     *     *")
print(" *   TE AMO  *")
print("  *         *")
print("    *      *")
print("      *  *")
print("        *")