from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from models.base import Base 

class Libros(Base):
    __tablename__ = "Libros"
    
    ContenidoID = Column(Integer, ForeignKey("Contenido.ContenidoID", ondelete="CASCADE"), primary_key=True)
    isbn = Column(String(20), unique=True, nullable=False)
    Editorial = Column(String(100), nullable=False)
    AñoPublicacion = Column(Integer, nullable=False)
    Edicion = Column(Integer, nullable=False)