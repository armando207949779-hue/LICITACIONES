import streamlit as st

st.title("🌐 Módulo 01: Accesos Rápidos y Recursos de Licitaciones")
st.markdown(
    "Directorio centralizado de plataformas oficiales, herramientas de datos abiertos "
    "y accesos directos del sistema de compras públicas de Chile."
)

st.divider()

# -----------------------------------------------------------------------------
# 1. BUSCADOR RÁPIDO DE LICITACIÓN POR CÓDIGO
# -----------------------------------------------------------------------------
st.subheader("🔍 Acceso Directo por Código de Licitación")
col_input, col_btn = st.columns([3, 1])

with col_input:
    id_licitacion = st.text_input(
        "Ingrese ID de Licitación:",
        placeholder="Ej: 1234-56-LR26 o 2408-12-L126",
        help="Introduce el código identificador de la licitación para abrir la búsqueda directamente."
    )

with col_btn:
    st.write("")  # Espaciador vertical
    st.write("")
    if id_licitacion.strip():
        url_busqueda = f"https://www.mercadopublico.cl/Home/BuscarLicitacion?searchTerm={id_licitacion.strip()}"
        st.link_button("Buscar en Mercado Público ↗", url_busqueda, use_container_width=True)
    else:
        st.button("Buscar en Mercado Público ↗", disabled=True, use_container_width=True)

st.divider()

# -----------------------------------------------------------------------------
# 2. PORTALES OPERATIVOS Y TRANSACCIONALES
# -----------------------------------------------------------------------------
st.subheader("🏢 Plataformas Principales de Operación")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("#### Mercado Público")
        st.caption("Plataforma transaccional para postular a licitaciones, compras ágiles y convenios marco.")
        st.link_button("Ir a Mercado Público", "https://www.mercadopublico.cl", use_container_width=True)

with col2:
    with st.container(border=True):
        st.markdown("#### ChileCompra")
        st.caption("Dirección de Compras Públicas: noticias, directivas de contratación, capacitaciones y soporte.")
        st.link_button("Ir a ChileCompra", "https://www.chilecompra.cl", use_container_width=True)

with col3:
    with st.container(border=True):
        st.markdown("#### ChileProveedores")
        st.caption("Registro Oficial de Proveedores del Estado: estados de habilidad, acreditaciones y certificados.")
        st.link_button("Ir a ChileProveedores", "https://www.chileproveedores.cl", use_container_width=True)

# -----------------------------------------------------------------------------
# 3. DATOS ABIERTOS, INTELIGENCIA Y API
# -----------------------------------------------------------------------------
st.subheader("📊 Datos Abiertos y Desarrollo")

col4, col5, col6 = st.columns(3)

with col4:
    with st.container(border=True):
        st.markdown("#### Portal Datos Abiertos")
        st.caption("Estadísticas del gasto fiscal, trazabilidad y comportamiento de compras públicas.")
        st.link_button("Portal Datos Abiertos", "https://datos-abiertos.chilecompra.cl", use_container_width=True)

with col5:
    with st.container(border=True):
        st.markdown("#### Descargas Masivas (.7z / CSV)")
        st.caption("Bases de datos consolidadas de órdenes de compra, ofertas y licitaciones históricas.")
        st.link_button("Centro de Descargas", "https://datos-abiertos.chilecompra.cl/descargas", use_container_width=True)

with col6:
    with st.container(border=True):
        st.markdown("#### API Mercado Público")
        st.caption("Servicios web (JSON/XML) para extraer licitaciones y órdenes de compra en tiempo real.")
        st.link_button("Documentación y Tickets API", "https://api.mercadopublico.cl", use_container_width=True)

# -----------------------------------------------------------------------------
# 4. MARCO REGULATORIO Y FISCALIZACIÓN
# -----------------------------------------------------------------------------
st.subheader("⚖️ Marco Normativo y Reclamaciones")

col7, col8 = st.columns(2)

with col7:
    with st.container(border=True):
        st.markdown("#### Tribunal de Contratación Pública (TCP)")
        st.caption("Órgano jurisdiccional para interponer acciones de impugnación contra actos u omisiones ilegales en licitaciones.")
        st.link_button("Tribunal de Contratación Pública", "https://www.tribunaldecontratacionpublica.cl", use_container_width=True)

with col8:
    with st.container(border=True):
        st.markdown("#### Contraloría General de la República")
        st.caption("Jurisprudencia administrativa, dictámenes sobre contratación pública y fiscalización estatal.")
        st.link_button("Portal Contraloría (CGR)", "https://www.contraloria.cl", use_container_width=True)

# -----------------------------------------------------------------------------
# 5. GUÍA RÁPIDA DE TIPOS DE LICITACIÓN (REFERENCIA)
# -----------------------------------------------------------------------------
with st.expander("📌 Glosario de Tipos de Compra y Códigos"):
    st.markdown("""
    | Tipo | Nomenclatura | Descripción / Rango de Monto |
    | :--- | :--- | :--- |
    | **L1** | Licitación Pública | Menor a 100 UTM |
    | **LE** | Licitación Pública | Entre 100 y 1.000 UTM |
    | **LP** | Licitación Pública | Mayor a 1.000 UTM |
    | **LS** | Licitación Pública | Servicios personales especializados |
    | **CO** | Compra Ágil | Compras menores a 30 UTM con cotizaciones directas |
    | **CM** | Convenio Marco | Catálogo electrónico para adquisiciones estandarizadas |
    """)
    
