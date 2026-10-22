import streamlit as st
import pandas as pd
from datetime import datetime

# -----------------------------------------------------------------------------
# ENCABEZADO Y ESTADO DE LA EMPRESA
# -----------------------------------------------------------------------------
st.title("🏢 Módulo 02: Perfil y Operaciones de la Empresa")

# Ficha principal de la empresa y estado de habilidad
with st.container(border=True):
    col_logo, col_info, col_status = st.columns([1, 4, 2])
    
    with col_logo:
        st.markdown("# 🏛️")
        
    with col_info:
        st.subheader("CENTRO DE CAPACITACION SANTA MONICA LIMITADA")
        st.markdown("**RUT:** `76.176.857-3` &nbsp;|&nbsp; **Giro:** Capacitación y Formación Laboral")
        st.caption("Última sincronización con ChileProveedores: 22-10-2026 15:03:41")
        
    with col_status:
        st.success("● ESTADO: HÁBIL", icon="✅")
        st.caption("Permite contratar y recibir pagos de organismos del Estado.")

# Banner de acciones pendientes
st.info("✨ **¡Estás al día!** No hay acciones pendientes ni observaciones que requieran tu atención en Mercado Público.", icon="ℹ️")

# Botón interactivo de actualización
col_act, col_spacer = st.columns([2, 5])
with col_act:
    if st.button("🔄 Forzar actualización de datos...", use_container_width=True):
        st.toast("Datos sincronizados con éxito con el Registro de Proveedores.")

st.divider()

# -----------------------------------------------------------------------------
# 1. RESUMEN DE PROCESOS Y ÓRDENES DE COMPRA (KPIs)
# -----------------------------------------------------------------------------
st.subheader("📊 Actividad Operacional en Mercado Público")
st.caption("Comparativa acumulada y variaciones respecto al mes de Septiembre 2026.")

tab_oc, tab_procesos = st.tabs(["📦 Órdenes de Compra (OC)", "📑 Procesos de Compra & Ofertas"])

with tab_oc:
    col_oc1, col_oc2, col_oc3, col_oc4 = st.columns(4)
    
    with col_oc1:
        st.metric(
            label="Pendientes de Aceptación",
            value="1",
            delta="Requiere revisión",
            delta_color="inverse"
        )
    with col_oc2:
        st.metric(
            label="OC Aceptadas",
            value="2",
            delta="+2 vs Septiembre",
            delta_color="normal"
        )
    with col_oc3:
        st.metric(
            label="OC Rechazadas",
            value="1",
            delta="+1 vs Septiembre",
            delta_color="inverse"
        )
    with col_oc4:
        st.metric(
            label="Canceladas / En Solicitud",
            value="0",
            delta="0 vs Septiembre",
            delta_color="off"
        )
        
    st.info("⚠️ Tienes **1 orden de compra pendiente de aceptación**. Recuerda aceptarla oportunamente para evitar cancelaciones administrativas.")

with tab_procesos:
    col_pr1, col_pr2, col_pr3 = st.columns(3)
    
    with col_pr1:
        st.metric(
            label="Cotizaciones en Compra Ágil",
            value="10",
            delta="+2 vs Septiembre",
            delta_color="normal"
        )
    with col_pr2:
        st.metric(
            label="Ofertas en Licitaciones",
            value="1",
            delta="0 vs Septiembre",
            delta_color="off"
        )
    with col_pr3:
        st.metric(
            label="Consultas al Mercado",
            value="0",
            delta="0 vs Septiembre",
            delta_color="off"
        )

st.divider()

# -----------------------------------------------------------------------------
# 2. MODALIDADES DE VENTA Y CONTRATACIÓN
# -----------------------------------------------------------------------------
st.subheader("💼 Modalidades de Venta y Canales Habilitados")

col_v1, col_v2, col_v3, col_v4 = st.columns(4)

with col_v1:
    with st.container(border=True):
        st.markdown("##### ⚡ Compra Ágil")
        st.markdown("Mayor foco comercial activo.")
        st.caption("10 cotizaciones enviadas este período.")

with col_v2:
    with st.container(border=True):
        st.markdown("##### 📑 Licitación Pública")
        st.markdown("Participación en curso.")
        st.caption("1 oferta presentada.")

with col_v3:
    with st.container(border=True):
        st.markdown("##### 🤝 Trato Directo")
        st.markdown("Contrataciones directas.")
        st.caption("Disponible bajo causal legal.")

with col_v4:
    with st.container(border=True):
        st.markdown("##### 🏬 Convenio Marco")
        st.markdown("Catálogo electrónico.")
        st.caption("Sujeto a convocatorias de rubro.")

st.caption("📌 *Nota: Para auditar órdenes de compra históricas y montos brutos, puedes descargar los consolidados en el Portal de Datos Abiertos de ChileCompra.*")

st.divider()

# -----------------------------------------------------------------------------
# 3. ACCESOS DIRECTOS DE GESTIÓN ADMINISTRATIVA
# -----------------------------------------------------------------------------
st.subheader("⚙️ Gestión y Acreditaciones de la Empresa")

col_acc1, col_acc2, col_acc3 = st.columns(3)

with col_acc1:
    with st.container(border=True):
        st.markdown("##### 📄 Registro de Proveedores")
        st.caption("Verificación de socios, poderes vigentes y Declaración Jurada anual.")
        st.link_button("Revisar Habilidad y Ficha ↗", "https://www.chileproveedores.cl", use_container_width=True)

with col_acc2:
    with st.container(border=True):
        st.markdown("##### 📦 Gestión de Órdenes (OC)")
        st.caption("Aceptar, rechazar o adjuntar recepciones conformes pendientes.")
        st.link_button("Ir a Mis Órdenes de Compra ↗", "https://www.mercadopublico.cl", use_container_width=True)

with col_acc3:
    with st.container(border=True):
        st.markdown("##### 🎯 Rubros y Oportunidades")
        st.caption("Actualización de códigos ONU de actividades de capacitación.")
        st.link_button("Editar Rubros Notificados ↗", "https://www.mercadopublico.cl", use_container_width=True)
