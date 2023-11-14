# Closure is a function that defines another function and returns it
# The nested function can access local variables defined in the main function o external

def operacion(a,b):
    def suma():
        return print(f'{a+b}')
    return suma()

def operacion2(a,b):
    multiply = lambda: print(f'{a*b}')
    return multiply()
def main():
    operacion(5,5)
    operacion2(5,5)

main()