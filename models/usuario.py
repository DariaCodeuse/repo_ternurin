from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Usuario(Base):
    __tablename__ = "Usuario"
    
    UsuarioID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(50), nullable=False)
    A_Paterno = Column(String(50), nullable=False)
    A_Materno = Column(String(50), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Contraseña = Column(Text, nullable=False)
    Rol = Column(String(18), nullable=False)
    
    __table_args__ = (
        CheckConstraint("Rol IN ('admin', 'usuario')", name="chk_usuario_rol"),
    )
