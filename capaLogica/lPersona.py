from capaDatos.dPersona import DPersona

class LPersona:
    def __init__(self):
        self.__dPersona = DPersona()

    def mostrarPersona(self):
        return self.__dPersona.mostrarPersona()

    def buscarProducto(self, nombre):
        return self.__dPersona.buscarProducto(nombre)

    def actualizarProducto(self, id_producto, nombre=None, precio=None, cantidad=None):
        return self.__dPersona.actualizarProducto(id_producto, nombre, precio, cantidad)