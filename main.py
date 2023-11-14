def main():
    suma = lambda a=5,b=5: print(f'{a} + {b} = {a+b}')
    suma(6,11)
    print('')
    resta = lambda a=10,b=11: print(f'{a} - {b} = {a-b}')
    resta()
    largo = lambda a, b, c=3, *args, **kwargs: print(f'{a}+{b}+{c}+{args}{kwargs} = {a+b+c+len(args)+len(kwargs)}')
    largo(1,2,3,4,5,6,lado=10,ancho=20)
main()