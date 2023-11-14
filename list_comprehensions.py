numeros = range(11)
lista_pares = []

print('''

///Sin list comprenhensions

for numero in numeros:
    if numero % 2 == 0 and numero > 0:
        lista_pares.append(numero*numero)
''')


lista_pares = [numero*numero for numero in numeros if numero % 2 == 0 and numero > 0]
print(f'{lista_pares} con {len((lista_pares))} de items')

mochila = [number for number in range(50) if number % 2 == 0 and number % 6 == 0]
print(mochila)

lista_par = []
lista_impar = []

[lista_par.append(number) if number % 2 == 0 else lista_impar.append(number) for number in range(50)]
print(lista_par)
print(lista_impar)