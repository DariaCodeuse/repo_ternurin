import sys
from pathlib import Path

# Añade el directorio padre al path de Python
sys.path.append(str(Path(__file__).parent.parent))

from db.db import engine, Base
from models import Usuario, Contenido  # Importa todos tus modelos aquí

def init_db():
    print("Creando tablas...")
    Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas exitosamente!")

if __name__ == "__main__":
    init_db()