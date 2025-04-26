from werkzeug.security import generate_password_hash
from models import Usuario, Estudiantes

def registrar_administrador(db, nombre, apellido_paterno, apellido_materno, correo, contraseña, confirmar_contraseña, rol):

    # Validar campos vacíos
    campos_obligatorios = [nombre, apellido_paterno, apellido_materno, correo, contraseña, confirmar_contraseña]
    if not all(campos_obligatorios):
        return False, "Todos los campos son obligatorios."

    # Validar contraseñas
    if contraseña != confirmar_contraseña:
        return False, "Las contraseñas no coinciden."

    # Validar correo repetido
    if db.query(Usuario).filter_by(Email=correo).first():
        return False, "El correo ya está registrado."

    # Crear nuevo usuario
    nuevo_usuario = Usuario(
        Nombre=nombre,
        A_Paterno=apellido_paterno,
        A_Materno=apellido_materno,
        Email=correo,
        Contraseña=generate_password_hash(contraseña),
        Rol=rol
    )
    db.add(nuevo_usuario)
    db.commit()

    return True, "Registro exitoso."

def registrar_estudiante(db, nombre, apellido_paterno, apellido_materno, correo, matricula, semestre, carrera, contraseña, confirmar_contraseña, rol):

    # Validar campos vacíos
    campos_obligatorios = [nombre, apellido_paterno, apellido_materno, correo, contraseña, confirmar_contraseña]
    if not all(campos_obligatorios):
        return False, "Todos los campos son obligatorios."

    # Validar contraseñas
    if contraseña != confirmar_contraseña:
        return False, "Las contraseñas no coinciden."

    # Validar correo repetido
    if db.query(Usuario).filter_by(Email=correo).first():
        return False, "El correo ya está registrado."

    # Validar matrícula repetida (solo si es estudiante)
    if rol == "usuario" and db.query(Estudiantes).filter_by(Matricula=matricula).first():
        return False, "La matrícula ya está en uso."

    # Crear nuevo usuario
    nuevo_usuario = Usuario(
        Nombre=nombre,
        A_Paterno=apellido_paterno,
        A_Materno=apellido_materno,
        Email=correo,
        Contraseña=generate_password_hash(contraseña),
        Rol=rol
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

    return True, "Registro exitoso."
