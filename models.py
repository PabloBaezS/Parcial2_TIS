class Flight:
    _id_counter = 1

    def __init__(self, nombre, tipo, precio):
        self.id = Flight._id_counter
        Flight._id_counter += 1
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Precio: {self.precio}"
