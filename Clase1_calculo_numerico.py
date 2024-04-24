class Persona():
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

    def verificar(self):
        if self.edad > 18:
            return True
        else:
            return False

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Cédula:", self.cedula)
        print("Validación:", self.verificar())

# Ejemplo 1
per1 = Persona("Juan", 19, 30604052)
per1.imprimir()
print("")

# Ejemplo 2 con getter y setter
per1.nombre = "Carlos"  # Setter
per1.imprimir()  # Imprimir después de modificar el nombre
print("")
print("Por getter:",per1.cedula)  # Getter para obtener la cédula
print("")

# Utilizar con listas
per2 = Persona("Maria", 26, 30865052)
per3 = Persona("Jaime", 15, 32645052)  # Se inicializa la cédula
lista = []
lista.append(per1)
lista.append(per2)
lista.append(per3)

for i in range(len(lista)):
    per = lista[i]
    per.imprimir()
    print("")

    
