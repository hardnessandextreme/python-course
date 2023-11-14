import time

# Funcion especial, retorna secuencia de valores
# suspende la ejecucion de la funcion yield (producir) o sea no usa el return

def generador():
    time.sleep(0.7)
    yield 1
    time.sleep(0.7)
    yield 2
    time.sleep(0.7)
    yield 3

for valor in generador():
    print(valor)