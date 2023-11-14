class Conversor:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura C demasiado alto: {celsius}')
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiado alto: {fahrenheit}')
        return (fahrenheit-32) * 5/9

if __name__ == '__main__':
    a_convertir = 45
    resultado = Conversor.c_f(a_convertir)
    print(f'{a_convertir} C a F: {resultado:.2f}')

    resultado2 = Conversor.f_c(resultado)
    print(f'{resultado} F a C: {resultado2:.2f}')