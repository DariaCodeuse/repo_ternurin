import streamlit as st
from utils import construir_ruta_archivo, extraer_portada_pdf
import os

def buscador_contenido(db, Contenido):
    _, col, _ = st.columns([1, 6, 1])
    with col:
        st.subheader("🎓 Bienvenido al Repositorio Académico", divider="rainbow")
        query = st.text_input("🔍 Buscar contenido", placeholder="Escribe un título o palabra clave...")

    if query:
        st.subheader("🔎 Resultados de búsqueda")
        resultados = db.query(Contenido).filter(
            (Contenido.Titulo.ilike(f"%{query}%")) |
            (Contenido.Materia.ilike(f"%{query}%"))
        ).all()

        if resultados:
            for item in resultados:
                with st.expander(f"📚 {item.Titulo} ({item.TipoContenido})"):
                    colData, colImg = st.columns([2, 1])
                    ruta_pdf = construir_ruta_archivo(item.Titulo, item.TipoContenido)
                    portada = extraer_portada_pdf(ruta_pdf)

                    with colData:
                        st.write(f"**Formato:** {item.Formato}")
                        st.write(f"**Estado:** {item.Estado}")
                        st.write(f"**Vistas:** {item.Vistas}")
                        st.write(f"**Autor:** {item.Autor}")
                        st.write(f"**Fecha de Subida:** {item.FechaSubida.strftime('%d/%m/%Y') if item.FechaSubida else 'N/A'}")
                        st.markdown(f"**Descripción:**  \n{item.Descripcion}")

                        if os.path.exists(ruta_pdf):
                            with open(ruta_pdf, "rb") as f:
                                st.download_button(
                                    label="⬇️ Descargar contenido",
                                    data=f.read(),
                                    file_name=f"{item.Titulo}.pdf",
                                    mime="application/pdf",
                                    use_container_width=True
                                )

                    with colImg:
                        if portada:
                            st.image(portada, caption=f"Portada de {item.Titulo}", use_container_width=True)
        else:
            st.info("No se encontraron resultados.")
        st.markdown("---")
