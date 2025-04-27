from sqlalchemy.orm import Session
from sqlalchemy import desc
from models import Contenido
import streamlit as st
import fitz
import os
import base64

def contar_registros(db: Session, modelo):
    return db.query(modelo).count()

def obtener_ultimos_contenidos(db: Session, modelo, limite=5):
    return db.query(modelo, Contenido)\
             .join(Contenido, Contenido.ContenidoID == modelo.ContenidoID)\
             .order_by(desc(Contenido.ContenidoID))\
             .limit(limite)\
             .all()

def extraer_portada_pdf(ruta_pdf):
    """Extrae la primera página de un PDF y la convierte en imagen."""
    try:
        pdf_documento = fitz.open(ruta_pdf)
        primera_pagina = pdf_documento[0]
        pix = primera_pagina.get_pixmap()
        imagen_bytes = pix.tobytes("png")
        pdf_documento.close()
        return imagen_bytes
    except Exception as e:
        st.error(f"Error al extraer la portada de {ruta_pdf}: {e}")
        return None

def construir_ruta_pdf(titulo, tipo_contenido):
    titulo = titulo.replace(" ", "_")
    return f"./files/{tipo_contenido}/{titulo}.pdf".lower()

def visualizar_pdf(ruta_pdf):
    # Verificar si el archivo PDF existe
    if os.path.exists(ruta_pdf):
        with open(ruta_pdf,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    else:
        st.warning(f"No se encontró el archivo PDF en {ruta_pdf}")

# Función para proporcionar la opción de descargar el PDF
def descargar_pdf(ruta_pdf, titulo):
    with open(ruta_pdf, "rb") as f:
        pdf_bytes = f.read()
    st.download_button(
        label="Descargar PDF",
        data=pdf_bytes,
        file_name=f"{titulo}.pdf",
        mime="application/pdf",
    )

# Función para obtener todos los contenidos
def obtener_contenidos(db: Session):
    return db.query(Contenido).all()

# Función para filtrar contenidos
def filtrar_contenidos(contenidos, filtro_tipo, filtro_keywords):
    contenidos_filtrados = contenidos
    if filtro_tipo != "Todos":
        contenidos_filtrados = [c for c in contenidos_filtrados if c.TipoContenido == filtro_tipo]

    if filtro_keywords != "Todos":
        filtro_keywords_lower = filtro_keywords.lower()
        contenidos_filtrados = [c for c in contenidos_filtrados if filtro_keywords_lower in c.Keywords.lower()]
    
    return contenidos_filtrados

# Función para mostrar los contenidos
def mostrar_contenidos(db: Session, contenidos_filtrados):
    for contenido in contenidos_filtrados:
        with st.expander(f" {contenido.Titulo} ({contenido.TipoContenido})"):
            colData, colImg = st.columns([2, 1])
            with colData:
                st.write(f"**Materia:** {contenido.Materia}")
                st.write(f"**Formato:** {contenido.Formato}")
                st.write(f"**Estado:** {contenido.Estado}")
                st.write(f"**Vistas:** {contenido.Vistas}")
                st.write(f"**Autor:** {contenido.Autor}")
                st.write(f"**Fecha de Subida:** {contenido.FechaSubida}")
                st.write(f"**Descripción:** {contenido.Descripcion}")
                
                st.button("❌ Eliminar contenido", key=f"eliminar_{contenido.ContenidoID}", on_click=eliminar_contenido, args=(contenido, db), use_container_width=True)

            with colImg:
                ruta_pdf = construir_ruta_pdf(contenido.Titulo, contenido.TipoContenido)
                portada = extraer_portada_pdf(ruta_pdf)
                if portada:
                    st.image(portada, caption=f"{contenido.Titulo}", use_container_width=True)
                if os.path.exists(ruta_pdf):
                    descargar_pdf(ruta_pdf, contenido.Titulo)

                else:
                    st.warning(f"No se encontró el archivo PDF para {contenido.Titulo}")
                
            # st.button("📄 Ver PDF", key=f"ver_pdf_{contenido.ContenidoID}", on_click=visualizar_pdf, args=(ruta_pdf,))

# Función para eliminar un contenido
def eliminar_contenido(contenido, db: Session):
    db.delete(contenido)
    db.commit()
    st.warning("Contenido eliminado.")
    st.rerun()


