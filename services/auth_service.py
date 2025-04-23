from streamlit import session_state as st
from components.database_utils import obtener_sesion
from components.auth_utils import autenticar_usuario

def iniciar_sesion(correo: str, contraseña: str, rol: str) -> dict:
    """
    Maneja toda la lógica de autenticación
    Retorna:
        {
            "exito": bool,
            "mensaje": str,
            "nombre": str (opcional)
        }
    """
    with obtener_sesion() as db:
        autenticado, usuario = autenticar_usuario(correo, contraseña, db)
        
        if not autenticado or not usuario:
            return {
                "exito": False,
                "mensaje": "Correo o contraseña incorrectos"
            }
        
        # Verificar coincidencia de rol
        rol_usuario = "admin" if usuario.Rol == "Administrador" else "usuario"
        if (rol == "Administrador" and rol_usuario != "admin") or \
           (rol == "Usuario" and rol_usuario != "usuario"):
            return {
                "exito": False,
                "mensaje": "No tienes permisos para este rol"
            }
        
        # Actualizar sesión
        st.session_state.update({
            'autenticado': True,
            'rol': rol_usuario,
            'usuario_id': usuario.UsuarioID,
            'nombre': f"{usuario.Nombre} {usuario.A_Paterno}",
            'view': 'inicio' if rol_usuario == 'usuario' else 'panel_admin'
        })
        
        return {
            "exito": True,
            "mensaje": "Autenticación exitosa",
            "nombre": f"{usuario.Nombre} {usuario.A_Paterno}"
        }