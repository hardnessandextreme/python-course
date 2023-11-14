class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'

persona1 = Persona(nombre='Jonathan', apellido='Quinte')

print(persona1)