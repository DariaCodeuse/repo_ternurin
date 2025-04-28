import streamlit as st
from db import get_db
from models import Contenido
from utils import buscador_contenido, mostrar_contenido_reciente, panel_materias

def main():
    st.title("🏠 Inicio")
    st.write("Bienvenido al Repositorio Ternurin!")
    st.info("Explora los contenidos disponibles por materia.")

    st.image("./images/repositorio.png", use_container_width=True)
    db = next(get_db())

    # Secciones
    buscador_contenido(db, Contenido)
    mostrar_contenido_reciente(db, Contenido)
    panel_materias()

if __name__ == "__main__":
    main()