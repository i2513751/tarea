from conexion import ConexionDB

class DPersona:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__table = 'productos'

    def __ejecutarConsulta(self, consulta):
        try:
            resultado = consulta.execute().data
            return resultado
        except Exception as e:
            return f'Error:{e}'

    def mostrarPersona(self):
        consulta = self.__db.table(self.__table).select('*')
        return self.__ejecutarConsulta(consulta)

    def buscarProducto(self, nombre):
        consulta = (self.__db.table(self.__table).select('*').ilike('nombre', f'%{nombre}%'))
        return self.__ejecutarConsulta(consulta)