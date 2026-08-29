HealthSignal LATAM — RISA Data V1.0
Pipeline explicable de integración, detección híbrida, razonamiento clínico cruzado y priorización
Equipo ClinIA — Hackathon Perú 2026 (Talento TECH)
Esta versión agrega una capa nueva sobre el pipeline validado: el Panel de Razonamiento Clínico Cruzado — para cada desviación detectada, el sistema responde explícitamente "¿hay un medicamento activo o un contexto conductual que la explique, o no?", usando medication_administrations.csv y patient_context.csv reales (antes cargados pero nunca usados).

Esta capa fue diseñada para pesar en tres criterios de la rúbrica oficial a la vez:

Criterio oficial	Puntos	Cómo lo atiende esta capa
Identificación de señales de riesgo	8	Distingue una desviación real de una explicada por fármaco/actividad — exactamente "diferenciar comportamientos esperados de situaciones potencialmente relevantes" (texto literal del desafío)
Explicabilidad y trazabilidad	5	Cada variable trae su propio veredicto (explicada / reforzada / sin confusor) con la razón exacta y el registro fuente citado
Innovación	15	Nadie más va a cruzar tres fuentes (vitales + medicamentos + contexto conductual) para razonar sobre causalidad clínica, no solo para detectar anomalías
Cuatro correcciones aplicadas en esta versión (encontradas y corregidas contra el validador oficial real, no solo por inspección de código):

evidence_role de la nueva evidencia se restringe a {PRIMARY, SUPPORTING, CONTEXT, QUALITY} — un rol MEDICATION habría sido rechazado por validate_submission.py.
El ajuste del score por confusores se aplica antes de la agregación por episodio, para que toda la cadena (patrones internos, priorización, salida oficial) use el mismo score corregido — evita que dos lugares del pipeline calculen el ajuste de forma distinta y queden desalineados.
El piso de seguridad de reglas duras se reaplica después del ajuste por confusores — un medicamento no puede nunca bajar una alerta que ya era CRITICAL por umbral duro.
La evidencia de confusores usa el mismo T_event de la observación que explica, garantizando available_datetime ≤ decision_datetime sin excepción.
Cómo está organizado
#	Sección	Qué responde
1	Rutas e ingesta cruda	Resolución robusta del dataset en Kaggle + carga de TODAS las tablas
2	Catálogo completo de variables	Qué contiene cada tabla, variable por variable, con gráficos
3	Interoperabilidad	Fuentes con distinta frecuencia/unidad/estructura, unidas por ID canónico
4	Catálogo de calidad	Cada fenómeno con tratamiento justificado
5	Temporalidad	Ventanas, tendencias, combinaciones
6	Motor híbrido	Reglas duras + reglas de tendencia + combinación multivariable + ML/SHAP
7	Razonamiento clínico cruzado (NUEVO)	Medicamentos + contexto conductual explican o refuerzan cada desviación
8	Alertas irrelevantes	Demostración de que el pipeline NO sobre-alerta, ahora con confusores reales
9	Patrones internos RISA	Clasificador heurístico de NORMAL...COMPLEX
10	Priorización	Agregación por episodio + recalibración por percentil
11	Salida oficial	signals.csv/evidence.csv con evidencia de confusores incluida
12	Consola interactiva	Consulta in-notebook — ahora muestra el panel de razonamiento cruzado
13	Validación oficial	Corrida real de validate_submission.py
14	Síntesis	Respuesta explícita a la pregunta central del desafío
add Codeadd Markdown
