import streamlit as st
from db import get_db
from sqlalchemy.orm import Session
from utils import obtener_contenidos, filtrar_contenidos, mostrar_contenidos, agregar_contenido, ui_registro_contenido

def main():
    st.title("👤 Añadir contenido")
    st.write("Aquí podrás añadir archivos de interés para compartir con tus compañeros.")

    db: Session = next(get_db())

    # Obtener todos los contenidos --------------
    contenidos = obtener_contenidos(db)

    tipos_contenido = ["Libros", "Revistas", "Tesis", "Videos", "Podcasts"]
    materia = ["Análisis de Vulnerabilidades", "Conmutadores y Redes Inalámbricas ", "Desarrollo de Aplicaciones Web y Móviles", "Inteligencia Artificial", "Seguridad en Cómputo", "Sistemas Operativos"]
    formatos = ["PDF", "MP4", "MP3", "DOCX", "PPTX"]

    # Registrar nuevo contenido --------------
    contenido_data = ui_registro_contenido(tipos_contenido, materia, formatos)

    if st.button("Agregar Contenido", use_container_width=True):
        agregar_contenido(db, contenido_data)

    # Editar contenido --------------


if __name__ == "__main__":
    main()