from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Estudiantes(Base):
    __tablename__ = "Estudiantes"
    
    EstudianteID = Column(Integer, primary_key=True, autoincrement=True)
    UsuarioID = Column(Integer, ForeignKey("Usuario.UsuarioID", ondelete="CASCADE"), unique=True, nullable=False)
    Matricula = Column(String(10), unique=True, nullable=False)
    Semestre = Column(Integer, nullable=False)
    Carrera = Column(String(100), nullable=False)
    
    __table_args__ = (
        CheckConstraint("Semestre BETWEEN 1 AND 12", name="chk_estudiantes_semestre"),
    )
