import streamlit as st
from db import get_db
from sqlalchemy.orm import Session
from utils import obtener_contenidos, filtrar_contenidos, mostrar_contenidos, agregar_contenido, ui_registro_contenido

def main():
    st.title("📂 Gestión de Contenido")
    st.write("Aquí podrás gestionar el contenido del repositorio.")
    st.info("Listado y opciones de edición/eliminación irán aquí.")

    db: Session = next(get_db())

    # Obtener todos los contenidos --------------
    contenidos = obtener_contenidos(db)

    tipos_contenido = ["Libros", "Revistas", "Tesis", "Videos", "Podcasts"]
    materia = ["Análisis de Vulnerabilidades", "Conmutadores y Redes Inalámbricas ", "Desarrollo de Aplicaciones Web y Móviles", "Inteligencia Artificial", "Seguridad en Cómputo", "Sistemas Operativos"]
    formatos = ["PDF", "MP4", "MP3", "DOCX", "PPTX"]

    # Filtro por tipo de contenido
    colTitulo, colFiltro, colBusqueda = st.columns([2, 1, 2])

    with colTitulo:
        st.subheader("📑 Lista de Contenidos")

    with colFiltro:
        filtro_tipo = st.selectbox("Filtrar por tipo:", ["Todos"] + tipos_contenido)

    with colBusqueda:
        filtro_keywords = st.selectbox("Buscar por palabra clave:", ["Todos"] + materia)

    # Aplicar los filtros
    contenidos_filtrados = filtrar_contenidos(contenidos, filtro_tipo, filtro_keywords)

    # Mostrar los contenidos filtrados
    mostrar_contenidos(db, contenidos_filtrados)

    # Registrar nuevo contenido --------------
    contenido_data = ui_registro_contenido(tipos_contenido, materia, formatos)

    if st.button("Agregar Contenido", use_container_width=True):
        agregar_contenido(db, contenido_data)

    # Editar contenido --------------


if __name__ == "__main__":
    main()