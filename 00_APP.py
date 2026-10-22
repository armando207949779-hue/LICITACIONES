import streamlit as st

# 1. Configuración global de la aplicación (debe ser la primera llamada de Streamlit)
st.set_page_config(
    page_title="Plataforma de Gestión y Licitaciones",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Definición de la estructura de páginas y submódulos
# Nota: Los nombres de archivo deben coincidir exactamente con los archivos creados en el repositorio
paginas = {
    "Licitaciones & Mercado": [
        st.Page("01_APP.py", title="01 - Links & Recursos", icon="🌐", default=True),
        st.Page("02_APP.py", title="02 - Estado Empresa & OC", icon="🏢"),
    ],
    # Módulos futuros (descomentar al crear los archivos):
    # "Análisis y Reportes": [
    #     st.Page("03_APP.py", title="03 - Reportes & KPI", icon="📈"),
    # ]
}

# 3. Inicializar el router de navegación
navegacion = st.navigation(paginas)

# 4. Barra lateral común
with st.sidebar:
    st.markdown("### Navegación")
    st.caption("Sistema de Gestión de Compras Públicas")

# 5. Ejecutar la vista seleccionada
navegacion.run()
