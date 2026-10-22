# -*- coding: utf-8 -*-
"""
MOTOR DE CONSENSOS, ALGORITMOS VIVOS Y COPILOTO IA — DIAGUÍAS IA ENFERMERÍA (OPCIÓN B)
Plataforma Basada en Guías Oficiales (ADA 2025/2026 • SAD • MSAL Argentina • IWGDF • FITTER)
Diferencial de Mercado:
- A diferencia de la Opción A (Atlas Fotográfico 360°), la Opción B funciona como un
  «UpToDate + Algoritmo Interactivo + Simulador IA de Guardia» pensado específicamente
  para Enfermería hispanohablante, donde cada decisión muestra el respaldo exacto de
  la Guía / Consenso y permite consultar a la IA con anclaje en evidencia.
"""
import os
from typing import Dict, Any, List, Optional

try:
    from google import genai
    GENAI_AVAILABLE = True
except Exception:
    GENAI_AVAILABLE = False


# ==============================================================================
# 1. BASE DE GUÍAS Y CONSENSOS OFICIALES (EVIDENCIA ESTRUCTURADA PARA ENFERMERÍA)
# ==============================================================================
CONSENSOS_OFICIALES: Dict[str, Dict[str, Any]] = {
    "ada_hospital": {
        "id": "ada_hospital",
        "sigla": "ADA 2025/2026 • Cap. 16",
        "titulo": "Manejo de la Hiperglucemia en Pacientes Hospitalizados (No Críticos y UCI)",
        "entidad": "American Diabetes Association (Standards of Care in Diabetes) + Consenso SAD",
        "meta_glucemica": "140 a 180 mg/dL en la mayoría de pacientes internados (UCI y Sala General). Metas más estrictas (110–140 mg/dL) solo en pacientes seleccionados sin riesgo de hipoglucemia.",
        "umbral_alerta": "< 70 mg/dL (Nivel 1: Alerta de Hipoglucemia) • < 54 mg/dL (Nivel 2: Neuroglucopenia crítica) • > 180 mg/dL persistente (Iniciar/ajustar insulinoterapia).",
        "regla_oro_enfermeria": "PROHIBIDO el uso exclusivo de «Escala Móvil / Correcciones aisladas» (Sliding Scale sola) en pacientes con hiperglucemia persistente. El estándar de oro en sala general es el esquema BASAL + BOLO + CORRECCIÓN (o Basal + Corrección si el paciente está en NPO).",
        "recomendaciones_evidencia": [
            {
                "grado": "Nivel A (Evidencia Fuerte)",
                "regla": "Realizar control de glucemia capilar (HGT) antes de las comidas y a las 22:00 hs si el paciente come; o cada 4 a 6 horas si está en ayunas (NPO) o con nutrición enteral/parenteral continua."
            },
            {
                "grado": "Nivel A (Seguridad Hospitalaria)",
                "regla": "Suspender Sulfonilureas, Metformina e iSGLT2 al ingreso en intercurrencias agudas, hipoxia, sepsis, contraste iodado o cirugía. Manejar con insulina programada."
            },
            {
                "grado": "Nivel B (Transición EV a SC)",
                "regla": "Al pasar de Bomba de Insulina EV a Insulina Subcutánea (NPH o Glargina), aplicar la primera dosis basal SC entre 2 y 4 HORAS ANTES de apagar la bomba endovenosa para evitar rebote de cetoacidosis."
            }
        ]
    },
    "fitter_inyeccion": {
        "id": "fitter_inyeccion",
        "sigla": "Consenso FITTER / SAD",
        "titulo": "Recomendaciones Internacionales de Técnica de Inyección de Insulina y Conservación",
        "entidad": "Forum for Injection Technique and Therapy Expert Recommendations (FITTER) & SAD",
        "meta_glucemica": "Absorción subcutánea predecible (0% de inyecciones intramusculares accidentales y 0% de lipohipertrofia).",
        "umbral_alerta": "Agujas > 6 mm en adultos aumentan drásticamente el riesgo de inyección intramuscular inadvertida (que acelera la absorción y causa hipoglucemia grave).",
        "regla_oro_enfermeria": "Aguja de 4 mm en lapicera insertada a 90° sin pliegue cutáneo es segura y eficaz para TODOS los adultos (incluso con obesidad). Solo hacer pliegue en niños pequeños o adultos con caquexia extrema.",
        "recomendaciones_evidencia": [
            {
                "grado": "Grado A1 (FITTER)",
                "regla": "Contar 10 SEGUNDOS completos con el botón de la lapicera presionado a fondo antes de retirar la aguja de la piel para asegurar la entrega total de la dosis."
            },
            {
                "grado": "Grado A1 (FITTER)",
                "regla": "Inspeccionar y PALPAR de pie y acostado los sitios de punción en busca de Lipohipertrofia. Prohibido inyectar dentro de tejido lipohipertrófico."
            },
            {
                "grado": "Grado A2 (Resuspensión NPH)",
                "regla": "Las insulinas turbias (NPH y premezclas) deben rolarse 20 veces entre las palmas e invertirse 10 veces suavemente hasta lograr aspecto blanco lechoso uniforme."
            }
        ]
    },
    "iwgdf_pie": {
        "id": "iwgdf_pie",
        "sigla": "IWGDF / MSAL Argentina",
        "titulo": "Guía Internacional de Prevención y Clasificación del Pie Diabético (SINBAD / WIfI)",
        "entidad": "International Working Group on the Diabetic Foot (IWGDF) & Ministerio de Salud de la Nación",
        "meta_glucemica": "Detección precoz de Pérdida de Sensibilidad Protectora (PSP) y Enfermedad Arterial Periférica (EAP).",
        "umbral_alerta": "Puntaje SINBAD ≥ 3 o presencia de isquemia crítica / infección profunda requiere derivación urgente a equipo multidisciplinario de Pie Diabético.",
        "regla_oro_enfermeria": "Todo paciente con diabetes internado (por cualquier causa) debe tener documentado el examen de los pies sin medias y la palpación de pulsos pedios/tibiales al ingreso.",
        "recomendaciones_evidencia": [
            {
                "grado": "Recomendación Fuerte (IWGDF)",
                "regla": "Estratificar el riesgo anual: Riesgo 0 (sin PSP ni EAP: control anual), Riesgo 1 (PSP o EAP: cada 6 meses), Riesgo 2 (PSP + EAP o deformidad: cada 3-6 meses), Riesgo 3 (antecedente de úlcera o amputación: cada 1-3 meses)."
            },
            {
                "grado": "Contraindicación Absoluta",
                "regla": "Nunca realizar debridamiento cortante en escaras secas de talón o dedos si el pie es ISQUÉMICO (sin pulsos, frío) hasta evaluar revascularización."
            }
        ]
    },
    "sad_cad_ehh": {
        "id": "sad_cad_ehh",
        "sigla": "Consenso SAD / Crisis Hiperglucémicas",
        "titulo": "Protocolo de Emergencia en Cetoacidosis Diabética (CAD) y Estado Hiperosmolar (EHH)",
        "entidad": "Sociedad Argentina de Diabetes (SAD) & Consenso Conjunto ADA/EASD 2024-2025",
        "meta_glucemica": "Descenso gradual de glucemia de 50 a 75 mg/dL por hora (evitar caídas bruscas > 100 mg/dL/h por riesgo de edema cerebral).",
        "umbral_alerta": "Potasio sérico (K+) < 3.3 mEq/L CONTRAINDICA temporalmente el inicio de la infusión de insulina hasta reponer K+.",
        "regla_oro_enfermeria": "El orden terapéutico salvavidas en CAD/EHH es: 1° Expansión con Solución Fisiológica 0.9%, 2° Verificación y reposición de Potasio (K+), 3° Bomba de Insulina Corriente EV (0.1 UI/kg/h).",
        "recomendaciones_evidencia": [
            {
                "grado": "Seguridad Crítica (Nivel A)",
                "regla": "Cuando la glucemia desciende a 200–250 mg/dL en CAD, agregar Dextrosa al 5% o 10% en paralelo y reducir la infusión de insulina a 0.02–0.05 UI/kg/h hasta que cierre el Anión Gap y el pH sea > 7.30."
            },
            {
                "grado": "Alerta Farmacovigilancia",
                "regla": "Sospechar CAD Euglucémica (glucemia < 200 mg/dL con acidosis y cetonemia alta) en todo paciente tratado con gliflozinas (Empagliflozina/Dapagliflozina) que presente náuseas, vómitos, dolor abdominal o taquipnea."
            }
        ]
    }
}


# ==============================================================================
# 2. ÁRBOLES DE DECISIÓN INTERACTIVOS PASO A PASO (ALGORITMOS VIVOS DE GUARDIA)
# ==============================================================================
ALGORITMOS_INTERACTIVOS: Dict[str, Dict[str, Any]] = {
    "algo_hipoglucemia": {
        "id": "algo_hipoglucemia",
        "nombre": "Algoritmo Vivo: Paciente con HGT < 70 mg/dL en Internación",
        "guia_base": "ADA Standards of Care 2025/2026 • Protocolo Regla del 15",
        "nodo_inicial": "paso_1",
        "nodos": {
            "paso_1": {
                "pregunta": "PASO 1: Confirmaste HGT capilar < 70 mg/dL. ¿Cuál es el estado de conciencia y la capacidad de tragar del paciente?",
                "contexto": "Nunca demores el tratamiento esperando confirmación de laboratorio venoso si el paciente tiene síntomas adrenérgicos o neuroglucopénicos.",
                "opciones": [
                    {"texto": "🟢 Paciente DESPIERTO, orientado y puede tragar sin riesgo", "ir_a": "paso_2_consciente"},
                    {"texto": "🔴 Paciente SOMNOLIENTO, confuso, convulsionando o en AYUNAS estricto (NPO)", "ir_a": "paso_2_inconsciente"}
                ]
            },
            "paso_2_consciente": {
                "pregunta": "PASO 2 (Vía Oral Segura): Aplicás la «Regla del 15». ¿Qué le administrás exactamente ahora mismo?",
                "contexto": "Guía ADA/SAD: Se requieren 15 a 20 gramos de carbohidratos de absorción rápida (glucosa pura o sacarosa simple, SIN grasas ni proteínas).",
                "opciones": [
                    {"texto": "🥤 150-200 ml de jugo/gaseosa regular (NO light) o 1 cucharada sopera (3 sobres) de azúcar en agua", "ir_a": "paso_3_control"},
                    {"texto": "🍫 Un chocolate, leche entera o una factura dulce", "ir_a": "error_grasa"}
                ]
            },
            "error_grasa": {
                "pregunta": "⚠️ CORRECCIÓN DE GUÍA: Las grasas y proteínas enlentecen el vaciamiento gástrico y retrasan la subida de glucemia.",
                "contexto": "En la fase aguda de una hipoglucemia el cerebro necesita glucosa inmediata en sangre. Evitá chocolates, leche entera o panificados con grasa en el minuto cero.",
                "opciones": [
                    {"texto": "🔄 Entendido: administrar 15 g de azúcar disuelta en agua e ir al control de los 15 minutos", "ir_a": "paso_3_control"}
                ]
            },
            "paso_2_inconsciente": {
                "pregunta": "PASO 2 (Emergencia Nivel 3 — Vía Oral PROHIBIDA): Protegés vía aérea lateralizando al paciente. ¿Tiene vía venosa permeable?",
                "contexto": "Intentar dar líquidos por boca en este estado provoca neumonía aspirativa o asfixia.",
                "opciones": [
                    {"texto": "💉 SÍ tiene vía periférica permeable", "ir_a": "paso_3_ev"},
                    {"texto": "🚨 NO tiene vía venosa (o colapsó el acceso periférico)", "ir_a": "paso_3_glucagon"}
                ]
            },
            "paso_3_ev": {
                "pregunta": "PASO 3 (Rescate Endovenoso): Administrás 15 a 25 g de Glucosa hipertónica EV en bolo lento (ej. 3 a 5 ampollas de Dextrosa 25% o 50% diluidas, seguido de lavado con SF) y dejás infusión continua de Dextrosa 10%.",
                "contexto": "El efecto del bolo EV de dextrosa dura apenas 30-45 minutos; si la causa fue Insulina NPH, Glargina o Glibenclamida, volverá a caer si no dejás goteo de mantenimiento.",
                "opciones": [
                    {"texto": "✅ Pasar al control a los 15 minutos y auditoría de causa raíz", "ir_a": "paso_final_exito"}
                ]
            },
            "paso_3_glucagon": {
                "pregunta": "PASO 3 (Rescate Intramuscular/Subcutáneo): Administrás Glucagón 1 mg IM o SC en muslo/deltoides mientras otro operador coloca vía venosa.",
                "contexto": "El Glucagón libera las reservas de glucógeno del hígado en 10-15 minutos. Al despertar, suele causar náuseas: mantener al paciente en decúbito lateral.",
                "opciones": [
                    {"texto": "✅ Pasar al control a los 15 minutos y auditoría de causa raíz", "ir_a": "paso_final_exito"}
                ]
            },
            "paso_3_control": {
                "pregunta": "PASO 3 (Reevaluación Cronometrada a los 15 Minutos): Repetís el HGT capilar a los 15 minutos exactos. ¿Qué valor obtenés?",
                "contexto": "No esperes 1 hora para volver a medir. El control es estrictamente a los 15 minutos.",
                "opciones": [
                    {"texto": "📈 HGT subió a 84 mg/dL (Ya superó los 70 mg/dL)", "ir_a": "paso_4_colacion"},
                    {"texto": "📉 HGT sigue en 58 mg/dL (Continúa < 70 mg/dL)", "ir_a": "paso_2_consciente"}
                ]
            },
            "paso_4_colacion": {
                "pregunta": "PASO 4 (Prevención de Recaída): Como falta más de 1 hora para su próxima comida, le indicás una colación con carbohidrato complejo + proteína (ej. 3 galletitas de agua con queso o medio sándwich).",
                "contexto": "¡Atención Enfermería! Nunca suspendas la dosis basal de insulina del día siguiente sin orden médica, pero sí auditá por qué ocurrió la hipoglucemia.",
                "opciones": [
                    {"texto": "🏁 Finalizar protocolo y ver Checklist de Registro de Enfermería", "ir_a": "paso_final_exito"}
                ]
            },
            "paso_final_exito": {
                "pregunta": "🏆 PROTOCOLO COMPLETADO SEGÚN GUÍA ADA / SAD",
                "contexto": "Registro obligatorio en evolución de enfermería: 1) Hora y valor de HGT inicial, 2) Síntomas presentes, 3) gramos y vía de carbohidrato administrado, 4) HGT a los 15 minutos, 5) Causa probable (¿comió menos de la bandeja? ¿pico de NPH nocturna? ¿sulfonilurea en falla renal?).",
                "opciones": [
                    {"texto": "🔁 Reiniciar Algoritmo desde el Paso 1", "ir_a": "paso_1"}
                ]
            }
        }
    },
    "algo_preoperatorio": {
        "id": "algo_preoperatorio",
        "nombre": "Algoritmo Vivo: Paciente con Diabetes que va a Cirugía o Contraste EV",
        "guia_base": "Consenso Perioperatorio SAD / ADA 2025",
        "nodo_inicial": "inicio_preop",
        "nodos": {
            "inicio_preop": {
                "pregunta": "PASO 1: El paciente queda en AYUNAS a partir de las 22:00 hs para cirugía o estudio con contraste mañana a las 08:00 hs. ¿Qué medicación toma habitualmente?",
                "contexto": "El 60% de los eventos adversos glucémicos en sala quirúrgica ocurren por errores en el manejo de la medicación la mañana del procedimiento.",
                "opciones": [
                    {"texto": "💊 Toma Antidiabéticos Orales (Metformina, Glibenclamida, Empagliflozina)", "ir_a": "preop_orales"},
                    {"texto": "💉 Usa Insulina Basal (NPH o Glargina) + Insulina Rápida en las comidas", "ir_a": "preop_insulina"}
                ]
            },
            "preop_orales": {
                "pregunta": "PASO 2 (Manejo de Comprimidos): ¿Qué indica el consenso para la mañana de la cirugía/estudio?",
                "contexto": "Revisá el tiempo de suspensión de cada familia farmacológica:",
                "opciones": [
                    {"texto": "✅ Suspender Sulfonilureas y Metformina esa mañana (y mantener Metformina suspendida 48 hs si recibe contraste iodado). Confirmar que iSGLT2 se haya suspendido 3-4 días antes.", "ir_a": "preop_cierre"},
                    {"texto": "❌ Darle sus comprimidos habituales a las 06:00 AM con un sorbo de agua.", "ir_a": "preop_error_oral"}
                ]
            },
            "preop_error_oral": {
                "pregunta": "⚠️ ALERTA DE SEGURIDAD: Administrar secretagogos (Glibenclamida/Glimepirida) en ayunas quirúrgico causa hipoglucemia intraquirúrgica enmascarada por la anestesia.",
                "contexto": "Durante la anestesia general el paciente no puede manifestar sudoración ni temblor.",
                "opciones": [
                    {"texto": "🔄 Volver y aplicar protocolo correcto de suspensión", "ir_a": "preop_orales"}
                ]
            },
            "preop_insulina": {
                "pregunta": "PASO 2 (Manejo de Insulinas en Ayuno Quirúrgico): El paciente está en ayunas a las 07:00 AM. ¿Se suspende TODA la insulina o se deja una parte de la basal?",
                "contexto": "Guía ADA/SAD: Si suspendés el 100% de la insulina basal en un paciente insulinorrequiriente o DBT1, entrará en Cetoacidosis en pleno quirófano por las hormonas de estrés quirúrgico.",
                "opciones": [
                    {"texto": "✅ SUSPENDER toda insulina prandial (Rápida/Ultrarrápida del desayuno), pero ADMINISTRAR la Insulina Basal reducida (75-80% de la dosis de Glargina, o 50% de la dosis matinal de NPH) según indicación médica, con control de HGT cada 2-4 hs y Dextrosa EV si es necesario.", "ir_a": "preop_cierre"},
                    {"texto": "❌ Suspender absolutamente todas las insulinas (incluso la basal) hasta el día siguiente.", "ir_a": "preop_insulina"}
                ]
            },
            "preop_cierre": {
                "pregunta": "🏆 CHECKLIST PERIOPERATORIO COMPLETADO",
                "contexto": "Meta glucémica intra y perioperatoria según consenso: mantener HGT entre 140 y 180 mg/dL con controles cada 2 a 4 horas mientras dure el ayuno.",
                "opciones": [
                    {"texto": "🔁 Reiniciar Algoritmo Perioperatorio", "ir_a": "inicio_preop"}
                ]
            }
        }
    }
}


# ==============================================================================
# 3. COPILOTO IA RAG ESTILO NOTEBOOKLM CONECTADO A LAS 10 UNIDADES Y GUÍAS
# ==============================================================================
def consultar_copiloto_guias(
    consulta: str,
    consenso_foco: str = "todos",
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Motor RAG Clínico estilo NotebookLM:
    - Permite consultar en lenguaje natural las 10 Unidades Académicas, los Consensos
      Oficiales (ADA 2025/2026, SAD, MSAL, FITTER, IWGDF), escenarios especiales de
      guardia y documentos propios agregados al Cuaderno RAG.
    - Soporta agregar nuevos documentos/apuntes al RAG mediante el prefijo ADD_RAG_DOC::
    - Soporta filtro de fuentes y modo de respuesta (estudio / guardia / examen) en consenso_foco.
    """
    import importlib
    import rag_notebooklm_engine as rag_mod
    importlib.reload(rag_mod)

    # Si el usuario está guardando un nuevo documento/guía en la Biblioteca RAG
    if consulta.startswith("ADD_RAG_DOC::"):
        partes = consulta.split("::", 3)
        titulo_doc = partes[1] if len(partes) > 1 else "Apunte Clínico"
        fuente_doc = partes[2] if len(partes) > 2 else "Bibliografía Propia"
        texto_doc = partes[3] if len(partes) > 3 else ""
        nuevo = rag_mod.guardar_documento_custom_rag(titulo_doc, texto_doc, fuente_doc)
        docs_totales = rag_mod.cargar_documentos_custom_rag()
        return {
            "modo": "Biblioteca RAG Actualizada",
            "respuesta": f"✅ **Documento «{nuevo['titulo']}» indexado exitosamente en el Cuaderno RAG.** Ahora podés hacerle cualquier pregunta abierta y el Copiloto lo citará junto con las 10 Unidades y las Guías Oficiales.",
            "citas": [f"[Nuevo] {nuevo['fuente']} — {nuevo['titulo']}"],
            "citas_detalle": [{
                "num": 1,
                "titulo": nuevo["titulo"],
                "fuente": nuevo["fuente"],
                "unidad_num": 0,
                "extracto": nuevo["contenido"][:300]
            }],
            "preguntas_sugeridas": [
                f"Resumime los puntos clave de {nuevo['titulo']}",
                "¿Qué dice este documento sobre los cuidados de enfermería?"
            ],
            "custom_docs_count": len(docs_totales)
        }

    # Parsear alcance_fuentes y modo_respuesta desde consenso_foco (formato "alcance|modo")
    alcance = "todas"
    modo = "estudio"
    if consenso_foco and "|" in consenso_foco:
        p1, p2 = consenso_foco.split("|", 1)
        alcance = p1.strip() or "todas"
        modo = p2.strip() or "estudio"
    elif consenso_foco:
        alcance = consenso_foco.strip()

    return rag_mod.ejecutar_consulta_rag_notebooklm(
        consulta=consulta,
        consensos_oficiales=CONSENSOS_OFICIALES,
        alcance_fuentes=alcance,
        modo_respuesta=modo,
        api_key=api_key
    )

