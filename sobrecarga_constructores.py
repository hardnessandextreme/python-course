# Sobrecarga de constructores simulacion
# permite crear objetos en python deotra forma

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return (f'Nombre: {self.nombre}\n'
                f'Apellido: {self.apellido}')

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_valores(cls, nombre, apellido):
        return cls(nombre, apellido)


persona1 = Persona(nombre='Jonathan', apellido='Quinte')
persona2 = Persona.crear_persona_vacia()
persona3 = Persona.crear_persona_valores(nombre='Joel', apellido='Sarmiento')

print(persona1)
print(persona2)
print(persona3)
