# def generador():
#     for numero in range(1,6):
#         yield numero
#
# gen = generador()
# try:
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
# except StopIteration as e:
#     print(f'Error: {e}')

suma = sum(valor*valor for valor in range(101))
print(f'{suma}')

lista = ['Jonathan', 'Robin', 'Gustavo']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))
print(next(generador))


lista2 = lista.copy()
contador = 0

def incrementar():
    global contador
    contador +=1
    return contador

generador2 = (f'{incrementar()}. {nombre}' for nombre in lista2)
print(next(generador2))