import streamlit as st
from sqlalchemy.orm import Session
from db import get_db
from models import Contenido, Usuario, Libros, Revistas, Tesis
from utils import contar_registros, obtener_ultimos_contenidos

def main():
    st.title("🏠 Panel de Administrador")
    st.write("Bienvenido al Repositorio Ternurin!")
    st.info("Explora los contenidos disponibles por materia.")
    st.markdown("---")

    db: Session = next(get_db())

    # Estadísticas principales
    total_usuarios = contar_registros(db, Usuario)
    total_libros = contar_registros(db, Libros)
    total_revistas = contar_registros(db, Revistas)
    total_tesis = contar_registros(db, Tesis)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Usuarios", total_usuarios)
    col2.metric("📚 Libros", total_libros)
    col3.metric("📰 Revistas", total_revistas)
    col4.metric("🎓 Tesis", total_tesis)

    st.markdown("---")

    # Últimos documentos agregados
    st.subheader("📌 Últimos documentos agregados")

    ultimos_libros = obtener_ultimos_contenidos(db, Libros)
    ultimos_revistas = obtener_ultimos_contenidos(db, Revistas)
    ultimos_tesis = obtener_ultimos_contenidos(db, Tesis)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("📚 **Libros:**")
        for _, contenido in ultimos_libros:
            st.write(f"- {contenido.Titulo}")
    with col2:
        st.write("📰 **Revistas:**")
        for _, contenido in ultimos_revistas:
            st.write(f"- {contenido.Titulo}")
    with col3:
        st.write("🎓 **Tesis:**")
        for _, contenido in ultimos_tesis:
            st.write(f"- {contenido.Titulo}")

    st.markdown("---")
    st.success("🎯 Panel listo para administrar el contenido y usuarios.")

if __name__ == "__main__":
    main()