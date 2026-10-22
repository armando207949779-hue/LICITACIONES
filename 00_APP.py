import streamlit as st

# 1. Configuración global de la aplicación (debe ser la primera llamada de Streamlit)
st.set_page_config(
    page_title="Plataforma de Control y Optimización",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Definición de la estructura de páginas/módulos
# Importante: El nombre del archivo debe coincidir exactamente con "01_APP.py" (mayúsculas)
paginas = {
    "General": [
        st.Page("01_APP.py", title="01 - Resumen & Datos", icon="📊", default=True),
    ],
    # Módulos futuros (descomentar cuando crees los archivos correspondientes):
    # "Módulos Operacionales": [
    #     st.Page("02_APP.py", title="02 - Modelado & Optimización", icon="⚙️"),
    #     st.Page("03_APP.py", title="03 - Reportes & KPI", icon="📈"),
    # ]
}

# 3. Inicializar el router de navegación
navegacion = st.navigation(paginas)

# 4. Barra lateral común (opcional)
with st.sidebar:
    st.markdown("### Navegación")
    st.caption("Sistema de Gestión y Licitaciones")

# 5. Ejecución del módulo seleccionado
navegacion.run()
