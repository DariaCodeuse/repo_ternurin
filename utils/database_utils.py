from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from db.db import SessionLocal
from models.usuario import Usuario  # Importación añadida
from models.estudiantes import Estudiantes  # Importación añadida

@contextmanager
def obtener_sesion():
    """Gestor de contexto para sesiones de DB"""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def usuario_existe(db, correo: str, matricula: str) -> tuple[bool, str]:
    """Verifica si correo o matrícula ya están registrados"""
    # Ahora las consultas pueden ejecutarse correctamente
    if db.query(Usuario).filter_by(Email=correo).first():
        return True, "El correo ya está registrado"
    if db.query(Estudiantes).filter_by(Matricula=matricula).first():
        return True, "La matrícula ya está en uso"
    return False, ""