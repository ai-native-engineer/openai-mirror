<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/security-hardening -->

Usa `$codex-security:propose-security-hardening` para convertir una recopilación de
evidencia de seguridad en opciones de refuerzo estructural o arquitectónico. El
flujo de trabajo puede analizar un escaneo finalizado de Codex Security o partir de los
hallazgos proporcionados, informes de divulgación, revisiones de incidentes, documentos de evaluación y
código fuente.

El resultado es un portafolio de diseño, no un parche, y no demuestra que corrija una
vulnerabilidad. Codex solo modifica el repositorio después de que selecciones una opción y
le pidas explícitamente que haga ese cambio.

## Preparar la evidencia

Proporciona lo siguiente al flujo de trabajo:

- Un directorio de escaneo o una colección de hallazgos e informes definida explícitamente.
- El árbol de código fuente de destino y, cuando esté disponible, la revisión o instantánea pertinente.
- Pruebas de concepto, trazas, evidencia de incidentes o material de evaluación que respalden los
hallazgos.
- Restricciones relacionadas con el rendimiento, la memoria, la compatibilidad, la confiabilidad, las operaciones,
el tiempo de entrega o el alcance del cambio.

El flujo de trabajo usa la evidencia para identificar incumplimientos recurrentes de invariantes, controles
dispersos, puntos de concentración de privilegios, límites de aislamiento débiles y patrones
recurrentes de remediación. También puede concluir que las correcciones locales son más
proporcionales que un cambio arquitectónico.

## Ejecutar el flujo de trabajo

Envía un prompt como este:

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## Revisar el portafolio

Un portafolio útil debería:

- Vincular cada cambio propuesto con hallazgos concretos, el código fuente y la evidencia del modelo de
amenazas.
- Describir el diseño actual y los invariantes de seguridad que el nuevo diseño debería
preservar.
- Comparar distintas opciones en cuanto al riesgo residual, el rendimiento,
la confiabilidad, las operaciones, la compatibilidad y el costo de migración.
- Recomendar una opción solo cuando la evidencia la respalde, con supuestos
explícitos y preguntas abiertas.
- Incluir lineamientos para el despliegue, la validación, la reversión y la implementación.
- Separar los hechos observados, las inferencias y las propiedades de diseño propuestas.

Revisa la evidencia y las ventajas y desventajas antes de elegir una opción. Un diagrama de arquitectura
o una recomendación de diseño no sustituye la validación de los hallazgos
originales ni de la corrección implementada.

## Usar las recomendaciones de refuerzo de seguridad de un escaneo

Puedes solicitar un portafolio de refuerzo para un escaneo estándar, profundo o de cambios con
hallazgos que deban incluirse en un informe. Codex guarda el portafolio en `hardening/hardening.md`,
el análisis estructurado en `hardening/hardening.json` y las propuestas
o los diagramas complementarios en `hardening/`. El escaneo incluye un enlace al portafolio en `report.md`.

Conserva el directorio completo del escaneo para que esos enlaces sigan funcionando. Para revisar
los informes individuales en los que se basa el portafolio, consulta [Redactar informes de
vulnerabilidades](/es-419/codex/security/plugin/vulnerability-reports).
