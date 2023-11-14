# Decorators is a function that receives an function and returns another function
# 1. function decorator (a)
# 2. function to decorate (b)
# 3. function decorated (c)

def decorator_a(function_2decorate):
    def function_decorated():
        print('-------------------------------------------------')
        function_2decorate()
        print('-------------------------------------------------')
    return function_decorated

def decorator_b(function_2decorate):
    def function_decorated(*args, **kwargs):
        print('-------------------------------------------------')
        result = function_2decorate(*args, **kwargs)
        print('-------------------------------------------------')
        return result
    return function_decorated

@decorator_a
def saludo():
    print('Hola')

saludo()

print()
@decorator_b
def sumita(a,b):
    return print(f'{a+b}')

sumita(5,6)