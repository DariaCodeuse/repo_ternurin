import streamlit as st
from datetime import datetime
from models import Contenido, Libros, Revistas, Tesis, Videos, Podcasts
from utils import construir_ruta_archivo
from sqlalchemy.orm import Session
import os

def ui_registro_contenido(tipos_contenido, palabras_clave, formatos):
    st.subheader("➕ Agregar Nuevo Contenido")
    
    colTipo, colTitulo = st.columns([1, 2])
    with colTipo:
        tipo_contenido = st.selectbox("Selecciona el tipo de contenido:", tipos_contenido, index=0)
    with colTitulo:
        titulo = st.text_input("Título:")

    autor = st.text_area("Autor:", placeholder="Nombre del autor o autores")
    descripcion = st.text_area("Descripción:", placeholder="Descripción del contenido")
    keywords = st.selectbox("Palabras clave: ", palabras_clave, index=0, placeholder="Selecciona una palabra clave")

    colFormato, colEstado = st.columns([1, 1])
    with colFormato:
        formato = st.selectbox("Formato (ej. PDF, MP4, MP3):", formatos, placeholder="Selecciona un formato")
    with colEstado:
        estado = st.selectbox("Estado:", ["Publicado", "Borrador"])

    # Variables específicas por tipo de contenido
    tipo_contenido_especifico = {}
    if tipo_contenido == "Libro":
        tipo_contenido_especifico = formulario_libro()
    elif tipo_contenido == "Revista":
        tipo_contenido_especifico = formulario_revista()
    elif tipo_contenido == "Tesis":
        tipo_contenido_especifico = formulario_tesis()
    elif tipo_contenido == "Video":
        tipo_contenido_especifico = formulario_video()
    elif tipo_contenido == "Podcast":
        tipo_contenido_especifico = formulario_podcast()

    archivo = st.file_uploader("Sube el archivo del contenido:", type=None)

    return {
        "tipo_contenido": tipo_contenido,
        "titulo": titulo,
        "autor": autor,
        "descripcion": descripcion,
        "keywords": keywords,
        "formato": formato,
        "estado": estado,
        "archivo": archivo,
        **tipo_contenido_especifico
    }

def formulario_libro():
    colisbn, colEditorial = st.columns([1, 2])
    with colisbn:
        isbn = st.text_input("ISBN:")
    with colEditorial:
        editorial = st.text_input("Editorial:")

    colAño, colEdicion = st.columns([1, 1])
    with colAño:
        año_publicacion = st.number_input("Año de Publicación:", min_value=1900, max_value=datetime.today().year, step=1)
    with colEdicion:
        edicion = st.number_input("Edición:", min_value=1, step=1)

    return {"isbn": isbn, "editorial": editorial, "año_publicacion": año_publicacion, "edicion": edicion}

def formulario_revista():
    colEstado, colVolumen = st.columns([1, 1])
    with colEstado:
        volumen = st.number_input("Volumen:", min_value=1, step=1)
    with colVolumen:
        numero = st.number_input("Número:", min_value=1, step=1)

    return {"volumen": volumen, "numero": numero}

def formulario_tesis():
    colAsesor, colAño = st.columns([2, 1])
    with colAsesor:
        asesor = st.text_input("Asesor:")
    with colAño:
        año_defensa = st.number_input("Año de Defensa:", min_value=1900, max_value=datetime.today().year, step=1)

    return {"asesor": asesor, "año_defensa": año_defensa}

def formulario_video():
    colDuracion, colTamaño, colResolucion = st.columns([1, 1, 1 ])
    with colDuracion:
        duracion = st.number_input("Duración (en minutos):", min_value=1, step=1)
    with colTamaño:
        tamaño = st.number_input("Tamaño (MB):", min_value=1, step=1)
    with colResolucion:
        resolucion = st.text_input("Resolución (ej. 1080p, 4K):")

    return {"duracion": duracion, "tamaño": tamaño, "resolucion": resolucion}

def formulario_podcast():
    colTema, colDuracion, colEpisodios = st.columns([1, 1, 1])
    with colTema:
        tema = st.text_input("Tema:")
    with colDuracion:
        duracion = st.number_input("Duración (en minutos):", min_value=1, step=1)
    with colEpisodios:
        episodios = st.number_input("Número de Episodios:", min_value=1, step=1)
    locutor = st.text_input("Locutor:")

    return {"tema": tema, "duracion": duracion, "episodios": episodios, "locutor": locutor}

def agregar_contenido(db: Session, contenido_data: dict):
    tipo_contenido = contenido_data['tipo_contenido']
    titulo = contenido_data['titulo']
    autor = contenido_data['autor']
    descripcion = contenido_data['descripcion']
    keywords = contenido_data['keywords']
    formato = contenido_data['formato']
    estado = contenido_data['estado']
    archivo = contenido_data['archivo']

    # Validación
    if not titulo or not descripcion or not formato or not archivo:
        st.error("Todos los campos generales y el archivo son obligatorios.")
        return

    # Guardar contenido en la base de datos
    nuevo_contenido = Contenido(
        Titulo=titulo,
        Autor=autor,
        Descripcion=descripcion,
        TipoContenido=tipo_contenido,
        Keywords=keywords,
        Vistas=0,
        Estado=estado,
        Formato=formato,
        FechaSubida=datetime.utcnow(),
        UsuarioID=1  # Cambiar el ID según corresponda
    )
    
    db.add(nuevo_contenido)
    db.commit()

    # Guardar archivo localmente
    nombre_archivo = archivo.name
    ruta_archivo = construir_ruta_archivo(nombre_archivo, tipo_contenido)
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

    with open(ruta_archivo, "wb") as f:
        f.write(archivo.read())

    st.success(f"{tipo_contenido} '{titulo}' agregado exitosamente.")

    # Relacionar con información específica de cada tipo de contenido
    contenido_id = nuevo_contenido.ContenidoID

    if tipo_contenido == "Libro":
        db.add(Libros(ContenidoID=contenido_id, isbn=contenido_data["isbn"], Editorial=contenido_data["editorial"], AñoPublicacion=contenido_data["año_publicacion"], Edicion=contenido_data["edicion"]))
    elif tipo_contenido == "Revista":
        db.add(Revistas(ContenidoID=contenido_id, Volumen=contenido_data["volumen"], Numero=contenido_data["numero"]))
    elif tipo_contenido == "Tesis":
        db.add(Tesis(ContenidoID=contenido_id, Asesor=contenido_data["asesor"], AñoDefensa=contenido_data["año_defensa"]))
    elif tipo_contenido == "Video":
        db.add(Videos(ContenidoID=contenido_id, Duracion=contenido_data["duracion"], Tamaño=contenido_data["tamaño"], Resolucion=contenido_data["resolucion"]))
    elif tipo_contenido == "Podcast":
        db.add(Podcasts(ContenidoID=contenido_id, Duracion=contenido_data["duracion"], Locutor=contenido_data["locutor"], Tema=contenido_data["tema"], Episodios=contenido_data["episodios"]))

    db.commit()
