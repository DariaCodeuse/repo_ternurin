from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Videos(Base):
    __tablename__ = "Videos"
    
    ContenidoID = Column(Integer, ForeignKey("Contenido.ContenidoID", ondelete="CASCADE"), primary_key=True)
    Duracion = Column(Integer, nullable=False)
    Tamaño = Column(Integer, nullable=False)
    Resolucion = Column(String(20), nullable=False)
    
    __table_args__ = (
        CheckConstraint("Duracion > 0", name="chk_videos_duracion"),
        CheckConstraint("Tamaño > 0", name="chk_videos_tamaño"),
    )
    