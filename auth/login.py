import streamlit as st
from sqlalchemy.orm import Session
from db import get_db
from models import Usuario
from werkzeug.security import check_password_hash
from PIL import Image

def main():
    # Logo en la parte superior
    st.logo("images/logounach.png")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.title("Repositorio LIDTS")
        st.subheader("Séptimo Semestre")

        correo = st.text_input("Correo Electrónico:")
        contraseña = st.text_input("Contraseña:", type="password")

        if st.button("Iniciar Sesión", use_container_width=True):
            if not correo or not contraseña:
                st.error("Correo y contraseña son obligatorios.")
            else:
                db: Session = next(get_db())
                usuario = db.query(Usuario).filter(Usuario.Email == correo).first()

                if usuario and check_password_hash(usuario.Contraseña, contraseña):
                    rol_usuario = usuario.Rol.lower()
                    if rol_usuario == "usuario":
                        st.session_state.role = "Estudiante"
                        st.rerun()
                    elif rol_usuario == "admin":
                        st.session_state.role = "Administrador"
                        st.rerun()
                    else:
                        st.error("Rol de usuario no reconocido.")
                else:
                    st.error("Correo o contraseña incorrectos.")

    with col2:
        imagen = Image.open('./images/inicio.jpg')
        st.image(imagen, use_container_width='auto', output_format='PNG')

if __name__ == "__main__":
    main()


# import streamlit as st

# def main():
#     st.title("🔒 Iniciar Sesión")
#     username = st.text_input("Usuario:")
#     password = st.text_input("Contraseña:", type="password")
#     if st.button("Iniciar Sesión"):
#         if username == "admin" and password == "admin":
#             st.session_state.role = "Administrador"
#             st.rerun()
#         elif username == "estudiante" and password == "estudiante":
#             st.session_state.role = "Estudiante"
#             st.rerun()
#         else:
#             st.error("Credenciales incorrectas.")

# if __name__ == "__main__":
#     main()