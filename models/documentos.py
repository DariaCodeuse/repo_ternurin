from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Documentos(Base):
    __tablename__ = "Documentos"
    
    ContenidoID = Column(Integer, ForeignKey("Contenido.ContenidoID", ondelete="CASCADE"), primary_key=True)
    Tamaño = Column(Integer, nullable=False)
    Paginas = Column(Integer, nullable=False)
    
    __table_args__ = (
        CheckConstraint("Tamaño > 0", name="chk_documentos_tamaño"),
        CheckConstraint("Paginas > 0", name="chk_documentos_paginas"),
    )