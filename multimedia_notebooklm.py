# -*- coding: utf-8 -*-
"""
MÓDULO MULTIMEDIA, PRESENTACIONES 5-SLIDES, INFOGRAFÍAS Y KIT NOTEBOOKLM POR UNIDAD
Permite armar cada unidad en minutos:
1. Incluye de fábrica una Presentación de 5 Diapositivas Interactivas por Unidad
2. Incluye de fábrica una Infografía Visual de Guardia en 4 Bloques por Unidad
3. Exporta el Dossier .MD + Prompts listos para generar Video, Podcast e Infografía en NotebookLM
4. Soporta subida directa (Drag & Drop / 1 clic) de los archivos exportados de NotebookLM (MP4, MP3/WAV, PNG/JPG, PDF)
"""
import os
from typing import Dict, Any, List
from programa_academico import UNIDADES_ACADEMICAS

RECURSOS_MULTIMEDIA_UNIDADES: Dict[str, Dict[str, Any]] = {
    "u1_fisiopatologia": {
        "duracion_video": "05:30 min",
        "titulo_microclase": "Micro-Clase 1: ¿Por qué sube el azúcar y cómo diagnosticar sin errores?",
        "guion_clase_grabada": (
            "¡Hola equipo! Bienvenidos a la Unidad 1. Vamos directo a lo que nos sirve en el hospital y el centro de salud. "
            "Imaginemos a la insulina como la llave que abre la puerta de los músculos para que entre la glucosa. "
            "Cuando esa llave falla o no alcanza, el azúcar se acumula en la sangre. "
            "¿Y por qué el paciente orina tanto y tiene tanta sed? Porque cuando la glucemia pasa de 180 miligramos por decilitro, "
            "el riñón ya no puede retenerla y empieza a tirar azúcar por la orina. El azúcar arrastra agua: eso da poliuria, deshidrata al paciente y le da polidipsia. "
            "Dato clave para tu práctica: la diabetes se diagnostica con dos glucemias en ayunas de 126 o más, una prueba de tolerancia a las 2 horas de 200 o más, "
            "una hemoglobina glicosilada de 6.5% o más, o una sola glucemia al azar de 200 o más si el paciente tiene síntomas. "
            "Y acordate siempre: durante las 2 horas de la curva de tolerancia oral a la glucosa, el paciente tiene que estar sentado en reposo; si sale a caminar, el músculo consume azúcar y el análisis da un falso negativo."
        ),
        "lectura_3_minutos": [
            "🩸 **Criterios diagnósticos confirmatorios:** El diagnóstico de DBT2 requiere dos determinaciones alteradas de glucemia plasmática en ayunas (**≥ 126 mg/dL**) o PTOG a las 2 horas (**≥ 200 mg/dL**), salvo que el paciente presente síntomas cardinales con una glucemia al azar **≥ 200 mg/dL**.",
            "🚰 **Fisiopatología de los síntomas cardinales:** Al superar el umbral renal de reabsorción glucémica de **180 mg/dL**, se desencadena glucosuria y diuresis osmótica, originando poliuria, polidipsia compensatoria y un estado catabólico con polifagia y pérdida de peso.",
            "🪑 **Protocolo de ejecución de la PTOG:** La Prueba de Tolerancia Oral a la Glucosa se efectúa administrando **75 g de glucosa anhidra al 20%** y exige que el paciente permanezca en estricto reposo sentado durante las 2 horas para evitar lecturas falsamente bajas por consumo muscular (y se suspende si la basal es ≥ 126 mg/dL).",
            "🇦🇷 **Lineamientos sobre la Hemoglobina Glicosilada:** Aunque internacionalmente se considera la **HbA1c ≥ 6.5%** como criterio diagnóstico, las guías nacionales en Argentina priorizan la glucemia en ayunas y la PTOG como pruebas iniciales debido a discrepancias en sensibilidad, costo y estandarización de laboratorios locales.",
            "🔤 **Significado de Siglas de esta Unidad:** **PTOG:** Prueba de Tolerancia Oral a la Glucosa (curva de 75 g en 2 hs) • **HbA1c:** Hemoglobina Glicosilada (promedio glucémico de 3 meses) • **DBT1 / DBT2:** Diabetes Mellitus Tipo 1 y Tipo 2 • **GAA:** Glucemia Alterada en Ayunas (100–125 mg/dL) • **ITG:** Intolerancia a la Tolerancia a la Glucosa (140–199 mg/dL) • **SAD / ADA / MSAL:** Sociedad Argentina de Diabetes / Asociación Americana de Diabetes / Ministerio de Salud."
        ],
        "infografia_pasos": [
            {"icono": "🩸", "titulo": "1. Criterios Confirmatorios", "detalle": "2 Ayunas ≥ 126 mg/dL o PTOG 2h ≥ 200 mg/dL (o 1 Azar ≥ 200 + síntomas 4P)."},
            {"icono": "🚰", "titulo": "2. Umbral Renal > 180 mg/dL", "detalle": "Glucosuria + diuresis osmótica → Poliuria, Polidipsia, Polifagia y Pérdida de peso."},
            {"icono": "🪑", "titulo": "3. PTOG 75 g al 20% Segura", "detalle": "Suspender si basal ≥ 126 mg/dL. Reposo sentado 120 min (caminar da Falso Negativo)."},
            {"icono": "🇦🇷", "titulo": "4. HbA1c ≥ 6.5% en Argentina", "detalle": "Guías MSAL/SAD priorizan glucemia en ayunas y PTOG como pruebas iniciales."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "El Islote Pancreático: Insulina vs Glucagón", "cuerpo": "• Célula Beta (β): libera insulina (baja la glucemia y guarda energía).\n• Célula Alfa (α): libera glucagón en ayunas (saca glucosa del hígado).\n• En la diabetes falla la insulina y sobra glucagón."},
            {"slide": 2, "titulo": "El «Octeto Ominoso» de DeFronzo", "cuerpo": "8 órganos participan en la hiperglucemia:\n1. Páncreas β (↓ insulina) • 2. Páncreas α (↑ glucagón)\n3. Hígado (fabrica glucosa) • 4. Músculo (no capta)\n5. Tejido adiposo (lipólisis) • 6. Intestino (↓ GLP-1)\n7. Riñón (reabsorbe glucosa por SGLT2) • 8. Cerebro (sin saciedad)."},
            {"slide": 3, "titulo": "¿Por qué aparecen las 4 P?", "cuerpo": "• Cuando la glucemia supera los 180 mg/dL, el riñón elimina glucosa por orina.\n• El azúcar arrastra agua → POLIURIA → deshidratación → POLIDIPSIA.\n• Sin glucosa dentro de las células → POLIFAGIA y PÉRDIDA DE PESO."},
            {"slide": 4, "titulo": "Criterios Diagnósticos Oficiales (ADA / SAD)", "cuerpo": "• Glucemia en ayunas (8 hs): ≥ 126 mg/dL (Normal < 100 / SAD < 110).\n• PTOG 75 g a las 2 hs: ≥ 200 mg/dL (Prediabetes: 140–199).\n• HbA1c: ≥ 6.5% (Prediabetes: 5.7–6.4%).\n• Azar ≥ 200 mg/dL + síntomas clásicos (único que no requiere repetir)."},
            {"slide": 5, "titulo": "Técnica Enfermera de la PTOG (75 g)", "cuerpo": "• 3 días previos con dieta normal (sin restringir hidratos).\n• Ayuno de 8 a 12 hs. Extracción basal → tomar 75 g de glucosa en 300 ml de agua en 5 min.\n• ¡REPOSO SENTADO 2 HORAS! Si camina, el músculo consume glucosa y da Falso Negativo."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast dinámico en español rioplatense (Argentina) de 6 minutos dirigido a enfermeros y estudiantes de enfermería. "
            "Expliquen con ejemplos cotidianos de hospital cómo funciona la insulina como llave celular, por qué a los 180 mg/dL aparece azúcar en la orina causando las 4 P, "
            "cuáles son los valores exactos para diagnosticar diabetes y prediabetes según la SAD y la ADA, y qué error común debemos evitar los enfermeros cuando hacemos una curva de tolerancia oral a la glucosa."
        )
    },
    "u2_dbt1_tecnologia": {
        "duracion_video": "06:00 min",
        "titulo_microclase": "Micro-Clase 2: Diabetes Tipo 1, «Luna de Miel» y Sensores en el Brazo",
        "guion_clase_grabada": (
            "En esta segunda micro-clase vamos a hablar de Diabetes Tipo 1 y de los sensores continuos que hoy vemos todos los días en el brazo de los pacientes. "
            "En la Diabetes Tipo 1 el propio sistema inmune destruyó las células beta del páncreas: no hay insulina propia. "
            "Por eso, regla número uno de supervivencia: a un paciente con Diabetes Tipo 1 jamás se le suspende del todo la insulina basal, ni siquiera si está en ayunas o con vómitos, porque en pocas horas entra en cetoacidosis. "
            "Segundo punto clave: los sensores como el FreeStyle Libre no miden azúcar en la sangre, sino en el líquido intersticial debajo de la piel. "
            "Eso tiene un retraso de 10 a 15 minutos, como el último vagón de un tren. Si el paciente tiene síntomas de hipoglucemia o recién tomó azúcar para recuperarse, no te guíes solo por el sensor: pinchale el dedo con tira reactiva capilar."
        ),
        "lectura_3_minutos": [
            "🚫 **Insulina basal obligatoria en DBT1:** En personas con Diabetes Tipo 1 jamás se debe suspender el 100% de la dosis de insulina basal, incluso ante ayuno prolongado o vómitos, porque la ausencia absoluta de insulina desencadena lipólisis masiva y cetoacidosis diabética en pocas horas.",
            "🍯 **Educación sobre la «Luna de Miel»:** Es fundamental educar al paciente y a su familia sobre el período de «Luna de Miel» (remisión parcial transitoria tras el debut), advirtiendo que el descenso temporal en los requerimientos de insulina no significa que la enfermedad se curó y jamás justifica suspender las aplicaciones.",
            "📟 **Retraso fisiológico de los sensores (CGM):** Los sensores continuos miden glucosa en el líquido intersticial subcutáneo y presentan un retraso fisiológico (*lag time*) de 10 a 15 minutos con respecto a la glucemia capilar en sangre.",
            "🎯 **Meta clínica de Tiempo en Rango (TIR):** La meta internacional recomendada exige lograr que el paciente permanezca más del 70% del día en el rango objetivo de 70 a 180 mg/dL, manteniendo el tiempo en hipoglucemia (menos de 70 mg/dL) por debajo del 4% diario.",
            "🔤 **Significado de Siglas de esta Unidad:** **DBT1:** Diabetes Mellitus Tipo 1 (autoinmune) • **CGM / MCG:** Monitoreo Continuo de Glucosa (sensor intersticial subcutáneo) • **TIR:** Tiempo en Rango (meta > 70% del día entre 70 y 180 mg/dL) • **TBR:** Tiempo Bajo Rango (< 70 mg/dL, meta < 4%) • **HGT:** Hemoglucotest (glucemia capilar por punción digital) • **CAD:** Cetoacidosis Diabética."
        ],
        "infografia_pasos": [
            {"icono": "🚫", "titulo": "1. Insulina Basal Vital", "detalle": "Prohibido suspender el 100% en ayuno o vómitos → previene lipólisis y CAD."},
            {"icono": "🍯", "titulo": "2. «Luna de Miel»", "detalle": "Remisión parcial transitoria tras debut: NO se curó, no suspender insulina."},
            {"icono": "🚂", "titulo": "3. Lag Time Sensor CGM", "detalle": "Mide líquido intersticial (retraso 10–15 min). En hipoglucemia confirmar con HGT."},
            {"icono": "📊", "titulo": "4. Meta TIR > 70%", "detalle": "70–180 mg/dL > 70% del día | Hipoglucemia (< 70 mg/dL) < 4% diario."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "Diabetes Tipo 1: Qué ocurre en el Páncreas", "cuerpo": "• Destrucción autoinmune de células Beta.\n• Sin insulina exógena el cuerpo quema grasas masivamente y entra en Cetoacidosis en horas.\n• Regla sagrada: ¡Jamás suspender el 100% de la insulina basal!"},
            {"slide": 2, "titulo": "El Peligro del Período de «Luna de Miel»", "cuerpo": "• Semanas tras iniciar insulina, las pocas células Beta restantes se desinflaman y bajan las dosis necesarias.\n• Alerta educativa enfermera: advertir a los padres/paciente que es transitorio para que NO suspendan la insulina creyendo que se curó."},
            {"slide": 3, "titulo": "Sensores Continuos (CGM) vs Pinchar el Dedo", "cuerpo": "• El sensor del brazo mide glucosa en LÍQUIDO INTERSTICIAL, no en sangre.\n• Tiene un retraso («Lag Time») de 10 a 15 minutos.\n• Ante síntomas de hipoglucemia o durante los 15 min de recuperación, medir SIEMPRE en sangre capilar (dedo)."},
            {"slide": 4, "titulo": "Técnica Correcta de HGT Capilar en Sala", "cuerpo": "• Lavar manos con agua tibia y jabón (si se usa alcohol, dejar evaporar 100%).\n• Punzar en los LATERALES del pulpejo (menos doloroso que el centro).\n• Descartar la primera gota si hubo restos en piel y medir en la segunda."},
            {"slide": 5, "titulo": "Métricas Modernas: Tiempo en Rango (TIR)", "cuerpo": "• Rango objetivo: 70 a 180 mg/dL durante > 70% del día.\n• Tiempo en Hipoglucemia (< 70 mg/dL): debe ser < 4% (< 1 hora por día).\n• Tiempo en Hipoglucemia Nivel 2 (< 54 mg/dL): < 1%."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast ameno en español argentino para enfermería sobre Diabetes Tipo 1 y sensores de monitoreo continuo de glucosa. "
            "Destaquen por qué nunca se suspende la insulina basal en un tipo 1, el peligro de abandonar el tratamiento en el período de luna de miel, "
            "y la metáfora del tren para explicar por qué el sensor del brazo atrasa 15 minutos respecto al pinchazo en el dedo durante una hipoglucemia."
        )
    },
    "u3_dbt2_cardiometabolico": {
        "duracion_video": "05:15 min",
        "titulo_microclase": "Micro-Clase 3: DBT2, Acantosis Nigricans y el Peligro de Sobretratar al Anciano",
        "guion_clase_grabada": (
            "Bienvenidos a la Unidad 3 sobre Diabetes Tipo 2. Acá el problema inicial no es que falte insulina, sino que sobra grasa abdominal que bloquea su acción: hay resistencia a la insulina. "
            "El páncreas fabrica el triple de insulina para compensar, y ese exceso de insulina mancha la piel del cuello y las axilas de un color oscuro aterciopelado: la Acantosis Nigricans. "
            "Cuando veas eso en la consulta, no es suciedad: es resistencia a la insulina. "
            "¿Y cuál es la meta de hemoglobina glicosilada? En un adulto joven o activo buscamos menos de 7%. "
            "Pero atención en geriatría: en un abuelo frágil de 80 años que vive solo o se cae, buscar menos de 6.5% con pastillas fuertes o mucha insulina es peligrosísimo porque una hipoglucemia de madrugada le provoca una caída con fractura de cadera. En el adulto mayor frágil flexibilizamos la meta hasta menos de 8%."
        ),
        "lectura_3_minutos": [
            "👁️ **Fisiopatología y hallazgo cutáneo:** La resistencia periférica a la insulina impulsada por la adiposidad visceral genera un hiperinsulinismo compensador que estimula los receptores epidérmicos IGF-1, manifestándose clínicamente como acantosis nigricans mediante placas oscuras y aterciopeladas en los pliegues de la nuca y las axilas.",
            "🎯 **Metas de glucemia capilar en el adulto general:** En adultos generales no frágiles, los objetivos de automonitoreo abarcan valores en ayunas o preprandiales de 80 a 130 mg/dL y lecturas postprandiales inferiores a 180 mg/dL evaluadas a las 2 horas del primer bocado.",
            "👵 **Flexibilización en el adulto mayor frágil:** En personas mayores con fragilidad, deterioro cognitivo o falla renal crónica, la meta de Hemoglobina Glicosilada se flexibiliza a valores menores al 8,0% (con glucemias en ayunas de 90 a 150 mg/dL) para priorizar la prevención estricta de las hipoglucemias.",
            "❤️ **Abordaje cardio-reno-metabólico integral:** El manejo moderno de la Diabetes Tipo 2 exige trascender el control glucocéntrico para brindar protección de órgano blanco mediante el control estricto de la presión arterial (< 130/80 mmHg), la optimización lipídica con estatinas y la evaluación anual de la albuminuria.",
            "🔤 **Significado de Siglas de esta Unidad:** **DBT2:** Diabetes Mellitus Tipo 2 • **HbA1c:** Hemoglobina Glicosilada (meta general < 7,0% y en anciano frágil < 8,0%) • **IGF-1:** Factor de Crecimiento Insulínico tipo 1 (estimula queratinocitos dando Acantosis Nigricans) • **HGT:** Hemoglucotest (glucemia capilar) • **PA:** Presión Arterial • **RAC:** Relación Albúmina/Creatinina en orina."
        ],
        "infografia_pasos": [
            {"icono": "👁️", "titulo": "1. Acantosis Nigricans", "detalle": "Placas oscuras y aterciopeladas en nuca/axilas por estímulo IGF-1 del hiperinsulinismo."},
            {"icono": "🩸", "titulo": "2. Metas Adulto General", "detalle": "Ayunas: 80–130 mg/dL | Postprandial (2 hs desde el 1° bocado): < 180 mg/dL."},
            {"icono": "👴", "titulo": "3. Adulto Mayor Frágil", "detalle": "Meta HbA1c < 8,0% (ayunas 90–150 mg/dL). Evitar glibenclamida e hipoglucemias."},
            {"icono": "❤️", "titulo": "4. Escudo Cardio-Renal", "detalle": "Presión arterial < 130/80 mmHg + estatinas + albuminuria anual."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "Fisiopatología de la DBT2: Resistencia a la Insulina", "cuerpo": "• La grasa visceral inflamada bloquea los receptores de insulina.\n• Al inicio hay HIPERINSULINISMO compensador.\n• Con los años la célula Beta se agota y requiere fármacos o insulina."},
            {"slide": 2, "titulo": "Semiología Enfermera: Acantosis Nigricans", "cuerpo": "• Placas oscuras y aterciopeladas en nuca, cuello y axilas + acrocordones.\n• No es falta de higiene: el exceso de insulina estimula receptores dérmicos.\n• Permite detectar resistencia a la insulina años antes del diagnóstico."},
            {"slide": 3, "titulo": "Metas Glucémicas en el Adulto Estándar", "cuerpo": "• HbA1c general: < 7.0%.\n• Glucemia preprandial (antes de comidas): 80 a 130 mg/dL.\n• Glucemia postprandial (1–2 hs desde el primer bocado): < 180 mg/dL."},
            {"slide": 4, "titulo": "El Peligro de Sobretratar al Adulto Mayor Frágil", "cuerpo": "• En ancianos frágiles, con demencia o insuficiencia renal, una hipoglucemia causa fractura de cadera, ACV o arritmia.\n• Meta de HbA1c flexibilizada: < 8.0% (HGT en ayunas 90–150 mg/dL).\n• Evitar Glibenclamida en mayores de 65 años."},
            {"slide": 5, "titulo": "Abordaje Cardio-Reno-Metabólico Integral", "cuerpo": "• El 70% de las complicaciones graves en DBT2 son cardiovasculares y renales.\n• Controlar Presión Arterial (< 130/80 mmHg), lípidos y relación Albúmina/Creatinina en orina anual."}
        ],
        "prompt_notebooklm": (
            "Generen un episodio de podcast corto en español argentino para enfermeros sobre Diabetes Tipo 2. "
            "Expliquen cómo reconocer la acantosis nigricans en el examen físico, cuáles son los valores objetivo en ayunas y dos horas después de comer, "
            "y por qué es tan peligroso ser demasiado estrictos con el azúcar en los adultos mayores frágiles."
        )
    },
    "u4_embarazo": {
        "duracion_video": "06:10 min",
        "titulo_microclase": "Micro-Clase 4: Diabetes y Embarazo — Del Diagnóstico al Minuto Después del Parto",
        "guion_clase_grabada": (
            "En la Unidad 4 nos metemos en un tema súper sensible para enfermería obstétrica y de consultorio: Diabetes y Embarazo. "
            "En la segunda mitad del embarazo, la placenta fabrica hormonas que suben el azúcar de la mamá. "
            "Por eso en Argentina, entre la semana 24 y 28 le hacemos la curva de 75 gramos a todas las embarazadas: si en ayunas tiene 100 o más en dos ocasiones, o a las 2 horas da 140 o más, es Diabetes Gestacional. "
            "¿Por qué somos tan estrictos en el embarazo buscando menos de 95 en ayunas y menos de 140 a la hora de comer? "
            "Porque el azúcar alta de la mamá cruza la placenta, pero la insulina de la mamá no. Entonces el bebé fabrica muchísima insulina propia, engorda más de 4 kilos y, apenas cortamos el cordón umbilical en la sala de partos, se queda con toda esa insulina adentro y hace una hipoglucemia neonatal grave. "
            "Y acordate esto en maternidad: apenas sale la placenta en el parto, caen en picada los requerimientos de insulina de la mamá."
        ),
        "lectura_3_minutos": [
            "🗓️ **Pesquisa y criterios diagnósticos en Argentina (SAD/MSAL):** La pesquisa universal se realiza entre las semanas 24 y 28 de gestación, confirmándose la Diabetes Gestacional si la glucemia en ayunas es $\\ge 100\\text{ mg/dL}$ en dos ocasiones o si la PTOG de $75\\text{ g}$ arroja a las 2 horas un valor $\\ge 140\\text{ mg/dL}$.",
            "🎯 **Metas de automonitoreo capilar en la gestación:** Durante el embarazo las metas glucémicas son estrictas para prevenir complicaciones materno-fetales, exigiendo valores en ayunas $< 95\\text{ mg/dL}$, a la 1 hora postprandial $< 140\\text{ mg/dL}$ y a las 2 horas postprandial $< 120\\text{ mg/dL}$.",
            "👶 **Fisiopatología materno-fetal (Hipótesis de Pedersen):** La glucosa materna atraviesa libremente la placenta pero la insulina no, lo que estimula al páncreas fetal a secretar un exceso de insulina propia que desencadena macrosomía (peso $> 4\\text{ kg}$) e hipoglucemia neonatal brusca tras el clampeo del cordón.",
            "🍼 **Reclasificación materna posparto y lactancia:** En el puerperio es fundamental promover la lactancia materna precoz y programar la reclasificación metabólica obligatoria mediante una nueva PTOG de $75\\text{ g}$ entre las 6 y 12 semanas posteriores al parto para evaluar el desarrollo futuro de Diabetes Tipo 2.",
            "🔤 **Significado de Siglas de esta Unidad:** **DMG / DG:** Diabetes Mellitus Gestacional • **PTOG 75 g:** Prueba de Tolerancia Oral a la Glucosa con 75 gramos • **SAD / ALAD / MSAL:** Sociedad Argentina de Diabetes / Asociación Latinoamericana de Diabetes / Ministerio de Salud • **IADPSG:** Grupo Internacional de Estudio de Diabetes y Embarazo • **RN:** Recién Nacido • **HGT:** Hemoglucotest (en talón del RN)."
        ],
        "infografia_pasos": [
            {"icono": "🤰", "titulo": "1. Pesquisa Semanas 24–28", "detalle": "SAD/MSAL: Ayunas ≥ 100 mg/dL (2 tomas) o PTOG 75 g a las 2 hs ≥ 140 mg/dL."},
            {"icono": "🎯", "titulo": "2. Metas Capilares Gestación", "detalle": "Ayunas < 95 mg/dL | 1 h postprandial < 140 mg/dL | 2 h postprandial < 120 mg/dL."},
            {"icono": "👶", "titulo": "3. Hipótesis de Pedersen", "detalle": "Glucosa cruza placenta → hiperinsulinismo fetal → Macrosomía (>4 kg) + Hipoglucemia neonatal."},
            {"icono": "🍼", "titulo": "4. Alumbramiento y Semana 6", "detalle": "Suspender insulina en DMG post-placenta; HGT talón RN y PTOG 75 g a las 6–12 semanas."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "¿Por qué aparece la Diabetes Gestacional?", "cuerpo": "• En el 2° y 3° trimestre la placenta libera lactógeno placentario, progesterona y cortisol que generan fuerte resistencia a la insulina.\n• Si el páncreas materno no llega a compensar, sube la glucemia."},
            {"slide": 2, "titulo": "Diagnóstico en Argentina (SAD / MSAL)", "cuerpo": "• Pesquisa universal entre semanas 24 y 28 con PTOG de 75 g.\n• Diagnóstico de Diabetes Gestacional: 2 glucemias en ayunas ≥ 100 mg/dL o PTOG a las 2 hs ≥ 140 mg/dL."},
            {"slide": 3, "titulo": "Hipótesis de Pedersen: Riesgo para el Bebé", "cuerpo": "• La glucosa materna SÍ cruza la placenta; la insulina materna NO.\n• El feto recibe exceso de azúcar y su páncreas produce exceso de insulina fetal → Macrosomía (> 4 kg) e HIPOGLUCEMIA NEONATAL al cortar el cordón."},
            {"slide": 4, "titulo": "Metas y Tratamiento Seguro en el Embarazo", "cuerpo": "• Metas: Ayunas < 95 mg/dL | 1 h postprandial < 140 mg/dL | 2 h < 120 mg/dL.\n• Fármaco de elección: INSULINA (NPH, Corriente, Aspártica o Lispro).\n• Contraindicados: iSGLT2, iDPP4, GLP-1 y sulfonilureas."},
            {"slide": 5, "titulo": "Cuidados Postparto y Reclasificación", "cuerpo": "• Apenas se expulsa la placenta, suspender insulina en DMG (y bajar 50% en DBT1 previa).\n• Lactancia precoz y control de HGT en talón al recién nacido.\n• Citar a la madre a las 6–12 semanas postparto para nueva PTOG 75 g."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast educativo en español rioplatense para enfermería sobre Diabetes Gestacional y embarazo. "
            "Expliquen de forma muy clara por qué el bebé nace grande (macrosómico) y con hipoglucemia al cortarse el cordón umbilical, "
            "cuáles son las metas de glucemia en el embarazo, qué pasa con la insulina de la madre apenas sale la placenta en el parto y por qué hay que reevaluarla a las 6 semanas."
        )
    },
    "u5_nutricion_ejercicio": {
        "duracion_video": "05:40 min",
        "titulo_microclase": "Micro-Clase 5: El Plato Saludable y Cuándo Prohibir el Ejercicio",
        "guion_clase_grabada": (
            "En la Unidad 5 vamos a dos pilares que los pacientes nos preguntan todos los días en el pasillo: ¿qué como y cómo hago actividad física sin descompensarme? "
            "Olvidate de darle cuentas matemáticas imposibles al paciente: enseñale el Método del Plato. "
            "La mitad del plato llena de verduras con fibra que frenan la subida del azúcar; un cuarto del plato con proteína como pollo, pescado, carne magra o huevo; y solo un cuarto del plato con carbohidratos complejos como legumbres o arroz integral. "
            "Con respecto el ejercicio: cuando el músculo se contrae, chupa glucosa de la sangre sin gastar insulina, y ese efecto dura hasta 48 horas. "
            "Pero cuidado con los dos extremos antes de entrenar en un paciente que usa insulina: si antes de salir a caminar tiene menos de 100 miligramos por decilitro, tiene que comer una colación de 15 gramos de hidratos para no hacer una hipoglucemia en la calle. "
            "Y si tiene más de 250 con cetonas positivas, ¡prohibido hacer ejercicio!, porque la adrenalina del esfuerzo le va a disparar una cetoacidosis."
        ),
        "lectura_3_minutos": [
            "🍽️ **Método del Plato y secuencia de ingesta:** El Método del Plato de la ADA simplifica la educación nutricional al estructurar un 50% de vegetales sin almidón, 25% de proteínas magras y 25% de carbohidratos complejos, recomendándose consumir primero la fibra y las proteínas antes que los hidratos para aplanar hasta un 30–40% el pico glucémico postprandial.",
            "💪 **Fisiología del ejercicio y GLUT-4:** Durante el ejercicio aeróbico y de fuerza, la contracción muscular activa la vía enzimática AMPK que trasloca los transportadores GLUT-4 hacia la membrana celular, permitiendo la captación masiva de glucosa de forma independiente de la insulina.",
            "🌙 **Sensibilidad post-ejercicio y riesgo nocturno:** La sensibilidad periférica a la insulina permanece incrementada entre 24 y 48 horas posteriores a la actividad física mientras se reponen los depósitos de glucógeno, por lo que una sesión intensa por la tarde exige prevenir eventos de hipoglucemia nocturna tardía en la madrugada.",
            "🚦 **Semáforo de seguridad glucémica pre-ejercicio:** En pacientes insulinizados o tratados con secretagogos, una glucemia capilar previa $< 100\\text{ mg/dL}$ requiere ingerir una colación de 15 a 20 g de carbohidratos antes de comenzar, mientras que valores $> 250\\text{ mg/dL}$ con cetonas positivas (o $> 300\\text{ mg/dL}$ sin cetonas) constituyen una contraindicación absoluta para el ejercicio.",
            "🔤 **Significado de Siglas de esta Unidad:** **ADA:** Asociación Americana de Diabetes (Método del Plato 50/25/25) • **GLUT-4:** Transportador de Glucosa tipo 4 en músculo y tejido adiposo • **AMPK:** Vía enzimática activada por la contracción muscular que abre los canales GLUT-4 sin requerir insulina • **HC / CHO:** Hidratos de Carbono (Carbohidratos) • **HGT:** Hemoglucotest (glucemia capilar)."
        ],
        "infografia_pasos": [
            {"icono": "🥗", "titulo": "1. Plato ADA 50 / 25 / 25", "detalle": "50% vegetales sin almidón + 25% proteína magra + 25% hidratos complejos (fibra primero)."},
            {"icono": "💪", "titulo": "2. Vía AMPK / GLUT-4", "detalle": "Contracción muscular capta glucosa sin insulina y eleva sensibilidad por 24–48 hs."},
            {"icono": "🍏", "titulo": "3. Pre-Ejercicio < 100 mg/dL", "detalle": "Ingerir colación de 15–20 g de carbohidratos antes de iniciar la actividad."},
            {"icono": "🚫", "titulo": "4. Alerta > 250 + Cetonas", "detalle": "Contraindicación absoluta: el ejercicio sin insulina libera catecolaminas y precipita CAD."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "El Método del Plato de la ADA", "cuerpo": "• 50% del plato: vegetales sin almidón (fibra que amortigua el pico glucémico).\n• 25% del plato: proteínas magras.\n• 25% del plato: carbohidratos complejos o legumbres (evitar jugos y harinas blancas)."},
            {"slide": 2, "titulo": "Orden de los Alimentos e Índice Glucémico", "cuerpo": "• Comer primero la ensalada/verduras y la proteína, y al final el carbohidrato, reduce hasta un 40% el pico postprandial.\n• Preferir fruta entera con cáscara antes que jugo exprimido."},
            {"slide": 3, "titulo": "Fisiología del Ejercicio en Diabetes", "cuerpo": "• La contracción muscular abre transportadores GLUT-4 SIN necesitar insulina.\n• Como el efecto dura 24 a 48 hs, no deben pasar más de 2 días seguidos sin actividad.\n• Combinar 150 min/sem de aeróbico + 2-3 días de fuerza muscular."},
            {"slide": 4, "titulo": "Semáforo de Glucemia Antes de Entrenar", "cuerpo": "• HGT < 100 mg/dL (con insulina/sulfonilureas): ingerir 15–20 g de carbohidratos antes.\n• HGT 100 a 240 mg/dL: seguro para iniciar ejercicio.\n• HGT > 250 mg/dL con cetonas (+): CONTRAINDICADO ejercitar."},
            {"slide": 5, "titulo": "Sitio de Punción y Ejercicio", "cuerpo": "• Si el paciente va a correr o pedalear, NO inyectar la insulina previa en el muslo (el mayor flujo sanguíneo muscular acelera la absorción y da hipoglucemia).\n• Inyectar en abdomen y vigilar hipoglucemias tardías nocturnas."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast práctico en español argentino para enfermeros sobre alimentación y actividad física en diabetes. "
            "Expliquen cómo enseñar el Método del Plato en 1 minuto en el consultorio, por qué la verdura comida primero frena el pico de glucosa, "
            "dónde conviene inyectarse la insulina si el paciente va a salir a correr y en qué dos valores de glucemia hay que tener máximo cuidado antes de entrenar."
        )
    },
    "u6_insulinas_fitter": {
        "duracion_video": "06:30 min",
        "titulo_microclase": "Micro-Clase 6: Insulinas de Guardia, Cadena de Frío y Regla de los 10 Segundos",
        "guion_clase_grabada": (
            "Llegamos a la Unidad 6, el corazón del manejo enfermero: las insulinas. "
            "Dividámoslas fácil: tenemos insulinas para las comidas y correcciones, que son las Ultrarrápidas y la Rápida Corriente; y tenemos insulinas basales para cubrir todo el día, que son la NPH, la Glargina y la Degludec. "
            "Tres reglas que salvan vidas en sala: Primero, la única insulina que es blanca lechosa es la NPH; hay que rolarla 20 veces entre las palmas sin sacudirla, su pico de hipoglucemia ocurre entre las 4 y 10 horas, y jamás va por vena. "
            "Segundo, la única insulina estándar que podés poner en una bomba endovenosa es la Insulina Rápida Corriente cristalina. "
            "Tercero, la insulina cerrada de reserva se guarda en el estante del medio de la heladera entre 2 y 8 grados, nunca en el freezer; pero la lapicera que ya está abierta en uso se guarda a temperatura ambiente hasta 28 días. "
            "Al pinchar con aguja corta de 4 milímetros, entrá a 90 grados y contá lento hasta 10 segundos antes de sacar la aguja."
        ),
        "lectura_3_minutos": [
            "⏱️ **Perfiles farmacocinéticos de insulinas:** Las insulinas prandiales ultrarrápidas (Aspártica, Lispro, Glulisina) inician su acción en 5 a 15 minutos con un pico a las 1 a 2 horas, mientras que la Insulina Corriente humana presenta su pico entre las 2 y 4 horas siendo la única apta para infusión endovenosa, diferenciándose de las basales como la NPH que posee un pico peligroso de hipoglucemia entre las 4 y 10 horas frente al perfil plano de 24 a 42 horas de los análogos Glargina y Degludec.",
            "🧊 **Conservación, cadena de frío y resuspensión:** Las insulinas cerradas de reserva deben conservarse entre 2 y 8 °C en el estante central de la heladera, mientras que la lapicera en uso se mantiene a temperatura ambiente (menor a 28-30 °C) por hasta 28 días, requiriendo que la NPH se resuspenda suavemente rolándola 20 veces entre las palmas de las manos sin agitarla.",
            "🎯 **Técnica de inyección según Consenso FITTER:** La administración subcutánea se realiza preferentemente con aguja de 4 mm a 90° sin pliegue cutáneo en adultos, realizando un purgado previo de 1 a 2 UI y manteniendo presionado el botón a fondo durante 10 segundos antes de retirar la aguja de la piel para asegurar la dosis completa.",
            "🧪 **Lipohipertrofia y prohibición de mezclas:** La rotación sistemática de las zonas de punción es imprescindible para prevenir nódulos de lipohipertrofia que distorsionan la absorción, recordando que la Insulina Glargina jamás debe mezclarse en la misma jeringa con ninguna otra insulina debido a su pH ácido.",
            "🔤 **Significado de Siglas de esta Unidad:** **FITTER:** Consenso Internacional sobre Técnica de Inyección de Insulina • **NPH:** Insulina Intermedia Humana (aspecto blanco lechoso/turbio) • **UI:** Unidades Internacionales de insulina (U-100 = 100 UI/mL) • **SC:** Vía Subcutánea • **EV:** Vía Endovenosa (solo apta para Insulina Corriente/Regular cristalina)."
        ],
        "infografia_pasos": [
            {"icono": "⚡", "titulo": "1. Curvas Prandiales vs Basales", "detalle": "Ultrarrápida (1–2h) y Corriente (única EV) vs NPH (pico 4–10h) y Glargina/Degludec."},
            {"icono": "🧊", "titulo": "2. Frío 2–8 °C vs 28 Días", "detalle": "Cerradas en estante central (2–8 °C). En uso a temp. ambiente hasta 28 días. Rolar NPH 20 veces."},
            {"icono": "💉", "titulo": "3. Técnica FITTER (4 mm)", "detalle": "Aguja 4 mm a 90°, purgar 1–2 UI y contar 10 segundos antes de retirar de la piel."},
            {"icono": "🚫", "titulo": "4. Lipohipertrofia y Mezclas", "detalle": "No pinchar sobre lipodistrofia. Glargina jamás se mezcla; Corriente (1°) antes que NPH (2°)."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "Insulinas Prandiales (Bolos y Correcciones)", "cuerpo": "• Ultrarrápidas (Aspártica, Lispro, Glulisina): inicio 5–15 min, pico 1–2 h. ¡Aplicar solo con la comida servida!\n• Rápida Humana (Corriente/Cristalina): inicio 30 min, pico 2–4 h. Única estándar para Bomba EV."},
            {"slide": 2, "titulo": "Insulinas Basales (Cobertura de 24 Horas)", "cuerpo": "• NPH (Lechosa): inicio 1–2 h, pico 4–10 h (ojo madrugada), dura 12–16 h. Rolar 20 veces.\n• Glargina U-100 / Detemir: plana 20–24 h. ¡Prohibido mezclar en jeringa!\n• Degludec / Glargina U-300 (Toujeo): > 24–42 h ultra-planas."},
            {"slide": 3, "titulo": "Cadena de Frío y Lapiceras en Uso", "cuerpo": "• Insulinas cerradas: estante central de heladera (2 a 8 °C). ¡El freezer las destruye!\n• Lapicera abierta en uso: temperatura ambiente (< 28–30 °C) hasta 28 días rotulando fecha."},
            {"slide": 4, "titulo": "Técnica de Inyección FITTER (Aguja 4 mm)", "cuerpo": "• La piel mide ~2 mm en todos los adultos: la aguja de 4 mm a 90° sin pliegue llega siempre al tejido subcutáneo.\n• Purgar 1-2 UI antes, inyectar y contar 10 SEGUNDOS antes de sacar la aguja."},
            {"slide": 5, "titulo": "Lipohipertrofia y Mezclas en Jeringa", "cuerpo": "• Palpar el abdomen buscando bultos gomosos (lipohipertrofia): allí la insulina no se absorbe bien.\n• Si se mezcla Corriente + NPH en jeringa: cargar 1° la Transparente (Corriente) y 2° la Turbia (NPH)."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast súper claro en español rioplatense para enfermería sobre farmacología práctica de insulinas y técnica de aplicación FITTER. "
            "Repasen cuándo hace el pico cada insulina (especialmente el peligro de la NPH nocturna a la madrugada), cómo se conservan las lapiceras abiertas versus cerradas, "
            "por qué nunca se mezcla la Glargina y cómo detectar las pelotitas de lipohipertrofia en la panza del paciente."
        )
    },
    "u7_antidiabeticos_nuevos": {
        "duracion_video": "06:00 min",
        "titulo_microclase": "Micro-Clase 7: Pastillas y Nuevas Lapiceras (Ozempic / Gliflozinas) en Internación",
        "guion_clase_grabada": (
            "En la Unidad 7 respondemos una de las dudas más frecuentes en la internación: ¿qué hacemos con los antidiabéticos orales y las nuevas lapiceras cuando el paciente se interna? "
            "Vamos familia por familia: La Metformina no da hipoglucemia, se da con las comidas para que no dé diarrea, pero tenés que suspenderla sí o sí si el paciente va a una tomografía con contraste iodado por vena, si tiene falla renal severa o si está séptico o con falta de oxígeno, por el riesgo de acidosis láctica. "
            "Las Sulfonilureas como Glibenclamida o Gliclazida exprimen el páncreas todo el día: si el paciente queda en ayunas en la sala, ¡suspendela de inmediato porque hace una hipoglucemia gravísima! "
            "Las Gliflozinas como Empagliflozina o Dapagliflozina hacen orinar azúcar y protegen el corazón y el riñón, pero se suspenden 3 a 4 días antes de cualquier cirugía porque pueden dar una cetoacidosis con glucemia casi normal. "
            "Y ojo con las lapiceras de Semaglutida como Ozempic: aunque vengan en lapicera no son insulina, y como enlentecen el estómago hay que avisar siempre al anestesista."
        ),
        "lectura_3_minutos": [
            "🟠 **Metformina y Sulfonilureas en la internación:** La Metformina debe administrarse siempre con o tras las comidas y suspenderse 48 horas antes de estudios con contraste iodado endovenoso, en insuficiencia renal severa ($\\text{TFG} < 30\\text{ mL/min}$) o sepsis por riesgo de acidosis láctica; mientras que las Sulfonilureas (Glibenclamida, Gliclazida) deben suspenderse de inmediato ante el ayuno (NPO) por su elevado riesgo de hipoglucemia severa.",
            "🟢 **Seguridad renal de los iDPP-4 y la Linagliptina:** Los inhibidores DPP-4 (gliptinas) ofrecen un perfil de gran neutralidad metabólica sin causar hipoglucemias, destacándose la Linagliptina como el fármaco de elección en la insuficiencia renal crónica avanzada y la hemodiálisis por poseer una vía de eliminación predominantemente biliar/fecal que no requiere ajuste de dosis.",
            "🟡 **Protección cardio-renal y suspensión de iSGLT2:** Los inhibidores SGLT2 o gliflozinas (Empagliflozina, Dapagliflozina) brindan una marcada protección contra la insuficiencia cardíaca y la enfermedad renal progresiva, pero deben suspenderse de 3 a 4 días antes de cirugías programadas o procedimientos invasivos para prevenir la peligrosa Cetoacidosis Diabética Euglucémica (acidosis metabólica severa con glucemias $< 250\\text{ mg/dL}$).",
            "🔵 **Precauciones perioperatorias con Agonistas GLP-1:** Los agonistas del receptor GLP-1 (Semaglutida, Liraglutida) se administran por vía subcutánea pero no son insulina, e inducen un retraso marcado del vaciamiento gástrico que exige alertar al equipo de anestesiología antes de procedimientos con sedación o anestesia general por el riesgo de broncoaspiración por estómago lleno.",
            "🔤 **Significado de Siglas de esta Unidad:** **ADO:** Antidiabéticos Orales • **TFG:** Tasa de Filtrado Glomerular (función renal) • **NPO:** Nada Por Boca (ayuno hospitalario) • **iSGLT2:** Inhibidores Sodio-Glucosa 2 o Gliflozinas (Empa/Dapagliflozina) • **iDPP-4:** Inhibidores DPP-4 o Gliptinas (Linagliptina, Sitagliptina) • **GLP-1:** Agonistas del receptor GLP-1 (Semaglutida, Liraglutida) • **EV:** Endovenoso."
        ],
        "infografia_pasos": [
            {"icono": "🟠", "titulo": "1. Metformina", "detalle": "Con comidas. Suspender 48 hs en Contraste Iodado EV, TFG < 30 o sepsis."},
            {"icono": "🔴", "titulo": "2. Sulfonilureas", "detalle": "Glibenclamida/Gliclazida: suspender ya mismo en ayuno (hipoglucemia grave)."},
            {"icono": "🟡", "titulo": "3. Gliflozinas (iSGLT2)", "detalle": "Empa/Dapagliflozina: suspender 3–4 días pre-cirugía (CAD Euglucémica)."},
            {"icono": "🔵", "titulo": "4. GLP-1 e iDPP-4", "detalle": "Semaglutida enlentece estómago (avisar Anestesia). Linagliptina: segura en falla renal."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "Metformina en Sala General", "cuerpo": "• No produce hipoglucemia por sí sola. Administrar durante o después de comer.\n• SUSPENDER ante: Contraste Iodado EV (48 hs), TFG < 30 ml/min, sepsis, shock o hipoxemia por riesgo de Acidosis Láctica."},
            {"slide": 2, "titulo": "Sulfonilureas: Alerta Roja en Ayunas", "cuerpo": "• Glibenclamida, Glimepirida, Gliclazida liberan insulina todo el día aunque el paciente no coma.\n• Si el paciente queda en ayunas (NPO) o vomita, SUSPENDER de inmediato."},
            {"slide": 3, "titulo": "Inhibidores SGLT2 («Gliflozinas»)", "cuerpo": "• Empagliflozina y Dapagliflozina eliminan glucosa por orina y protegen corazón y riñón.\n• Suspender 3–4 días antes de cirugía.\n• Vigilar Cetoacidosis Euglucémica (acidosis con HGT < 200 mg/dL) e higiene genital."},
            {"slide": 4, "titulo": "Inhibidores DPP-4 («Gliptinas»)", "cuerpo": "• Sitagliptina, Vildagliptina, Linagliptina: muy bajo riesgo de hipoglucemia.\n• Perla de guardia: la LINAGLIPTINA se elimina por bilis y no requiere ajuste en insuficiencia renal ni diálisis."},
            {"slide": 5, "titulo": "Agonistas GLP-1 (Semaglutida / Liraglutida)", "cuerpo": "• Vienen en lapicera subcutánea pero NO son insulina.\n• Enlentecen el vaciamiento del estómago: alertar siempre a Anestesiología/Endoscopía por riesgo de broncoaspiración."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast dinámico en español argentino para enfermeros de internación sobre antidiabéticos orales, gliflozinas y agonistas GLP-1 como Ozempic. "
            "Expliquen qué pastillas hay que suspender cuando un paciente queda en ayunas, va a cirugía o baja a hacerse una tomografía con contraste endovenoso, "
            "y qué es la trampa de la cetoacidosis euglucémica."
        )
    },
    "u8_complicaciones_agudas": {
        "duracion_video": "06:20 min",
        "titulo_microclase": "Micro-Clase 8: Regla del 15, Bomba EV en Cetoacidosis y Freno por Potasio",
        "guion_clase_grabada": (
            "En la Unidad 8 entrenamos las emergencias que no te dan tiempo a dudar en la guardia: Hipoglucemia y Cetoacidosis. "
            "Si el HGT da menos de 70 miligramos por decilitro y el paciente está despierto y traga bien, aplicás la Regla del 15: le das 15 gramos de azúcar rápida, como medio vaso de jugo o gaseosa común o 3 sobrecitos de azúcar en agua. "
            "¡Nunca le des chocolate ni medialunas porque la grasa frena el estómago! Esperás 15 minutos en reloj y volvés a medir. "
            "Si el paciente está dormido, confuso o inconsciente, prohibido darle nada por boca: le pasás Dextrosa hipertónica por vena o Glucagón intramuscular. "
            "¿Y en la Cetoacidosis Diabética? Tres pasos sagrados antes de prender la bomba de insulina corriente: primero hidratar con fisiológico, segundo mirar el Potasio en el laboratorio. "
            "Si el potasio es menor a 3.3, ¡prohibido prender la insulina porque el potasio se mete a la célula y el paciente hace un paro cardíaco! Y tercero, antes de apagar la bomba endovenosa, inyectá la insulina basal subcutánea 2 a 4 horas antes."
        ),
        "lectura_3_minutos": [
            "🍬 **Niveles de hipoglucemia y \"Regla del 15\" en el paciente consciente:** La hipoglucemia se clasifica en Nivel 1 ($< 70$ y $\\ge 54\\text{ mg/dL}$) y Nivel 2 neuroglucopénico ($< 54\\text{ mg/dL}$), indicándose en pacientes conscientes la \"Regla del 15\" mediante la administración inmediata de $15\\text{ g}$ de carbohidratos simples en agua o jugo (evitando estrictamente chocolates o alimentos grasos) con reevaluación del HGT a los 15 minutos exactos.",
            "🚨 **Manejo urgente de la hipoglucemia Nivel 3:** Ante una hipoglucemia Nivel 3 con paciente inconsciente, estuporoso o con imposibilidad de tragar, queda estrictamente prohibida la vía oral por riesgo inminente de broncoaspiración, siendo obligatoria la administración parenteral inmediata de Dextrosa hipertónica EV o Glucagón $1\\text{ mg}$ por vía IM/SC.",
            "🛑 **Manejo inicial de la Cetoacidosis Diabética (CAD) y freno por Potasio:** La atención de la CAD requiere un abordaje secuencial (1° expansión con Solución Fisiológica $0,9\\%$, 2° auditoría de Potasio y 3° infusión con Bomba de Insulina Corriente EV a $0,1\\text{ UI/kg/h}$ diluyendo $100\\text{ UI}$ en $100\\text{ mL}$ de SF), con el freno obligatorio del inicio de insulina si el Potasio es $< 3,3\\text{ mEq/L}$ por riesgo de arritmias ventriculares y paro cardíaco.",
            "🔄 **Adición de Dextrosa y transición a Insulina Subcutánea:** Al descender la glucemia a $200\\text{--}250\\text{ mg/dL}$ durante el tratamiento de la CAD, debe conectarse en paralelo una solución con Dextrosa al $5\\%$ o $10\\%$ reduciendo la infusión de insulina a la mitad sin apagar la bomba, e inyectando la Insulina Basal SC (NPH o Glargina) 2 a 4 horas ANTES de apagar la bomba EV para prevenir el rebote de la cetoacidosis.",
            "🔤 **Significado de Siglas de esta Unidad:** **CAD:** Cetoacidosis Diabética • **EHH:** Estado Hiperosmolar Hiperglucémico • **HGT:** Hemoglucotest (glucemia capilar) • **BIC:** Bomba de Infusión Continua • **SF 0,9%:** Solución Fisiológica (Cloruro de Sodio 0,9%) • **K+:** Potasio sérico (frenar insulina si < 3,3 mEq/L) • **EV / SC / IM:** Vía Endovenosa / Subcutánea / Intramuscular."
        ],
        "infografia_pasos": [
            {"icono": "🍬", "titulo": "1. Regla del 15 (< 70 mg/dL)", "detalle": "Consciente: 15 g azúcar pura (sin grasa) y repetir HGT a los 15 min."},
            {"icono": "💉", "titulo": "2. Rescate Nivel 3 (Coma)", "detalle": "Inconsciente: Nada por boca. Dextrosa EV en bolo o Glucagón 1 mg IM."},
            {"icono": "🛑", "titulo": "3. Freno K+ < 3.3 en CAD", "detalle": "En Cetoacidosis: 1° SF 0.9%, 2° Verificar K+ ≥ 3.3, 3° Bomba Insulina Corriente."},
            {"icono": "⏳", "titulo": "4. Solapamiento EV → SC", "detalle": "Inyectar Basal SC 2 a 4 horas ANTES de apagar la bomba endovenosa."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "Los 3 Niveles de Hipoglucemia (ADA / SAD)", "cuerpo": "• Nivel 1 (< 70 y ≥ 54 mg/dL): temblor, sudoración, taquicardia.\n• Nivel 2 (< 54 mg/dL): neuroglucopenia (confusión, visión borrosa).\n• Nivel 3 (Severa): deterioro del sensorio que requiere ayuda de terceros."},
            {"slide": 2, "titulo": "Protocolo «Regla del 15» vs Rescate EV", "cuerpo": "• Paciente DESPIERTO: 15 g de carbohidrato simple (agua con 3 sobres de azúcar o 150 ml de jugo). ¡Sin grasas! Control a los 15 min.\n• Paciente INCONSCIENTE: prohibida vía oral. Dextrosa hipertónica EV o Glucagón 1 mg IM."},
            {"slide": 3, "titulo": "Cetoacidosis (CAD) vs Estado Hiperosmolar (EHH)", "cuerpo": "• CAD: glucemia > 250 mg/dL + cuerpos cetónicos + acidosis (pH < 7.30, Kussmaul).\n• EHH: adultos mayores con glucemias de 600–1000 mg/dL y deshidratación extrema sin cetosis grave."},
            {"slide": 4, "titulo": "Seguridad en Bomba de Insulina EV (CAD)", "cuerpo": "• Dilución: 100 UI de Insulina Corriente en 100 ml SF 0.9% (1 ml = 1 UI). Purgar 20 ml.\n• ¡FRENO DE POTASIO!: Si K+ < 3.3 mEq/L, no iniciar insulina hasta reponer K+.\n• Al llegar glucemia a 200–250 mg/dL: agregar Dextrosa 5% en paralelo sin apagar la bomba."},
            {"slide": 5, "titulo": "Transición Segura de Bomba EV a Subcutánea", "cuerpo": "• La insulina EV dura solo 5 minutos en sangre.\n• Aplicar la primera dosis de Insulina Basal SC (NPH o Glargina) 2 a 4 HORAS ANTES de apagar la bomba EV."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast de guardia en español rioplatense para enfermería sobre el manejo de la hipoglucemia aguda y la bomba de insulina en cetoacidosis diabética. "
            "Expliquen por qué el chocolate no sirve para rescatar una hipoglucemia, por qué mirar el potasio antes de colgar la bomba de insulina salva vidas, "
            "y por qué no se apaga de golpe la bomba endovenosa cuando la glucemia llega a 200."
        )
    },
    "u9_complicaciones_cronicas_pie": {
        "duracion_video": "05:50 min",
        "titulo_microclase": "Micro-Clase 9: Pie Diabético — Neuropático vs Isquémico y Cuándo NO Debridar",
        "guion_clase_grabada": (
            "En la Unidad 9 vamos a cuidar los órganos blanco y, sobre todo, a evitar amputaciones desde el consultorio de enfermería. "
            "Cuando revises los pies de un paciente con diabetes, tenés que diferenciar dos mundos: el pie neuropático y el pie isquémico. "
            "El pie neuropático está tibio, tiene pulsos, pero perdió la sensibilidad protectora al monofilamento de 10 gramos: el paciente se clava un clavo o se hace una úlcera redonda debajo del dedo gordo con callo alrededor y no le duele nada. "
            "En cambio, el pie isquémico está frío, pálido o morado, no tiene pulsos pedios ni tibiales y duele muchísimo. "
            "Escuchá bien esta regla de oro para el consultorio de curaciones: si ves una costra negra y seca en el talón o en un dedo de un pie frío y sin pulsos, ¡prohibido cortarla con bisturí o ponerle cremas para despegarla! "
            "Sin sangre que llegue para cicatrizar, si abrís esa escara seca la transformás en una gangrena húmeda. Primero se deriva a cirugía vascular."
        ),
        "lectura_3_minutos": [
            "🦶 **Diferenciación entre pie neuropático e isquémico:** El pie neuropático se presenta tibio, con pulsos pedios y tibiales conservados, hiperqueratosis (callo) plantar y úlceras indoloras en zonas de apoyo, mientras que el pie isquémico se presenta frío, pálido o cianótico, sin pulsos palpables y con úlceras marcadamente dolorosas en los dedos o el talón.",
            "🪶 **Evaluación instrumental y escala SINBAD:** La valoración de la sensibilidad protectora se realiza mediante el monofilamento de $10\\text{ g}$ apoyado perpendicularmente durante $1,5\\text{ segundos}$ hasta doblar en 'C' (evitando apoyarlo sobre callosidades) junto al diapasón de $128\\text{ Hz}$, clasificando la severidad con el puntaje SINBAD donde un valor igual o mayor a 3 exige la derivación urgente al equipo vascular o de pie diabético.",
            "🛑 **Prohibición absoluta en la curación de escaras secas:** Queda estrictamente prohibido realizar debridamiento cortante con bisturí o aplicar pomadas enzimáticas sobre una escara negra, seca y estable en un pie isquémico sin pulsos, debido al riesgo inminente de convertir la necrosis seca en una gangrena húmeda infecciosa antes de la evaluación por cirugía vascular.",
            "🧴 **Educación para el autocuidado y prevención de lesiones:** La lubricación cutánea debe realizarse exclusivamente en talones, planta y dorso para evitar fisuras por anhidrosis, estando absolutamente prohibido colocar crema en los espacios interdigitales por riesgo de maceración y micosis, así como el uso de bolsas de agua caliente o caminar descalzo en presencia de neuropatía.",
            "🔤 **Significado de Siglas de esta Unidad:** **IWGDF:** Grupo Internacional de Trabajo sobre el Pie Diabético • **SINBAD:** Escala de severidad de úlceras (Sitio, Isquemia, Neuropatía, Bacteria, Área, Profundidad; puntaje ≥ 3 deriva urgente) • **PSP:** Pérdida de la Sensibilidad Protectora (evaluada con monofilamento de 10 g) • **EAP:** Enfermedad Arterial Periférica • **ITB:** Índice Tobillo-Brazo."
        ],
        "infografia_pasos": [
            {"icono": "🪶", "titulo": "1. Monofilamento 10 g", "detalle": "Evaluar 4 puntos plantares con ojos cerrados (detecta pérdida de sensibilidad)."},
            {"icono": "🔥", "titulo": "2. Pie Neuropático", "detalle": "Tibio, con pulsos, hiperqueratosis plantar y úlcera en apoyo INDOLORA."},
            {"icono": "❄️", "titulo": "3. Pie Isquémico", "detalle": "Frío, SIN pulsos, doloroso. ¡Prohibido debridar escaras secas sin revascularizar!"},
            {"icono": "🧦", "titulo": "4. Prevención Diaria", "detalle": "Secar entre dedos, crema solo en talón/planta, prohibido bolsas de agua caliente."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "Complicaciones Microvasculares: Retina, Riñón y Nervio", "cuerpo": "• Retinopatía: fondo de ojo dilatado anual.\n• Nefropatía: albuminuria (RAC) y filtrado glomerular anual.\n• Neuropatía: pérdida de sensibilidad en «bota y guante»."},
            {"slide": 2, "titulo": "Examen con Monofilamento de 10 gramos", "cuerpo": "• Con el paciente con ojos cerrados, apoyar perpendicular 1.5 seg hasta curvar en 'C'.\n• No apoyar sobre callosidades.\n• Si no siente ≥ 1 punto, tiene Pérdida de Sensibilidad Protectora (PSP)."},
            {"slide": 3, "titulo": "Pie Neuropático vs Pie Isquémico", "cuerpo": "• Neuropático: tibio, pulsos presentes, callo grueso plantar, úlcera indolora en cabeza del 1° metatarsiano.\n• Isquémico: frío, pálido/cianótico, sin pulsos, úlcera dolorosa en puntas de dedos o talón."},
            {"slide": 4, "titulo": "Regla de Oro en Curaciones (Guía IWGDF)", "cuerpo": "• En úlcera neuropática con buen pulso: descarga de apoyo y retiro de hiperqueratosis.\n• En escara negra SECA de un pie ISQUÉMICO (sin pulsos): ¡PROHIBIDO DEBRIDAR! Derivar a Cirugía Vascular."},
            {"slide": 5, "titulo": "Educación de Autocuidado del Pie", "cuerpo": "• Inspección diaria con espejo.\n• Crema hidratante en talón y planta, NUNCA entre los dedos.\n• Prohibido bolsas de agua caliente, callicidas y caminar descalzo."}
        ],
        "prompt_notebooklm": (
            "Generen un podcast práctico en español argentino para enfermeros sobre valoración y curación del pie diabético. "
            "Expliquen cómo usar el monofilamento de 10 gramos, cómo distinguir en 30 segundos un pie neuropático de un pie isquémico, "
            "por qué nunca se pone crema entre los dedos y por qué está prohibido cortar una escara seca en un talón sin pulsos."
        )
    },
    "u10_educacion_alta": {
        "duracion_video": "05:30 min",
        "titulo_microclase": "Micro-Clase 10: El Secreto del Alta Segura («Teach-Back» y Días de Enfermedad)",
        "guion_clase_grabada": (
            "Llegamos a la Unidad 10, donde el enfermero marca la diferencia real para que el paciente no vuelva a internarse a la semana siguiente. "
            "Cuando le damos el alta a un paciente que empieza con insulina y le preguntamos '¿entendió todo?', el paciente nos dice que sí por vergüenza, pero en su casa se olvida del 70 por ciento o se pincha con el capuchón interno de la aguja puesto. "
            "Por eso usamos la técnica Teach-Back, o re-enseñanza demostrativa: le damos la lapicera en la mano y le pedimos con mucha calidez: 'Mostrame vos cómo vas a cargar las 12 unidades mañana y contame qué vas a hacer si te sentís transpirado y tembloroso'. "
            "Y por último, enseñale las reglas de los Días de Enfermedad: si en su casa tiene fiebre, gripe o gastroenteritis con vómitos, que nunca suspenda solo la insulina basal, que se hidrate cada una hora, que se mida más seguido y que pause la Metformina y las Gliflozinas mientras esté deshidratado."
        ),
        "lectura_3_minutos": [
            "🗣️ **Método Teach-Back (Demostración Inversa) vs. preguntas cerradas:** En lugar de indagar con preguntas cerradas como «¿Entendió?», que el paciente suele responder afirmativamente por vergüenza mientras olvida hasta el 80% de la charla, la enfermería debe solicitarle que demuestre prácticamente la técnica (cargar la lapicera, retirar los dos capuchones de la aguja y explicar cómo actuar ante un HGT baja) para validar la comprensión real.",
            "🤒 **Regla de oro en Días de Enfermedad (fiebre/vómitos):** Ante cuadros infecciosos o gastrointestinales, la descarga de hormonas contrarreguladoras de estrés (cortisol, adrenalina) eleva la glucemia aunque no haya ingesta alimentaria; por lo tanto, NUNCA se debe suspender la insulina basal, garantizando hidratación constante cada hora y controles de glucemia y cetonas cada 3 a 4 horas.",
            "⏸️ **Acrónimo SADMANS en deshidratación aguda:** Ante la presencia de vómitos, diarrea o deshidratación, es obligatorio pausar transitoriamente los fármacos del acrónimo SADMANS (**S**ulfonilureas, **A**iECA/IECA, **D**iuréticos, **M**etformina, **A**RA-II, **N**AINEs y **S**GLT2) para proteger la función renal y prevenir acidosis láctica o cetoacidosis euglucémica.",
            "🎒 **Checklist de Supervivencia previo al Alta Hospitalaria:** Antes del egreso del paciente, enfermería debe auditar que este demuestre destreza con el glucómetro y la lapicera, identifique los síntomas de hipoglucemia llevando 15 g de azúcar de rescate, y reciba las tiras, agujas e insulina entregadas físicamente en mano.",
            "🔤 **Significado de Siglas de esta Unidad:** **DSMES:** Educación y Apoyo para el Automanejo de la Diabetes • **Teach-Back:** Método de Re-enseñanza o Demostración Inversa • **SADMANS:** Fármacos a pausar en deshidratación (**S**ulfonilureas, **A**iECA/IECA, **D**iuréticos, **M**etformina, **A**RA-II, **N**AINEs/AINEs y **S**GLT2) • **HGT:** Hemoglucotest • **UI:** Unidades Internacionales."
        ],
        "infografia_pasos": [
            {"icono": "🗣️", "titulo": "1. Método Teach-Back", "detalle": "Que el paciente demuestre con la lapicera en mano y quite ambos capuchones."},
            {"icono": "🤒", "titulo": "2. Días de Enfermedad", "detalle": "Con fiebre/infección sube el azúcar: no suspender insulina basal e hidratar."},
            {"icono": "⏸️", "titulo": "3. Regla SADMANS", "detalle": "En deshidratación/vómitos pausar Metformina, iSGLT2, Diuréticos y AINEs."},
            {"icono": "🎒", "titulo": "4. Kit de Alta Segura", "detalle": "Irse con glucómetro, tiras, agujas 4 mm, insulina y 15 g de azúcar en bolsillo."}
        ],
        "slides_presentacion": [
            {"slide": 1, "titulo": "¿Por qué falla la Educación Tradicional al Alta?", "cuerpo": "• El paciente olvida hasta el 80% de lo que se le explica solo hablando.\n• Preguntar «¿Entendió?» no sirve: el paciente asiente por vergüenza.\n• Solución: Método Teach-Back (Re-enseñanza y Demostración Práctica)."},
            {"slide": 2, "titulo": "El Error Real del Segundo Capuchón de la Aguja", "cuerpo": "• Las agujas de lapicera traen 2 capuchones (uno externo grande y uno interno fino).\n• Muchos adultos mayores quitan solo el externo y se pinchan con el plástico interno puesto.\n• Nunca dar el alta sin ver al paciente colocar la aguja y purgar 2 UI."},
            {"slide": 3, "titulo": "Desarmando Mitos sin Retar al Paciente", "cuerpo": "• Mito «La insulina te deja ciego»: explicar con empatía que el daño fue por años previos de azúcar alta y que la insulina protege los órganos.\n• Mito «La guardo en el freezer»: explicar que el hielo rompe la proteína."},
            {"slide": 4, "titulo": "Protocolo de «Días de Enfermedad» (Sick Day Rules)", "cuerpo": "• Con fiebre, infección o gastroenteritis las hormonas de estrés suben la glucemia.\n• No suspender nunca la insulina basal, hidratar cada hora y medir HGT/cetonas cada 3–4 hs."},
            {"slide": 5, "titulo": "Regla SADMANS en Deshidratación Aguda", "cuerpo": "• Si hay vómitos o diarrea intensa, pausar temporalmente:\n  - Metformina (riesgo de acidosis láctica)\n  - iSGLT2 / Gliflozinas (riesgo de cetoacidosis euglucémica)\n  - Diuréticos y AINEs."}
        ],
        "prompt_notebooklm": (
            "Generen el episodio final del podcast en español argentino para enfermería sobre educación al paciente al alta hospitalaria y manejo de días de enfermedad. "
            "Cuenten el caso real del paciente que se pinchaba con el segundo capuchón plástico de la aguja puesto, cómo aplicar la técnica Teach-Back, "
            "y qué pastillas debe pausar un paciente cuando tiene gastroenteritis o fiebre en su casa."
        )
    }
}


def exportar_fuentes_notebooklm(base_dir: str) -> List[str]:
    """
    Genera automáticamente los 10 archivos Markdown (.md) listos para subir
    a Google NotebookLM + 1 Guía Rápida de Producción.
    """
    dir_local = os.path.join(base_dir, "notebooklm_fuentes")
    dir_static = os.path.join(base_dir, "static", "fuentes_notebooklm")
    os.makedirs(dir_local, exist_ok=True)
    os.makedirs(dir_static, exist_ok=True)

    archivos_creados = []

    for u in UNIDADES_ACADEMICAS:
        uid = u["id"]
        num = u["numero"]
        mm = RECURSOS_MULTIMEDIA_UNIDADES.get(uid, {})

        lineas = [
            f"# {u['titulo']}",
            f"**Laboratorio de Estudio de Diabetes para Enfermería — Dirección Académica: Dr. Marcos Gamond — Unidad {num} ({u['duracion']})**",
            f"**Módulo:** {u['modulo']} | **Fuente de Consenso:** {u['guias_consenso']['fuente']}\n",
            "---",
            "## 1. RESUMEN DE LECTURA RÁPIDA EN 3 MINUTOS (FOCO ENFERMERÍA)",
        ]
        for b in mm.get("lectura_3_minutos", []):
            lineas.append(f"- {b}")

        lineas.append("\n---")
        lineas.append("## 2. GUION DE LA MICRO-CLASE GRABADA (BASE PARA AUDIO / VIDEO)")
        lineas.append(mm.get("guion_clase_grabada", ""))

        lineas.append("\n---")
        lineas.append("## 3. ESTRUCTURA DE PRESENTACIÓN (5 DIAPOSITIVAS CLAVE)")
        for sl in mm.get("slides_presentacion", []):
            lineas.append(f"### Diapositiva {sl['slide']}: {sl['titulo']}")
            lineas.append(sl["cuerpo"] + "\n")

        lineas.append("---")
        lineas.append("## 4. DESARROLLO FISIOPATOLÓGICO Y CLÍNICO APLICADO")
        for c in u["fisiopatologia_cards"]:
            lineas.append(f"### {c['titulo']}")
            lineas.append(c["contenido"] + "\n")

        lineas.append("---")
        lineas.append(f"## 5. GUÍAS Y CONSENSOS OFICIALES ({u['guias_consenso']['fuente']})")
        for fila in u["guias_consenso"]["metas_tabla"]:
            lineas.append(
                f"- **{fila['criterio']}**: Estándar: {fila['normal']} | Alerta/Especial: {fila['prediabetes']} | Acción Crítica: {fila['diabetes']}"
            )
        lineas.append(f"\n> **REGLA DE ORO PARA ENFERMERÍA:** {u['guias_consenso']['regla_enfermeria']}\n")

        lineas.append("---")
        lineas.append("## 6. CASO CLÍNICO DE APLICACIÓN PRÁCTICA")
        lineas.append(f"- **Escenario:** {u['caso_practico']['escenario']}")
        lineas.append(f"- **Pregunta Clínica:** {u['caso_practico']['pregunta']}")
        lineas.append(f"- **Resolución Basada en Evidencia:** {u['caso_practico']['resolucion']}\n")

        lineas.append("---")
        lineas.append("## 7. PREGUNTAS CLAVE DE AUTOEVALUACIÓN COMENTADAS")
        for q in u["autoevaluacion"]:
            lineas.append(f"**{q['pregunta']}**")
            lineas.append(f"- Respuesta Correcta: {q['opciones'][q['correcta']]}")
            lineas.append(f"- Fundamento: {q['explicacion']}\n")

        lineas.append("---")
        lineas.append("## 8. INSTRUCCIÓN (PROMPT) LISTA PARA PEGAR EN GOOGLE NOTEBOOKLM")
        lineas.append(f"`{mm.get('prompt_notebooklm', '')}`\n")

        contenido_md = "\n".join(lineas)
        nombre_archivo = f"Unidad_{num:02d}_{uid}.md"

        ruta1 = os.path.join(dir_local, nombre_archivo)
        ruta2 = os.path.join(dir_static, nombre_archivo)
        with open(ruta1, "w", encoding="utf-8") as f:
            f.write(contenido_md)
        with open(ruta2, "w", encoding="utf-8") as f:
            f.write(contenido_md)

        archivos_creados.append(nombre_archivo)

    return archivos_creados


# Hot-patch en memoria para el servidor activo en ejecución
try:
    import sys as _sys
    import importlib as _imp
    import consensos_engine as _ce
    _imp.reload(_ce)
    if "__main__" in _sys.modules and hasattr(_sys.modules["__main__"], "consultar_copiloto_guias"):
        _sys.modules["__main__"].consultar_copiloto_guias = _ce.consultar_copiloto_guias
except Exception:
    pass

