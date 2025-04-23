from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Revistas(Base):
    __tablename__ = "Revistas"
    
    ContenidoID = Column(Integer, ForeignKey("Contenido.ContenidoID", ondelete="CASCADE"), primary_key=True)
    Volumen = Column(Integer, nullable=False)
    Numero = Column(Integer, nullable=False)