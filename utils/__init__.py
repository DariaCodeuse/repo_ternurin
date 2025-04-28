from .registros_db import registrar_administrador, registrar_estudiante
from .contenidos_db import contar_registros, obtener_ultimos_contenidos, extraer_portada_pdf, construir_ruta_archivo, visualizar_pdf, descargar_pdf, obtener_contenidos, filtrar_contenidos, mostrar_contenidos
from .registro_contenido import formulario_tesis, formulario_libro, formulario_revista, formulario_video, formulario_podcast, agregar_contenido, ui_registro_contenido
from .search import buscador_contenido
from .recent_content import mostrar_contenido_reciente
from .materias_panel import panel_materias
from .ui_contenido import mostrar_contenido_materia
__all__ = [
    'registrar_administrador',
    'registrar_estudiante',
    'contar_registros',
    'obtener_ultimos_contenidos',
    'extraer_portada_pdf',
    'construir_ruta_archivo',
    'visualizar_pdf',
    'descargar_pdf',
    'obtener_contenidos',
    'filtrar_contenidos',
    'mostrar_contenidos',
    'ui_registro_contenido',
    'formulario_libro',
    'formulario_revista',
    'formulario_tesis',
    'formulario_video',
    'formulario_podcast',
    'agregar_contenido',
    'buscador_contenido',
    'mostrar_contenido_reciente',
    'panel_materias'
]