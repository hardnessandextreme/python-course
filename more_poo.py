# Atributos de clase y objetos

class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



persona1 = Persona(nombre='Jonathan', apellido='Quinte')
print(persona1.__dict__)