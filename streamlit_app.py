# -*- coding: utf-8 -*-
"""
STREAMLIT CLOUD APP — LABORATORIO DE ESTUDIO DE DIABETES PARA ENFERMERÍA
Dirección Académica: Dr. Marcos Gamond (60 hs cátedra • 10 Unidades)
Incluye:
1. Modo Público / Alumno sin botones de edición docente.
2. Videos (.mp4) y Podcasts (.mp3) por streaming directo CDN (video/mp4 y audio/mpeg) + Reproductor nativo.
3. Sistema de Acceso (Alumno / Vista Previa / Panel de Estadísticas y Notas del Director Académico).
"""
import os
import re
import json
import base64
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

from programa_academico import META_PROGRAMA, UNIDADES_ACADEMICAS
from multimedia_notebooklm import RECURSOS_MULTIMEDIA_UNIDADES
from consensos_engine import CONSENSOS_OFICIALES, ALGORITMOS_INTERACTIVOS

try:
    import campus_ui_bundle as _bundle
    HTML_TEMPLATE = getattr(_bundle, "HTML_TEMPLATE", "")
    CSS_CONTENT = getattr(_bundle, "CSS_CONTENT", "")
    JS_CONTENT = getattr(_bundle, "JS_CONTENT", "")
    SVG_DATA_URI = getattr(_bundle, "SVG_DATA_URI", "")
    INFOGRAFIAS_DATA_URI = getattr(_bundle, "INFOGRAFIAS_DATA_URI", {})
    UNIT_THUMBNAILS_URI = getattr(_bundle, "UNIT_THUMBNAILS_URI", {})
except Exception:
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

# Estilo limpio para ocupar toda la pantalla
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      .block-container {
        padding-top: 0.6rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.6rem !important;
        padding-right: 0.6rem !important;
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
DB_ALUMNOS_PATH = os.path.join(BASE_DIR, "registro_alumnos_diabetes.json")

# CDN jsDelivr sirve los archivos de GitHub con Content-Type: video/mp4 y audio/mpeg (indispensable para Chrome/Edge)
CDN_BASE = "https://cdn.jsdelivr.net/gh/marcosgamond-hash/laboratorio-diabetes-enfermeria-@main"
UNIDADES_CON_VIDEO = {1, 2, 3, 4, 5, 6, 7, 8, 9}
UNIDADES_CON_AUDIO = {1, 2, 3, 4, 5, 6, 7, 9}


def cargar_db_alumnos() -> dict:
    if os.path.exists(DB_ALUMNOS_PATH):
        try:
            with open(DB_ALUMNOS_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    # Base inicial con claves de ejemplo y estadísticas
    return {
        "alumnos": {
            "DEMO2026": {
                "codigo": "DEMO2026",
                "nombre": "Enfermero/a Invitado (Demo)",
                "dni": "00.000.000",
                "institucion": "Hospital / Institución",
                "activo": True,
                "ingresos": 1,
                "ultimo_acceso": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "unidades_aprobadas": {"u1": 100},
                "promedio": 100.0,
            }
        }
    }


def guardar_db_alumnos(db: dict) -> None:
    try:
        with open(DB_ALUMNOS_PATH, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def buscar_archivo_media(filename: str) -> str:
    p_root = os.path.join(BASE_DIR, filename)
    if os.path.exists(p_root):
        return p_root
    p_mm = os.path.join(MULTIMEDIA_DIR, filename)
    if os.path.exists(p_mm):
        return p_mm
    return ""


def cargar_archivos_ui():
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


@st.cache_data(show_spinner=False)
def construir_html_completo():
    html_str, css_str, js_str, svg_uri = cargar_archivos_ui()
    unidades_enriquecidas = []

    for u in UNIDADES_ACADEMICAS:
        copia = json.loads(json.dumps(u))
        uid = u["id"]
        num = u["numero"]
        mm = json.loads(json.dumps(RECURSOS_MULTIMEDIA_UNIDADES.get(uid, {})))

        tiene_video = (num in UNIDADES_CON_VIDEO) or bool(buscar_archivo_media(f"unidad_{num}.mp4"))
        tiene_audio = (num in UNIDADES_CON_AUDIO) or bool(buscar_archivo_media(f"unidad_{num}.mp3"))
        info_uri = INFOGRAFIAS_DATA_URI.get(num) or INFOGRAFIAS_DATA_URI.get(str(num))
        tiene_infografia = bool(info_uri)

        mm["estado_archivos"] = {
            "tiene_audio": tiene_audio,
            "tiene_video": tiene_video,
            "tiene_infografia": tiene_infografia,
            "tiene_pdf": False,
        }
        if tiene_video:
            mm["video_clase_url"] = f"{CDN_BASE}/unidad_{num}.mp4"
        if tiene_audio:
            mm["audio_podcast_url"] = f"{CDN_BASE}/unidad_{num}.mp3"
        if info_uri:
            mm["infografia_data_uri"] = info_uri

        copia["multimedia"] = mm
        unidades_enriquecidas.append(copia)

    prog_data = {
        "meta": META_PROGRAMA,
        "unidades": unidades_enriquecidas,
    }
    cons_data = {
        "consensos": CONSENSOS_OFICIALES,
        "algoritmos": ALGORITMOS_INTERACTIVOS,
    }

    if svg_uri:
        html_str = html_str.replace('src="/static/assets/circulo_azul_diabetes.svg"', f'src="{svg_uri}"')
    thumb_1 = UNIT_THUMBNAILS_URI.get(1) or UNIT_THUMBNAILS_URI.get("1") or svg_uri
    if thumb_1:
        html_str = html_str.replace('src="/static/assets/paciente_internacion.jpg"', f'src="{thumb_1}"')

    # Ocultar todos los botones de edición/subida docente en la vista pública
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

    html_str = re.sub(
        r'<script\s+src="/static/js/diaguias\.js[^"]*"></script>',
        lambda _m: f"<script>{js_str}</script>",
        html_str,
    )
    return html_str


# ==============================================================================
# BARRA SUPERIOR DE VIDEO-CLASES, PODCASTS Y PANEL DOCENTE (DR. MARCOS GAMOND)
# ==============================================================================
col_media, col_admin = st.columns([3, 2])

with col_media:
    with st.expander("🎬 Reproductor Directo de Video-Clases y Podcasts (Unidades 1 a 10)", expanded=False):
        u_num = st.selectbox(
            "Elegí la Unidad para ver su Video o escuchar su Podcast:",
            options=list(range(1, 11)),
            format_func=lambda n: f"Unidad {n}: {UNIDADES_ACADEMICAS[n-1]['titulo']}",
        )
        c_vid, c_aud = st.columns(2)
        with c_vid:
            local_v = buscar_archivo_media(f"unidad_{u_num}.mp4")
            if local_v:
                st.caption(f"📺 Video-Clase — Unidad {u_num}")
                st.video(local_v)
            elif u_num in UNIDADES_CON_VIDEO:
                st.caption(f"📺 Video-Clase — Unidad {u_num}")
                st.video(f"{CDN_BASE}/unidad_{u_num}.mp4")
            else:
                st.info(f"La Unidad {u_num} utiliza las Diapositivas Narradas interactivas del Campus.")
        with c_aud:
            local_a = buscar_archivo_media(f"unidad_{u_num}.mp3")
            if local_a:
                st.caption(f"🎙️ Podcast — Unidad {u_num}")
                st.audio(local_a)
            elif u_num in UNIDADES_CON_AUDIO:
                st.caption(f"🎙️ Podcast — Unidad {u_num}")
                st.audio(f"{CDN_BASE}/unidad_{u_num}.mp3")
            else:
                st.info(f"Podcast de la Unidad {u_num} próximamente.")

with col_admin:
    with st.expander("🔐 Gestión de Alumnos, Notas y Control de Acceso (Exclusivo Dr. Marcos Gamond)", expanded=False):
        clave_docente = st.text_input("Clave de Director Académico:", type="password", placeholder="Ingresá Gamond2026")
        if clave_docente == "Gamond2026":
            db = cargar_db_alumnos()
            alumnos_dict = db.get("alumnos", {})
            total_al = len(alumnos_dict)
            egresados = sum(1 for a in alumnos_dict.values() if len(a.get("unidades_aprobadas", {})) >= 10)
            prom_gral = (
                round(sum(a.get("promedio", 0) for a in alumnos_dict.values()) / total_al, 1)
                if total_al > 0 else 0.0
            )
            m1, m2, m3 = st.columns(3)
            m1.metric("👨‍⚕️ Inscriptos", total_al)
            m2.metric("🎓 Finalizaron", egresados)
            m3.metric("📊 Promedio", f"{prom_gral}%")

            st.markdown("##### ➕ Habilitar Nuevo Alumno Pago")
            with st.form("alta_alumno_form", clear_on_submit=True):
                f_nom = st.text_input("Nombre y Apellido del Enfermero/a")
                f_dni = st.text_input("DNI / Matrícula")
                f_cod = st.text_input("Código / Clave asignada (ej: ENF2026)")
                if st.form_submit_button("Habilitar Acceso"):
                    if f_nom and f_cod:
                        db["alumnos"][f_cod.strip().upper()] = {
                            "codigo": f_cod.strip().upper(),
                            "nombre": f_nom.strip(),
                            "dni": f_dni.strip(),
                            "institucion": "Curso 60 hs",
                            "activo": True,
                            "ingresos": 0,
                            "ultimo_acceso": "-",
                            "unidades_aprobadas": {},
                            "promedio": 0.0,
                        }
                        guardar_db_alumnos(db)
                        st.success(f"✅ Alumno {f_nom} habilitado con clave {f_cod.upper()}")

            if alumnos_dict:
                filas_csv = ["Codigo,Nombre,DNI,Ingresos,Unidades_Aprobadas,Promedio_Pct"]
                for k, v in alumnos_dict.items():
                    u_ap = len(v.get("unidades_aprobadas", {}))
                    filas_csv.append(f"{k},{v.get('nombre','')},{v.get('dni','')},{v.get('ingresos',0)},{u_ap}/10,{v.get('promedio',0)}%")
                st.download_button(
                    "📥 Descargar Planilla de Alumnos y Puntajes (.CSV / Excel)",
                    data="\n".join(filas_csv).encode("utf-8"),
                    file_name="alumnos_notas_diabetes_gamond.csv",
                    mime="text/csv",
                )

# Renderizar el Campus Completo Interactivo
html_campus = construir_html_completo()
components.html(html_campus, height=2150, scrolling=True)
