# -*- coding: utf-8 -*-
"""
STREAMLIT CLOUD APP — LABORATORIO DE ESTUDIO DE DIABETES PARA ENFERMERÍA
Dirección Académica: Dr. Marcos Gamond (60 hs cátedra • 10 Unidades)
Edición Lanzamiento 14 de Noviembre (Día Mundial de la Diabetes)
"""
import os
import re
import json
import base64
from datetime import datetime
from collections import Counter
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

# ==============================================================================
# ESTÉTICA CLÍNICA CLARA (BLANCO Y AZUL MÉDICO — ELIMINA EL MODO OSCURO/NEGRO)
# ==============================================================================
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header[data-testid="stHeader"] {
        display: none !important;
      }
      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stMain"],
      [data-testid="stVerticalBlock"] {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
      }
      .block-container {
        padding-top: 0.45rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
        max-width: 100% !important;
      }
      iframe {
        border: none !important;
        width: 100% !important;
        display: block !important;
        border-radius: 12px !important;
      }

      /* Tarjetas desplegables superiores: diseño blanco y celeste hospitalario en 1 sola línea */
      div[data-testid="stExpander"] {
        background: #ffffff !important;
        border: 1.5px solid #7dd3fc !important;
        border-radius: 12px !important;
        margin-bottom: 6px !important;
        box-shadow: 0 2px 8px rgba(2, 132, 199, 0.08) !important;
        overflow: hidden !important;
      }
      div[data-testid="stExpander"] details {
        background: #ffffff !important;
        border: none !important;
      }
      div[data-testid="stExpander"] summary {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%) !important;
        color: #0369a1 !important;
        padding: 8px 14px !important;
        border-radius: 10px !important;
      }
      div[data-testid="stExpander"] summary:hover {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%) !important;
      }
      div[data-testid="stExpander"] summary p {
        color: #0369a1 !important;
        font-weight: 800 !important;
        font-size: 0.88rem !important;
        margin: 0 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      div[data-testid="stExpander"] summary svg {
        fill: #0369a1 !important;
        color: #0369a1 !important;
      }
      div[data-testid="stExpanderDetails"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        padding: 12px 16px !important;
        border-top: 1px solid #e0f2fe !important;
      }

      /* Formularios y campos de texto siempre claros (nunca negros) */
      div[data-testid="stForm"] {
        background-color: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
        padding: 12px !important;
      }
      label,
      div[data-testid="stWidgetLabel"] p,
      div[data-testid="stCaptionContainer"] p,
      div[data-testid="stMarkdownContainer"] p {
        color: #0f172a !important;
      }
      div[data-baseweb="input"],
      div[data-baseweb="base-input"],
      div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #94a3b8 !important;
        border-radius: 8px !important;
      }
      input {
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        background-color: #ffffff !important;
      }
      input::placeholder {
        color: #64748b !important;
        -webkit-text-fill-color: #64748b !important;
      }
      div[data-baseweb="select"] span,
      div[data-baseweb="select"] div {
        color: #0f172a !important;
      }
      ul[role="listbox"],
      li[role="option"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
      }

      /* Botones principales en azul médico */
      div[data-testid="stFormSubmitButton"] button,
      div[data-testid="stDownloadButton"] button {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 0.45rem 1.1rem !important;
      }

      /* Métricas del panel de estadísticas */
      div[data-testid="stMetric"] {
        background-color: #f0f9ff !important;
        border: 1px solid #bae6fd !important;
        border-radius: 10px !important;
        padding: 8px 12px !important;
      }
      div[data-testid="stMetricLabel"] p {
        color: #0369a1 !important;
        font-weight: 700 !important;
      }
      div[data-testid="stMetricValue"] div {
        color: #0f172a !important;
        font-weight: 800 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
MULTIMEDIA_DIR = os.path.join(STATIC_DIR, "multimedia")
DB_CURSANTES_PATH = os.path.join(BASE_DIR, "cursantes_14nov_diabetes.json")

CDN_BASE = "https://cdn.jsdelivr.net/gh/marcosgamond-hash/laboratorio-diabetes-enfermeria-@main"
UNIDADES_CON_VIDEO = {1, 2, 3, 4, 5, 6, 7, 8, 9}
UNIDADES_CON_AUDIO = {1, 2, 3, 4, 5, 6, 7, 9}

SERVICIOS_OPCIONES = [
    "Guardia / Emergencias",
    "Sala de Internación General / Clínica Médica",
    "Terapia Intensiva (UTI / UCO)",
    "Consultorios Externos / Diabetología",
    "Atención Primaria (CAPS / Centro de Salud)",
    "Maternidad / Obstetricia / Pediatría",
    "Quirófano / Recuperación",
    "Docencia / Estudiante de Enfermería",
    "Gestión / Dirección / Polo Tecnológico",
    "Otro Servicio",
]


def cargar_db_cursantes() -> dict:
    if os.path.exists(DB_CURSANTES_PATH):
        try:
            with open(DB_CURSANTES_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"cursantes": {}}


def guardar_db_cursantes(db: dict) -> None:
    try:
        with open(DB_CURSANTES_PATH, "w", encoding="utf-8") as f:
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
# 1. BARRA SUPERIOR BLANCA Y CELESTE (INSCRIPCIÓN 14 NOV + ESTADÍSTICAS DOCENTES)
# ==============================================================================
col_reg, col_admin = st.columns([3, 2])

with col_reg:
    with st.expander("🔵 Inscripción y Acreditación de Cursantes (14 de Noviembre)", expanded=False):
        st.caption(
            "Registrá tus datos institucionales y tu calificación final (**Dirección Académica: Dr. Marcos Gamond**)."
        )
        with st.form("form_registro_enfermeria", clear_on_submit=False):
            c1, c2 = st.columns(2)
            with c1:
                r_nombre = st.text_input("Nombre y Apellido *", placeholder="Ej: Lic. Ana Pérez")
                r_dni = st.text_input("DNI o Matrícula *", placeholder="Ej: 34.567.890")
                r_localidad = st.text_input("Localidad y Provincia *", placeholder="Ej: Neuquén Capital")
            with c2:
                r_hospital = st.text_input("Hospital / Institución / CAPS *", placeholder="Ej: Hospital Dr. Horacio Heller")
                r_servicio = st.selectbox("Servicio en el que se desempeña *", options=SERVICIOS_OPCIONES)
                r_contacto = st.text_input("Email o WhatsApp", placeholder="Ej: ana@email.com / 299...")

            c3, c4 = st.columns(2)
            with c3:
                r_estado = st.selectbox(
                    "Estado de cursada:",
                    options=["En curso", "Curso Finalizado (10/10 Unidades Aprobadas)"],
                )
            with c4:
                r_puntaje = st.number_input("Puntaje obtenido (%)", min_value=0, max_value=100, value=90, step=5)

            if st.form_submit_button("✅ Guardar Mi Inscripción / Calificación"):
                if r_nombre.strip() and r_dni.strip() and r_hospital.strip():
                    db = cargar_db_cursantes()
                    key = re.sub(r"\W+", "", r_dni.strip()) or r_nombre.strip().upper()
                    db["cursantes"][key] = {
                        "dni": r_dni.strip(),
                        "nombre": r_nombre.strip(),
                        "localidad": r_localidad.strip() or "No especificada",
                        "hospital": r_hospital.strip(),
                        "servicio": r_servicio,
                        "contacto": r_contacto.strip(),
                        "estado": r_estado,
                        "finalizo": "Finalizado" in r_estado,
                        "puntaje": int(r_puntaje),
                        "fecha_registro": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    }
                    guardar_db_cursantes(db)
                    st.success(f"🎉 ¡Datos registrados correctamente para {r_nombre} ({r_hospital})!")
                else:
                    st.warning("Por favor completá Nombre, DNI e Institución/Hospital.")

with col_admin:
    with st.expander("📊 Estadísticas de Cursantes (Dr. Marcos Gamond)", expanded=False):
        clave_docente = st.text_input("Clave de Director Académico:", type="password", placeholder="Ingresá Gamond2026")
        if clave_docente == "Gamond2026":
            db = cargar_db_cursantes()
            cursantes = list(db.get("cursantes", {}).values())
            total_c = len(cursantes)
            finalizados = [c for c in cursantes if c.get("finalizo")]
            total_fin = len(finalizados)
            prom_nota = round(sum(c.get("puntaje", 0) for c in cursantes) / total_c, 1) if total_c > 0 else 0.0

            m1, m2, m3 = st.columns(3)
            m1.metric("👨‍⚕️ Inscriptos", total_c)
            m2.metric("🎓 Terminaron", total_fin)
            m3.metric("⭐ Promedio", f"{prom_nota}%")

            if cursantes:
                top_hosp = Counter(c.get("hospital", "Otro") for c in cursantes).most_common(5)
                top_loc = Counter(c.get("localidad", "Otra") for c in cursantes).most_common(5)
                top_serv = Counter(c.get("servicio", "Otro") for c in cursantes).most_common(5)

                st.markdown("**🏥 Por Hospital:** " + " • ".join(f"{h} ({n})" for h, n in top_hosp))
                st.markdown("**📍 Por Localidad:** " + " • ".join(f"{l} ({n})" for l, n in top_loc))
                st.markdown("**🩺 Por Servicio:** " + " • ".join(f"{s} ({n})" for s, n in top_serv))

                filas_csv = ["DNI,Nombre,Localidad,Hospital_Institucion,Servicio,Contacto,Estado,Puntaje_Pct,Fecha"]
                for c in cursantes:
                    filas_csv.append(
                        f"\"{c.get('dni','')}\",\"{c.get('nombre','')}\",\"{c.get('localidad','')}\",\"{c.get('hospital','')}\",\"{c.get('servicio','')}\",\"{c.get('contacto','')}\",\"{c.get('estado','')}\",{c.get('puntaje',0)}%,\"{c.get('fecha_registro','')}\""
                    )
                st.download_button(
                    "📥 Descargar Planilla Excel (.CSV)",
                    data="\n".join(filas_csv).encode("utf-8-sig"),
                    file_name="estadisticas_enfermeria_14nov_gamond.csv",
                    mime="text/csv",
                )
            else:
                st.info("Aún no hay cursantes registrados.")


# ==============================================================================
# 2. CAMPUS INTERACTIVO COMPLETO (10 UNIDADES, MULTIMEDIA, CALCULADORAS, TUTOR)
# ==============================================================================
html_campus = construir_html_completo()
components.html(html_campus, height=2050, scrolling=True)
