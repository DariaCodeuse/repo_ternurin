from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Podcasts(Base):
    __tablename__ = "Podcasts"
    
    ContenidoID = Column(Integer, ForeignKey("Contenido.ContenidoID", ondelete="CASCADE"), primary_key=True)
    Duracion = Column(Integer, nullable=False)
    Locutor = Column(String(100), nullable=False)
    Tema = Column(String(255), nullable=False)
    Episodios = Column(Integer, nullable=False)
    
    __table_args__ = (
        CheckConstraint("Episodios >= 1", name="chk_podcasts_episodios"),
    )