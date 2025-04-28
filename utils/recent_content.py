import streamlit as st
import os
from utils import construir_ruta_archivo, extraer_portada_pdf

def mostrar_contenido_reciente(db, Contenido):
    st.subheader("🆕 Contenido Reciente", divider="rainbow")
    recientes = db.query(Contenido).order_by(Contenido.FechaSubida.desc()).limit(4).all()

    if recientes:
        cols = st.columns(4)

        st.markdown("""<style>
        div[data-testid="column"] { flex: 1 1 25% !important; min-width: 23% !important; }
        @media (max-width: 1000px) {
            div[data-testid="column"] { min-width: 48% !important; max-width: 50% !important; }
        }
        </style>""", unsafe_allow_html=True)

        for idx, item in enumerate(recientes):
            with cols[idx]:
                with st.container(border=True, height=700):
                    st.markdown("""<div style="display:flex;flex-direction:column;align-items:center;">""", unsafe_allow_html=True)
                    
                    ruta_pdf = construir_ruta_archivo(item.Titulo, item.TipoContenido)
                    portada = extraer_portada_pdf(ruta_pdf)

                    if portada:
                        st.image(portada, width=160, use_container_width=True)
                    else:
                        st.image("./images/placeholder_book.png", width=160, use_container_width=True)

                    st.markdown(f"<b>{item.Titulo}</b>", unsafe_allow_html=True)
                    st.markdown(f"Tipo: {item.TipoContenido}<br>Materia: {item.Materia}", unsafe_allow_html=True)

                    if st.button("Ver más", key=f"ver_mas_{item.ContenidoID}"):
                        st.session_state["ver_contenido"] = item.ContenidoID
                        st.rerun()

                    st.markdown("</div>", unsafe_allow_html=True)

        if "ver_contenido" in st.session_state:
            detalle_id = st.session_state["ver_contenido"]
            seleccionado = db.query(Contenido).filter_by(ContenidoID=detalle_id).first()
            if seleccionado:
                st.markdown("---")
                st.subheader(f"📘 {seleccionado.Titulo}")
                st.write(f"**Autor:** {seleccionado.Autor}")
                st.write(f"**Descripción:** {seleccionado.Descripcion}")
                st.write(f"**Tipo:** {seleccionado.TipoContenido}")
                st.write(f"**Formato:** {seleccionado.Formato}")
                st.write(f"**Palabras clave:** {seleccionado.Materia}")
                st.write(f"**Fecha de subida:** {seleccionado.FechaSubida}")

                ruta_pdf = construir_ruta_archivo(seleccionado.Titulo, seleccionado.TipoContenido)
                if os.path.exists(ruta_pdf):
                    with open(ruta_pdf, "rb") as f:
                        st.download_button("📂 Acceder al contenido", f.read(), file_name=f"{seleccionado.Titulo}.pdf", mime="application/pdf")
                else:
                    st.warning("Archivo no encontrado.")
    else:
        st.info("No hay contenido reciente disponible.")
