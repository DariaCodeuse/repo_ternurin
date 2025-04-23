from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Tesis(Base):
    __tablename__ = "Tesis"
    
    ContenidoID = Column(Integer, ForeignKey("Contenido.ContenidoID", ondelete="CASCADE"), primary_key=True)
    Asesor = Column(String(100), nullable=False)
    AñoDefensa = Column(Integer, nullable=False)