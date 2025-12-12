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
