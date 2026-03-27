import streamlit as st
import pandas as pd
import os
from generador import generar_propuesta  # tu .py

# ---------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------
st.set_page_config(
    page_title="Epsilon-ScreenFloow",
    page_icon=":clipboard:",
    layout="wide"
)

# ---------------------------
# TÍTULO Y DESCRIPCIÓN
# ---------------------------
st.title(":clipboard: Creador de Propuesta en Excel")
st.markdown("Esta plataforma está diseñada para crear propuestas de manera automatizada para ScreenFloow, optimizando tiempos y asegurando consistencia en cada entrega. A través de la integración de datos, audiencias y parámetros estratégicos, la herramienta genera propuestas personalizadas de forma eficiente, facilitando la toma de decisiones y agilizando los procesos comerciales.")

# ---------------------------
# CARGA DE ARCHIVOS
# ---------------------------
st.subheader(":memo: Crear Propuesta")
st.write("En esta sección debes agregar todos los archivos necesarios para la creación de la propuesta. Todos los archivos deben estar en formato Excel (.xlsx).")
st.write("Archivos obligatorios:")
st.markdown("""
- Campaña
- Line Items
""")
st.write("Archivos opcionales:")
st.markdown("""
- Creative specs
""")

# ---------------------------
# FILE UPLOADER
# ---------------------------
st.subheader("📂 Subir archivos")

archivos = st.file_uploader(
    "Sube los archivos necesarios para crear la propuesta",
    type=["xlsx"],
    accept_multiple_files=True
)

if archivos:
    for archivo in archivos:
        st.write(f"📄 Archivo: {archivo.name}")
        #df = pd.read_excel(archivo)


# ---------------------------
# INPUT DEL URL
# ---------------------------
st.subheader(":link: URL")

new_url = st.text_input("Ingresa la URL de OutMoove:")

if st.button("Generar Propuesta"):
    
    errores = []

    if not archivos or len(archivos) < 2:
        errores.append("Debes subir al menos 2 archivos de Excel.")

    if not new_url or new_url.strip() == "":
        errores.append("Debes ingresar una URL de OutMoove.")

    if errores:
        for error in errores:
            st.error(error)
    
    else:
        # 🔄 Mensaje dinámico
        status = st.empty()
        status.success("🚀 Generando Propuesta...")

        # Simula / ejecuta proceso
        ruta_archivo = generar_propuesta(archivos, new_url)

        # Cuando termina
        status.success("🚀 Propuesta Generada")
        nombre_archivo = os.path.basename(ruta_archivo)
        nombre_archivo = nombre_archivo.replace("_UPDATED", "")

        # ---------------------------
        # DESCARGA DEL ARCHIVO
        # ---------------------------
        with open(ruta_archivo, "rb") as file:
            st.download_button(
                label="📥 Descargar Propuesta",
                data=file,
                file_name=nombre_archivo,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.caption("Hecho con ❤️ equipo de ALab")