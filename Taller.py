class Automovil:
    def __init__(self, marca, modelo, color, placa, nombre_del_cliente, problema_técnico):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.nombre_del_cliente = nombre_del_cliente
        self.problema_técnico = problema_técnico

    def info_automovil(self):
        return f"{self.marca} {self.modelo} - {self.color} - {self.placa} - {self.nombre_del_cliente} - {self.problema_técnico}"
    
class Taller:
    def __init__(self, nombre, ubicacion, contacto):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contacto = contacto
        self.automoviles = []

    def agregar_automovil(self, automovil):
        self.automoviles.append(automovil)

    def listar_automoviles(self):
        for auto in self.automoviles:
            print(auto.info_automovil())

mi_taller = Taller("AutoFix", "Managua", "8888-1234")

auto1 = Automovil("Toyota", "Corolla", "Rojo", "M123456", "Carlos Pérez", "Frenos fallando")
auto2 = Automovil("Honda", "Civic", "Azul", "N654321", "Ana López", "Cambio de aceite")

mi_taller.agregar_automovil(auto1)
mi_taller.agregar_automovil(auto2)

mi_taller.listar_automoviles()