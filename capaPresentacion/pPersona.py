import streamlit as st
from capaLogica.lPersona import LPersona

class PPersona:
    def __init__(self):
        self.__lPersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):

        if 'carrito' not in st.session_state:
            st.session_state['carrito'] = []

        col1, col2, col3 = st.columns([6, 1, 1])
        with col3:
            cantidad = len(st.session_state['carrito'])
            st.markdown(f"""<div style="text-align:right; font-size:22px; font-weight:600;"> 🛒 {cantidad}</div>""",unsafe_allow_html=True)

        st.title("CATALOGO DE PRODUCTOS")
        st.subheader("Buscar producto por nombre")

        with st.form("form_busqueda"):
            nombre = st.text_input("Nombre del producto:")
            buscar = st.form_submit_button("Buscar")

        if buscar:
            if nombre.strip() == "":
                st.warning("Ingrese un nombre para buscar.")
            else:
                datos = self.__lPersona.buscarProducto(nombre)

                if not datos:
                    st.error("No se encontraron productos con ese nombre.")
                else:
                    st.success(f"Se encontraron {len(datos)} productos.")
                    st.dataframe(datos)

                    producto = datos[0]

    def mostrarPersona(self):
        resultado = self.__lPersona.mostrarPersona()
        st.dataframe(resultado)

import streamlit as st

# Título de la página
st.title("Bienvenidos a nuestra Tienda Online")

# Sección de catálogo
st.header("Catálogo de Productos")
st.write("Aquí puedes encontrar nuestros productos disponibles:")

# Lista de productos para mostrar visualmente
productos = [
    {"nombre": "Cargador VEX 3.1A", "precio": 25, "descripcion": "Cargador rápido USB + USB-C"},
    {"nombre": "Cable USB Tipo C 1m", "precio": 12, "descripcion": "Cable de alta durabilidad"},
    {"nombre": "Funda Shockproof A03", "precio": 18, "descripcion": "Funda resistente a golpes"},
]

# Mostrar productos
for producto in productos:
    st.subheader(f"{producto['nombre']} - S/ {producto['precio']}")
    st.write(f"Descripción: {producto['descripcion']}")
    st.write("------")

# Barra lateral
st.sidebar.header("Información adicional")
st.sidebar.write("Visítanos para más productos y promociones.")
st.sidebar.image("https://via.placeholder.com/150", caption="Tienda Online")
