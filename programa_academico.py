# -*- coding: utf-8 -*-
"""
PROGRAMA ACADÉMICO ASINCRÓNICO COMPLETO EN DIABETOLOGÍA PARA ENFERMERÍA
10 Unidades Estructuradas + Fisiopatología + Guías ADA/SAD/MSAL + Casos + Autoevaluación
Diseñado para comercialización como Curso / Diplomatura Asincrónica (60 hs cátedra)
"""
from typing import List, Dict, Any

META_PROGRAMA: Dict[str, Any] = {
    "titulo": "Laboratorio de Estudio de Diabetes para Enfermería — Dr. Marcos Gamond",
    "subtitulo": "Escuela de Educación en Diabetes • Dirección Académica: Dr. Marcos Gamond (ADA • SAD • MSAL • IWGDF • FITTER)",
    "director": "Dr. Marcos Gamond",
    "horas_catedra": 60,
    "total_unidades": 10,
    "nota_aprobacion": 70
}

UNIDADES_ACADEMICAS: List[Dict[str, Any]] = [
    # ==========================================================================
    # UNIDAD 1: FISIOPATOLOGÍA, CLASIFICACIÓN Y DIAGNÓSTICO
    # ==========================================================================
    {
        "numero": 1,
        "id": "u1_fisiopatologia",
        "icono": "🧬",
        "titulo": "Unidad 1: Principios Fisiopatológicos, Clasificación y Diagnóstico",
        "modulo": "Bases Biomédicas Aplicadas",
        "duracion": "6 hs cátedra",
        "resumen": "Cómo funciona el eje insulina-glucagón, el Octeto Ominoso de DeFronzo, diferencias entre insulinorresistencia e insulinopenia y criterios diagnósticos oficiales.",
        "fisiopatologia_cards": [
            {
                "titulo": "La Insulina como «Llave Celular» y el Islote de Langerhans",
                "contenido": "Las células Beta (β) del páncreas secretan insulina de forma bifásica: una secreción basal continua las 24 hs (que frena la producción hepática de glucosa) y bolos pulsátiles al comer (que abren los transportadores GLUT-4 en músculo y tejido adiposo). Las células Alfa (α) secretan glucagón, hormona contrarreguladora que libera glucosa del hígado en el ayuno."
            },
            {
                "titulo": "Del Triunvirato al «Octeto Ominoso» (Fisiopatología Moderna)",
                "contenido": "En la hiperglucemia intervienen 8 mecanismos simultáneos: 1) Menor secreción de insulina por la célula β, 2) Exceso de glucagón por la célula α, 3) Mayor producción hepática de glucosa, 4) Resistencia muscular a la insulina, 5) Lipólisis acelerada en adipocitos, 6) Déficit del efecto incretina intestinal (GLP-1/GIP), 7) Mayor reabsorción renal de glucosa por transportadores SGLT2, y 8) Disfunción de neurotransmisores hipotalámicos (saciedad)."
            },
            {
                "titulo": "Fisiopatología de los «4 Síntomas Cardinales» (Las 4 P)",
                "contenido": "Cuando la glucemia supera el umbral renal (~180 mg/dL), aparece GLUCOSURIA. La glucosa en los túbulos renales arrastra agua por ósmosis → POLIURIA (orinar mucho) → deshidratación intracelular que estimula el centro de la sed → POLIDIPSIA. Como la glucosa no entra a las células, hay hambre celular → POLIFAGIA y catabolismo proteico/graso → PÉRDIDA DE PESO."
            }
        ],
        "guias_consenso": {
            "fuente": "ADA Standards of Care 2025/2026 (Cap. 2) & Sociedad Argentina de Diabetes (SAD)",
            "metas_tabla": [
                {"criterio": "Glucemia Plasmática en Ayunas (8 hs)", "normal": "< 100 mg/dL (SAD < 110)", "prediabetes": "100 a 125 mg/dL", "diabetes": "≥ 126 mg/dL (repetir para confirmar)"},
                {"criterio": "PTOG 75 g a las 2 horas", "normal": "< 140 mg/dL", "prediabetes": "140 a 199 mg/dL (Tolerancia alterada)", "diabetes": "≥ 200 mg/dL"},
                {"criterio": "Hemoglobina Glicosilada (HbA1c)", "normal": "< 5.7%", "prediabetes": "5.7% a 6.4%", "diabetes": "≥ 6.5% (método estandarizado NGSP)"},
                {"criterio": "Glucemia al Azar + Síntomas Clásicos (4 P)", "normal": "-", "prediabetes": "-", "diabetes": "≥ 200 mg/dL (Diagnóstico directo sin repetir)"}
            ],
            "regla_enfermeria": "Durante la realización de una Prueba de Tolerancia Oral a la Glucosa (PTOG) con 75 g de glucosa anhidra al 20%, es una regla clínica prioritaria de enfermería garantizar que el paciente permanezca sentado en reposo absoluto, sin comer, fumar ni caminar durante los 120 minutos que dura la prueba (si camina, los músculos captan glucosa por vías independientes de la insulina generando un falso negativo). Asimismo, la prueba debe suspenderse de inmediato si la glucemia basal en ayunas arroja un valor ≥ 126 mg/dL o si ocurren vómitos. Recordá además que una glucemia al azar ≥ 200 mg/dL acompañada de síntomas clásicos (4 P) es el único criterio que confirma la diabetes en una sola toma sin requerir repetición."
        },
        "caso_practico": {
            "escenario": "En la guardia ambulatoria de enfermería recibís a un paciente de 52 años citado para realizarse una PTOG de 75 g. Al tomar la muestra de glucemia basal en ayunas antes de darle el vaso, el glucómetro/laboratorio indica 138 mg/dL.",
            "pregunta": "¿Le administrás los 75 g de glucosa o suspendés la sobrecarga? ¿Por qué?",
            "resolucion": "Se SUSPENDE la administración de la sobrecarga de glucosa, se registra el valor basal (138 mg/dL ≥ 126 mg/dL) y se deriva al médico para repetir una segunda glucemia plasmática en ayunas otro día. Administrar 75 g de glucosa a un paciente que ya tiene ≥ 126 mg/dL en ayunas sobrecarga innecesariamente al páncreas y expone a hiperglucemia severa."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En la guardia ambulatoria de enfermería recibís a un paciente de 52 años citado para realizarse una PTOG de 75 g. Al tomar la muestra de glucemia basal en ayunas, el laboratorio/glucómetro indica 138 mg/dL. ¿Cuál es la conducta de enfermería adecuada y justificada?",
                "opciones": [
                    "A) Administrar la solución con 75 g de glucosa anhidra y tomar la segunda extracción a los 120 minutos.",
                    "B) Suspender la administración de la sobrecarga de glucosa, registrar el valor basal y derivar al médico para repetir una glucemia plasmática en ayunas de confirmación otro día.",
                    "C) Indicar al paciente que camine durante 20 minutos para reducir la glucemia antes de ingerir la carga de glucosa."
                ],
                "correcta": 1,
                "explicacion": "Un valor de glucemia basal en ayunas igual o mayor a 126 mg/dL ya cumple criterio de sospecha/confirmación de diabetes. Las normas de procedimiento establecen suspender la PTOG ante valores basales ≥ 126 mg/dL para evitar sobrecargar innecesariamente al páncreas y prevenir picos de hiperglucemia severa iatrogénica; el paciente debe reevaluarse con una segunda glucemia plasmática en ayunas en otro día."
            },
            {
                "pregunta": "2. Situación clínica: Atendés en el centro de salud a una paciente que refiere sed intensa (polidipsia), necesidad de orinar frecuentemente durante la noche (poliuria) y pérdida de 5 kg de peso en el último mes. Al realizar una glucemia plasmática al azar (sin ayuno previo), se obtiene un valor de 220 mg/dL. ¿Cómo se interpreta este resultado?",
                "opciones": [
                    "A) Es un valor no diagnóstico por no estar en ayunas, requiriéndose citar a la paciente al día siguiente para una glucemia plasmática en ayunas.",
                    "B) Es indispensable realizar una PTOG de 75 g para confirmar si existe diabetes o prediabetes.",
                    "C) Confirma el diagnóstico definitivo de Diabetes Mellitus, siendo el único criterio que no requiere una segunda prueba de confirmación."
                ],
                "correcta": 2,
                "explicacion": "La presencia de los síntomas cardinales indica que las glucemias han superado persistentemente el umbral renal de reabsorción de glucosa (180 mg/dL), desencadenando diuresis osmótica y catabolismo proteico y lipídico. Ante este cuadro clínico claro, una glucemia plasmática al azar ≥ 200 mg/dL establece el diagnóstico inmediato de diabetes mellitus en una sola determinación."
            },
            {
                "pregunta": "3. Situación clínica: Durante los 120 minutos de espera de una PTOG, un paciente decide salir a caminar rápido alrededor del centro asistencial para «distraerse». ¿Qué repercusión fisiopatológica tiene esta conducta en el resultado del examen?",
                "opciones": [
                    "A) Ninguna, porque el metabolismo de la sobrecarga de glucosa depende exclusivamente de la secreción pancreática basal de insulina.",
                    "B) Genera un resultado falso negativo, ya que la contracción muscular estimula la captura celular de glucosa de forma independiente de la insulina.",
                    "C) Produce un falso positivo, ya que la actividad física genera acumulación de lactato que se transforma en glucosa en el hígado."
                ],
                "correcta": 1,
                "explicacion": "El ejercicio físico y la contracción del músculo esquelético activan la señalización intracelular (vía AMPK) que moviliza los transportadores GLUT4 hacia la membrana celular sin requerir estimulación por insulina. Esto acelera artificialmente la depuración de la glucosa circulante, arrojando un valor erróneamente bajo a las 2 horas y enmascarando una posible intolerancia a la glucosa o diabetes."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 2: DIABETES TIPO 1 (DBT1), AUTOMONITOREO Y TECNOLOGÍA
    # ==========================================================================
    {
        "numero": 2,
        "id": "u2_dbt1_tecnologia",
        "icono": "📟",
        "titulo": "Unidad 2: Diabetes Tipo 1 (DBT1), Automonitoreo y Tecnología (CGM)",
        "modulo": "Clínica y Tecnología",
        "duracion": "6 hs cátedra",
        "resumen": "Destrucción autoinmune de células Beta, período de «luna de miel», insulinoterapia intensificada Basal-Bolo, sensores continuos de glucosa (CGM) y Tiempo en Rango (TIR).",
        "fisiopatologia_cards": [
            {
                "titulo": "Autoinmunidad y Déficit Absoluto de Insulina",
                "contenido": "En la DBT1 (y en la LADA del adulto) autoanticuerpos (anti-GAD65, anti-IA2, anti-insulina, anti-ZnT8) destruyen más del 80-90% de las células Beta. Sin insulina exógena diaria, la lipólisis descontrolada produce cuerpos cetónicos llevando a la Cetoacidosis en pocas horas."
            },
            {
                "titulo": "El Fenómeno de «Luna de Miel» (Remisión Parcial Transitoria)",
                "contenido": "Semanas después de iniciar insulina en el debut de DBT1, al corregirse la glucotoxicidad, las pocas células Beta sobrevivientes recuperan función temporalmente y las necesidades de insulina bajan drásticamente. ¡Rol crítico de enfermería!: educar a la familia para que NO crean que «se curó» ni suspendan jamás la insulina por su cuenta."
            },
            {
                "titulo": "Monitoreo Continuo de Glucosa (CGM) vs Glucemia Capilar (HGT)",
                "contenido": "Los sensores intersticiales (ej. FreeStyle Libre / Dexcom) miden glucosa en el líquido intersticial subcutáneo, NO en sangre capilar. Existe un retraso fisiológico («Lag Time») de 5 a 15 minutos («el tren»: la sangre es la locomotora y el intersticio es el último vagón)."
            }
        ],
        "guias_consenso": {
            "fuente": "Consenso Internacional ATTD / ADA 2025 sobre Monitoreo Continuo y Tiempo en Rango (TIR)",
            "metas_tabla": [
                {"criterio": "Tiempo en Rango (TIR: 70 a 180 mg/dL)", "normal": "Meta estándar: > 70% del día (> 16 hs 48 min)", "prediabetes": "Adultos frágiles: > 50%", "diabetes": "Embarazo DBT1: > 70% (en rango 63-140 mg/dL)"},
                {"criterio": "Tiempo Bajo Rango (< 70 mg/dL)", "normal": "< 4% del día (< 1 hora/día)", "prediabetes": "Adultos frágiles: < 1%", "diabetes": "Nivel 2 (< 54 mg/dL): < 1% (< 15 min/día)"},
                {"criterio": "Tiempo Sobre Rango (> 180 mg/dL)", "normal": "< 25% del día", "prediabetes": "-", "diabetes": "Nivel 2 (> 250 mg/dL): < 5%"}
            ],
            "regla_enfermeria": "REGLA SALVAVIDAS DE LA UNIDAD: Ante un paciente usuario de sensor continuo de glucosa (CGM) que presenta síntomas clínicos de hipoglucemia (sudoración fría, temblor, mareos) o durante los primeros 15 minutos posteriores a ingerir hidratos de carbono simples para corregir un evento, nunca te confíes únicamente en la lectura del sensor. Como el filamento mide glucosa en el líquido intersticial y no en sangre capilar, existe un desfasaje fisiológico de 10 a 15 minutos (lag time); por lo tanto, el sensor puede seguir mostrando valores bajos aunque la glucemia capilar ya se haya recuperado, o registrar valores normales mientras la sangre ya cayó a niveles críticos. La regla de oro de enfermería indica comprobar siempre con una punción capilar en el dedo (HGT) lavado con agua y jabón antes de tomar conductas, evitando así sobrecorrecciones innecesarias con rebote hiperglucémico o demoras en la atención de una hipoglucemia real."
        },
        "caso_practico": {
            "escenario": "Durante el turno noche en la sala de internación, un paciente de 22 años con DBT1 que utiliza sensor continuo (CGM) refiere palpitaciones, sudoración fría y ansiedad. Al escanear el sensor del brazo, la pantalla indica 105 mg/dL con flecha horizontal de tendencia.",
            "pregunta": "¿Qué acción debe realizar el profesional de enfermería de inmediato?",
            "resolucion": "Realizar una glucemia capilar (HGT) mediante punción digital en el borde lateral del pulpejo (lavado con agua y jabón) para verificar el valor en sangre en tiempo real, dado el retraso fisiológico (lag time) de 10 a 15 minutos del líquido intersticial respecto a la sangre capilar."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: Ingresa al shockroom de la guardia un paciente de 18 años con Diabetes Tipo 1 conocido, quien cursa un cuadro de gastroenteritis aguda con vómitos e imposibilidad de tolerar la vía oral desde hace 8 horas. La madre consulta si debe omitir la dosis nocturna de insulina basal (Glargina/NPH) ya que el joven no ha comido nada. ¿Cuál es la conducta de enfermería adecuada y fundamentada?",
                "opciones": [
                    "A) Indicar la suspensión completa de la insulina basal hasta que el paciente tolere alimentos sólidos para prevenir una hipoglucemia severa.",
                    "B) Explicar que la insulina basal no se debe suspender bajo ninguna circunstancia, manteniendo el monitoreo glucémico y evaluando la hidratación y la presencia de cetonas.",
                    "C) Reemplazar la insulina basal por bolos de insulina rápida cada 2 horas únicamente si la glucemia supera los 300 mg/dL."
                ],
                "correcta": 1,
                "explicacion": "La Diabetes Tipo 1 implica una destrucción autoinmune de las células beta y la ausencia absoluta de producción endógena de insulina. La insulina basal cubre las necesidades metabólicas independientes de las ingestas; si se suspende por completo, se desencadena una lipólisis descontrolada y la formación acelerada de cuerpos cetónicos, llevando al paciente a una Cetoacidosis Diabética (CAD) en cuestión de horas, aun estando en ayunas."
            },
            {
                "pregunta": "2. Situación clínica: Durante el turno noche en la sala de internación, un paciente de 22 años con DBT1 que utiliza sensor continuo (CGM) refiere palpitaciones, sudoración fría y ansiedad. Al escanear el sensor del brazo, la pantalla indica 105 mg/dL con flecha horizontal de tendencia. ¿Qué acción debe realizar el profesional de enfermería de inmediato?",
                "opciones": [
                    "A) Tranquilizar al paciente informándole que su lectura de glucosa está normal y pedirle que vuelva a dormir.",
                    "B) Realizar una glucemia capilar (HGT) mediante punción digital para verificar el valor en sangre en tiempo real.",
                    "C) Administrar de inmediato 30 gramos de glucosa pura sin realizar mediciones adicionales para tratar el síntoma."
                ],
                "correcta": 1,
                "explicacion": "El sensor de glucosa mide la concentración en el líquido intersticial subcutáneo, el cual presenta un retraso fisiológico (lag time) de 10 a 15 minutos respecto a la concentración capilar sanguínea. Ante cambios glucémicos abruptos o discordancia entre la sintomatología adrenérgica del paciente y el valor mostrado por el dispositivo, es obligatorio confirmar el resultado mediante HGT capilar para descartar una hipoglucemia no detectada aún por el sensor."
            },
            {
                "pregunta": "3. Situación clínica: En el consultorio ambulatorio de diabetología, evaluás el reporte de los últimos 14 días del perfil ambulatorio de glucosa (AGP) de un paciente. Registra un Tiempo en Rango (TIR 70-180 mg/dL) del 74%, un Tiempo Bajo Rango (TBR < 70 mg/dL) del 2.5% y un Tiempo Sobre Rango (TAR > 180 mg/dL) del 23.5%. ¿Cómo valorás este informe según las metas internacionales vigentes?",
                "opciones": [
                    "A) El control es inadecuado porque el paciente debe lograr un Tiempo en Rango del 100% del día sin ninguna fluctuación.",
                    "B) El perfil cumple satisfactoriamente con los objetivos recomendados, ya que supera el 70% de Tiempo en Rango y mantiene las hipoglucemias por debajo del 4%.",
                    "C) Es prioritario aumentar la dosis total de insulina para reducir el Tiempo Sobre Rango a menos del 10%, sin importar que aumente el tiempo en hipoglucemia."
                ],
                "correcta": 1,
                "explicacion": "Según el Consenso Internacional (ATTD/ADA), la meta estándar para la mayoría de las personas con diabetes es alcanzar un Tiempo en Rango (70–180 mg/dL) superior al 70% del tiempo diario, asociado a un Tiempo Bajo Rango (< 70 mg/dL) menor al 4%. Lograr estos parámetros se asocia de forma directa con una drástica reducción del riesgo de complicaciones microvasculares a largo plazo sin incrementar el riesgo de hipoglucemia severa."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 3: DIABETES TIPO 2 (DBT2) Y SÍNDROME CARDIO-RENO-METABÓLICO
    # ==========================================================================
    {
        "numero": 3,
        "id": "u3_dbt2_cardiometabolico",
        "icono": "❤️",
        "titulo": "Unidad 3: Diabetes Tipo 2 (DBT2) y Enfoque Cardio-Reno-Metabólico",
        "modulo": "Clínica Integral",
        "duracion": "6 hs cátedra",
        "resumen": "Adiposidad visceral, insulinorresistencia, signos clínicos (acantosis nigricans), metas ABCDE e individualización de HbA1c según fragilidad.",
        "fisiopatologia_cards": [
            {
                "titulo": "Insulinorresistencia y Lipotoxicidad Visceral",
                "contenido": "El tejido adiposo visceral inflamado libera ácidos grasos libres y citoquinas (TNF-α, IL-6) que bloquean la señal intracelular del receptor de insulina en hígado y músculo. Al principio el páncreas compensa con HIPERINSULINISMO (que causa acantosis nigricans y acrocordones en cuello/axilas), hasta que la célula Beta se agota."
            },
            {
                "titulo": "Del Control Glucocéntrico a la Protección de Órgano Blanco",
                "contenido": "La principal causa de mortalidad en la DBT2 es la enfermedad cardiovascular aterosclerótica y la insuficiencia cardíaca/renal. Hoy enfermería evalúa el riesgo integral: glucemia + presión arterial + colesterol LDL + albuminuria + tabaquismo."
            }
        ],
        "guias_consenso": {
            "fuente": "ADA Standards of Care 2025/2026 (Cap. 6, 10 y 11) & Guías SAD",
            "metas_tabla": [
                {"criterio": "HbA1c en Adulto General sin hipoglucemias", "normal": "< 7.0%", "prediabetes": "Joven sin comorbilidad: < 6.5%", "diabetes": "Adulto mayor frágil / demencia / ERC terminal: < 8.0%"},
                {"criterio": "Glucemia Capilar Preprandial (Ayunas / Antes de comer)", "normal": "80 a 130 mg/dL", "prediabetes": "-", "diabetes": "Adulto mayor frágil: 90 a 150 mg/dL"},
                {"criterio": "Glucemia Capilar Postprandial (1 a 2 hs después de empezar a comer)", "normal": "< 180 mg/dL", "prediabetes": "-", "diabetes": "Adulto mayor frágil: < 200 mg/dL"},
                {"criterio": "Presión Arterial en Paciente con Diabetes", "normal": "< 130/80 mmHg", "prediabetes": "-", "diabetes": "Usar IECA o ARA-II si hay albuminuria (RAC ≥ 30 mg/g)"}
            ],
            "regla_enfermeria": "REGLA SALVAVIDAS DE LA UNIDAD: En la atención de enfermería de adultos mayores frágiles, buscar un control glucémico intensivo rígido (HbA1c < 6.5%) mediante sulfonilureas de vida media prolongada como la glibenclamida o esquemas intensivos de insulina constituye una práctica de alto riesgo que multiplica las hipoglucemias nocturnas desapercibidas, desencadenando arritmias, accidentes cerebrovasculares y caídas graves con fractura de cadera. Por esta razón, las guías internacionales y nacionales exigen flexibilizar la meta de HbA1c a niveles menores al 8.0% en esta población vulnerable, priorizando la seguridad y la calidad de vida sobre el rigor glucocéntrico. Asimismo, para un automonitoreo glucémico preciso en el adulto general, recordá educar al paciente sobre la técnica correcta de medición postprandial: la punción capilar (HGT) debe realizarse exactamente entre 1 y 2 horas contadas desde el primer bocado de la comida y no al finalizar la ingesta, asegurando que el resultado se mantenga por debajo del valor objetivo de 180 mg/dL."
        },
        "caso_practico": {
            "escenario": "En la consulta ambulatoria de enfermería valorás a un paciente de 45 años con obesidad central (perímetro de cintura de 106 cm) que presenta placas hiperpigmentadas, oscuras y aterciopeladas en la nuca y las axilas, refiriendo que intenta limpiarse enérgicamente porque cree que es suciedad acumulada.",
            "pregunta": "¿Cuál es la interpretación clínica y la conducta de enfermería adecuada?",
            "resolucion": "Explicar que el signo es Acantosis Nigricans, producido por el estímulo del hiperinsulinismo compensador sobre los receptores dérmicos de crecimiento (IGF-1), y solicitar laboratorio de glucemia en ayunas, HbA1c y perfil lipídico."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En la consulta ambulatoria de enfermería valorás a un paciente de 45 años con obesidad central (perímetro de cintura de 106 cm) que presenta placas hiperpigmentadas, oscuras y aterciopeladas en la nuca y las axilas, refiriendo que intenta limpiarse enérgicamente porque cree que es suciedad acumulada. ¿Cuál es la interpretación clínica y la conducta de enfermería adecuada?",
                "opciones": [
                    "A) Indicar exfoliación tópica con jabón neutro y esponja vegetal para remover la hiperpigmentación cutánea.",
                    "B) Explicar que el signo es Acantosis Nigricans, producido por el estímulo del hiperinsulinismo compensador sobre los receptores dérmicos de crecimiento, y solicitar laboratorio de glucemia en ayunas y perfil lipídico.",
                    "C) Derivar de urgencia a dermatología por sospecha de una infección fúngica contagiosa en pliegues."
                ],
                "correcta": 1,
                "explicacion": "La Acantosis Nigricans es la manifestación dermatológica cardinal de la resistencia severa a la insulina. El exceso de insulina circulante (hiperinsulinismo compensador) se une a los receptores del factor de crecimiento similar a la insulina tipo 1 (IGF-1) en queratinocitos y fibroblastos dérmicos, estimulando la proliferación epidérmica y la hiperqueratosis en las zonas de pliegues."
            },
            {
                "pregunta": "2. Situación clínica: Un paciente de 82 años con hipertensión, demencia senil leve y marcha inestable concurre al control de enfermería con una HbA1c reciente de 7.7% y glucemias capilares en ayunas de 115–135 mg/dL mientras toma metformina. Su familiar pregunta si se le debería agregar glibenclamida para lograr una HbA1c menor a 6.5%. ¿Qué respuesta técnica de enfermería es la correcta?",
                "opciones": [
                    "A) Explicar que el valor actual de HbA1c (< 8.0%) es adecuado y seguro para un adulto mayor frágil, desaconsejando agregar glibenclamida debido al altísimo riesgo de hipoglucemias severas, caídas y fracturas.",
                    "B) Aceptar la sugerencia e indicar la adición de glibenclamida a dosis máximas antes del desayuno para normalizar la HbA1c a menos de 6.5%.",
                    "C) Suspender la metformina e iniciar un esquema intensificado con insulina corriente antes de cada comida principal."
                ],
                "correcta": 0,
                "explicacion": "En adultos mayores con fragilidad, deterioro cognitivo o insuficiencia renal, el daño agudo de una hipoglucemia (arritmia, ACV, caídas con fracturas de cadera) supera ampliamente cualquier beneficio de un control glucémico estricto. La glibenclamida posee una vida media prolongada y depuración renal reducida en el anciano, por lo que las guías internacionales (ADA/SAD) contraindican su uso y recomiendan flexibilizar la meta de HbA1c a menos de 8.0%."
            },
            {
                "pregunta": "3. Situación clínica: Educás a una persona con Diabetes Tipo 2 sobre el automonitoreo glucémico en el hogar. El paciente refiere que habitualmente se realiza el control capilar (HGT) 2 horas después de terminar de tomar el café al finalizar su almuerzo, demorando en total casi 3 horas desde que empezó a comer. ¿Cómo debés corregir su técnica?",
                "opciones": [
                    "A) Indicarle que el monitoreo postprandial debe realizarse exactamente entre 1 y 2 horas contadas a partir del primer bocado de la comida, buscando un valor objetivo menor a 180 mg/dL.",
                    "B) Explicarle que debe punzarse el dedo inmediatamente después de tragar el último bocado de alimento para registrar la glucemia máxima.",
                    "C) Sugerirle que espere 4 horas posteriores a la comida para garantizar el vaciamiento gástrico completo antes de la punción capilar."
                ],
                "correcta": 0,
                "explicacion": "Por consenso clínico internacional, la glucemia postprandial evalúa el pico plasmático de absorción de glucosa e inóculo insulínico. Contar el tiempo desde el primer bocado estandariza la medición (meta < 180 mg/dL en adultos generales); postergar el inicio del conteo al finalizar la comida subestima el pico glucémico real y distorsiona la evaluación del control metabólico."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 4: DIABETES Y EMBARAZO (DIABETES GESTACIONAL Y PREGESTACIONAL)
    # ==========================================================================
    {
        "numero": 4,
        "id": "u4_embarazo",
        "icono": "🤰",
        "titulo": "Unidad 4: Diabetes y Embarazo (Diabetes Gestacional y Pregestacional)",
        "modulo": "Salud Materno-Fetal",
        "duracion": "6 hs cátedra",
        "resumen": "Hormonas placentarias diabetogénicas, pesquisa universal semanas 24–28 (criterios ALAD/SAD/MSAL vs IADPSG), metas glucémicas estrictas, insulinoterapia segura y cuidados del recién nacido.",
        "fisiopatologia_cards": [
            {
                "titulo": "Fisiopatología Placentaria (2° y 3° Trimestre)",
                "contenido": "A partir de la semana 20-24, la placenta secreta lactógeno placentario humano, progesterona, cortisol y prolactina que generan fuerte resistencia a la insulina materna para asegurar glucosa al feto. Si el páncreas materno no logra triplicar su secreción de insulina, aparece la Diabetes Mellitus Gestacional (DMG)."
            },
            {
                "titulo": "Hipótesis de Pedersen: ¿Por qué el bebé nace Macrosómico e Hipoglucémico?",
                "contenido": "La GLUCOSA materna atraviesa libremente la placenta, pero la INSULINA materna NO la atraviesa. Ante la hiperglucemia materna, el páncreas del feto secreta exceso de insulina fetal (hiperinsulinismo fetal). Como la insulina es anabólica, el feto crece en exceso (Macrosomía > 4 kg, distocia de hombros) y, al cortarse el cordón umbilical en el parto, ese exceso de insulina fetal le provoca HIPOGLUCEMIA NEONATAL severa."
            }
        ],
        "guias_consenso": {
            "fuente": "Consenso SAD / ALAD / Ministerio de Salud de la Nación Argentina & ADA Cap. 15",
            "metas_tabla": [
                {"criterio": "Pesquisa Universal DMG (Semanas 24 a 28 con PTOG 75g)", "normal": "Ayunas < 100 mg/dL (IADPSG < 92)", "prediabetes": "-", "diabetes": "SAD/MSAL: Dos ayunas ≥ 100 mg/dL o PTOG 2h ≥ 140 mg/dL"},
                {"criterio": "Meta Glucémica en Ayunas durante el Embarazo", "normal": "< 95 mg/dL (Óptimo SAD: 70 a 90 mg/dL)", "prediabetes": "-", "diabetes": "Sin hipoglucemias (< 60 mg/dL)"},
                {"criterio": "Meta Postprandial a 1 Hora (desde el primer bocado)", "normal": "< 140 mg/dL (SAD estricto: < 120–130 mg/dL)", "prediabetes": "-", "diabetes": "-"},
                {"criterio": "Meta Postprandial a 2 Horas", "normal": "< 120 mg/dL", "prediabetes": "-", "diabetes": "Reclasificación postparto: PTOG 75g a las 6 semanas del parto"}
            ],
            "regla_enfermeria": "REGLA SALVAVIDAS DE LA UNIDAD: En el puerperio inmediato, la expulsión de la placenta (alumbramiento) provoca el colapso repentino de los niveles de hormonas contrarreguladoras de origen placentario (lactógeno placentario, progesterona y cortisol), lo que restaura la sensibilidad materna a la insulina en cuestión de minutos. La regla de oro de enfermería obstétrica establece que se debe suspender inmediatamente la administración de insulina en pacientes que cursaron Diabetes Gestacional (y reducir la dosis a un 50% respecto al tercer trimestre en aquellas con Diabetes pregestacional), ya que mantener el esquema del embarazo desencadenará hipoglucemias maternas severas e invalidantes. Asimismo, el equipo de enfermería neonatal debe iniciar la vigilancia capilar en el talón del recién nacido dentro de la primera hora de vida, manteniendo un control estricto para detectar y corregir de forma precoz la hipoglucemia neonatal (definida por valores < 40-45 mg/dL) derivada del hiperinsulinismo fetal persistente."
        },
        "caso_practico": {
            "escenario": "En la sala de maternidad atendés a una puérpera que acaba de tener su parto hace 2 horas y cursó Diabetes Gestacional tratada con 28 UI diarias de insulina NPH durante el tercer trimestre.",
            "pregunta": "¿Cuál es la conducta de enfermería adecuada respecto al esquema de insulina?",
            "resolucion": "Suspender la administración de insulina NPH en la Diabetes Gestacional tras el alumbramiento placentario, notificar al médico, iniciar control de glucemia capilar (HGT) y favorecer la lactancia materna precoz."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En el control prenatal de la semana 26 de gestación, una embarazada asintomática sin antecedentes previos presenta una glucemia en ayunas de 88 mg/dL. Al realizar la PTOG con 75 g de glucosa, el valor obtenido a las 2 horas es de 146 mg/dL. ¿Cómo se interpreta este resultado según los criterios vigentes en Argentina (SAD/MSAL)?",
                "opciones": [
                    "A) Es una prueba normal, ya que la glucemia a las 2 horas es menor a 200 mg/dL y la basal estuvo en rango.",
                    "B) Confirma el diagnóstico de Diabetes Mellitus Gestacional, dado que el valor a las 2 horas de la PTOG es igual o mayor a 140 mg/dL.",
                    "C) Es un valor indicativo de prediabetes gestacional que únicamente requiere repetir la curva en la semana 36."
                ],
                "correcta": 1,
                "explicacion": "De acuerdo con los criterios del Ministerio de Salud de la Nación y la Sociedad Argentina de Diabetes (SAD/MSAL), en la gestación un valor de glucemia plasmática a las 2 horas de la PTOG de 75 g igual o mayor a 140 mg/dL (o dos glucemias basales en ayunas >= 100 mg/dL) confirma el diagnóstico de Diabetes Gestacional, reflejando una capacidad insulínica insuficiente para compensar la resistencia insulínica placentaria."
            },
            {
                "pregunta": "2. Situación clínica: En la sala de maternidad atendés a una puérpera que acaba de tener su parto hace 2 horas y cursó Diabetes Gestacional tratada con 28 UI diarias de insulina NPH durante el tercer trimestre. ¿Cuál es la conducta de enfermería adecuada respecto al esquema de insulina?",
                "opciones": [
                    "A) Aplicar la dosis habitual de 28 UI de insulina NPH para evitar un rebote de hiperglucemia tras el esfuerzo del trabajo de parto.",
                    "B) Suspender la administración de insulina NPH en la Diabetes Gestacional, notificar al médico, iniciar control de glucemia capilar (HGT) y favorecer la lactancia materna precoz.",
                    "C) Reemplazar la insulina NPH por insulina corriente en dosis fijas antes de cada comida principal."
                ],
                "correcta": 1,
                "explicacion": "Con el alumbramiento y la remoción de la placenta cesa inmediatamente la producción de lactógeno placentario, progesterona y cortisol, inductores de la resistencia insulínica durante la gestación. La sensibilidad a la insulina de los tejidos maternos retorna súbitamente a su estado previo al embarazo; si se aplican las dosis de insulina que la paciente recibía en el tercer trimestre, sufrirá una hipoglucemia materna severa."
            },
            {
                "pregunta": "3. Situación clínica: Recibís en la servocuna de neonatología a un recién nacido de 4,200 kg (macrosómico) hijo de una madre con Diabetes Gestacional que tuvo controles glucémicos irregulares. A los 45 minutos de vida, el lactante presenta hipotonía y temblores. ¿Cuál es el mecanismo fisiopatológico (Hipótesis de Pedersen) que explica este cuadro?",
                "opciones": [
                    "A) La insulina materna cruzó en exceso la placenta durante el trabajo de parto, provocando la caída de la glucosa neonatal.",
                    "B) La hiperglucemia materna continua cruzó la placenta e indujo hiperinsulinismo fetal; al clampear el cordón cesó el aporte de glucosa materna pero persistió la secreción elevada de insulina fetal.",
                    "C) El estrés del parto inhibió la síntesis de glucagón en el páncreas del recién nacido, impidiendo la glucogenólisis."
                ],
                "correcta": 1,
                "explicacion": "La glucosa materna atraviesa la barrera placentaria por difusión facilitada, pero la insulina materna no. La hiperglucemia materna continua expone al feto a sobrecarga de sustrato, estimulando la hiperplasia de sus células beta y un hiperinsulinismo fetal (que estimula la macrosomía). Al clampear el cordón umbilical, el aporte exógeno de glucosa finaliza de golpe, pero los elevados niveles de insulina endógena del neonato captan rápidamente la glucosa circulante, desencadenando hipoglucemia neonatal severa."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 5: NUTRICIÓN TERAPÉUTICA Y ACTIVIDAD FÍSICA EN DIABETES
    # ==========================================================================
    {
        "numero": 5,
        "id": "u5_nutricion_ejercicio",
        "icono": "🥗",
        "titulo": "Unidad 5: Nutrición Terapéutica y Prescripción Segura de Actividad Física",
        "modulo": "Estilo de Vida Terapéutico",
        "duracion": "6 hs cátedra",
        "resumen": "Método del Plato de la ADA, índice glucémico y fibra, conteo práctico de carbohidratos, fisiología del ejercicio y reglas de seguridad glucémica pre-entrenamiento.",
        "fisiopatologia_cards": [
            {
                "titulo": "El Método Visual del Plato Saludable (ADA)",
                "contenido": "La herramienta educativa más eficaz para enfermería sin requerir balanza: dividir un plato de 23 cm en: • 50% (Mitad del plato): Vegetales sin almidón (hojas verdes, tomate, brócoli, calabaza, berenjena) ricos en fibra que enlentecen la absorción de glucosa. • 25% (Un cuarto): Proteínas magras (pollo, pescado, huevo, carnes magras). • 25% (Un cuarto): Carbohidratos complejos/granos integrales o legumbres (lentejas, arroz integral, papa/batata enfriada con almidón resistente)."
            },
            {
                "titulo": "Fisiología del Ejercicio: Transportadores GLUT-4 Independientes de Insulina",
                "contenido": "La contracción muscular activa la vía de la enzima AMPK, que lleva transportadores GLUT-4 a la membrana de la fibra muscular SIN NECESIDAD DE INSULINA. Además, una sola sesión de ejercicio aeróbico + fuerza aumenta la sensibilidad a la insulina durante las siguientes 24 a 48 horas (¡atención al riesgo de hipoglucemia nocturna tardía post-ejercicio!)."
            }
        ],
        "guias_consenso": {
            "fuente": "ADA Standards of Care 2025/2026 (Cap. 5 Facilitating Positive Health Behaviors) & Consenso SAD",
            "metas_tabla": [
                {"criterio": "Volumen Semanal de Ejercicio Aeróbico", "normal": "≥ 150 minutos/semana (intensidad moderada)", "prediabetes": "Distribuido en al menos 3 días", "diabetes": "No pasar más de 2 días consecutivos sin ejercicio (para no perder el efecto GLUT-4)"},
                {"criterio": "Entrenamiento de Fuerza Muscular", "normal": "2 a 3 sesiones por semana en días no consecutivos", "prediabetes": "-", "diabetes": "El músculo es el principal consumidor del 80% de la glucosa postprandial"},
                {"criterio": "Seguridad Pre-Ejercicio: HGT < 100 mg/dL (en insulinizados)", "normal": "Riesgo de hipoglucemia intra-ejercicio", "prediabetes": "-", "diabetes": "Ingerir colación de 15–20 g de carbohidratos antes de empezar"},
                {"criterio": "Contraindicación de Ejercicio: HGT > 250 mg/dL con Cetonas (+)", "normal": "-", "prediabetes": "-", "diabetes": "¡PROHIBIDO EJERCITAR! Las hormonas de estrés del ejercicio (adrenalina/cortisol) sin insulina empeoran la Cetoacidosis"}
            ],
            "regla_enfermeria": "REGLA SALVAVIDAS DE LA UNIDAD: Constituye un error clínico grave y potencialmente mortal permitir que un paciente con Diabetes Tipo 1 o déficit insulínico severo realice ejercicio físico cuando presenta una glucemia pre-ejercicio > 250 mg/dL con cetonas positivas (o > 300 mg/dL) bajo el falso mito de que «transpirar le va a bajar el azúcar». Sin suficiente insulina circulante, la glucosa es incapaz de ingresar al músculo; el estrés del esfuerzo físico desencadena la liberación masiva de hormonas contrarreguladoras (adrenalina, noradrenalina, glucagón y cortisol) que estimulan la producción hepática de glucosa y la lipólisis descontrolada, acelerando la cetogénesis y precipitando rápidamente una Cetoacidosis Diabética (CAD). Asimismo, recordá educar al paciente para que nunca inyecte la insulina rápida en los muslos antes de correr o hacer sentadillas, ya que el mayor flujo sanguíneo en la masa muscular ejercitada acelera bruscamente su absorción, desencadenando una hipoglucemia aguda en plena actividad."
        },
        "caso_practico": {
            "escenario": "Un paciente de 22 años con Diabetes Tipo 1 concurre a una clase de spinning a las 17:00 hs. Al realizarse el control de automonitoreo glucémico capilar (HGT) previo, obtiene 310 mg/dL y la tira reactiva registra cetonemia de 1,8 mmol/L (cetonas positivas). Expresa: «Voy a pedalear fuerte una hora para quemar el azúcar que me quedó alta por haberme olvidado la insulina del almuerzo».",
            "pregunta": "¿Cuál es la conducta de enfermería adecuada y su fundamento fisiopatológico?",
            "resolucion": "Prohibir de inmediato la realización de la clase de actividad física, indicar la corrección con insulina rápida según esquema médico, rehidratar y reevaluar los parámetros, ya que el ejercicio sin insulina libera catecolaminas y glucagón que precipitan una Cetoacidosis Diabética."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En el consultorio de educación diabetológica atendés a un paciente con Diabetes Tipo 2 que no logra controlar las glucemias postprandiales a las 2 horas de almorzar y refiere gran dificultad para realizar conteo de hidratos de carbono. ¿Qué recomendación nutricional de enfermería basada en el Método del Plato de la ADA es la adecuada?",
                "opciones": [
                    "A) Indicar la eliminación total de los carbohidratos en el almuerzo y basar la ingesta exclusivamente en proteínas de origen animal.",
                    "B) Estructurar el plato de 23 cm con 50% de vegetales sin almidón, 25% de proteínas magras y 25% de carbohidratos complejos, aconsejando ingerir primero la fibra y la proteína antes de la porción de carbohidratos.",
                    "C) Permitir un plato con 75% de carbohidratos simples siempre que realice una caminata de 10 minutos inmediatamente después de almorzar."
                ],
                "correcta": 1,
                "explicacion": "El Método del Plato simplifica la educación sin requerir pesaje de alimentos. Los vegetales sin almidón aportan fibra soluble e insoluble que enlentece el vaciamiento gástrico. Al ingerir primero la fibra y las proteínas, se ralentiza el tránsito intestinal y la absorción de los carbohidratos consumidos en último término, reduciendo significativamente (hasta un 30–40%) el pico de glucemia postprandial."
            },
            {
                "pregunta": "2. Situación clínica: Un paciente joven con Diabetes Tipo 1 adecuadamente controlado entrena intensamente en el gimnasio realizando musculación y carrera aeróbica entre las 18:00 y las 19:30 hs. Durante la madrugada (03:30 hs), despierta con sudoración profusa, temblores y un HGT de 48 mg/dL. ¿Qué mecanismo fisiopatológico explica este evento nocturno?",
                "opciones": [
                    "A) El ejercicio inhibió totalmente la síntesis de glucagón hepático durante las siguientes 24 horas.",
                    "B) La contracción muscular activó la vía AMPK traslocando GLUT-4, manteniendo la sensibilidad a la insulina elevada durante 24 a 48 horas para la resíntesis de glucógeno muscular.",
                    "C) El paciente sufrió un pico tardío de absorción de los hidratos ingeridos antes de entrenar que bloqueó la neoglucogénesis renal."
                ],
                "correcta": 1,
                "explicacion": "La contracción muscular durante el ejercicio moviliza transportadores GLUT-4 a la membrana celular de forma independiente de la insulina. Finalizado el entrenamiento, el músculo agotado mantiene una sensibilidad a la insulina aumentada durante 24 a 48 horas con el fin de captar glucosa plasmática para reponer sus depósitos de glucógeno. En pacientes insulinizados, este efecto de captación continua sumado a la dosis basal habitual produce el pico de hipoglucemia nocturna tardía durante la madrugada."
            },
            {
                "pregunta": "3. Situación clínica: Un paciente de 22 años con Diabetes Tipo 1 concurre a una clase de spinning a las 17:00 hs. Al realizarse el control de automonitoreo glucémico capilar (HGT) previo, obtiene 310 mg/dL y la tira reactiva registra cetonemia de 1,8 mmol/L (cetonas positivas). Expresa: «Voy a pedalear fuerte una hora para quemar el azúcar que me quedó alta por haberme olvidado la insulina del almuerzo». ¿Cuál es la conducta de enfermería adecuada?",
                "opciones": [
                    "A) Prohibir de inmediato la realización de la clase de actividad física, indicar la corrección con insulina rápida según esquema médico, rehidratar y reevaluar los parámetros.",
                    "B) Autorizar el entrenamiento reduciendo la intensidad a la mitad y recomendando tomar 1 litro de bebida isotónica durante la clase.",
                    "C) Indicar que realice 20 minutos de ejercicios respiratorios antes de subir a la bicicleta estática para reducir la glucemia por relajación."
                ],
                "correcta": 0,
                "explicacion": "Un valor de glucemia > 250 mg/dL con cetonas positivas indica una falta severa de insulina en el organismo. Si el paciente realiza ejercicio físico en este estado, el estrés metabólico desencadena una descarga masiva de hormonas contrarreguladoras (adrenalina, glucagón, cortisol) que estimulan la neoglucogénesis hepática y la lipólisis en el tejido adiposo, empeorando drásticamente la hiperglucemia y acelerando la progresión hacia una Cetoacidosis Diabética (CAD) severa."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 6: FARMACOLOGÍA DE INSULINAS, CONSERVACIÓN Y TÉCNICA (FITTER)
    # ==========================================================================
    {
        "numero": 6,
        "id": "u6_insulinas_fitter",
        "icono": "💉",
        "titulo": "Unidad 6: Farmacología de Insulinas, Cadena de Frío y Técnica FITTER",
        "modulo": "Farmacología Clínica I",
        "duracion": "6 hs cátedra",
        "resumen": "Perfiles farmacocinéticos (Ultrarrápidas, Regular, NPH, Glargina U-100, Degludec y Glargina U-300), conservación, técnica con agujas de 4 mm y prevención de lipohipertrofia.",
        "fisiopatologia_cards": [
            {
                "titulo": "Clasificación Práctica de Insulinas: Prandiales (Bolos) vs Basales",
                "contenido": "• INSULINAS PRANDIALES (Para cubrir comidas y hacer correcciones): 1) Análogos Ultrarrápidos (Aspártica, Lispro, Glulisina): inicio 5-15 min, pico 1-2 h, duración 3-5 h. 2) Insulina Rápida Humana (Regular/Corriente): inicio 30-45 min, pico 2-4 h, duración 6-8 h (ÚNICA estándar para Bomba EV). • INSULINAS BASALES (Para cubrir las 24 hs en ayuno): 3) NPH Humana (Turbia/Lechosa): inicio 1-2 h, pico 4-10 h, duración 12-16 h. 4) Glargina U-100 / Detemir: inicio 1.5-3 h, sin pico pronunciado, duración 20-24 h. 5) Ultraprolongadas (Degludec / Glargina U-300 Toujeo): > 24-42 h, perfil ultra-plano."
            },
            {
                "titulo": "Cadena de Frío, Apertura de Lapiceras y Resuspensión de NPH",
                "contenido": "• Reserva CERRADA: en heladera (estante central, nunca en freezer ni puerta) entre 2 °C y 8 °C hasta su vencimiento. • Lapicera o frasco EN USO (Abierto): a temperatura ambiente (< 28-30 °C, lejos del sol) hasta por 28 DÍAS (rotular fecha de apertura). Inyectar insulina fría duele y retrasa absorción. • NPH (Lechosa): rolar 20 veces entre las palmas e invertir 10 veces sin agitar."
            }
        ],
        "guias_consenso": {
            "fuente": "Consenso Internacional FITTER (Forum for Injection Technique) & Guía SAD",
            "metas_tabla": [
                {"criterio": "Largo de Aguja Recomendado en Lapicera", "normal": "4 mm para TODOS los adultos y niños (sin importar IMC)", "prediabetes": "Inserción a 90° sin pliegue cutáneo", "diabetes": "Hacer pliegue solo en niños ≤ 6 años o adultos muy caquécticos"},
                {"criterio": "Tiempo de Espera con Botón Presionado en Piel", "normal": "Contar 10 segundos lentos antes de retirar la aguja", "prediabetes": "-", "diabetes": "Evita reflujo/fuga de insulina por el trayecto de punción"},
                {"criterio": "Velocidad de Absorción según Zona Anatómica", "normal": "1° Abdomen (Más rápida) > 2° Deltoides > 3° Muslos > 4° Glúteos (Más lenta)", "prediabetes": "-", "diabetes": "Rotar dejando 1 a 2 cm entre punciones; evitar lipohipertrofia"}
            ],
            "regla_enfermeria": "REGLA SALVAVIDAS DE LA UNIDAD: En el manejo hospitalario y ambulatorio de insulinas, el equipo de enfermería debe aplicar rigurosamente tres reglas críticas de seguridad para evitar descompensaciones severas y errores de dosificación. En primer lugar, al utilizar dispositivos tipo lapicera, es obligatorio mantener la aguja insertada a 90° en el tejido subcutáneo contando lentamente hasta 10 segundos con el botón presionado a fondo para evitar la fuga o reflujo del fármaco y garantizar la entrega del 100% de la dosis programada. En segundo lugar, es imprescindible inspeccionar y palpar activamente el tejido antes de cada inyección, prohibiendo la aplicación sobre zonas con lipohipertrofia («pelotitas» de tejido adiposo fibroso) ya que provocan una absorción errática, hiperglucemias inexplicables e hipoglucemias nocturnas tardías. Por último, en relación con la compatibilidad de mezclas en jeringa, la Insulina Glargina (formulada a pH ácido 4.0) NUNCA se debe mezclar en la misma jeringa con ninguna otra insulina porque pierde su perfil basal de liberación lenta; mientras que, al preparar una mezcla de Insulina Corriente con NPH, la regla de oro exige cargar siempre primero la insulina transparente (Corriente) y luego la turbia (NPH) para no contaminar el frasco de rápida con protamina."
        },
        "caso_practico": {
            "escenario": "En la guardia de un hospital, tenés que administrar insulina por vía subcutánea. En el primer caso, tenés indicación de preparar en la misma jeringa Insulina Corriente y NPH. En el segundo caso, un colega sugiere mezclar en la misma jeringa Insulina Glargina con Insulina Aspártica para «dar un solo pinchazo».",
            "pregunta": "¿Cuál es la conducta y fundamentación técnica correcta?",
            "resolucion": "Prohibir de forma absoluta la mezcla de Glargina en la jeringa (por su pH ácido 4.0 que precipitaría al juntarse con otra insulina), y para la mezcla Corriente + NPH cargar siempre primero la transparente (Corriente) y luego la turbia (NPH) para evitar contaminar el vial de rápida con protamina."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En la recabación de datos de enfermería, un paciente con Diabetes Tipo 1 tratado con Insulina NPH a las 22:00 hs refiere que despierta habitualmente a las 04:00 AM con sudoración fría, temblores y un HGT de 54 mg/dL. Además, al observar cómo manipula su medicación, notás que agita la lapicera de arriba a abajo enérgicamente y la guarda en el anaquel de la puerta de la heladera. ¿Cuál es la interpretación clínica y la intervención de enfermería adecuada?",
                "opciones": [
                    "A) Indicarle que aumente la dosis de NPH nocturna porque la glucemia a las 04:00 AM debe estar por debajo de 60 mg/dL y enseñarle a guardar la lapicera en el freezer.",
                    "B) Explicar que el pico de acción de la NPH ocurre entre las 4 y 10 horas de aplicada (coincidiendo con las 04:00 AM), corregir la resuspensión rolándola suavemente 20 veces entre las palmas sin agitarla y reubicar la reserva en el estante central de la heladera.",
                    "C) Recomendar suspender la NPH y reemplazarla por insulina rápida regular inyectada inmediatamente antes de ir a dormir."
                ],
                "correcta": 1,
                "explicacion": "La Insulina NPH es una insulina de acción intermedia con un pico máximo que se produce entre las 4 y 10 horas posteriores a su administración subcutánea; aplicada a las 22:00 hs, su mayor efecto hipoglucemiante coincide críticamente con la madrugada (04:00 AM), exigiendo reevaluar la dosis, la colación nocturna o la rotación a análogos basales planos. Respecto a la conservación y técnica, la NPH es una suspensión lechosa que requiere ser homogeneizada rolándola suavemente entre las manos (agitarla con violencia genera burbujas que alteran la dosificación e impulsan la desnaturalización proteica). Finalmente, la reserva cerrada debe almacenarse en el estante central de la heladera (2 a 8 °C), ya que los cambios térmicos de la puerta degradan la molécula."
            },
            {
                "pregunta": "2. Situación clínica: Durante la supervisión de la administración de insulinas en la sala de internación, un enfermero utiliza una aguja de 4 mm en un paciente adulto con sobrepeso. Introduce la aguja a 90°, presiona el émbolo e inmediatamente retira la aguja de la piel. Al retirarla, observás una gota de insulina refluyendo por el sitio de punción. ¿Cómo se corrige la técnica según el Consenso FITTER y cuál es su fundamento?",
                "opciones": [
                    "A) Indicar que se debe hacer un pliegue cutáneo profundo, ingresar a 45° y retirar la aguja de inmediato para evitar hematomas.",
                    "B) Indicar que con aguja de 4 mm la inserción es a 90° sin pliegue en adultos, pero es obligatorio mantener el botón presionado a fondo contando 10 segundos antes de retirar la aguja para asegurar la dosis completa y evitar el reflujo.",
                    "C) Explicar que la aguja de 4 mm es corta para un paciente con sobrepeso y se debe cambiar por una aguja de 12.7 mm reingresando rápidamente."
                ],
                "correcta": 1,
                "explicacion": "El Consenso Internacional FITTER establece que el espesor de la piel (epidermis + dermis) en adultos mide entre 1,8 y 2,5 mm independientemente del IMC, por lo que una aguja de 4 mm a 90° deposita siempre el fármaco en el tejido subcutáneo de forma segura y sin necesidad de pliegue. La retención de la aguja con el botón presionado a fondo durante 10 segundos completos permite la equiparación de presiones dentro del tejido subcutáneo y la entrega total del volumen a través del estrecho calibre de la aguja; retirarla prematuramente causa pérdida por reflujo (subdosificación) e inestabilidad en el control glucémico. Asimismo, las agujas deben ser de un solo uso para prevenir la deformación del bisel y la formación de lipohipertrofia."
            },
            {
                "pregunta": "3. Situación clínica: En la guardia de un hospital, tenés que administrar insulina por vía subcutánea. En el primer caso, tenés indicación de preparar en la misma jeringa Insulina Corriente y NPH. En el segundo caso, un colega sugiere mezclar en la misma jeringa Insulina Glargina con Insulina Aspártica para «dar un solo pinchazo». ¿Cuál es la conducta y fundamentación técnica correcta?",
                "opciones": [
                    "A) Permitir la mezcla de Glargina con Aspártica sin restricciones, y al mezclar Corriente con NPH cargar siempre en primer lugar la insulina turbia (NPH).",
                    "B) Prohibir de forma absoluta la mezcla de Glargina en la jeringa (por su pH ácido 4.0 que precipitaría al juntarse con otra insulina), y para la mezcla Corriente + NPH cargar siempre primero la transparente (Corriente) y luego la turbia (NPH).",
                    "C) Realizar la mezcla de Glargina únicamente si se administra por vía endovenosa directa."
                ],
                "correcta": 1,
                "explicacion": "La Insulina Glargina es un análogo basal cristalino formulado a un pH ácido (pH 4.0); al inyectarse sola en el tejido subcutáneo a pH neutro (7.4), precipita en microcristales que garantizan su liberación lenta y constante durante 24 horas. Si la Glargina se mezcla en la jeringa con insulinas de pH neutro (7.4), precipita de inmediato dentro del instrumento y pierde su perfil farmacocinético predecible. Por su parte, la combinación de Insulina Corriente y NPH en la misma jeringa es compatible, pero exige una secuencia estricta: se debe aspirar 1° la insulina transparente (Corriente) y 2° la insulina turbia (NPH) para evitar que microgotas de NPH con protamina ingresen al vial de insulina rápida y alteren su velocidad de acción."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 7: ANTIDIABÉTICOS ORALES Y NUEVOS INYECTABLES (iSGLT2, GLP-1, GIP)
    # ==========================================================================
    {
        "numero": 7,
        "id": "u7_antidiabeticos_nuevos",
        "icono": "💊",
        "titulo": "Unidad 7: Antidiabéticos Orales y Nuevos Tratamientos (iSGLT2 y GLP-1)",
        "modulo": "Farmacología Clínica II",
        "duracion": "6 hs cátedra",
        "resumen": "Metformina, Sulfonilureas, Gliptinas (iDPP-4), Gliflozinas (iSGLT2) y Agonistas GLP-1 / Duales (Semaglutida, Liraglutida, Tirzepatida): manejo en sala, ayuno, cirugía y contraste.",
        "fisiopatologia_cards": [
            {
                "titulo": "La Revolución Cardio-Renal: Inhibidores SGLT2 («Gliflozinas») y Agonistas GLP-1",
                "contenido": "• iSGLT2 (Empagliflozina, Dapagliflozina): bloquean la reabsorción de glucosa y sodio en el túbulo proximal renal (provocando glucosuria terapéutica de 60-80 g/día). Reducen hospitalizaciones por Insuficiencia Cardíaca y frenan la progresión de la Enfermedad Renal Crónica (incluso en no diabéticos). • Agonistas GLP-1 (Semaglutida, Liraglutida, Dulaglutida) y Duales GIP/GLP-1 (Tirzepatida): estimulan insulina solo cuando sube la glucosa, frenan el glucagón, enlentecen el vaciamiento gástrico y actúan en hipotálamo logrando descensos de peso del 10 al 20% y reducción de infarto/ACV."
            },
            {
                "titulo": "Fármacos Clásicos en Sala: Metformina, Sulfonilureas e iDPP-4",
                "contenido": "• Metformina: primera línea metabólica, sin riesgo de hipoglucemia; exige función renal (TFG ≥ 30 ml/min) y oxigenación tisular normal. • Sulfonilureas (Glibenclamida, Glimepirida, Gliclazida): secretagogos con ALTO RIESGO de hipoglucemia en ancianos y ayuno. • iDPP-4 (Sitagliptina, Vildagliptina, Linagliptina): seguros y neutros; Linagliptina se elimina por bilis (ideal en insuficiencia renal/diálisis)."
            }
        ],
        "guias_consenso": {
            "fuente": "Consenso ADA/EASD 2025 & Guías Perioperatorias SAD",
            "metas_tabla": [
                {"criterio": "Metformina en Internación / Contraste EV", "normal": "Dar con comidas", "prediabetes": "Ajustar si TFG 30-45 ml/min", "diabetes": "SUSPENDER en contraste iodado EV (48 hs), TFG < 30, sepsis o hipoxia (Acidosis Láctica)"},
                {"criterio": "Sulfonilureas (Glibenclamida / Glimepirida)", "normal": "30 min antes de comer", "prediabetes": "Evitar en > 65 años", "diabetes": "SUSPENDER DE INMEDIATO ante ayuno (NPO), vómitos o falla renal"},
                {"criterio": "Inhibidores SGLT2 (Empagliflozina / Dapagliflozina)", "normal": "Educar higiene genital e hidratación", "prediabetes": "-", "diabetes": "SUSPENDER 3 a 4 DÍAS ANTES de cirugía o en ayuno/sepsis (Cetoacidosis Euglucémica)"},
                {"criterio": "Agonistas GLP-1 (Semaglutida / Liraglutida)", "normal": "Vía SC semanal o diaria (¡No son insulina!)", "prediabetes": "-", "diabetes": "ALERTAR A ANESTESIOLOGÍA por estómago lleno / gastroparesia farmacológica"}
            ],
            "regla_enfermeria": "En el entorno asistencial hospitalario y quirúrgico, el equipo de enfermería debe aplicar un checklist de seguridad estricto frente a los antidiabéticos orales y biológicos para prevenir eventos adversos graves o mortales. La alerta clínica principal de esta unidad radica en la Cetoacidosis Diabética Euglucémica secundaria a gliflozinas (iSGLT2): ante un paciente bajo tratamiento con Empagliflozina o Dapagliflozina que ingresa por sepsis, trauma, ayuno o un postoperatorio agudo presentando náuseas, dolor abdominal, vómitos o respiración rápida de Kussmaul, nunca se debe descartar cetoacidosis basándose en un HGT engañosamente normal o levemente elevado (< 200–250 mg/dL), ya que la glucosuria obligada por el fármaco enmascara el nivel de glucemia plasmática mientras se acumulan cuerpos cetónicos y acidosis metabólica. Asimismo, como parte del protocolo prequirúrgico y procedimental, es imperativo suspender los iSGLT2 entre 3 y 4 días antes de la cirugía, suspender de inmediato las Sulfonilureas (Glibenclamida/Gliclazida) si el paciente entra en ayuno programado (NPO) para evitar comas hipoglucémicos, suspender la Metformina 48 horas ante estudios con contraste iodado endovenoso o inestabilidad hemodinámica para evitar acidosis láctica, y notificar a Anestesiología si el paciente utiliza un Agonista GLP-1 (Semaglutida/Liraglutida) debido a que la gastroparesia farmacológica puede mantener el estómago con residuos alimentarios a pesar de haber cumplido las horas teóricas de ayuno."
        },
        "caso_practico": {
            "escenario": "Paciente de 68 años internado por colecistitis aguda en ayunas (NPO) con plan quirúrgico. En su casa toma Empagliflozina 10 mg, Metformina 850 mg y Gliclazida 60 mg. El enfermero del turno mañana pregunta si le administra sus 3 pastillas habituales con un sorbo de agua.",
            "pregunta": "¿Qué debe hacerse con las 3 drogas y cuál es el fundamento de seguridad de cada una?",
            "resolucion": "Se SUSPENDEN las 3 drogas: 1) Gliclazida por riesgo de hipoglucemia grave en ayunas; 2) Metformina por cirugía aguda, ayuno y riesgo de acidosis láctica; 3) Empagliflozina por riesgo de Cetoacidosis Diabética Euglucémica perioperatoria. Se maneja con hidratación y esquema de insulina subcutánea."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En la sala de clínica médica recibís a un paciente de 65 años internado por un cuadro abdominal que pasa a ayuno estricto (NPO) por haber sido programado para una Tomografía Computada de abdomen con contraste iodado endovenoso en 48 horas. En su ficha farmacológica figuran Metformina 850 mg con el almuerzo y Glibenclamida 5 mg antes del desayuno. ¿Cuál es la conducta de enfermería correcta fundamentada en la seguridad del paciente?",
                "opciones": [
                    "Mantener la Glibenclamida para controlar la glucemia durante el ayuno y suspender la Metformina únicamente 10 minutos antes de ingresar al tomógrafo.",
                    "Suspender de inmediato la Glibenclamida por el riesgo inminente de hipoglucemia severa en ayunas y suspender la Metformina 48 horas antes del contraste iodado EV notificando al médico para manejar la glucemia con insulina rápida según escala.",
                    "Continuar con ambas medicaciones orales administrándolas con un sorbo de agua para evitar que el paciente desarrolle cetoacidosis."
                ],
                "correcta": 1,
                "explicacion": "Las sulfonilureas (como la Glibenclamida) son secretagogos que estimulan la liberación continua de insulina por las células beta del páncreas independientemente de la ingesta; si el paciente permanece en ayunas (NPO), la hiperinsulinemia exógena desencadenará una hipoglucemia severa. Por su parte, la Metformina combinada con el contraste iodado endovenoso puede inducir una nefropatía por contraste o falla renal aguda que bloquee su eliminación, provocando una acumulación tóxica del fármaco y acidosis láctica grave; por ello debe suspenderse 48 horas antes de la administración del contraste y mantenerse suspendida 48 horas posteriores evaluando la función renal."
            },
            {
                "pregunta": "2. Situación clínica: Un paciente de 58 años tratado con Empagliflozina 10 mg/día ingresa a la guardia al tercer día de un postoperatorio de cirugía menor presentando astenia marcada, náuseas, dolor abdominal difuso y taquipnea. Al tomar un HGT capilar en el office de enfermería, el glucómetro registra 175 mg/dL. Un integrante del equipo sugiere que no es nada urgente porque 'la glucemia está normal en 175'. ¿Cuál es la conducta y fundamentación de enfermería adecuada?",
                "opciones": [
                    "Aceptar la sugerencia y dar el alta al paciente recomendando que tome un té con azúcar para aliviar la astenia.",
                    "Sospechar inmediatamente una Cetoacidosis Diabética Euglucémica, solicitar determinación de cetonemia/cetonuria y gases en sangre, suspender la Empagliflozina e iniciar hidratación parenteral y evaluación médica urgente.",
                    "Indicar la administración de una dosis de sulfato de atropina oral por sospecha de espasmo intestinal postquirúrgico."
                ],
                "correcta": 1,
                "explicacion": "Los inhibidores SGLT2 (gliflozinas) bloquean la reabsorción renal de glucosa provocando una glucosuria terapéutica masiva. Ante un desencadenante como el estrés quirúrgico, la infección o el ayuno, el déficit relativo de insulina induce una lipólisis acelerada y formación de cuerpos cetónicos (acidosis metabólica); sin embargo, como el riñón continúa excretando glucosa por la orina impulsado por el fármaco, la glucemia plasmática no alcanza los niveles hiperglucémicos clásicos (> 250 mg/dL) y se mantiene deceptivamente baja (Cetoacidosis Euglucémica). Ignorar este cuadro basándose solo en el HGT normal retrasa el tratamiento de una urgencia vital."
            },
            {
                "pregunta": "3. Situación clínica: En el consultorio externo de diabetología y prequirúrgico valorás a dos pacientes. El primer paciente presenta una Insuficiencia Renal Crónica avanzada en estadio 4 (TFG = 22 mL/min) y requiere inicio de una gliptina (iDPP-4). El segundo paciente utiliza una lapicera semanal de Semaglutida (Ozempic®) y tiene programada una endoscopía digestiva alta con sedación para la semana siguiente. ¿Qué decisiones clínicas son las técnicamente correctas?",
                "opciones": [
                    "Indicar Sitagliptina a dosis máxima para el paciente renal y autorizar la Semaglutida el mismo día de la endoscopía sin aviso a Anestesiología.",
                    "Seleccionar Linagliptina para el paciente con falla renal severa (al no requerir ajuste de dosis por su eliminación biliar) y reportar de inmediato a Anestesiología el uso de Semaglutida por el riesgo de gastroparesia farmacológica y broncoaspiración.",
                    "Suspender la Linagliptina en el paciente renal por toxicidad hepática y reemplazar la Semaglutida por glibenclamida prequirúrgica."
                ],
                "correcta": 1,
                "explicacion": "A diferencia de otros iDPP-4 que dependen de la excreción renal y requieren reducir la dosis según el aclaramiento de creatinina, la Linagliptina posee una eliminación hepatobiliar y fecal predominantemente mayor al 85%, lo que la convierte en la gliptina más segura y sin necesidad de ajuste de dosis en cualquier estadio de insuficiencia renal crónica o hemodiálisis. Por otro lado, los agonistas GLP-1 como la Semaglutida enlentecen drásticamente la motilidad y el vaciamiento gástrico; en pacientes quirúrgicos o bajo sedación/anestesia, esto puede generar la presencia de residuos alimentarios gástricos abundantes pese a haber realizado el ayuno habitual, elevando significativamente el riesgo de regurgitación y broncoaspiración durante la inducción anestésica, lo que exige la notificación previa al anestesiólogo y la suspensión oportuna según protocolo."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 8: COMPLICACIONES AGUDAS (HIPOGLUCEMIA, CETOACIDOSIS Y EHH)
    # ==========================================================================
    {
        "numero": 8,
        "id": "u8_complicaciones_agudas",
        "icono": "🚨",
        "titulo": "Unidad 8: Complicaciones Agudas (Hipoglucemia, CAD y Estado Hiperosmolar)",
        "modulo": "Emergencias y Guardia",
        "duracion": "6 hs cátedra",
        "resumen": "Niveles de hipoglucemia, Regla del 15, rescate EV/Glucagón, manejo de Bomba de Insulina EV en Cetoacidosis, regla del Potasio y transición segura a subcutánea.",
        "fisiopatologia_cards": [
            {
                "titulo": "Los 3 Niveles de Hipoglucemia (Consenso ADA / SAD)",
                "contenido": "• NIVEL 1 (Valor de Alerta: < 70 mg/dL y ≥ 54 mg/dL): Descarga adrenérgica neurovegetativa (temblor, sudoración fría, palpitaciones, ansiedad, hambre). Activar de inmediato la Regla del 15. • NIVEL 2 (Hipoglucemia Clínicamente Significativa: < 54 mg/dL): Umbral de NEUROGLUCOPENIA (el sistema nervioso central sufre privación energética: confusión, visión borrosa, disartria, incoordinación). • NIVEL 3 (Hipoglucemia Severa): Cualquier evento caracterizado por alteración del estado mental o físico (estupor, convulsiones, coma) que exige la asistencia activa de un tercero. ¡Prohibida la vía oral!"
            },
            {
                "titulo": "Cetoacidosis Diabética (CAD) vs Estado Hiperosmolar Hiperglucémico (EHH)",
                "contenido": "• CAD: Déficit absoluto de insulina más exceso de hormonas contrarreguladoras → lipólisis descontrolada → liberación de ácidos grasos libres hacia el hígado con oxidación a cuerpos cetónicos (β-hidroxibutirato y acetoacetato) → Acidosis metabólica con Anión Gap elevado (pH < 7.30, bicarbonato < 18 mEq/L, respiración compensadora rápida y profunda de Kussmaul y aliento cetónico). • EHH: Típico en adultos mayores con DBT2 que conservan una mínima reserva de insulina endógena (suficiente para inhibir la lipólisis y evitar la cetosis severa, manteniendo pH > 7.30), pero desarrollan hiperglucemias extremas (> 600–1000 mg/dL), hiperosmolaridad plasmática efectiva > 320 mOsm/kg, déficit hídrico de 8 a 10 litros y compromiso neurológico grave."
            }
        ],
        "guias_consenso": {
            "fuente": "Consenso Conjunto ADA/EASD 2024-2025 sobre Crisis Hiperglucémicas & Guía SAD",
            "metas_tabla": [
                {"criterio": "1° Paso en CAD / EHH (Hora 0 a 1)", "normal": "Expansión con Solución Fisiológica 0.9% (1000 ml en la 1° hora)", "prediabetes": "-", "diabetes": "Restaura perfusión tisular/renal y reduce la glucemia por hemodilución"},
                {"criterio": "2° Paso: Auditoría de Potasio (K+) antes de la Insulina", "normal": "Si K+ es ≥ 3.3 y ≤ 5.2 mEq/L: iniciar insulina + agregar 20-30 mEq KCl por litro de suero", "prediabetes": "-", "diabetes": "Si K+ < 3.3 mEq/L: ¡FRENAR INSULINA! Reponer K+ primero (riesgo de arritmia letal)"},
                {"criterio": "3° Paso: Bomba de Insulina Corriente EV (1 ml = 1 UI)", "normal": "0.1 UI/kg/hora en infusión continua (purgar 20 ml en tubuladura)", "prediabetes": "Al llegar glucemia a 200-250 mg/dL: agregar Dextrosa 5-10% y bajar bomba a 0.02-0.05 UI/kg/h", "diabetes": "Para pasar a SC: inyectar Basal SC 2 a 4 hs ANTES de apagar la bomba EV"}
            ],
            "regla_enfermeria": "En el abordaje de las emergencias glucémicas en la guardia y la unidad de cuidados intensivos, el equipo de enfermería debe aplicar tres principios críticos de seguridad que salvan vidas. En primer lugar, está estrictamente prohibido iniciar la Bomba de Insulina Endovenosa en una Cetoacidosis Diabética si el Potasio sérico es menor a 3.3 mEq/L, ya que la insulina activa la bomba Na+/K+ ATPasa introduciendo masivamente el potasio intravascular al espacio intracelular, desencadenando una hipokalemia severísima con arritmias letales y paro cardiorrespiratorio. En segundo lugar, frente a un paciente con hipoglucemia Nivel 3 (inconsciente o estuporoso) queda totalmente contraindicada la vía oral por el altísimo riesgo de broncoaspiración, requiriéndose rescate parenteral inmediato (Dextrosa hipertónica EV o Glucagón IM/SC); asimismo, al aplicar la Regla del 15 en el paciente despierto, nunca se deben utilizar chocolates, alfajores ni productos lácteos enteros, dado que su contenido lipídico frena el vaciamiento gástrico y retarda la absorción del azúcar. Finalmente, la Insulina Corriente endovenosa posee una vida media plasmática de apenas 4 a 5 minutos, por lo que es obligatorio administrar la dosis de Insulina Basal Subcutánea (NPH o Glargina) entre 2 y 4 horas ANTES de apagar la bomba endovenosa, garantizando la presencia de un depósito subcutáneo activo para evitar el rebote fulminante de la cetoacidosis."
        },
        "caso_practico": {
            "escenario": "Paciente de 22 años en guardia con Cetoacidosis Diabética. Estuvo 10 horas con Bomba EV de Insulina Corriente. Ya tiene glucemia de 165 mg/dL, pH 7.36, bicarbonato 20 mEq/L y tiene apetito. El residente indica: «Apagale ya mismo la bomba EV y a las 22:00 hs (dentro de 6 horas) le empezamos la Glargina subcutánea».",
            "pregunta": "¿Qué va a pasar en 2 horas si apagás la bomba EV sin haber solapado antes la insulina subcutánea?",
            "resolucion": "La Insulina Corriente endovenosa tiene una vida media plasmática de solo 4 a 5 minutos. Si se apaga la bomba sin haber aplicado la Insulina Basal Subcutánea (NPH o Glargina) entre 2 y 4 horas ANTES, el paciente se queda con cero insulina circulante y vuelve a entrar en Cetoacidosis Diabética de rebote."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: En la sala de guardia atendés a dos pacientes que ingresan por hipoglucemia. El primer paciente está totalmente despierto, orientado, diaforético y con un HGT de 58 mg/dL. El segundo paciente ingresa estuporoso, no responde a estímulos verbales y presenta un HGT de 38 mg/dL. ¿Cuál es la conducta de enfermería adecuada y fundamentada para cada caso?",
                "opciones": [
                    "Administrar a ambos pacientes un vaso de leche entera con dos chocolates para elevar rápidamente la glucemia y prevenir el rebote.",
                    "Aplicar al paciente despierto la Regla del 15 con 15 g de hidratos de carbono simples en agua o jugo (evitando grasas) y repetir HGT a los 15 minutos; y al paciente estuporoso protegerle la vía aérea, prohibir la vía oral y administrar Dextrosa hipertónica EV (o Glucagón 1 mg IM/SC).",
                    "Indicar al paciente despierto que camine 10 minutos y al paciente estuporoso colocarle sobrecitos de azúcar debajo de la lengua."
                ],
                "correcta": 1,
                "explicacion": "En la hipoglucemia Nivel 1 y 2 en paciente consciente y con reflejo deglutorio conservado, la 'Regla del 15' restituye la glucemia en 15 minutos mediante carbohidratos simples (como 3 sobres de azúcar en agua o 150 mL de jugo); se prohíbe el uso de alimentos grasos como el chocolate porque los lípidos retrasan el vaciamiento gástrico y la absorción intestinal del azúcar. Por el contrario, en la hipoglucemia Nivel 3 (paciente inconsciente o estuporoso), el reflejo de deglución está abolido y la vía oral está estrictamente contraindicada por riesgo mortal de broncoaspiración, requiriendo resolución parenteral inmediata por vena (Dextrosa hipertónica) o por vía intramuscular/subcutánea (Glucagón)."
            },
            {
                "pregunta": "2. Situación clínica: Ingresa al shockroom un joven de 19 años con Cetoacidosis Diabética (glucemia 450 mg/dL, pH 7.12, cetonemia positiva). Se inicia la expansión con Solución Fisiológica al 0.9%. El laboratorio de urgencia informa un ionograma con Potasio (K+) de 2.8 mEq/L. El médico de guardia indica armar inmediatamente la bomba de infusión continua de Insulina Corriente EV y comenzar el goteo a 0.1 UI/kg/hora. ¿Qué acción de enfermería es la técnicamente correcta?",
                "opciones": [
                    "Iniciar de inmediato la bomba de insulina a 0.1 UI/kg/hora según la orden médica para bajar la glucemia lo antes posible.",
                    "Detener el inicio de la bomba de insulina endovenosa, notificar la alerta de Potasio menor a 3.3 mEq/L e indicar/reponer cloruro de potasio parenteral hasta lograr K+ ≥ 3.3 mEq/L antes de encender la infusión de insulina.",
                    "Aplicar una dosis de insulina NPH por vía intramuscular profunda para reemplazar la bomba endovenosa."
                ],
                "correcta": 1,
                "explicacion": "La insulina estimula directamente la bomba Sodio-Potasio ATPasa en las membranas celulares, promoviendo el desplazamiento masivo de potasio desde el espacio extracelular (sangre) hacia el espacio intracelular. Si se inicia la infusión de insulina en presencia de un Potasio basal < 3.3 mEq/L, la glucemia descenderá pero los niveles de potasio plasmático caerán a valores críticos, desencadenando arritmias ventriculares potencialmente letales, debilidad muscular respiratoria y paro cardíaco. Por ello, las guías internacionales (ADA/EASD) establecen el freno obligatorio de la insulina hasta corregir el potasio por encima de 3.3 mEq/L."
            },
            {
                "pregunta": "3. Situación clínica: Un paciente en tratamiento por Cetoacidosis Diabética lleva 8 horas en infusión continua con Bomba de Insulina Corriente EV. El control horario de HGT indica que la glucemia cayó de 380 mg/dL a 210 mg/dL, pero los gases venosos persisten con acidosis (pH 7.22 y Bicarbonato 12 mEq/L). El residente sugiere apagar la bomba EV en ese momento. ¿Cuál es la conducta de enfermería correcta y cómo debe planificarse la transición a insulina subcutánea?",
                "opciones": [
                    "Apagar de inmediato la bomba de insulina y no administrar nada más hasta que el paciente pida comida.",
                    "Mantener encendida la bomba de insulina (reduciendo la dosis a la mitad) y conectar en paralelo Dextrosa al 5% o 10% para corregir la acidosis sin causar hipoglucemia; y al resolver la CAD, inyectar la Insulina Basal SC 2 a 4 horas ANTES de apagar la bomba EV.",
                    "Aumentar el goteo de la bomba de insulina al doble para forzar la corrección del pH y suspender los sueros de hidratación."
                ],
                "correcta": 1,
                "explicacion": "En la Cetoacidosis Diabética, la corrección de la glucemia ocurre mucho más rápido que la resolución de la lipólisis y la acidosis metabólica. Si la bomba de insulina se apaga prematuramente al llegar a 200–250 mg/dL, la cetogénesis continuará y el paciente recaerá; por ello, se debe mantener la infusión de insulina infundiendo Dextrosa al 5% o 10% en paralelo para prevenir la hipoglucemia mientras se elimina la acidosis. Asimismo, como la insulina corriente EV se depura en 4 a 5 minutos al apagar la bomba, la transición a vía subcutánea exige solapar la administración de Insulina Basal SC 2 a 4 horas antes del apagado, garantizando un depósito tisular activo que impida el rebote de la cetoacidosis."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 9: COMPLICACIONES CRÓNICAS Y PIE DIABÉTICO (IWGDF)
    # ==========================================================================
    {
        "numero": 9,
        "id": "u9_complicaciones_cronicas_pie",
        "icono": "🦶",
        "titulo": "Unidad 9: Complicaciones Crónicas (Micro/Macro) y Pie Diabético (IWGDF)",
        "modulo": "Prevención de Secuelas",
        "duracion": "6 hs cátedra",
        "resumen": "Retinopatía, Nefropatía, Neuropatía periférica y autonómica, examen instrumental del Pie Diabético (monofilamento 10g, diapasón, pulsos), Score SINBAD y curaciones.",
        "fisiopatologia_cards": [
            {
                "titulo": "Tríada Microvascular: Retina, Riñón y Nervio Periférico",
                "contenido": "La hiperglucemia crónica daña el endotelio capilar por glicación avanzada (AGEs) y estrés oxidativo: 1) RETINOPATÍA: primera causa de ceguera prevenible (requiere fondo de ojo anual con pupila dilatada). 2) NEFROPATÍA: se detecta precozmente con la Relación Albúmina/Creatinina en orina aislada (RAC ≥ 30 mg/g) + cálculo de TFG. 3) NEUROPATÍA: en «bota y guante» (pérdida de sensibilidad termoalgésica y vibratoria) + neuropatía autonómica (hipotensión ortostática, gastroparesia, anhidrosis plantar e infarto silente sin dolor de pecho)."
            },
            {
                "titulo": "Diferenciación Clínica Vital: Pie Neuropático vs Pie Isquémico",
                "contenido": "• PIE NEUROPÁTICO: Pie TIBIO, seco (anhidrosis autonómica que genera grietas en talón), pulsos pedio y tibial posterior PRESENTES, dedos en garra/martillo, hiperqueratosis (callo) plantar en zonas de hiperpresión (cabezas de metatarsianos) y úlcera plantar redonda en sacabocados INDOLORA. • PIE ISQUÉMICO (Enfermedad Arterial Periférica): Pie FRÍO, pálido o cianótico/rubor de declive, SIN PULSOS, piel fina atrófica brillante sin vello, úlcera en punta de dedos, bordes laterales, maléolo o talón MUY DOLOROSA."
            }
        ],
        "guias_consenso": {
            "fuente": "Guía Internacional IWGDF 2023/2025 & Ministerio de Salud de la Nación Argentina",
            "metas_tabla": [
                {"criterio": "Monofilamento de Semmes-Weinstein (10 gramos)", "normal": "Percibe los puntos plantares evaluados (pulpejo del hallux y cabezas del 1°, 3° y 5° metatarsiano)", "prediabetes": "Aplicar perpendicular 1.5 seg con ojos cerrados hasta curvar en 'C' (sin tocar callos)", "diabetes": "La falta de percepción en ≥ 1 punto define Pérdida de Sensibilidad Protectora (PSP)"},
                {"criterio": "Sensibilidad Vibratoria Profunda", "normal": "Diapasón de 128 Hz en prominencia ósea interfalángica del Hallux", "prediabetes": "-", "diabetes": "Evalúa fibras gruesas mielinizadas; se altera precozmente"},
                {"criterio": "Clasificación SINBAD de Úlcera de Pie Diabético", "normal": "Evalúa: Sitio, Isquemia, Neuropatía, Bacteria, Área (≥ 1 cm²), Depth (Profundidad a tendón/hueso)", "prediabetes": "Puntaje < 3: manejo con descarga local y control estrecho", "diabetes": "Puntaje ≥ 3 (sobre 6): Derivación urgente a Equipo de Pie Diabético / Cirugía Vascular"}
            ],
            "regla_enfermeria": "En la curación y cuidado del pie diabético, el equipo de enfermería debe aplicar con máxima firmeza dos normas de seguridad de cumplimiento obligatorio para evitar amputaciones y lesiones graves. En primer lugar, está estrictamente prohibido cortar, debridar con bisturí o usar sustancias desbridantes en una escara necrótica negra, seca y sin secreción ubicada en un pie isquémico (frío y sin pulsos); al carecer de riego sanguíneo arterial para la cicatrización, romper esa barrera protectora natural sin revascularización previa transforma una necrosis seca e inerte en una gangrena húmeda e infecciosa que precipita la amputación mayor del miembro. En segundo lugar, respecto al autocuidado diario, jamás se debe colocar crema hidratante en los espacios interdigitales ni permitir el uso de bolsas de agua caliente, caloventores próximos o ladrillos calientes en pacientes con neuropatía; la humedad interdigital macerada por cremas constituye la puerta de entrada principal para micosis e infecciones bacterianas graves, mientras que la pérdida de la sensibilidad termoalgésica ('anestesia protectora') expone al paciente a sufrir quemaduras de segundo y tercer grado por fuentes de calor externas sin registrar señal alguna de dolor."
        },
        "caso_practico": {
            "escenario": "Un paciente de 64 años con 15 años de DBT2 llega al consultorio de enfermería en invierno con una ampolla gigante y quemadura de segundo grado en el dorso de ambos pies. Dice: «Anoche tenía los pies helados, puse una bolsa de agua hirviendo en la cama y ni sentí que estuviera caliente».",
            "pregunta": "¿Por qué sentía los pies helados pero se quemó sin sentir dolor, y qué educación clave le das?",
            "resolucion": "Sufre polineuropatía diabética distal en 'bota': tiene parestesias térmicas (sensación subjetiva de frío) combinadas con anestesia termoalgésica (perdió los receptores del dolor y calor). Por eso están estrictamente prohibidas las bolsas de agua caliente, ladrillos calientes, almohadillas eléctricas o acercar los pies a la estufa."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: Acude a la consulta de enfermería un paciente de 62 años con Diabetes Tipo 2 de 12 años de evolución para la valoración anual de pies. En la inspección observás una lesión ulcerada redonda e indolora debajo de la cabeza del primer metatarsiano, rodeada por un halo de hiperqueratosis gruesa (callo), con pie tibio y pulsos pedio y tibial posterior presentes. Para evaluar la pérdida de la sensibilidad protectora (PSP), preparás el monofilamento de 10 g de Semmes-Weinstein. ¿Cuál es la interpretación de la lesión y la técnica correcta de aplicación del monofilamento?",
                "opciones": [
                    "Es una úlcera isquémica pura; el monofilamento debe clavar la aguja metálica en el centro del callo para verificar la respuesta motora.",
                    "Es una úlcera neuropática; el monofilamento debe apoyarse perpendicularmente sobre piel indemne (evitando zonas con callo grueso) durante 1.5 segundos hasta curvarse en 'C', con los ojos del paciente cerrados.",
                    "Es una lesión infecciosa micótica; el monofilamento debe frotarse rápidamente entre los dedos de los pies para evaluar el reflujo capilar."
                ],
                "correcta": 1,
                "explicacion": "Las úlceras neuropáticas se caracterizan por ser indoloras, situarse en puntos de apoyo o hiperpresión plantar (como las cabezas metatarsianas), presentar piel tibia con pulsos conservados y estar rodeadas de hiperqueratosis secundaria al roce continuo. Para la valoración instrumental con el monofilamento de 10 g, la técnica exige que el paciente mantenga los ojos cerrados mientras se aplica el filamento de nylon perpendicularmente en áreas de piel limpia e indemne durante 1.5 segundos hasta que se doble formando una 'C'; está contraindicado apoyarlo sobre callosidades o tejido necrótico, ya que la hiperqueratosis actúa como una barrera mecánica dura que distorsiona la prueba generando falsos negativos."
            },
            {
                "pregunta": "2. Situación clínica: En la sala de internación o consultorio de curaciones asistís a un paciente de 68 años que presenta en el talón derecho una escara necrótica negra, totalmente seca, dura y adherida, sin eritema, secreción ni olor. Al palpar el pie, notás que el miembro está frío, pálido y no se palpan pulsos pedios ni tibiales posteriores. El paciente refiere dolor intenso que empeora al elevar la pierna. ¿Cuál es la conducta de enfermería correcta según los lineamientos de la guía internacional IWGDF?",
                "opciones": [
                    "Debridar inmediatamente la escara negra con bisturí y colocar pomada enzimática para acelerar la cicatrización del talón.",
                    "Mantener la escara seca, limpia y desinfectada, proteger el talón de todo apoyo con una descarga flotante, y derivar de urgencia a Cirugía Vascular para evaluación de revascularización arterial sin realizar debridamiento cortante.",
                    "Lavar la zona con abundante agua oxigenada y frotar con cepillo quirúrgico para remover la costra seca."
                ],
                "correcta": 1,
                "explicacion": "La presencia de un pie frío, doliente y sin pulsos indica una isquemia arterial periférica severa. Según la Guía Internacional IWGDF (International Working Group on the Diabetic Foot), ante una escara necrótica negra y seca en un pie isquémico sin signos de infección húmeda ni colección purulenta, está estrictamente prohibido realizar debridamiento cortante o enzimático. Sin una perfusión arterial adecuada que aporte oxígeno y nutrientes, remover esa escara seca (que actúa como una cubierta protectora biológica) expone planos profundos a la colonización bacteriana, transformando la necrosis seca e inerte en una gangrena húmeda e infecciosa con riesgo inminente de amputación mayor del miembro. La conducta exige mantener la escara seca, descargar el talón para evitar la presión y gestionar la evaluación vascular de urgencia."
            },
            {
                "pregunta": "3. Situación clínica: Durante el taller de educación en autocuidado para la prevención del pie diabético, un paciente de 60 años con polineuropatía sensitiva refiere que en invierno suele ponerse una bolsa de agua hirviendo en los pies dentro de la cama porque los siente 'helados', y que para evitar grietas se coloca abundante crema humectante entre todos los dedos antes de ponerse las medias. ¿Cómo debe corregir enfermería estas conductas y cuál es su fundamentación?",
                "opciones": [
                    "Felicitar al paciente por mantener sus pies calientes con la bolsa de agua y sugerirle agregar talco mentolado sobre la crema interdigital.",
                    "Explicar que la sensación de frío es una parestesia neuropática pero sus pies tienen 'anestesia protectora' que impide sentir quemaduras por la bolsa de agua, e indicar que la crema se aplica en talón, planta y dorso pero NUNCA entre los dedos por riesgo de maceración y micosis.",
                    "Recomendar cambiar la bolsa de agua por ladrillos calientes envueltos en toallas y colocar manteca en las zonas interdigitales."
                ],
                "correcta": 1,
                "explicacion": "La polineuropatía diabética periférica causa la pérdida de la sensibilidad termoalgésica (anestesia para el dolor y la temperatura) combinada frecuentemente con parestesias subjetivas (sensación engañosa de pies fríos o adormecidos). Colocar bolsas de agua caliente, compresas o estufas cerca de pies neuropáticos provoca quemaduras graves de segundo y tercer grado sin que el paciente perciba la agresión térmica. Con respecto a la hidratación, la neuropatía autonómica causa anhidrosis (falta de sudoración) produciendo piel seca y grietas en la planta y talón, por lo que se requiere crema hidratante en esas zonas; sin embargo, está prohibido aplicar crema en los pliegues interdigitales, ya que la acumulación de humedad en esos espacios macera la epidermis facilitando infecciones fúngicas (tinea pedis) y bacterianas que actúan como puerta de entrada para celulitis y flemones de pie."
            }
        ]
    },

    # ==========================================================================
    # UNIDAD 10: ROL DE ENFERMERÍA EN EDUCACIÓN TERAPÉUTICA, ALTA Y DÍAS DE ENFERMEDAD
    # ==========================================================================
    {
        "numero": 10,
        "id": "u10_educacion_alta",
        "icono": "🎓",
        "titulo": "Unidad 10: Educación Terapéutica (DSMES), Días de Enfermedad y Alta Segura",
        "modulo": "Liderazgo Enfermero y Educación",
        "duracion": "6 hs cátedra",
        "resumen": "Método Teach-Back (Re-enseñanza), desarme empático de mitos, protocolo de «Días de Enfermedad» (Sick Day Rules), regla SADMANS, kit de supervivencia al alta y adherencia familiar.",
        "fisiopatologia_cards": [
            {
                "titulo": "Por qué fracasan las «Charlas Tradicionales» y cómo funciona el Método Teach-Back",
                "contenido": "Los estudios demuestran que el paciente olvida entre el 40% y el 80% de la información médica oral apenas sale del consultorio, y cuando se le pregunta «¿Entendió Todo?» responde «Sí» por vergüenza o estrés hospitalario. El método TEACH-BACK (Re-enseñanza y Demostración Práctica) consiste en pedirle al paciente y a su familiar: «Para asegurarme de que me expliqué bien, ¿me mostrás vos con la lapicera en la mano cómo vas a quitar los dos capuchones, purgar 2 unidades y cargar las 10 unidades mañana?»."
            },
            {
                "titulo": "Protocolo de «Días de Enfermedad» (Sick Day Rules) y Regla SADMANS",
                "contenido": "Cuando un paciente con diabetes cursa fiebre, gripe, gastroenteritis o infección urinaria, las hormonas contrarreguladoras del estrés infeccioso (cortisol, adrenalina, glucagón) elevan la glucemia y la cetogénesis aunque el paciente no ingiera alimentos. Reglas vitales: 1) NUNCA suspender por cuenta propia la insulina basal, 2) Hidratarse cada hora y medir HGT/cetonas cada 3 a 4 hs, 3) Pausar transitoriamente los fármacos del acrónimo SADMANS (Sulfonilureas, IECA, Diuréticos, Metformina, ARA-II, AINEs e iSGLT2) si hay vómitos, diarrea o deshidratación aguda."
            }
        ],
        "guias_consenso": {
            "fuente": "Estándares Nacionales de Educación para el Automanejo de la Diabetes (DSMES - ADA 2025) & SAD",
            "metas_tabla": [
                {"criterio": "Validación Educativa al Alta", "normal": "Método Teach-Back (Demostración Inversa).", "prediabetes": "Pedir al paciente que arme la lapicera, purgue 2 UI, retire el segundo capuchón interno y explique el rescate de hipoglucemia.", "diabetes": "Peligro a evitar: Dar el alta tras hacer preguntas cerradas («¿Entendió todo?») donde el paciente asiente por vergüenza sin comprender la técnica."},
                {"criterio": "Reglas de Días de Enfermedad", "normal": "Preservación Basal e Hidratación.", "prediabetes": "Instar a mantener la dosis de insulina basal, controlar HGT/cetonas cada 3–4 hs e ingerir líquidos cada hora.", "diabetes": "Peligro a evitar: Suspender la insulina basal «porque el paciente no come o vomita», desencadenando Cetoacidosis Diabética."},
                {"criterio": "Suspensión por Deshidratación", "normal": "Acrónimo SADMANS.", "prediabetes": "Indicar la pausa temporal de Sulfonilureas, AiECA/IECA, Diuréticos, Metformina, ARA-II, NAINEs y SGLT2 ante diarrea o vómitos.", "diabetes": "Peligro a evitar: Mantener Metformina e iSGLT2 en un paciente deshidratado, induciendo acidosis láctica o cetoacidosis euglucémica."},
                {"criterio": "Kit de Alta Segura", "normal": "Checklist de Supervivencia.", "prediabetes": "Entregar en mano insulina, tiras reactivas, agujas de 4 mm y verificar que lleve 15 g de azúcar de rescate.", "diabetes": "Peligro a evitar: Otorgar el alta con recetas en papel sin asegurar la disponibilidad inmediata de los insumos en el hogar."}
            ],
            "regla_enfermeria": "Durante un 'día de enfermedad' (como gastroenteritis, gripe con fiebre o diarrea), suspender la insulina basal creyendo erróneamente que 'al no comer no se necesita insulina' constituye un error nefasto, ya que el aumento incontrolado de hormonas contrarreguladoras de estrés sin freno insulínico desencadena una Cetoacidosis Diabética (CAD) en pocas horas. Asimismo, resulta sumamente peligroso continuar administrando Metformina e inhibidores SGLT2 (gliflozinas) durante cuadros de vómitos o deshidratación aguda; la Metformina incrementa el riesgo de acidosis láctica por hipoperfusión renal, mientras que los iSGLT2 provocan Cetoacidosis Diabética Euglucémica (acidosis metabólica severa con glucemias engañosamente menores a 200–250 mg/dL). La regla de oro de enfermería exige mantener la insulina basal con monitoreos cada 3–4 horas, aplicar la pausa farmacológica SADMANS y asegurar una rehidratación oral continua."
        },
        "caso_practico": {
            "escenario": "Don Ernesto (71 años) reingresa por tercera vez con hiperglucemia de 420 mg/dL a pesar de tener indicada una lapicera de Insulina Glargina de 22 UI a la noche. En vez de retarlo, le pedís que te muestre cómo se aplica la insulina con su lapicera.",
            "pregunta": "Al observarlo, ves que gira el selector a 22, se pincha CON EL CAPUCHÓN INTERNO PLÁSTICO DE LA AGUJA PUESTO y aprieta el botón. ¿Qué lección deja este caso real de sala?",
            "resolucion": "Muchos pacientes mayores (especialmente con presbicia o retinopatía) quitan solo el capuchón externo grande de la aguja de la lapicera, pero no ven que queda un segundo capuchón interno finito cubriendo el bisel, o nunca purgan la aguja. Sin observación directa práctica (Teach-Back demostrativo) de enfermería, se le habría subido la dosis erróneamente."
        },
        "autoevaluacion": [
            {
                "pregunta": "1. Situación clínica: Durante la preparación del alta hospitalaria de un paciente que inicia insulinoterapia con lapicera, el enfermero le pregunta: «¿Le quedó claro cómo colocarse la insulina NPH esta noche?» y el paciente responde: «Sí, todo muy claro». ¿Cómo debe actuar el enfermero según las recomendaciones de las guías ADA/SAD?",
                "opciones": [
                    "Firmar la planilla de alta y despedir al paciente ya que confirmó haber comprendido las indicaciones.",
                    "Aplicar la técnica Teach-Back, entregándole la lapicera para que demuestre cómo purgará 2 UI, colocará la aguja removiendo ambos capuchones y marcará su dosis.",
                    "Entregarle un folleto explicativo impreso y pedirle que lo lea detenidamente al llegar a su domicilio."
                ],
                "correcta": 1,
                "explicacion": "El método Teach-Back y la demostración práctica son imprescindibles para detectar errores críticos de técnica (como dejar puesto el capuchón interno fino de la aguja) que las preguntas cerradas no logran evidenciar."
            },
            {
                "pregunta": "2. Situación clínica: Un paciente de 28 años con Diabetes Tipo 1 consulta telefónicamente a la guardia porque cursa una gastroenteritis con fiebre de 38,5 °C y náuseas. Refiere que, como no ha almorzado nada, decidió no inyectarse la insulina basal. ¿Cuál es la indicación de enfermería adecuada?",
                "opciones": [
                    "Felicitar al paciente por suspender la insulina basal para evitar una hipoglucemia severa mientras no tolere sólidos.",
                    "Explicar que las hormonas de estrés elevan la glucemia aunque no coma, indicando aplicar inmediatamente la insulina basal, rehidratarse y medir HGT cada 3–4 horas.",
                    "Indicar que reemplace la insulina basal por dosis dobles de metformina y antitérmicos cada 6 horas."
                ],
                "correcta": 1,
                "explicacion": "En días de enfermedad, las hormonas contrarreguladoras aumentan la gluconeogénesis; suspender la insulina basal en Diabetes Tipo 1 causa Cetoacidosis Diabética acelerada en pocas horas."
            },
            {
                "pregunta": "3. Situación clínica: Un paciente tratado con Metformina 850 mg y Empagliflozina 10 mg presenta un cuadro de 24 horas de evolución con diarrea abundante, vómitos repetidos y signos de deshidratación. ¿Qué conducta respecto a su medicación oral debe reforzarse según el acrónimo SADMANS?",
                "opciones": [
                    "Duplicar la dosis de Empagliflozina para compensar la pérdida de líquidos mediante diuresis osmótica.",
                    "Pausar temporalmente la Metformina y la Empagliflozina mientras persista el cuadro deshidratante y consultar al centro de salud.",
                    "Continuar con la Metformina pero tomarla en ayunas junto a un AINE para calmar el dolor abdominal."
                ],
                "correcta": 1,
                "explicacion": "Según la regla SADMANS, ante la deshidratación aguda deben pausarse la Metformina (riesgo de acidosis láctica) y los iSGLT2 (riesgo de Cetoacidosis Diabética Euglucémica) hasta la recuperación volémica."
            }
        ]
    }
]

# Inyección automática de la Tarjeta de Referencia de Siglas y Abreviaturas en cada Unidad
_SIGLAS_REFERENCIA_UNIDADES = {
    1: "PTOG = Prueba de Tolerancia Oral a la Glucosa (curva de 75 g en 300 mL de agua a las 2 hs) • HbA1c = Hemoglobina Glicosilada (promedio de glucemia de 90–120 días, tubo tapa violeta EDTA sin ayuno) • GAA = Glucemia Alterada en Ayunas (100–125 mg/dL) • ITG = Intolerancia a la Glucosa (140–199 mg/dL a las 2 hs) • DBT1 / DBT2 = Diabetes Mellitus Tipo 1 y Tipo 2 • Las 4 P = Poliuria, Polidipsia, Polifagia y Pérdida de peso.",
    2: "CGM / MCG = Monitoreo Continuo de Glucosa (sensor intersticial con retraso fisiológico o 'lag time' de 10–15 min) • TIR = Tiempo en Rango (70–180 mg/dL, meta >70% del día) • TBR = Tiempo Bajo Rango (<70 mg/dL, meta <4%) • HGT = Hemoglucotest (glucemia capilar en pulpejo lateral del dedo) • LADA = Diabetes Autoinmune Latente del Adulto.",
    3: "DBT2 = Diabetes Mellitus Tipo 2 • IGF-1 = Factor de Crecimiento Similar a la Insulina Tipo 1 (su activación en piel produce Acantosis Nigricans) • HbA1c = Hemoglobina Glicosilada • RAC = Relación Albúmina/Creatinina en orina (<30 mg/g) • PA = Presión Arterial (<130/80 mmHg).",
    4: "DG = Diabetes Gestacional • PTOG p75 = Prueba de Tolerancia Oral a la Glucosa con 75 g de glucosa anhidra • ALAD / SAD = Asociación Latinoamericana / Sociedad Argentina de Diabetes (diagnóstico en embarazo: ayunas ≥100 mg/dL o 2 hs ≥140 mg/dL) • IADPSG = Consenso Internacional de Diabetes y Embarazo (92 / 180 / 153 mg/dL).",
    5: "ADA = Asociación Americana de Diabetes (Método del Plato: 50% vegetales sin almidón, 25% proteínas, 25% carbohidratos) • GLUT-4 = Transportador de Glucosa Tipo 4 • AMPK = Proteína Quinasa Activada por AMP (abre canales GLUT-4 durante el ejercicio sin usar insulina) • HGT = Hemoglucotest capilar.",
    6: "NPH = Insulina Neutral Protamine Hagedorn (insulina intermedia de aspecto turbio/lechoso; rolar 20 veces) • UI = Unidades Internacionales (U-100 = 100 UI/mL) • FITTER = Consenso Internacional de Técnica de Inyección (aguja 4 mm a 90°) • SC / EV = Vía Subcutánea / Vía Endovenosa (solo la Insulina Corriente/Regular va por vía EV).",
    7: "ADO = Antidiabéticos Orales • iSGLT2 = Inhibidores del Cotransportador Sodio-Glucosa Tipo 2 (Empagliflozina/Dapagliflozina) • iDPP-4 = Inhibidores de DPP-4 o Gliptinas (Sitagliptina/Linagliptina) • GLP-1 = Agonistas del Receptor GLP-1 (Semaglutida/Liraglutida) • TFG / VFG = Tasa de Filtrado Glomerular renal • NPO = Nada Por Boca (ayuno hospitalario).",
    8: "HGT = Hemoglucotest capilar • CAD = Cetoacidosis Diabética • EHH = Estado Hiperosmolar Hiperglucémico • K+ = Potasio sérico (si K+ < 3.3 mEq/L, diferir insulina e infundir potasio primero) • EV / IM / SC = Vía Endovenosa / Intramuscular / Subcutánea • SF 0.9% = Solución Fisiológica (ClNa 0.9%).",
    9: "PSP = Pérdida de la Sensibilidad Protectora (evaluada con Monofilamento de 10 g y Diapasón de 128 Hz) • IWGDF = Grupo Internacional de Trabajo de Pie Diabético • SINBAD = Escala de severidad (Sitio, Isquemia, Neuropatía, Bacteriana, Área, Profundidad; ≥3 puntos exige derivación urgente) • ITB = Índice Tobillo-Brazo.",
    10: "DSMES = Educación y Apoyo para el Automanejo de la Diabetes • Teach-Back = Método de Demostración Inversa (el paciente demuestra la técnica) • SADMANS = Fármacos a pausar en deshidratación (Sulfonilureas, AiECA, Diuréticos, Metformina, ARA-II, NAINEs, SGLT2) • HGT = Hemoglucotest."
}

for _u in UNIDADES_ACADEMICAS:
    _num = _u.get("numero")
    if _num in _SIGLAS_REFERENCIA_UNIDADES:
        _u["fisiopatologia_cards"].insert(0, {
            "titulo": f"🔤 Glosario de Siglas y Abreviaturas de la Unidad {_num} (Ej: PTOG, HbA1c, HGT)",
            "contenido": _SIGLAS_REFERENCIA_UNIDADES[_num]
        })

