# -*- coding: utf-8 -*-
"""
STREAMLIT CLOUD APP — LABORATORIO DE ESTUDIO DE DIABETES PARA ENFERMERÍA
Dirección Académica: Dr. Marcos Gamond (60 hs cátedra • 10 Unidades)
MODO PÚBLICO / ALUMNO (Sin paneles de edición ni carga docente + Videos y Podcasts integrados)
"""
import os
import re
import json
import base64
import streamlit as st
import streamlit.components.v1 as components

from programa_academico import META_PROGRAMA, UNIDADES_ACADEMICAS
from multimedia_notebooklm import RECURSOS_MULTIMEDIA_UNIDADES
from consensos_engine import CONSENSOS_OFICIALES, ALGORITMOS_INTERACTIVOS

try:
    from campus_ui_bundle import (
        HTML_TEMPLATE,
        CSS_CONTENT,
        JS_CONTENT,
        SVG_DATA_URI,
        INFOGRAFIAS_DATA_URI,
        UNIT_THUMBNAILS_URI,
    )
except ImportError:
    HTML_TEMPLATE = ""
    CSS_CONTENT = ""
    JS_CONTENT = ""
    SVG_DATA_URI = ""
    INFOGRAFIAS_DATA_URI = {}
    UNIT_THUMBNAILS_URI = {}

st.set_page_config(
    page_title="Laboratorio de Estudio de Diabetes para Enfermería — Dr. Marcos Gamond",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Estilo para que el Campus ocupe toda la pantalla de Streamlit sin márgenes blancos
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {height: 0px !important; min-height: 0px !important; visibility: hidden;}
      .block-container {
        padding-top: 0.25rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.4rem !important;
        padding-right: 0.4rem !important;
        max-width: 100% !important;
      }
      iframe {
        border: none !important;
        width: 100% !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
MULTIMEDIA_DIR = os.path.join(STATIC_DIR, "multimedia")
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/marcosgamond-hash/laboratorio-diabetes-enfermeria-/main"


def buscar_archivo_media(filename: str) -> str:
    """Busca un archivo .mp4 o .mp3 tanto en la raíz del repo como en static/multimedia/."""
    p_root = os.path.join(BASE_DIR, filename)
    if os.path.exists(p_root):
        return p_root
    p_mm = os.path.join(MULTIMEDIA_DIR, filename)
    if os.path.exists(p_mm):
        return p_mm
    return ""


def cargar_archivos_ui():
    """Carga HTML, CSS, JS y SVG desde static/ si existen, o desde campus_ui_bundle.py."""
    html_p = os.path.join(STATIC_DIR, "index.html")
    css_p = os.path.join(STATIC_DIR, "css", "diaguias.css")
    js_p = os.path.join(STATIC_DIR, "js", "diaguias.js")
    svg_p = os.path.join(STATIC_DIR, "assets", "circulo_azul_diabetes.svg")

    html_str = open(html_p, "r", encoding="utf-8").read() if os.path.exists(html_p) else HTML_TEMPLATE
    css_str = open(css_p, "r", encoding="utf-8").read() if os.path.exists(css_p) else CSS_CONTENT
    js_str = open(js_p, "r", encoding="utf-8").read() if os.path.exists(js_p) else JS_CONTENT

    if os.path.exists(svg_p):
        svg_uri = "data:image/svg+xml;base64," + base64.b64encode(open(svg_p, "rb").read()).decode("ascii")
    else:
        svg_uri = SVG_DATA_URI

    return html_str, css_str, js_str, svg_uri


def construir_datos_programa():
    """Arma el JSON completo de las 10 unidades con sus infografías, videos y podcasts."""
    unidades_enriquecidas = []
    for u in UNIDADES_ACADEMICAS:
        copia = json.loads(json.dumps(u))
        uid = u["id"]
        num = u["numero"]
        mm = json.loads(json.dumps(RECURSOS_MULTIMEDIA_UNIDADES.get(uid, {})))

        path_audio = buscar_archivo_media(f"unidad_{num}.mp3")
        path_video = buscar_archivo_media(f"unidad_{num}.mp4")
        info_uri = INFOGRAFIAS_DATA_URI.get(num) or INFOGRAFIAS_DATA_URI.get(str(num))
        tiene_infografia = bool(info_uri) or os.path.exists(os.path.join(MULTIMEDIA_DIR, f"unidad_{num}_infografia.png"))

        mm["estado_archivos"] = {
            "tiene_audio": bool(path_audio),
            "tiene_video": bool(path_video),
            "tiene_infografia": tiene_infografia,
            "tiene_pdf": False,
        }
        if path_video:
            mm["video_clase_url"] = f"{GITHUB_RAW_BASE}/unidad_{num}.mp4"
        if path_audio:
            mm["audio_podcast_url"] = f"{GITHUB_RAW_BASE}/unidad_{num}.mp3"
        if info_uri:
            mm["infografia_data_uri"] = info_uri

        copia["multimedia"] = mm
        unidades_enriquecidas.append(copia)

    return {
        "meta": META_PROGRAMA,
        "unidades": unidades_enriquecidas,
    }


def construir_html_completo():
    html_str, css_str, js_str, svg_uri = cargar_archivos_ui()
    prog_data = construir_datos_programa()
    cons_data = {
        "consensos": CONSENSOS_OFICIALES,
        "algoritmos": ALGORITMOS_INTERACTIVOS,
    }

    # Reemplazar logo SVG y foto inicial por data URI
    html_str = html_str.replace('src="/static/assets/circulo_azul_diabetes.svg"', f'src="{svg_uri}"')
    thumb_1 = UNIT_THUMBNAILS_URI.get(1) or UNIT_THUMBNAILS_URI.get("1") or svg_uri
    html_str = html_str.replace('src="/static/assets/paciente_internacion.jpg"', f'src="{thumb_1}"')

    # CSS extra para MODO ALUMNO / PÚBLICO: oculta cualquier control de edición, subida o prompts de NotebookLM
    student_mode_css = """
      button[onclick*="viewUploadNLM"],
      button[onclick*="copiarPromptInfografiaUnidad"],
      button[onclick*="copiarPromptNotebookLM"],
      #viewUploadNLM,
      #btnDownloadNotebookLM,
      details:has(#newRagDocTitle) {
        display: none !important;
      }
    """

    # Inyectar CSS y datos precargados en <head>
    preload_script = f"""
    <style>{css_str}\n{student_mode_css}</style>
    <script>
      window.__STREAMLIT_STATIC_MODE__ = true;
      window.__UNIT_THUMBNAILS__ = {json.dumps(UNIT_THUMBNAILS_URI, ensure_ascii=False)};
      window.__PRELOADED_PROGRAMA__ = {json.dumps(prog_data, ensure_ascii=False)};
      window.__PRELOADED_CONSENSOS__ = {json.dumps(cons_data, ensure_ascii=False)};
    </script>
    """
    html_str = html_str.replace('<link rel="stylesheet" href="/static/css/diaguias.css?v=5.7" />', preload_script)
    if preload_script not in html_str:
        html_str = html_str.replace("</head>", preload_script + "\n</head>")

    # Reemplazar script JS externo por JS inline
    html_str = re.sub(
        r'<script\s+src="/static/js/diaguias\.js[^"]*"></script>',
        lambda _m: f"<script>{js_str}</script>",
        html_str,
    )

    return html_str


# Renderizar el Campus Completo Interactivo en Modo Alumno
html_campus = construir_html_completo()
components.html(html_campus, height=2150, scrolling=True)
