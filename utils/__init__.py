from .registros_db import registrar_administrador, registrar_estudiante
from .contenidos_db import contar_registros, obtener_ultimos_contenidos, extraer_portada_pdf, construir_ruta_pdf, visualizar_pdf, descargar_pdf, obtener_contenidos, filtrar_contenidos, mostrar_contenidos

__all__ = [
    'registrar_administrador',
    'registrar_estudiante',
    'contar_registros',
    'obtener_ultimos_contenidos',
    'extraer_portada_pdf',
    'construir_ruta_pdf',
    'visualizar_pdf',
    'descargar_pdf',
    'obtener_contenidos',
    'filtrar_contenidos',
    'mostrar_contenidos'
]