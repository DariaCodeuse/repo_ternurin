import streamlit as st
from PIL import Image
from db import get_db
from utils import registrar_estudiante

# Página de Registro
def main():
    db = next(get_db())  # Obtiene la sesión de base de datos

    col1, col2 = st.columns([1, 1], gap="large", vertical_alignment="center")

    with col1:
        st.title("Registro de Usuario")
        with st.form("Formulario de Registro Usuario", clear_on_submit=True):
            nombre = st.text_input("Nombre(s):")

            col_ap, col_am = st.columns(2)
            apellido_paterno = col_ap.text_input("Apellido Paterno:")
            apellido_materno = col_am.text_input("Apellido Materno:")

            correo = st.text_input("Correo Electrónico:")

            col_mat, col_sem = st.columns(2)
            matricula = col_mat.text_input("Matrícula:")
            semestre = col_sem.number_input("Semestre:", min_value=1, max_value=12, step=1)

            carrera = st.selectbox(
                "Carrera:",
                [
                    "Ingeniería en Desarrollo y Tecnologías de Software",
                    "Licenciatura en Sistemas Computacionales"
                ]
            )

            col_pass1, col_pass2 = st.columns(2)
            contraseña = col_pass1.text_input("Contraseña:", type="password")
            confirmar_contraseña = col_pass2.text_input("Confirmar Contraseña:", type="password")

            if st.form_submit_button("Registrar Usuario", use_container_width=True):
                success, message = registrar_estudiante(
                    db, nombre,apellido_paterno, apellido_materno, correo, matricula, semestre, carrera, contraseña, confirmar_contraseña, rol="usuario"
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)

    with col2:
        imagen = Image.open('./images/registro.png')
        st.image(imagen, use_container_width=True)
