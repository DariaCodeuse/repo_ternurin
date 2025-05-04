import streamlit as st
from PIL import Image
from auth import login, register
from admin import panel as admin_panel, gestion_usuarios, gestion_contenido
from estudiantes import añadir_contenido as estudiante_añadir_contenido, inicio as estudiante_inicio
from estudiantes import materia_analisis_vulnerabilidades, materia_conmutadores_redes, materia_desarrollo_web_movil, materia_inteligencia_artificial, materia_seguridad_computo, materia_sistemas_operativos
from models.base import Base
from db import engine
import logging

# Configuración de la página
st.set_page_config(
    page_title='Repo LIDTS',
    page_icon=Image.open('./images/logo.png'),
    layout='wide',
    initial_sidebar_state='auto',
)

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
# Inicializar el estado de la sesión si no existe
if 'role' not in st.session_state:
    st.session_state.role = None
if 'view' not in st.session_state:
    st.session_state.view = "login"

def set_view(view):
    st.session_state.view = view

def logout():
    st.session_state.role = None
    st.session_state.view = "login"
    st.rerun()

st.sidebar.title("📚 Repositorio Ternurin")

if st.session_state.role is None:
    # Barra lateral para usuarios no autenticados
    auth_selection = st.sidebar.radio("Autenticación", ["👤Iniciar Sesión", "📝Registrarse"])
    if auth_selection == "👤Iniciar Sesión":
        st.session_state.view = "login"
    elif auth_selection == "📝Registrarse":
        st.session_state.view = "register"  # Cambiamos la vista a "register"

    if st.session_state.view == "login":
        login.main()
    elif st.session_state.view == "register":
        register.main()

elif st.session_state.role == "Administrador":
    # Barra lateral para administradores
    st.sidebar.subheader("Administrador")
    admin_page = st.sidebar.radio("Navegación", ["Panel", "Gestión de Usuarios", "Gestión de Contenido"])
    st.sidebar.markdown("---")
    st.sidebar.button("Cerrar Sesión", on_click=logout, use_container_width=True)

    if admin_page == "Panel":
        admin_panel.main()
    elif admin_page == "Gestión de Usuarios":
        gestion_usuarios.main()
    elif admin_page == "Gestión de Contenido":
        gestion_contenido.main()

elif st.session_state.role == "Estudiante":
    # Barra lateral para estudiantes
    st.sidebar.subheader("Estudiante")
    estudiante_page = st.sidebar.radio(
        "Navegación",
        ["Inicio",
         "Análisis de Vulverabilidades",
         "Conmutadores y Redes Inalámbricas",
         "Desarrollo Web y Móvil",
         "Inteligencia Artificial",
         "Seguridad en Cómputo",
         "Sistemas Operativos",
         "Añadir Contenido",]
    )
    st.sidebar.markdown("---")  
    st.sidebar.button("Cerrar Sesión", on_click=logout)

    if estudiante_page == "Inicio":
        estudiante_inicio.main()
    elif estudiante_page == "Añadir Contenido":
        estudiante_añadir_contenido.main()
    elif estudiante_page == "Análisis de Vulverabilidades":
        materia_analisis_vulnerabilidades.main()
    elif estudiante_page == "Conmutadores y Redes Inalámbricas":
        materia_conmutadores_redes.main()
    elif estudiante_page == "Desarrollo Web y Móvil":
        materia_desarrollo_web_movil.main()
    elif estudiante_page == "Inteligencia Artificial":
        materia_inteligencia_artificial.main()
    elif estudiante_page == "Seguridad en Cómputo":
        materia_seguridad_computo.main()
    elif estudiante_page == "Sistemas Operativos":
        materia_sistemas_operativos.main()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("¡Base de datos creada correctamente!")
