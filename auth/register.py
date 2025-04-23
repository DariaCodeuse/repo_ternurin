import streamlit as st
from PIL import Image
from werkzeug.security import generate_password_hash
from db import get_db
from models import Usuario, Estudiantes  # Asegúrate que estos estén bien importados

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
                campos_obligatorios = [nombre, apellido_paterno, apellido_materno, correo, matricula, contraseña, confirmar_contraseña, carrera]
                if not all(campos_obligatorios):
                    st.error("Todos los campos son obligatorios.")
                elif contraseña != confirmar_contraseña:
                    st.error("Las contraseñas no coinciden.")
                elif db.query(Usuario).filter_by(Email=correo).first():
                    st.error("El correo ya está registrado.")
                elif db.query(Estudiantes).filter_by(Matricula=matricula).first():
                    st.error("La matrícula ya está en uso.")
                else:
                    nuevo_usuario = Usuario(
                        Nombre=nombre,
                        A_Paterno=apellido_paterno,
                        A_Materno=apellido_materno,
                        Email=correo,
                        Contraseña=generate_password_hash(contraseña),
                        Rol="usuario"
                    )
                    db.add(nuevo_usuario)
                    db.commit()

                    nuevo_estudiante = Estudiantes(
                        UsuarioID=nuevo_usuario.UsuarioID,
                        Matricula=matricula,
                        Semestre=semestre,
                        Carrera=carrera
                    )
                    db.add(nuevo_estudiante)
                    db.commit()

                    st.success("Registro exitoso. Ahora puedes iniciar sesión.")
                    st.session_state.view = "login"

    with col2:
        imagen = Image.open('./images/registro.png')
        st.image(imagen, use_container_width=True)
