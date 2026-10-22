import streamlit as st

# Configuración global de la aplicación (debe ir al inicio)
st.set_page_config(
    page_title="Plataforma de Control y Optimización",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definir la estructura y navegación de los módulos
paginas = {
    "General": [
        st.Page("01_app.py", title="01 - Resumen & Datos", icon="📊", default=True),
    ],
    "Módulos Operacionales": [
        st.Page("02_app.py", title="02 - Modelado & Optimización", icon="⚙️"),
        # st.Page("03_app.py", title="03 - Reportes & KPI", icon="📈"),
    ]
}

# Inicializar navegación
navegacion = st.navigation(paginas)

# Información global en la barra lateral (opcional)
with st.sidebar:
    st.markdown("### Navegación Principal")
    st.caption("Versión 1.0.0")

# Ejecutar el módulo seleccionado
navegacion.run()
