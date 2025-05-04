import base64
import os
import streamlit as st

def visualizar_pdf(titulo: str, ruta_pdf: str): 
    """Muestra un visor de PDF con opciones para mostrar u ocultar el contenido."""
    clave_estado = f"mostrar_pdf_{titulo.replace(' ', '_')}"

    if clave_estado not in st.session_state:
        st.session_state[clave_estado] = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Ver contenido", key=f"ver_{titulo}"):
            st.session_state[clave_estado] = True
    with col2:
        if st.button("❌ Ocultar visualizador", key=f"ocultar_{titulo}"):
            st.session_state[clave_estado] = False

    if st.session_state[clave_estado]:
        if os.path.exists(ruta_pdf):
            with open(ruta_pdf, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                visor = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900px" type="application/pdf"></iframe>'
                st.markdown(visor, unsafe_allow_html=True)
        else:
            st.warning("Archivo PDF no encontrado.")
