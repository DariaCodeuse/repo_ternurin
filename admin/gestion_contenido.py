import streamlit as st
from db import get_db
from sqlalchemy.orm import Session
from utils import obtener_contenidos, filtrar_contenidos, mostrar_contenidos

def main():
    st.title("📂 Gestión de Contenido")
    st.write("Aquí podrás gestionar el contenido del repositorio.")
    st.info("Listado y opciones de edición/eliminación irán aquí.")

    db: Session = next(get_db())

    # Obtener todos los contenidos
    contenidos = obtener_contenidos(db)

    tipos_contenido = ["Tesis", "Libro", "Revista", "Video", "Podcast"]
    palabras_clave = ["Análisis de Vulverabilidades", "Conmutadores y Redes Inalámbricas ", "Desarrollo de Aplicaciones Web y Móviles", "Inteligencia Artificial", "Seguridad en Cómputo", "Sistemas Operativos"]
    formatos = ["PDF", "MP4", "MP3", "DOCX", "PPTX"]

    # Filtro por tipo de contenido
    colTitulo, colFiltro, colBusqueda = st.columns([2, 1, 2])

    with colTitulo:
        st.subheader("📑 Lista de Contenidos")

    with colFiltro:
        filtro_tipo = st.selectbox("Filtrar por tipo:", ["Todos"] + tipos_contenido)

    with colBusqueda:
        filtro_keywords = st.selectbox("Buscar por palabra clave:", ["Todos"] + palabras_clave)

    # Aplicar los filtros
    contenidos_filtrados = filtrar_contenidos(contenidos, filtro_tipo, filtro_keywords)

    # Mostrar los contenidos filtrados
    mostrar_contenidos(contenidos, contenidos_filtrados)

if __name__ == "__main__":
    main()