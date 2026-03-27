import streamlit as st

# ---------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------
st.set_page_config(
    page_title="Mi primera app",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# TÍTULO Y DESCRIPCIÓN
# ---------------------------
st.title("🚀 Mi App en Streamlit")
st.markdown("Este es un template base para empezar rápido.")

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.header("Configuración")

nombre = st.sidebar.text_input("Tu nombre", "Usuario")
edad = st.sidebar.slider("Edad", 0, 100, 25)

# ---------------------------
# CONTENIDO PRINCIPAL
# ---------------------------
st.subheader("👋 Bienvenido")
st.write(f"Hola **{nombre}**, tienes {edad} años.")

# ---------------------------
# INPUTS
# ---------------------------
st.subheader("🧪 Interacción")

numero = st.number_input("Ingresa un número", value=10)

if st.button("Calcular cuadrado"):
    resultado = numero ** 2
    st.success(f"El cuadrado es: {resultado}")

# ---------------------------
# DATAFRAME
# ---------------------------
st.subheader("📊 Datos de ejemplo")

import pandas as pd

df = pd.DataFrame({
    "col1": [1, 2, 3],
    "col2": [4, 5, 6]
})

st.dataframe(df)

# ---------------------------
# GRÁFICO
# ---------------------------
st.subheader("📈 Gráfico")

st.line_chart(df)

# ---------------------------
# FILE UPLOADER
# ---------------------------
st.subheader("📂 Subir archivo")

archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo:
    df_upload = pd.read_csv(archivo)
    st.write(df_upload)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.caption("Hecho con ❤️ usando Streamlit")