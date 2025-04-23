from sqlalchemy.orm import Session
from sqlalchemy import desc
from models import Contenido

def contar_registros(db: Session, modelo):
    return db.query(modelo).count()

def obtener_ultimos_contenidos(db: Session, modelo, limite=5):
    return db.query(modelo, Contenido)\
             .join(Contenido, Contenido.ContenidoID == modelo.ContenidoID)\
             .order_by(desc(Contenido.ContenidoID))\
             .limit(limite)\
             .all()