import streamlit as st
from db import get_db
from sqlalchemy.orm import Session
from models import Contenido
from utils import mostrar_contenido_materia, obtener_contenidos

def main():
    st.title("💻️ Sistemas Operativos")
    st.info("Listado de recursos para esta materia.")

    db: Session = next(get_db())

    mostrar_contenido_materia(db, Contenido, materia="Sistemas Operativos")

if __name__ == "__main__":
    main()