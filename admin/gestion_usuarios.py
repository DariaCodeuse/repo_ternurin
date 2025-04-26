import streamlit as st
from db import get_db
from models import Usuario, Estudiantes
from sqlalchemy.orm import Session
from utils import registrar_estudiante, registrar_administrador

def main():
    st.title("👤 Gestión de Usuarios")
    st.write("Aquí podrás gestionar los usuarios.")

    # Inicializamos la lista de usuarios en session_state si no existe
    db: Session = next(get_db())

    # Obtener todos los usuarios
    usuarios = db.query(Usuario).all()
    roles = ["admin", "usuario"]

    # Filtro por rol
    colTitulo, colFiltro = st.columns([2, 1])
    with colTitulo:
        st.subheader("📑 Lista de Usuarios")
    with colFiltro:
        filtro_rol = st.selectbox("Filtrar por rol:", ["Todos"] + roles)
    if filtro_rol != "Todos":
        usuarios = [u for u in usuarios if u.Rol == filtro_rol]

    # Mostrar usuarios en tabla
    for usuario in usuarios:
        # Añadir icono dependiendo del rol
        if usuario.Rol == "admin":
            icono_rol = "🛡️"  # Icono de escudo para administradores
        else:
            icono_rol = "🎓"  # Icono de persona para usuarios

        with st.expander(f"{icono_rol} {usuario.Nombre} {usuario.A_Paterno} ({usuario.Rol})"):
            st.write(f"**Email:** {usuario.Email}")

            # Añadir iconos y colores para diferenciar roles
            if usuario.Rol == "admin":
                st.markdown(
                    "<span style='color: red; font-weight: bold;'>️ Administrador</span>", unsafe_allow_html=True)
            else:
                st.markdown(
                    "<span style='color: blue; font-weight: bold;'> Usuario</span>", unsafe_allow_html=True)

            # Mostrar datos de estudiantes si existen
            if usuario.Rol == "usuario":
                estudiante = db.query(Estudiantes).filter_by(
                    UsuarioID=usuario.UsuarioID).first()
                if estudiante:
                    st.write(f"**Matrícula:** {estudiante.Matricula}")
                    st.write(f"**Semestre:** {estudiante.Semestre}")
                    st.write(f"**Carrera:** {estudiante.Carrera}")

            col1, col2 = st.columns(2)
            with col1:
                nuevo_rol = st.selectbox("Cambiar rol:", roles, index=roles.index(
                    usuario.Rol), key=f"rol_{usuario.UsuarioID}")
            with col2:
                if st.button("Guardar cambios", key=f"guardar_{usuario.UsuarioID}"):
                    usuario.Rol = nuevo_rol
                    db.commit()
                    st.success("Rol actualizado.")
                    st.rerun()

            if st.button("❌ Eliminar usuario", key=f"eliminar_{usuario.UsuarioID}"):
                db.delete(usuario)
                db.commit()
                st.warning("Usuario eliminado.")
                st.rerun()

    # Añadir nuevo usuario
    st.subheader("➕ Registro de Usuario")
    registro_type = st.radio("¿Qué tipo de usuario será?:", ["Administrador", "Usuario"], horizontal=True)

    if registro_type == "Administrador":
        with st.form("Formulario de Registro Admin", clear_on_submit=True):
            colNombre, colAPaterno, colAMaterno = st.columns(3)
            with colNombre:
                nombre = st.text_input("Nombre(s):")
            with colAPaterno:
                apellido_paterno = st.text_input("Apellido Paterno:")
            with colAMaterno:
                apellido_materno = st.text_input("Apellido Materno:")

            correo = st.text_input("Correo Electrónico:")

            colPass1, colPass2 = st.columns(2)
            with colPass1:
                contraseña = st.text_input("Contraseña:", type="password")
            with colPass2:
                confirmar_contraseña = st.text_input("Confirmar Contraseña:", type="password")

            if st.form_submit_button("Registrar Admin", use_container_width=True):
                success, message = registrar_administrador(
                        db, nombre,apellido_paterno, apellido_materno, correo, contraseña, confirmar_contraseña, rol="admin"
                    )

                if success:
                    st.success(message)
                else:
                    st.error(message)

    elif registro_type == "Usuario":
        with st.form("Formulario de Registro Usuario", clear_on_submit=True):
            colNombre, colAPaterno, colAMaterno = st.columns(3)
            with colNombre:
                nombre = st.text_input("Nombre(s):")
            with colAPaterno:
                apellido_paterno = st.text_input("Apellido Paterno:")
            with colAMaterno:
                apellido_materno = st.text_input("Apellido Materno:")

            correo = st.text_input("Correo Electrónico:")

            colMatricula, colSemestre, colCarrera = st.columns([1, 1, 2], vertical_alignment="center")
            with colMatricula:
                matricula = st.text_input("Matrícula:")
            with colSemestre:
                semestre = st.number_input("Semestre:", min_value=1, max_value=12, step=1)
            with colCarrera:
                carrera = st.selectbox("Carrera:", ["Ingeniería en Desarrollo y Tecnologías de Software", "Licenciatura en Sistemas Computacionales"])
            
            colPass1, colPass2 = st.columns(2)
            with colPass1:
                contraseña = st.text_input("Contraseña:", type="password")
            with colPass2:
                confirmar_contraseña = st.text_input("Confirmar Contraseña:", type="password")

            if st.form_submit_button("Registrar Usuario", use_container_width=True):
                success, message = registrar_estudiante(
                    db, nombre,apellido_paterno, apellido_materno, correo, matricula, semestre, carrera, contraseña, confirmar_contraseña, rol="usuario"
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)

if __name__ == "__main__":
    main()
