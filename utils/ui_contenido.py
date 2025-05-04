import streamlit as st
import os
import base64
from utils import construir_ruta_archivo, extraer_portada_pdf, visualizar_pdf

def mostrar_contenido_materia(db, Contenido, materia):
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

    def mostrar_tarjetas_documentos(documentos):
        cols = st.columns(4)
        documento_seleccionado = None  # Guardamos el que elijan

        for idx, item in enumerate(documentos):
            with cols[idx]:
                with st.container(border=True):
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

                    st.markdown("</div>", unsafe_allow_html=True)

        # Mostrar detalle de documento abajo de las tarjetas, fuera del ciclo
        if "ver_contenido" in st.session_state:
            detalle_id = st.session_state["ver_contenido"]
            seleccionado = db.query(Contenido).filter_by(ContenidoID=detalle_id).first()
            if seleccionado:
                with st.container(border=True):

                    st.subheader(f"📘 {seleccionado.Titulo}")
                    st.write(f"**Autor:** {seleccionado.Autor}")
                    st.write(f"**Descripción:** {seleccionado.Descripcion}")
                    st.write(f"**Tipo:** {seleccionado.TipoContenido}")
                    st.write(f"**Formato:** {seleccionado.Formato}")
                    st.write(f"**Palabras clave:** {seleccionado.Materia}")
                    st.write(f"**Fecha de subida:** {seleccionado.FechaSubida}")

                    ruta_pdf = construir_ruta_archivo(seleccionado.Titulo, seleccionado.TipoContenido)
                    if seleccionado.Formato.lower() == "pdf":
                        clave_estado = f"mostrar_pdf_{seleccionado.Titulo.replace(' ', '_')}"

                        if clave_estado not in st.session_state:
                            st.session_state[clave_estado] = False

                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("📖 Ver contenido", key=f"ver_{seleccionado.Titulo}"):
                                st.session_state[clave_estado] = True
                        with col2:
                            if st.button("❌ Ocultar visualizador", key=f"ocultar_{seleccionado.Titulo}"):
                                st.session_state[clave_estado] = False

                        if st.session_state[clave_estado]:
                            st.write(ruta_pdf)
                            if os.path.exists(ruta_pdf):
                                with open(ruta_pdf, "rb") as f:
                                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                                    visor = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900px" type="application/pdf"></iframe>'
                                    st.markdown(visor, unsafe_allow_html=True)
                            else:
                                st.warning("Archivo PDF no encontrado.")
                    else:
                        st.warning("Archivo no encontrado o no es un PDF.")



    def mostrar_tarjetas_videos(lista):
        for item in lista:
            with st.container(border=True):
                col1, col2 = st.columns([2, 3])  # Izquierda: texto, Derecha: video

                with col1:
                    st.markdown(f"### {item.Titulo}")
                    st.markdown(f"**Autor:** {item.Autor}")
                    st.markdown(f"**Materia:** {item.Materia}")
                    st.markdown(item.Descripcion)

                with col2:
                    ruta_video = f"./files/{item.TipoContenido}/{item.Titulo.replace(' ', '_')}.{item.Formato}".lower()
                    st.video(ruta_video)

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

