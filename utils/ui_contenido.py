import streamlit as st
import os
from utils import construir_ruta_archivo, extraer_portada_pdf

def mostrar_contenido_materia(db, Contenido, materia):
    st.title(f"📚 Contenido de {materia}")

    # Filtrar contenido por materia
    contenidos = db.query(Contenido).filter(Contenido.Materia.ilike(f"%{materia}%")).all()

    # Separar por tipo
    documentos = [c for c in contenidos if c.TipoContenido in ['Libros', 'Tesis', 'Revistas']]
    videos = [c for c in contenidos if c.TipoContenido == 'Videos']
    audios = [c for c in contenidos if c.TipoContenido == 'Podcasts']

    # Estilos responsivos para tarjetas
    st.markdown("""<style>
    div[data-testid="column"] { flex: 1 1 25% !important; min-width: 23% !important; }
    @media (max-width: 1000px) {
        div[data-testid="column"] { min-width: 48% !important; max-width: 50% !important; }
    }
    </style>""", unsafe_allow_html=True)

    def mostrar_tarjetas_documentos(lista):
        cols = st.columns(4)
        for idx, item in enumerate(lista):
            with cols[idx % 4]:
                with st.container(border=True, height=620):
                    st.markdown("""<div style="display:flex;flex-direction:column;align-items:center;">""", unsafe_allow_html=True)

                    ruta_pdf = construir_ruta_archivo(item.Titulo, item.TipoContenido)
                    portada = extraer_portada_pdf(ruta_pdf)

                    if portada:
                        st.image(portada, width=160, use_container_width=True)
                    else:
                        st.image("./images/placeholder_book.png", width=160, use_container_width=True)

                    st.markdown(f"<b>{item.Titulo}</b>", unsafe_allow_html=True)
                    st.markdown(f"Sección: {item.TipoContenido}<br>Materia: {item.Materia}", unsafe_allow_html=True)

                    if st.button("Ver más", key=f"ver_doc_{item.ContenidoID}"):
                        st.session_state["ver_contenido"] = item.ContenidoID
                        st.rerun()

                    st.markdown("</div>", unsafe_allow_html=True)

    def mostrar_tarjetas_videos(lista):
        cols = st.columns(2)
        for idx, item in enumerate(lista):
            with cols[idx % 2]:
                with st.container(border=True, height=350):
                    ruta_video = construir_ruta_archivo(item.Titulo, item.TipoContenido)
                    portada = extraer_portada_pdf(ruta_video)  # O usar miniatura si tienes una para videos

                    if portada:
                        st.image(portada, use_container_width=True)
                    else:
                        st.image("./images/placeholder_video.png", use_container_width=True)

                    st.markdown(f"### {item.Titulo}")
                    st.markdown(f"**Autor:** {item.Autor}")
                    st.markdown(f"**Materia:** {item.Materia}")

                    if st.button("Ver más", key=f"ver_video_{item.ContenidoID}"):
                        st.session_state["ver_contenido"] = item.ContenidoID
                        st.rerun()

    def mostrar_tarjetas_audios(lista):
        # Definimos las columnas para mostrar los contenidos de forma ordenada
        cols = st.columns(2)
        for idx, item in enumerate(lista):
            with cols[idx % 2]:  # Alternamos las columnas para no sobrecargar una sola columna
                with st.container(border=True):
                    # Usamos un contenedor para mantener la estructura limpia
                    st.markdown(f"####  🎧 {item.Titulo}", unsafe_allow_html=True)
                    st.markdown(f"**Descripción:** {item.Descripcion}")

                    # Dividimos el espacio entre la imagen y los datos
                    colImg, colData = st.columns([1, 3])
                    with colImg:
                        # Imagen de placeholder o decorativa
                        ruta_audio = f"./files/{item.TipoContenido.lower()}/{item.Titulo.replace(' ', '_')}.mp3"  # Corrección en el nombre del archivo
                        if os.path.exists(ruta_audio):
                            st.image("./images/placeholder_audio.png", width=100)                        

                    with colData:
                        audio_bytes = open(ruta_audio, "rb").read()
                        st.markdown(f"**Autor:** {item.Autor}")
                        st.markdown(f"**Materia:** {item.Materia}")
                        st.audio(audio_bytes, format='audio/mp3')


    # Mostrar secciones
    if documentos:
        st.subheader("📄 Documentos", divider="rainbow")
        mostrar_tarjetas_documentos(documentos)

    if videos:
        st.subheader("🎥 Videos", divider="rainbow")
        mostrar_tarjetas_videos(videos)

    if audios:
        st.subheader("🎧 Audios", divider="rainbow")
        mostrar_tarjetas_audios(audios)

    # Si no hay contenido
    if not (documentos or videos or audios):
        st.info("No hay contenido disponible para esta materia.")

    # Mostrar detalle si hay "ver_contenido" en sesión
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

            ruta_archivo = construir_ruta_archivo(seleccionado.Titulo, seleccionado.TipoContenido)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, "rb") as f:
                    mime_type = "application/pdf" if seleccionado.TipoContenido in ['Libros', 'Tesis', 'Revistas'] else "audio/mp3" if seleccionado.TipoContenido == 'Podcasts' else "video/mp4"
                    st.download_button("📂 Acceder al contenido", f.read(), file_name=f"{seleccionado.Titulo}.{seleccionado.Formato.lower()}", mime=mime_type)
            else:
                st.warning("Archivo no encontrado.")
