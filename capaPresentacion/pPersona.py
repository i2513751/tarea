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

# Lista de productos (puedes actualizarla según lo necesites)
productos = [
    {"id": 1, "nombre": "Cargador VEX 3.1A", "precio": 25, "descripcion": "Cargador rápido USB + USB-C", "imagen": "https://via.placeholder.com/150"},
    {"id": 2, "nombre": "Cable USB Tipo C 1m", "precio": 12, "descripcion": "Cable de alta durabilidad", "imagen": "https://via.placeholder.com/150"},
    {"id": 3, "nombre": "Funda Shockproof A03", "precio": 18, "descripcion": "Funda anti-impactos resistente", "imagen": "https://via.placeholder.com/150"},
    {"id": 4, "nombre": "Vidrio Templado 9D", "precio": 10, "descripcion": "Protector de pantalla ultra resistente", "imagen": "https://via.placeholder.com/150"},
    {"id": 5, "nombre": "Auriculares Bluetooth X7", "precio": 30, "descripcion": "Sonido HD y batería 12h", "imagen": "https://via.placeholder.com/150"},
    {"id": 6, "nombre": "Cargador Turbo 25W", "precio": 35, "descripcion": "Carga rápida para Samsung y Android", "imagen": "https://via.placeholder.com/150"},
    # Agregar más productos aquí si es necesario
]

# Inicializar carrito
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Función para agregar al carrito
def agregar_al_carrito(producto):
    st.session_state.carrito.append(producto)

# Mostrar carrito en la barra lateral
st.sidebar.header("Carrito")
st.sidebar.write(f"Productos en el carrito: {len(st.session_state.carrito)}")
if len(st.session_state.carrito) > 0:
    for item in st.session_state.carrito:
        st.sidebar.write(f"- {item['nombre']} - S/ {item['precio']}")

# Mostrar los productos y agregar botones
st.title("CATÁLOGO DE PRODUCTOS")
for producto in productos:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.image(producto["imagen"], use_column_width=True)
        st.write(f"**{producto['nombre']}**")
        st.write(f"Precio: S/ {producto['precio']}")
        st.write(producto["descripcion"])
    
    with col2:
        if st.button(f"Agregar {producto['nombre']} al carrito", key=producto["id"]):
            agregar_al_carrito(producto)
            st.success(f"{producto['nombre']} agregado al carrito")

# Mostrar el número de productos en el carrito en la parte superior derecha
st.sidebar.write(f"Total productos en el carrito: {len(st.session_state.carrito)}")
