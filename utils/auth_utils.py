from streamlit import session_state as st
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import Session
from models.usuario import Usuario
from models.estudiantes import Estudiantes
import re

# -------------------------------
# Funciones de Validación (EXISTENTES)
# -------------------------------
def validar_correo(correo: str) -> bool:
    """Valida formato de correo institucional UNACH"""
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@(unach|estudiantes\.unach)\.mx$', correo))

def validar_matricula(matricula: str) -> bool:
    """Valida formato de matrícula UNACH (8 caracteres alfanuméricos)"""
    return len(matricula) == 8 and matricula.isalnum()

# -------------------------------
# Funciones de Autenticación (EXISTENTES)
# -------------------------------
def autenticar_usuario(correo: str, contraseña: str, db: Session) -> tuple[bool, Usuario | None]:
    """
    Autentica usuario contra la base de datos.
    
    Args:
        correo: Correo institucional
        contraseña: Contraseña en texto plano (se verifica contra el hash)
        db: Sesión de SQLAlchemy
    
    Returns:
        tuple: (success: bool, usuario: Usuario | None)
    """
    usuario = db.query(Usuario).filter_by(Email=correo).first()
    
    if usuario and check_password_hash(usuario.Contraseña, contraseña):
        return True, usuario
    return False, None

def crear_hash_contraseña(contraseña: str) -> str:
    """Genera hash seguro para almacenamiento usando werkzeug"""
    return generate_password_hash(contraseña)

# -------------------------------
# Funciones Añadidas (NUEVAS)
# -------------------------------
def verificar_sesion_activa(session_state: dict) -> bool:
    """
    Verifica si hay una sesión activa válida.
    Args:
        session_state: El st.session_state de Streamlit
    Returns:
        bool: True si la sesión es válida
    """
    required_keys = {'autenticado', 'rol', 'usuario_id'}
    return all(key in session_state for key in required_keys) and session_state['autenticado']

def redirigir_si_autenticado(session_state: dict, destino: str = 'main'):
    """
    Redirige a otra vista si el usuario ya está autenticado.
    Útil para evitar mostrar login/registro a usuarios ya logueados.
    """
    if verificar_sesion_activa(session_state):
        session_state['view'] = destino
        st.rerun()