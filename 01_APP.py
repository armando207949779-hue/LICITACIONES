import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.title("📊 Módulo 01: Ingesta y Análisis Exploratorio")
    st.markdown("Carga de conjuntos de datos, validación estructural y previsualización de variables operacionales.")
    
    # ---------------------------------------------------------
    # 1. ESTADO GLOBAL (st.session_state)
    # ---------------------------------------------------------
    if "df_datos" not in st.session_state:
        st.session_state.df_datos = None

    if "datos_validados" not in st.session_state:
        st.session_state.datos_validados = False

    # ---------------------------------------------------------
    # 2. SECCIÓN DE CARGA DE ARCHIVO
    # ---------------------------------------------------------
    st.subheader("1. Origen de Datos")
    
    col_upload, col_demo = st.columns([3, 1])
    
    with col_upload:
        archivo_cargado = st.file_uploader(
            "Cargar archivo CSV o Excel", 
            type=["csv", "xlsx"],
            help="Selecciona un archivo con variables numéricas y/o series temporales."
        )

    with col_demo:
        st.write("¿Sin datos a mano?")
        usar_demo = st.button("Cargar Datos de Prueba", use_container_width=True)

    # Procesar archivo cargado o generar dataset sintético
    if archivo_cargado is not None:
        try:
            if archivo_cargado.name.endswith(".csv"):
                df = pd.read_csv(archivo_cargado)
            else:
                df = pd.read_excel(archivo_cargado)
            
            st.session_state.df_datos = df
            st.session_state.datos_validados = True
            st.success(f"Archivo `{archivo_cargado.name}` cargado correctamente.")
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")
            
    elif usar_demo:
        # Generación de datos sintéticos de prueba
        np.random.seed(42)
        fechas = pd.date_range(start="2026-01-01", periods=100, freq="h")
        df_demo = pd.DataFrame({
            "Timestamp": fechas,
            "Flujo_Alimentacion": np.random.normal(loc=1200, scale=80, size=100).round(2),
            "Potencia": np.random.normal(loc=4500, scale=150, size=100).round(2),
            "Presion": np.random.normal(loc=75, scale=5, size=100).round(2),
            "Estado": np.random.choice(["Normal", "Alerta", "Estable"], size=100)
        })
        st.session_state.df_datos = df_demo
        st.session_state.datos_validados = True
        st.info("Datos de prueba cargados en memoria.")

    # ---------------------------------------------------------
    # 3. VISUALIZACIÓN Y ANÁLISIS SI EXISTEN DATOS
    # ---------------------------------------------------------
    if st.session_state.df_datos is not None:
        df = st.session_state.df_datos

        st.divider()
        st.subheader("2. Resumen General del Dataset")
        
        # Métricas principales en columnas
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Registros", f"{len(df):,}")
        m2.metric("Columnas", f"{df.shape[1]}")
        m3.metric("Valores Nulos", f"{df.isna().sum().sum()}")
        m4.metric("Memoria en RAM", f"{df.memory_usage().sum() / 1024:.1f} KB")

        # Filtros de visualización
        st.markdown("#### Vista Previa de Datos")
        num_filas = st.slider("Filas a mostrar:", min_value=5, max_value=min(100, len(df)), value=10)
        st.dataframe(df.head(num_filas), use_container_width=True)

        # ---------------------------------------------------------
        # 4. GRÁFICOS Y VARIABLES
        # ---------------------------------------------------------
        st.divider()
        st.subheader("3. Exploración de Variables Numéricas")

        columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

        if len(columnas_numericas) > 0:
            col_sel1, col_sel2 = st.columns(2)
            
            with col_sel1:
                var_analizar = st.selectbox("Seleccione variable para tendencia:", columnas_numericas)
            
            with col_sel2:
                tipo_grafico = st.radio("Tipo de vista:", ["Línea de tendencia", "Histograma / Distribución"], horizontal=True)

            if tipo_grafico == "Línea de tendencia":
                st.line_chart(df[var_analizar])
            else:
                conteo, bins = np.histogram(df[var_analizar].dropna(), bins=20)
                df_hist = pd.DataFrame({"Intervalo": bins[:-1].round(1), "Frecuencia": conteo}).set_index("Intervalo")
                st.bar_chart(df_hist)

            # Estadísticos descriptivos
            with st.expander("Ver Estadísticos Descriptivos"):
                st.write(df.describe())
        else:
            st.warning("No se detectaron columnas numéricas en el dataset cargado.")

        # Indicador de paso al siguiente módulo
        st.success("✅ Datos preparados en `st.session_state`. Puedes ir al Módulo 02 para continuar el procesamiento.")
    else:
        st.info("👈 Sube un archivo o presiona 'Cargar Datos de Prueba' para habilitar el análisis.")

# Ejecución automática al ser llamado por st.navigation (00_app.py) o ejecución directa
if __name__ == "__main__" or True:
    run()
