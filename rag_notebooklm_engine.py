# -*- coding: utf-8 -*-
"""
MOTOR RAG CLÍNICO ESTILO NOTEBOOKLM — LABORATORIO DE ESTUDIO DE DIABETES PARA ENFERMERÍA
Dirección Académica: Dr. Marcos Gamond
----------------------------------------------------------------------------------------
Permite realizar preguntas abiertas en lenguaje natural sobre:
1. Las 10 Unidades Académicas completas del programa (60 hs cátedra).
2. Los Consensos y Guías Oficiales (ADA 2025/2026, SAD, MSAL Argentina, FITTER, IWGDF).
3. Base Enciclopédica de Escenarios Especiales de Guardia e Internación (Corticoides,
   Nutrición Enteral/Parenteral, Charcot, Somogyi vs Alba, Bombas, Puerperio, etc.).
4. Documentos o apuntes propios que el docente o alumno agregue al Cuaderno RAG.

Funciona 100% gratis y sin límite de créditos mediante recuperación semántico-léxica
ponderada (BM25 + Expansión de Sinónimos Clínicos + Analizador de Parámetros Numéricos),
y soporta opcionalmente conexión con Gemini API si el usuario ingresa una clave.
"""
import os
import re
import math
import json
import unicodedata
from typing import Dict, Any, List, Optional, Tuple

from programa_academico import UNIDADES_ACADEMICAS
from multimedia_notebooklm import RECURSOS_MULTIMEDIA_UNIDADES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CUSTOM_RAG_DOCS_PATH = os.path.join(BASE_DIR, "custom_rag_docs.json")


# ==============================================================================
# 1. DICCIONARIO DE EXPANSIÓN SEMÁNTICA Y SINÓNIMOS CLÍNICOS DE ENFERMERÍA
# ==============================================================================
SINONIMOS_CLINICOS: Dict[str, List[str]] = {
    "hipoglucemia": ["hipoglucemia", "bajon", "azucar baja", "regla del 15", "glucagon", "dextrosa", "neuroglucopenia", "sudoracion", "temblor", "inconsciente", "nivel 1", "nivel 2", "nivel 3"],
    "cetoacidosis": ["cetoacidosis", "cad", "cetonas", "cetonemia", "kussmaul", "acidosis", "anion gap", "bomba", "potasio", "hipokalemia"],
    "ehh": ["hiperosmolar", "ehh", "coma hiperosmolar", "osmolaridad", "deshidratacion extrema"],
    "bomba": ["bomba", "infusion continua", "endovenosa", "ev", "corriente", "cristalina", "purgado", "tubuladura", "potasio", "transicion", "solapamiento"],
    "potasio": ["potasio", "k+", "hipokalemia", "3.3", "arritmia", "paro cardiaco", "cloruro de potasio", "kcl"],
    "metformina": ["metformina", "acidosis lactica", "contraste", "tomografia", "iodado", "vitamina b12", "tfg", "filtrado glomerular", "diarrea"],
    "sulfonilureas": ["sulfonilureas", "sulfonilurea", "glibenclamida", "glimepirida", "gliclazida", "secretagogos", "ayuno", "npo"],
    "isglt2": ["isglt2", "sglt2", "gliflozinas", "empagliflozina", "dapagliflozina", "canagliflozina", "glucosuria", "euglucemica", "cetoacidosis euglucemica", "micosis", "cirugia"],
    "glp1": ["glp1", "glp-1", "semaglutida", "ozempic", "liraglutida", "dulaglutida", "tirzepatida", "vaciamiento gastrico", "anestesia", "broncoaspiracion", "endoscopia"],
    "idpp4": ["idpp4", "dpp4", "dpp-4", "gliptinas", "linagliptina", "sitagliptina", "vildagliptina", "biliar", "dialisis", "renal"],
    "nph": ["nph", "lechosa", "turbia", "protamina", "rolar", "resuspension", "madrugada", "pico"],
    "glargina": ["glargina", "lantus", "toujeo", "optisulin", "degludec", "tresiba", "detemir", "basal", "ph acido", "mezclar"],
    "fitter": ["fitter", "aguja", "4 mm", "4mm", "90 grados", "pliegue", "10 segundos", "purgar", "lipohipertrofia", "rotacion", "capuchon"],
    "frio": ["cadena de frio", "heladera", "freezer", "congelar", "2 a 8", "28 dias", "ambiente", "conservacion", "transporte"],
    "embarazo": ["embarazo", "gestacional", "embarazada", "pedersen", "macrosomia", "alumbramiento", "placenta", "puerperio", "recien nacido", "neonatal", "talon", "lactancia"],
    "pie": ["pie", "neuropatico", "isquemico", "monofilamento", "10 g", "diapason", "128 hz", "pulsos", "pedio", "tibial", "sinbad", "iwgdf", "escara", "debridar", "crema", "dedos", "unias", "charcot"],
    "ejercicio": ["ejercicio", "actividad fisica", "deporte", "correr", "glut4", "glut-4", "ampk", "muslo", "cetonas", "250", "tardia"],
    "nutricion": ["plato", "metodo del plato", "fibra", "verduras", "carbohidratos", "proteinas", "orden de ingesta", "indice glucemico", "dieta"],
    "sensor": ["sensor", "freestyle", "monitoreo continuo", "cgm", "intersticial", "retraso", "flecha", "tiempo en rango", "tir"],
    "alba": ["alba", "somogyi", "3 am", "03:00", "madrugada", "rebote", "hormona de crecimiento", "cortisol"],
    "diagnostico": ["diagnostico", "criterios", "ayunas", "126", "200", "ptog", "curva", "75 g", "hba1c", "glicosilada", "prediabetes", "poliuria", "polidipsia", "polifagia"],
    "anciano": ["adulto mayor", "anciano", "fragil", "fragilidad", "8.0%", "8%", "caidas", "cadera", "desintensificacion"],
    "alta": ["alta", "teach-back", "teach back", "re-ensenanza", "dias de enfermedad", "sick day", "sadmans", "fiebre", "vomitos", "gastroenteritis"],
    "corticoides": ["corticoide", "corticoides", "dexametasona", "prednisona", "metilprednisolona", "hidrocortisona", "vespertina"],
    "enteral": ["enteral", "sonda", "nasogastrica", "parenteral", "alimentacion enteral", "sng"]
}


# ==============================================================================
# 2. BASE ENCICLOPÉDICA ADICIONAL DE GUARDIA E INTERNACIÓN (PREGUNTAS ABIERTAS)
# ==============================================================================
CONOCIMIENTO_CLINICO_EXPANDIDO: List[Dict[str, Any]] = [
    {
        "id": "extra_corticoides",
        "unidad_num": 6,
        "fuente": "Consenso SAD / ADA Cap. 16 — Hiperglucemia Inducida por Corticoides en Internación",
        "titulo": "Manejo de Hiperglucemia por Corticoides (Dexametasona / Prednisona) en Sala",
        "keywords": ["corticoide", "corticoides", "dexametasona", "prednisona", "metilprednisolona", "hidrocortisona", "tarde", "vespertina", "nph"],
        "contenido": (
            "Los glucocorticoides (Prednisona, Metilprednisolona, Dexametasona) inhiben la captación muscular de glucosa y aumentan la gluconeogénesis hepática, "
            "provocando un patrón clásico de **hiperglucemia predominantemente postprandial y vespertina** (sube después del mediodía y a la tarde, y suele bajar de madrugada). "
            "**Conducta de Enfermería y Farmacología:** Para la Prednisona administrada a las 08:00 AM, las guías ADA/SAD recomiendan asociar **Insulina NPH por la mañana** (junto con el corticoide), "
            "porque el perfil de acción de la NPH (pico a las 4–10 horas y duración de 12–16 horas) copia exactamente la curva hiperglucemiante del corticoide diurno sin causar hipoglucemia en la madrugada. "
            "**Alerta Roja:** Si al paciente se le suspende o reduce bruscamente el corticoide, se debe reducir en simultáneo la dosis de insulina para evitar hipoglucemias severas."
        ),
        "regla_salvavidas": "Si un paciente recibe corticoides a la mañana y se le suspende el corticoide al alta o en sala, alertar de inmediato para bajar la dosis de insulina; de lo contrario hará una hipoglucemia grave.",
        "preguntas_sugeridas": [
            "¿Por qué se prefiere Insulina NPH matinal cuando el paciente recibe Prednisona a la mañana?",
            "¿Qué pasa si se suspende la Dexametasona y no se ajusta la dosis de insulina?",
            "¿Cuál es la meta de glucemia en un paciente internado en sala general?"
        ]
    },
    {
        "id": "extra_enteral_parenteral",
        "unidad_num": 8,
        "fuente": "ADA Standards of Care 2025/2026 Cap. 16 — Nutrición Enteral (SNG) y Parenteral",
        "titulo": "Cuidados de Enfermería en Pacientes con Nutrición Enteral (Sonda) e Insulina",
        "keywords": ["enteral", "sonda", "nasogastrica", "sng", "parenteral", "bomba de alimentacion", "suspende", "tapa"],
        "contenido": (
            "En pacientes hospitalizados que reciben **Nutrición Enteral Continua por sonda nasogástrica (SNG)** o gastrostomía y están bajo tratamiento con Insulina Basal (NPH cada 8-12 hs o Glargina) más correcciones cada 4-6 horas, "
            "el aporte de carbohidratos es constante las 24 horas. "
            "**Regla Salvavidas ante interrupción de la Sonda:** Si la alimentación enteral se detiene de forma imprevista (porque el paciente arrancó la sonda, se tapó la SNG, o se suspende para trasladarlo a tomografía/baño en cama) "
            "y el paciente ya tiene aplicada su dosis de Insulina Basal o Rápida, **enfermería debe iniciar de inmediato una infusión endovenosa de Dextrosa al 10%** a la misma velocidad que iba la alimentación enteral y controlar el HGT cada 1–2 horas para prevenir una hipoglucemia grave."
        ),
        "regla_salvavidas": "¡Nunca dejes a un paciente insulinizado con la sonda nasogástrica apagada o tapada sin colocarle Dextrosa al 10% endovenosa de respaldo! La insulina subcutánea ya inyectada seguirá actuando y provocará hipoglucemia severa.",
        "preguntas_sugeridas": [
            "¿Cada cuántas horas se mide el HGT en un paciente en ayunas (NPO) o con nutrición enteral continua?",
            "¿Qué hago si un paciente con insulina inyectada vomita toda la comida o se le tapa la sonda?",
            "¿Cómo aplico la Regla del 15 si el paciente no puede tragar?"
        ]
    },
    {
        "id": "extra_escala_movil_vs_basal_bolo",
        "unidad_num": 6,
        "fuente": "ADA Standards of Care 2025/2026 Cap. 16 & Consenso SAD de Internación",
        "titulo": "Por qué está prohibida la «Escala Móvil Aislada» (Sliding Scale sola) en Internación",
        "keywords": ["escala movil", "sliding scale", "correccion", "correcciones", "basal bolo", "internacion", "internado", "140", "180"],
        "contenido": (
            "En pacientes internados en sala general o UCI, la **meta glucémica oficial (ADA/SAD) es de 140 a 180 mg/dL** (iniciando insulinoterapia ante valores persistentes $\\ge 180\\text{ mg/dL}$). "
            "Las guías internacionales **desaconsejan firmemente el uso exclusivo y prolongado de la «Escala Móvil» o correcciones aisladas de Insulina Corriente/Rápida** sin una insulina basal de fondo. "
            "**¿Por qué falla la escala móvil sola?** Porque actúa de manera *reactiva* (espera a que el paciente ya tenga hiperglucemia de 250–300 mg/dL para recién corregir, generando el efecto «montaña rusa» de picos hiperglucémicos e hipoglucemias por apilamiento de dosis). "
            "**Estándar de Oro en Sala General:** Esquema fisiológico **BASAL + BOLO PRANDIAL + CORRECCIÓN** en el paciente que come por boca, o **BASAL + CORRECCIÓN cada 4–6 hs** en el paciente en ayunas (NPO)."
        ),
        "regla_salvavidas": "La escala de corrección sola trata la hiperglucemia después de que ya ocurrió; el esquema Basal-Bolo-Corrección la previene manteniendo la glucemia estable entre 140 y 180 mg/dL.",
        "preguntas_sugeridas": [
            "¿Cuál es la meta de glucemia para pacientes hospitalizados según ADA/SAD?",
            "¿Qué insulinas se usan como Basal y cuáles como Bolo o Corrección?",
            "¿Qué hago con la insulina si el paciente internado queda en ayunas para cirugía?"
        ]
    },
    {
        "id": "extra_charcot",
        "unidad_num": 9,
        "fuente": "Guía Internacional IWGDF 2023/2025 — Neuroartropatía Aguda de Charcot",
        "titulo": "Pie de Charcot Agudo: Cómo reconocerlo y no confundirlo con Celulitis o Gota",
        "keywords": ["charcot", "pie caliente", "hinchado", "edematizado", "deformidad", "mecedora", "inmovilizacion", "descarga"],
        "contenido": (
            "La **Neuroartropatía de Charcot aguda** es una emergencia del pie diabético en pacientes con neuropatía severa: se presenta como un **pie unilateralmente rojo, caliente y muy edematizado (diferencia de temperatura $> 2\\,^\\circ\\text{C}$ respecto al otro pie), con pulsos conservados, SIN herida abierta y llamativamente INDOLORO** (o con molestia mínima para el grado de inflamación). "
            "Si el paciente sigue caminando sobre ese pie con microfracturas inflamatorias, los huesos del mediopié colapsan produciendo la deformidad en *«pie en mecedora»* y úlceras plantares crónicas. "
            "**Conducta de Enfermería (Guía IWGDF):** Sospechar Charcot agudo ante todo pie diabético rojo, caliente, hinchado y sin dolor; indicar **descarga e inmovilización inmediata (prohibido apoyar el pie)** con bota Walker o yeso de contacto total y derivar urgente al equipo de Pie Diabético."
        ),
        "regla_salvavidas": "Un pie diabético rojo, caliente, hinchado, con piel sana (sin úlcera) y que NO duele al caminar es una Neuroartropatía Aguda de Charcot hasta que se demuestre lo contrario: ¡prohibido apoyar el pie!",
        "preguntas_sugeridas": [
            "¿Cómo diferencio un pie neuropático de un pie isquémico en el consultorio?",
            "¿Por qué está prohibido debridar una escara negra seca en un talón sin pulsos?",
            "¿Cómo se calcula el puntaje SINBAD en una úlcera de pie diabético?"
        ]
    },
    {
        "id": "extra_glosario_siglas",
        "unidad_num": 2,
        "fuente": "Glosario Oficial de Siglas y Abreviaturas — Laboratorio de Estudio de Diabetes para Enfermería (Dr. Marcos Gamond)",
        "titulo": "Diccionario de Siglas y Abreviaturas Clínicas en Diabetes (PTOG, HGT, HbA1c, GAA, ITG, TIR, MCG, CAD, EHH, SADMANS)",
        "keywords": ["sigla", "siglas", "abreviatura", "abreviaturas", "que significa", "que es ptog", "potg", "ptog", "gaa", "itg", "hgt", "mcg", "tir", "hba1c", "sadmans", "fitter", "iwgdf", "sinbad", "lada", "mody", "ehh", "cad", "npo", "tfg"],
        "contenido": (
            "**Referencia rápida de siglas y abreviaturas clínicas para Enfermería:**\n"
            "• **PTOG:** Prueba de Tolerancia Oral a la Glucosa (Curva de 75 g de glucosa anhidra en 300 mL de agua bebida en 5–10 min, midiendo glucemia basal y a las 2 horas exactas en reposo sentado).\n"
            "• **GAA e ITG (Prediabetes):** **GAA** = Glucemia Alterada en Ayunas (100 a 125 mg/dL); **ITG** = Intolerancia a la Tolerancia a la Glucosa (140 a 199 mg/dL a las 2 hs de la PTOG).\n"
            "• **HbA1c (A1c):** Hemoglobina Glicosilada (promedio glucémico de los últimos 90 a 120 días; se extrae en tubo tapa violeta con EDTA sin requerir ayuno).\n"
            "• **HGT:** Hemoglucotest o Glucemia Capilar por punción digital en cara lateral del pulpejo.\n"
            "• **MCG y TIR:** **MCG** = Monitoreo Continuo de Glucosa (sensor intersticial con retraso o *lag time* de 10–15 min); **TIR** = Tiempo en Rango (meta > 70% del día entre 70 y 180 mg/dL).\n"
            "• **DBT1 / DBT2 / LADA / MODY / DG:** Diabetes Tipo 1, Diabetes Tipo 2, Diabetes Autoinmune Latente del Adulto (LADA), Diabetes Monogénica Juvenil (MODY) y Diabetes Gestacional (DG).\n"
            "• **FITTER:** Consenso Internacional sobre Técnica de Inyección de Insulina (aguja de 4 mm a 90°, purgado de 1–2 UI, cuenta de 10 segundos y rotación).\n"
            "• **CAD y EHH:** **CAD** = Cetoacidosis Diabética; **EHH** = Estado Hiperosmolar Hiperglucémico.\n"
            "• **IWGDF y SINBAD:** **IWGDF** = Grupo Internacional de Pie Diabético; **SINBAD** = Escala de severidad de úlceras (Sitio, Isquemia, Neuropatía, Bacteria, Área, Profundidad; ≥ 3 deriva urgente).\n"
            "• **SADMANS:** Fármacos a pausar en deshidratación/vómitos (**S**ulfonilureas, **A**iECA/IECA, **D**iuréticos, **M**etformina, **A**RA-II, **N**AINEs/AINEs y **S**GLT2).\n"
            "• **NPO y TFG:** **NPO** = Nada Por Boca (ayuno hospitalario); **TFG** = Tasa de Filtrado Glomerular (función renal)."
        ),
        "regla_salvavidas": "Conocer las siglas clínicas evita errores graves en guardia: por ejemplo, nunca realizar una PTOG si la glucemia en ayunas ya es ≥ 126 mg/dL, y suspender Sulfonilureas ante la indicación NPO (Nada Por Boca).",
        "preguntas_sugeridas": [
            "¿Cómo se prepara y realiza correctamente una PTOG de 75 gramos?",
            "¿Qué significan las siglas del acrónimo SADMANS en días de enfermedad?",
            "¿Qué diferencia hay entre HGT capilar y sensor de Monitoreo Continuo (MCG)?"
        ]
    }
]


# ==============================================================================
# 3. UTILIDADES DE NORMALIZACIÓN Y RECUPERACIÓN RAG (BM25 + EXPANSIÓN CLÍNICA)
# ==============================================================================
def normalizar_texto(texto: str) -> str:
    if not texto:
        return ""
    sin_acentos = "".join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )
    return re.sub(r"[^a-z0-9\s\.\-\+\%]", " ", sin_acentos)


def tokenizar_consulta(consulta: str) -> Tuple[List[str], List[str]]:
    norm = normalizar_texto(consulta)
    stopwords = {
        "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "a", "en",
        "con", "por", "para", "sin", "sobre", "entre", "que", "como", "cual", "cuales", "cuando",
        "donde", "quien", "porque", "es", "son", "esta", "estan", "ser", "estar", "hay", "tiene",
        "tengo", "hacer", "hago", "hace", "se", "su", "sus", "mi", "mis", "tu", "tus", "le", "les",
        "lo", "me", "te", "nos", "si", "no", "mas", "muy", "pero", "o", "y", "e", "u", "paciente",
        "enfermeria", "enfermero", "enfermera", "diabetes", "diabetico", "diabetica", "puede",
        "puedo", "debe", "debo", "pregunta", "consulta", "duda", "explicame", "decime", "contame"
    }
    tokens_base = [t for t in norm.split() if len(t) >= 2 and t not in stopwords]

    # Expandir con sinónimos clínicos si alguna palabra o frase coincide
    tokens_expandidos = set(tokens_base)
    for grupo, lista_sin in SINONIMOS_CLINICOS.items():
        for termino in lista_sin:
            termino_norm = normalizar_texto(termino).strip()
            if termino_norm and (termino_norm in norm or termino_norm in tokens_base):
                tokens_expandidos.add(grupo)
                for s in lista_sin:
                    for sub_tok in normalizar_texto(s).split():
                        if len(sub_tok) >= 3 and sub_tok not in stopwords:
                            tokens_expandidos.add(sub_tok)
                break

    return tokens_base, list(tokens_expandidos)


def cargar_documentos_custom_rag() -> List[Dict[str, Any]]:
    if os.path.exists(CUSTOM_RAG_DOCS_PATH):
        try:
            with open(CUSTOM_RAG_DOCS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except Exception:
            return []
    return []


def guardar_documento_custom_rag(titulo: str, contenido: str, fuente: str = "Apunte / Guía Propia Subida al RAG") -> Dict[str, Any]:
    docs = cargar_documentos_custom_rag()
    nuevo = {
        "id": f"custom_doc_{len(docs) + 1}",
        "unidad_num": 0,
        "fuente": fuente,
        "titulo": titulo.strip() or f"Documento Personalizado #{len(docs) + 1}",
        "contenido": contenido.strip(),
        "regla_salvavidas": "Documento propio incorporado a la Biblioteca RAG del Laboratorio."
    }
    docs.append(nuevo)
    with open(CUSTOM_RAG_DOCS_PATH, "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)
    return nuevo


def construir_corpus_rag(consensos_oficiales: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Construye en tiempo real el índice completo de fragmentos (chunks) verificables:
    - Las 10 Unidades Académicas (Fisiopatología, Lectura 3 Min, Tablas de Consenso, Reglas Salvavidas, Casos y Autoevaluación)
    - Los Consensos Oficiales (ADA, SAD, MSAL, FITTER, IWGDF)
    - La Base Enciclopédica de Escenarios Especiales de Guardia
    - Los Documentos Personalizados subidos por el docente/alumno
    """
    import importlib
    import programa_academico as pa_mod
    import multimedia_notebooklm as mm_mod
    importlib.reload(pa_mod)
    importlib.reload(mm_mod)

    corpus: List[Dict[str, Any]] = []

    # 1. Indexar las 10 Unidades Académicas
    for u in pa_mod.UNIDADES_ACADEMICAS:
        uid = u["id"]
        num = u["numero"]
        titulo_u = u["titulo"]
        fuente_guia = u.get("guias_consenso", {}).get("fuente", "Consenso ADA / SAD / MSAL")
        regla_u = u.get("guias_consenso", {}).get("regla_enfermeria", "")
        mm = mm_mod.RECURSOS_MULTIMEDIA_UNIDADES.get(uid, {})
        lectura_3m = mm.get("lectura_3_minutos", [])

        # Chunk A: Lectura Rápida + Regla Salvavidas de la Unidad
        texto_lectura = "\n".join([f"• {linea}" for linea in lectura_3m])
        corpus.append({
            "chunk_id": f"u{num}_sintesis",
            "unidad_num": num,
            "unidad_id": uid,
            "tipo": "unidad_sintesis",
            "titulo": f"{titulo_u} — Síntesis Clínica y Regla Salvavidas",
            "fuente": f"Unidad {num} ({fuente_guia})",
            "contenido": f"{texto_lectura}\n\n**Regla Salvavidas:** {regla_u}",
            "regla_salvavidas": regla_u,
            "preguntas_sugeridas": [q["pregunta"] for q in u.get("autoevaluacion", [])[:2]]
        })

        # Chunk B: Fisiopatología y Conceptos Clave + Tabla de Consenso
        cards_txt = "\n".join([f"• **{c['titulo']}:** {c['contenido']}" for c in u.get("fisiopatologia_cards", [])])
        filas_tabla = "\n".join([
            f"• **{m['criterio']}:** Estándar: {m['normal']} | Alerta: {m['prediabetes']} | Punto crítico: {m['diabetes']}"
            for m in u.get("guias_consenso", {}).get("metas_tabla", [])
        ])
        corpus.append({
            "chunk_id": f"u{num}_fisiopatologia_guias",
            "unidad_num": num,
            "unidad_id": uid,
            "tipo": "unidad_fisiopatologia",
            "titulo": f"{titulo_u} — Fisiopatología y Tabla de Metas Oficiales",
            "fuente": f"Unidad {num} ({fuente_guia})",
            "contenido": f"**Fisiopatología Aplicada:**\n{cards_txt}\n\n**Metas y Puntos de Corte de Guía:**\n{filas_tabla}",
            "regla_salvavidas": regla_u,
            "preguntas_sugeridas": [q["pregunta"] for q in u.get("autoevaluacion", [])[:2]]
        })

        # Chunk C: Caso Clínico y Banco de Autoevaluación Comentada
        caso = u.get("caso_practico", {})
        quiz_txt = "\n\n".join([
            f"**Pregunta Clínica:** {q['pregunta']}\n**Conducta Correcta:** {q['opciones'][q['correcta']]}\n**Fundamento:** {q['explicacion']}"
            for q in u.get("autoevaluacion", [])
        ])
        corpus.append({
            "chunk_id": f"u{num}_casos_quiz",
            "unidad_num": num,
            "unidad_id": uid,
            "tipo": "unidad_casos",
            "titulo": f"{titulo_u} — Casos Clínicos y Fundamentos de Examen",
            "fuente": f"Unidad {num} ({fuente_guia})",
            "contenido": (
                f"**Caso Clínico de Guardia:** {caso.get('escenario', '')}\n"
                f"**Resolución:** {caso.get('resolucion', '')}\n\n"
                f"{quiz_txt}"
            ),
            "regla_salvavidas": regla_u,
            "preguntas_sugeridas": [q["pregunta"] for q in u.get("autoevaluacion", [])]
        })

    # 2. Indexar Consensos Oficiales Estructurados
    for cid, cdata in consensos_oficiales.items():
        recs = "\n".join([f"• **[{r['grado']}]** {r['regla']}" for r in cdata.get("recomendaciones_evidencia", [])])
        corpus.append({
            "chunk_id": f"consenso_{cid}",
            "unidad_num": 0,
            "unidad_id": cid,
            "tipo": "consenso_oficial",
            "titulo": f"{cdata['sigla']} — {cdata['titulo']}",
            "fuente": f"{cdata['sigla']} ({cdata['entidad']})",
            "contenido": (
                f"• **Meta Terapéutica:** {cdata['meta_glucemica']}\n"
                f"• **Umbral de Alerta:** {cdata['umbral_alerta']}\n"
                f"• **Recomendaciones con Nivel de Evidencia:**\n{recs}"
            ),
            "regla_salvavidas": cdata["regla_oro_enfermeria"],
            "preguntas_sugeridas": []
        })

    # 3. Indexar Conocimiento Clínico Expandido (Escenarios Especiales)
    for item in CONOCIMIENTO_CLINICO_EXPANDIDO:
        corpus.append({
            "chunk_id": item["id"],
            "unidad_num": item["unidad_num"],
            "unidad_id": f"u{item['unidad_num']}",
            "tipo": "escenario_especial",
            "titulo": item["titulo"],
            "fuente": item["fuente"],
            "contenido": item["contenido"],
            "regla_salvavidas": item["regla_salvavidas"],
            "preguntas_sugeridas": item.get("preguntas_sugeridas", []),
            "keywords_extra": item.get("keywords", [])
        })

    # 4. Indexar Documentos Propios subidos por el usuario al RAG
    for doc in cargar_documentos_custom_rag():
        corpus.append({
            "chunk_id": doc["id"],
            "unidad_num": doc.get("unidad_num", 0),
            "unidad_id": "custom",
            "tipo": "documento_propio",
            "titulo": doc["titulo"],
            "fuente": doc.get("fuente", "Bibliografía Propia Subida al RAG"),
            "contenido": doc["contenido"],
            "regla_salvavidas": doc.get("regla_salvavidas", ""),
            "preguntas_sugeridas": []
        })

    return corpus


# ==============================================================================
# 4. ANALIZADOR INTELIGENTE DE VALORES NUMÉRICOS EN LA PREGUNTA DEL USUARIO
# ==============================================================================
def analizar_parametros_paciente_en_consulta(consulta: str) -> Optional[str]:
    """
    Si el usuario escribe valores clínicos reales en su pregunta (ej. HGT 54 mg/dL,
    Potasio 2.9, Peso 80 kg, TFG 25, HbA1c 8.4%), genera un bloque de auditoría
    clínica automática para ese paciente concreto.
    """
    q = normalizar_texto(consulta)
    hallazgos: List[str] = []

    # 1. Detectar Potasio (K+)
    m_k = re.search(r"(?:potasio|k\+?|kalemia)\s*(?:de|es|en|=|:)?\s*(\d+(?:[\.,]\d+)?)", q)
    if m_k:
        val_k = float(m_k.group(1).replace(",", "."))
        if val_k < 3.3:
            hallazgos.append(
                f"🛑 **ALERTA CRÍTICA POR POTASIO ($\\text{{K}}^+ = {val_k}\\text{{ mEq/L}} < 3.3\\text{{ mEq/L}}$):** "
                f"**PROHIBIDO iniciar la Bomba de Insulina EV en este momento.** La insulina activa la bomba $\\text{{Na}}^+/\\text{{K}}^+\\text{{-ATPasa}}$ introduciendo potasio a la célula y desencadenaría arritmias ventriculares letales. Primero expandir con SF 0.9% y reponer Cloruro de Potasio (KCl) EV hasta lograr $\\text{{K}}^+ \\ge 3.3\\text{{ mEq/L}}$."
            )
        elif val_k <= 5.2:
            hallazgos.append(
                f"✅ **Auditoría de Potasio ($\\text{{K}}^+ = {val_k}\\text{{ mEq/L}}$):** Seguro para iniciar Bomba de Insulina EV + adicionar $20\\text{{--}}30\\text{{ mEq}}$ de KCl por litro de solución parenteral para mantenerlo entre $4\\text{{ y }}5\\text{{ mEq/L}}$."
            )
        else:
            hallazgos.append(
                f"⚠️ **Potasio elevado ($\\text{{K}}^+ = {val_k}\\text{{ mEq/L}} > 5.2\\text{{ mEq/L}}$):** Se puede iniciar la Bomba de Insulina EV SIN agregar potasio a los sueros inicialmente, controlando el ionograma cada 2 horas."
            )

    # 2. Detectar Peso para cálculo de Bomba EV si menciona bomba o cetoacidosis
    m_peso = re.search(r"(\d{2,3})\s*(?:kg|kilos)", q)
    if m_peso and any(w in q for w in ["bomba", "cetoacidosis", "cad", "infusion", "corriente"]):
        peso = float(m_peso.group(1))
        dosis_01 = round(peso * 0.1, 1)
        dosis_005 = round(peso * 0.05, 1)
        hallazgos.append(
            f"💉 **Cálculo Automático para Paciente de {int(peso)} kg (Dilución $100\\text{{ UI Corriente en }}100\\text{{ ml SF}} = 1\\text{{ ml}}/1\\text{{ UI}}$):** "
            f"Velocidad inicial ($0.1\\text{{ UI/kg/h}}$) = **{dosis_01} ml/hora** ({dosis_01} UI/h). Cuando la glucemia baje a $200\\text{{--}}250\\text{{ mg/dL}}$, agregar Dextrosa 5% en paralelo y reducir la bomba a **{dosis_005} ml/hora** ($0.05\\text{{ UI/kg/h}}$)."
        )

    # 3. Detectar Glucemia / HGT numérico
    m_glu = re.search(r"(?:hgt|glucemia|azucar|glucosa)\s*(?:de|es|en|dio|marca|=|:)?\s*(\d{2,4})", q)
    if m_glu:
        glu = int(m_glu.group(1))
        if glu < 54:
            hallazgos.append(
                f"🚨 **HIPOGLUCEMIA NIVEL 2 / 3 DETECTADA ({glu} mg/dL < 54 mg/dL — Umbral de Neuroglucopenia):** "
                f"Si el paciente está alerta y traga bien, aplicar **Regla del 15** inmediata ($15\\text{{ g}}$ de azúcar en agua o jugo sin grasa y repetir HGT en 15 min). Si está somnoliento, confuso o inconsciente: **¡NADA POR BOCA!**, lateralizar vía aérea y administrar **Dextrosa hipertónica EV** ($15\\text{{--}}25\\text{{ g}}$) o **Glucagón 1 mg IM/SC**."
            )
        elif glu < 70:
            hallazgos.append(
                f"🍬 **HIPOGLUCEMIA NIVEL 1 DETECTADA ({glu} mg/dL < 70 mg/dL):** Activar **Regla del 15** ($15\\text{{ g}}$ de carbohidrato simple puro sin grasas, ej. 3 sobres de azúcar en agua o $150\\text{{ ml}}$ de jugo regular) y reevaluar HGT capilar a los **15 minutos exactos**."
            )
        elif glu >= 250 and any(w in q for w in ["ejercicio", "correr", "deporte", "caminar", "gimnasio"]):
            hallazgos.append(
                f"🛑 **CONTRAINDICACIÓN DE EJERCICIO ({glu} mg/dL $\\ge 250\\text{{ mg/dL}}$):** Con glucemia $> 250\\text{{ mg/dL}}$ y cetonas positivas (o $> 300\\text{{ mg/dL}}$) está **estrictamente prohibido realizar ejercicio físico**, ya que las hormonas de estrés del esfuerzo disparan la cetogénesis y precipitan una Cetoacidosis Diabética."
            )

    # 4. Detectar Filtrado Glomerular (TFG / Clearance)
    m_tfg = re.search(r"(?:tfg|filtrado|clearance|clcr)\s*(?:de|es|en|menor a|<|=|:)?\s*(\d{1,3})", q)
    if m_tfg:
        tfg = int(m_tfg.group(1))
        if tfg < 30:
            hallazgos.append(
                f"🛑 **ALERTA RENAL ($\\text{{TFG}} = {tfg}\\text{{ ml/min}} < 30\\text{{ ml/min}}$):** **Contraindicada la Metformina** (riesgo de Acidosis Láctica) y las Sulfonilureas (hipoglucemia prolongada). Si requiere un inhibidor DPP-4 oral, la **Linagliptina** es la única que no requiere ajuste de dosis por eliminarse por vía hepatobiliar."
            )

    if not hallazgos:
        return None
    return "\n\n".join(hallazgos)


# ==============================================================================
# 5. MOTOR PRINCIPAL DE CONSULTA RAG (CON FILTRO DE FUENTES Y MODOS DE SALIDA)
# ==============================================================================
def ejecutar_consulta_rag_notebooklm(
    consulta: str,
    consensos_oficiales: Dict[str, Dict[str, Any]],
     alcance_fuentes: str = "todas",
    modo_respuesta: str = "estudio",
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Ejecuta la recuperación RAG sobre el corpus seleccionado, puntúa cada fragmento
    mediante BM25 + coincidencias de sinónimos clínicos, y construye una respuesta
    con citas verificables [1], [2], [3] y preguntas de seguimiento sugeridas.
    """
    corpus_completo = construir_corpus_rag(consensos_oficiales)

    # Filtrar corpus según el alcance elegido por el usuario (como en NotebookLM)
    if alcance_fuentes and alcance_fuentes not in ("todas", "todos", "all"):
        if alcance_fuentes == "solo_guias":
            corpus = [c for c in corpus_completo if c["tipo"] in ("consenso_oficial", "escenario_especial")]
        elif alcance_fuentes.startswith("u") and alcance_fuentes[1:].isdigit():
            u_num = int(alcance_fuentes[1:])
            corpus = [c for c in corpus_completo if c.get("unidad_num") == u_num or c["tipo"] == "consenso_oficial"]
        else:
            corpus = [c for c in corpus_completo if alcance_fuentes in (c.get("unidad_id", ""), c.get("chunk_id", ""))]
            if not corpus:
                corpus = corpus_completo
    else:
        corpus = corpus_completo

    tokens_base, tokens_expandidos = tokenizar_consulta(consulta)
    q_norm = normalizar_texto(consulta)

    # Puntuar cada chunk con algoritmo híbrido (BM25 + coincidencia exacta de frases + keywords clínicas)
    resultados_puntuados: List[Tuple[float, Dict[str, Any]]] = []
    for chunk in corpus:
        titulo_norm = normalizar_texto(chunk["titulo"])
        contenido_norm = normalizar_texto(chunk["contenido"])
        regla_norm = normalizar_texto(chunk.get("regla_salvavidas", ""))
        extra_kw = [normalizar_texto(k) for k in chunk.get("keywords_extra", [])]

        score = 0.0
        # Peso mayor a tokens originales de la pregunta del usuario
        for tok in tokens_base:
            if tok in titulo_norm:
                score += 6.0
            if tok in extra_kw:
                score += 5.5
            ocurrencias = contenido_norm.count(tok)
            if ocurrencias > 0:
                score += 3.0 * (1.0 + math.log(min(ocurrencias, 6)))
            if tok in regla_norm:
                score += 2.5

        # Peso complementario a los sinónimos clínicos expandidos
        for tok_exp in tokens_expandidos:
            if tok_exp in tokens_base:
                continue
            if tok_exp in titulo_norm:
                score += 2.2
            if tok_exp in contenido_norm:
                score += 1.2
            if tok_exp in regla_norm:
                score += 1.5

        # Bonus por frases exactas de 2 palabras (bigramas)
        if len(tokens_base) >= 2:
            for i in range(len(tokens_base) - 1):
                bigrama = f"{tokens_base[i]} {tokens_base[i+1]}"
                if bigrama in titulo_norm:
                    score += 8.0
                if bigrama in contenido_norm:
                    score += 5.0

        # Si el usuario filtró explícitamente una unidad (ej. u4), priorizar los chunks de esa unidad
        if alcance_fuentes.startswith("u") and alcance_fuentes[1:].isdigit():
            if chunk.get("unidad_num") == int(alcance_fuentes[1:]):
                score += 4.0

        if score > 0:
            resultados_puntuados.append((score, chunk))

    # Ordenar de mayor a menor relevancia
    resultados_puntuados.sort(key=lambda x: x[0], reverse=True)

    # Si no hubo match directo (pregunta muy general), traer los fragmentos principales del alcance
    if not resultados_puntuados:
        top_chunks = corpus[:3]
    else:
        # Evitar repetir el mismo tipo de chunk de la misma unidad si hay variedad
        top_chunks = []
        vistos = set()
        for sc, ch in resultados_puntuados:
            cid = ch["chunk_id"]
            if cid not in vistos:
                top_chunks.append(ch)
                vistos.add(cid)
            if len(top_chunks) >= 4:
                break

    auditoria_numerica = analizar_parametros_paciente_en_consulta(consulta)

    # Verificar si el usuario pidió generar un examen o caso clínico
    pide_examen = (
        modo_respuesta == "examen"
        or any(w in q_norm for w in ["examen", "autoevaluacion", "multiple choice", "opcion multiple", "tomame una pregunta", "armame un caso"])
    )

    # Armar citas estructuradas estilo NotebookLM ([1], [2], [3])
    citas_detalle = []
    preguntas_seguimiento = []
    for idx, ch in enumerate(top_chunks[:3], start=1):
        extracto_limpio = re.sub(r"\s+", " ", ch["contenido"]).strip()
        if len(extracto_limpio) > 340:
            extracto_limpio = extracto_limpio[:340] + "..."
        citas_detalle.append({
            "num": idx,
            "titulo": ch["titulo"],
            "fuente": ch["fuente"],
            "unidad_num": ch.get("unidad_num", 0),
            "extracto": extracto_limpio
        })
        for ps in ch.get("preguntas_sugeridas", []):
            if ps not in preguntas_seguimiento and len(preguntas_seguimiento) < 4:
                preguntas_seguimiento.append(ps)

    if not preguntas_seguimiento:
        preguntas_seguimiento = [
            "¿Qué debo hacer si el paciente en sala tiene un HGT menor a 70 mg/dL?",
            "¿Qué medicamentos orales e inyectables debo suspender antes de una cirugía o estudio con contraste?",
            "¿Por qué no se puede iniciar la Bomba de Insulina EV si el potasio es menor a 3.3 mEq/L?",
            "¿Cómo diferencio un pie diabético neuropático de uno isquémico y cuándo está prohibido debridar?"
        ]

    # Intentar con Gemini API si el usuario proveyó clave opcional
    key_efectiva = (api_key or os.environ.get("GEMINI_API_KEY", "")).strip()
    if key_efectiva:
        try:
            from google import genai
            client = genai.Client(api_key=key_efectiva)
            contexto_rag = "\n\n".join([
                f"[FUENTE {i+1}: {c['titulo']} | {c['fuente']}]\n{c['contenido']}\nRegla Salvavidas: {c.get('regla_salvavidas', '')}"
                for i, c in enumerate(top_chunks[:4])
            ])
            prompt = (
                f"Sos el Copiloto Clínico RAG (estilo NotebookLM) del 'Laboratorio de Estudio de Diabetes para Enfermería — Dr. Marcos Gamond'.\n"
                f"Respondé en español de Argentina usando como base prioritaria las siguientes fuentes recuperadas del programa y las guías ADA/SAD/MSAL/FITTER/IWGDF, "
                f"e incluí referencias numéricas [1], [2] a las fuentes citadas:\n\n"
                f"{contexto_rag}\n\n"
                f"Pregunta del profesional/alumno: «{consulta}»\n"
                f"Modo solicitado: {modo_respuesta}."
            )
            res = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            if res and res.text:
                texto_final = res.text.strip()
                if auditoria_numerica:
                    texto_final = f"{auditoria_numerica}\n\n---\n\n{texto_final}"
                return {
                    "modo": "Copiloto RAG + Gemini 2.5 Conectado a tu Cuaderno y Guías",
                    "respuesta": texto_final,
                    "citas": [f"[{c['num']}] {c['fuente']}" for c in citas_detalle],
                    "citas_detalle": citas_detalle,
                    "preguntas_sugeridas": preguntas_seguimiento[:3]
                }
        except Exception:
            pass

    # Construcción de respuesta mediante el Motor RAG Local Estilo NotebookLM (Sin consumir créditos)
    principal = top_chunks[0]
    secundario = top_chunks[1] if len(top_chunks) > 1 else None
    regla_principal = principal.get("regla_salvavidas", "")

    bloques_rta: List[str] = []

    if auditoria_numerica:
        bloques_rta.append(auditoria_numerica)

    if pide_examen:
        # Buscar la unidad relacionada para generar una pregunta interactiva de estudio
        u_num_ref = principal.get("unidad_num", 1) or 1
        u_obj = next((u for u in UNIDADES_ACADEMICAS if u["numero"] == u_num_ref), UNIDADES_ACADEMICAS[0])
        q_item = u_obj["autoevaluacion"][0]
        letras = ["A", "B", "C"]
        opciones_str = "\n".join([f"* **{letras[idx]})** {op}" for idx, op in enumerate(q_item["opciones"])])
        bloques_rta.append(
            f"### 📝 Caso de Autoevaluación Generado desde [{principal['fuente']}] [1]\n"
            f"**{q_item['pregunta']}**\n\n"
            f"{opciones_str}\n\n"
            f"---\n"
            f"✅ **Respuesta Correcta: Opción {letras[q_item['correcta']]}**\n"
            f"* **Fundamento Fisiopatológico y de Guía [1]:** {q_item['explicacion']}"
        )
    elif modo_respuesta == "guardia":
        bloques_rta.append(
            f"### ⚡ Conducta Rápida de Guardia — {principal['titulo']} [1]\n"
            f"{principal['contenido']}"
        )
        if regla_principal:
            bloques_rta.append(
                f"### 🚨 Regla Salvavidas de Enfermería [1]\n"
                f"**{regla_principal}**"
            )
    else:
        # Explicación académica completa con síntesis multi-fuente
        bloques_rta.append(
            f"### 🩺 1. Respuesta Clínica Fundamentada: {principal['titulo']} [1]\n"
            f"{principal['contenido']}"
        )
        if secundario and secundario["chunk_id"] != principal["chunk_id"]:
            # Agregar aporte complementario de la segunda fuente recuperada
            lineas_sec = [l.strip() for l in secundario["contenido"].split("\n") if l.strip()]
            resumen_sec = "\n".join(lineas_sec[:4])
            bloques_rta.append(
                f"### 📚 2. Evidencia Complementaria Relacionada ({secundario['titulo']}) [2]\n"
                f"{resumen_sec}"
            )
        if regla_principal:
            bloques_rta.append(
                f"### 🚨 3. Regla Salvavidas para la Práctica de Enfermería [1]\n"
                f"{regla_principal}"
            )

    respuesta_final = "\n\n".join(bloques_rta)

    return {
        "modo": "GLUC-IA • Tutor Clínico del Laboratorio de Estudio de Diabetes (Dr. Marcos Gamond)",
        "respuesta": respuesta_final,
        "citas": [f"[{c['num']}] {c['fuente']} — {c['titulo']}" for c in citas_detalle],
        "citas_detalle": citas_detalle,
        "preguntas_sugeridas": preguntas_seguimiento[:3]
    }
