from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Contenido(Base):
    __tablename__ = "Contenido"

    ContenidoID = Column(Integer, primary_key=True, autoincrement=True)
    Titulo = Column(String(100), nullable=False)
    Autor = Column(Text)
    Descripcion = Column(Text)
    TipoContenido = Column(String(50), nullable=False)
    Materia = Column(Text)
    Vistas = Column(Integer, default=0)
    Estado = Column(String(20), nullable=False)
    Formato = Column(String(50), nullable=False)
    FechaSubida = Column(Date, default=datetime.date.today)
    UsuarioID = Column(Integer, ForeignKey("Usuario.UsuarioID", ondelete="SET NULL"), nullable=False)

    __table_args__ = (
        CheckConstraint("Estado IN ('Publicado', 'Borrador')", name="chk_contenido_estado"),
    )