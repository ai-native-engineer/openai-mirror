<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/scans -->

Comienza con un análisis estándar de Codex Security para una revisión inicial o una evaluación rutinaria
del repositorio o de un componente. Este ejecuta una vez el flujo de trabajo completo del análisis.

Para realizar una evaluación más exhaustiva, revisa los resultados y luego ejecuta un [análisis
profundo](/es-419/codex/security/plugin/deep-scans). Los análisis profundos tardan más y realizan búsquedas
más exhaustivas.

## Elegir el área de análisis

En la App de escritorio, abre **Seguridad**, selecciona **Análisis** y luego **+ Análisis**.
Elige un repositorio existente u otra carpeta y, después, selecciona **Base de código**.

Analiza todo el repositorio cuando necesites una cobertura amplia y el repositorio sea una
unidad de revisión adecuada. En un monorepo, elige una carpeta cuando un servicio,
paquete o componente tenga un responsable y un límite de seguridad claramente definidos.

También puedes iniciar un análisis desde una conversación de Codex:

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities.

Para centrar esa conversación en una carpeta específica, identifica el componente:

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities, focusing on the services/billing component.

  En un monorepo grande, comienza por un producto o servicio con límites bien definidos.

## Configurar el análisis

Para obtener la mejor calidad de análisis, usa <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
con un esfuerzo de razonamiento `xhigh`.

1. Selecciona **Base de código** y deja **Análisis profundo** desactivado.
2. Confirma el repositorio seleccionado, la rama actual y la revisión más reciente.
3. Establece **Área de análisis** en todo el repositorio o elige una carpeta.
4. Elige un modelo y un esfuerzo de razonamiento.
5. Abre **Contexto adicional** solo cuando modifique la revisión. Un contexto útil
   identifica las entradas controladas por atacantes, los límites de confianza, las acciones sensibles o un
   área específica que se debe priorizar.
6. Selecciona **Iniciar análisis**.

Agrega `SECURITY.md` a la raíz del repositorio para proporcionar directrices de seguridad persistentes.
Describe el modelo de amenazas, las invariantes de seguridad, los criterios para informar hallazgos,
las exclusiones y el contexto de gravedad. Agrega archivos `SECURITY.md` anidados con directrices
específicas para cada directorio. Cuando las políticas entren en conflicto, prevalece el archivo más cercano al
código. Codex Security trata estos archivos como contexto de políticas,
no como instrucciones ejecutables.

Usa `AGENTS.md` para indicar los comandos de compilación y validación admitidos, así como otras
instrucciones específicas del repositorio.

## Esperar a que finalicen las fases

Un análisis ejecuta estas fases en orden:

1. El **modelado de amenazas** identifica los activos, los puntos de entrada, los límites de confianza y las
   invariantes de seguridad.
2. La **detección de hallazgos** revisa el código solicitado en busca de posibles fallas en los
   controles y rutas desde el origen hasta el punto de destino.
3. La **validación** prueba o comprueba por otros medios cada candidato y registra la evidencia
   o los aspectos que aún no se han demostrado.
4. El **análisis de impacto y rutas** evalúa las rutas realistas de cada candidato,
   su impacto y su gravedad.
5. La **generación de informes** registra los hallazgos validados, la cobertura y los metadatos del análisis.
   Los informes detallados de cada hallazgo están disponibles cuando se solicitan.
6. El **fortalecimiento estructural**, cuando se solicita, analiza el conjunto de hallazgos y
   genera directrices de diseño.
7. La **finalización** valida el contrato estructurado del análisis y genera
`report.md`, que incluye enlaces a los informes detallados o las directrices de fortalecimiento correspondientes.

El entorno de trabajo muestra la fase activa del análisis y los avances que informa el complemento.
Selecciona **Ver actividad** para inspeccionar la tarea de Codex. Espera a obtener el resultado
completo, en lugar de evaluar candidatos preliminares o interrumpir el análisis porque una fase tarda
más que otra.

## Revisar el análisis completado

Revisa el resultado en este orden:

1. Confirma el objetivo, la revisión y el área de análisis.
2. Consulta las superficies revisadas y todas las áreas expresamente aplazadas o sujetas a seguimiento.
3. Para cada hallazgo, examina el control raíz o el punto de destino, la entrada controlada por el atacante,
el método de validación, la incertidumbre restante, la alcanzabilidad realista,
la justificación de la gravedad y la corrección propuesta.
4. Descarta los hallazgos cuya evidencia no respalde la ruta o el impacto indicados.
5. Selecciona un hallazgo aceptado antes de comenzar una corrección.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revisa la gravedad, el estado de validación, la causa raíz y la ruta de
ataque del hallazgo.
  </figcaption>
</figure>

## Evaluar un primer análisis

Antes de analizar, elige entre dos y cuatro criterios de evaluación, como la detección
independiente, la calidad de la evidencia, los falsos positivos o la calidad de la corrección. Si
haces una prueba con un hallazgo conocido, registra si se lo proporcionaste a Codex o si
no se lo revelaste durante el análisis.

Registra la revisión del repositorio, la versión del complemento, el modelo y el esfuerzo de razonamiento.
Usa esta referencia inicial para comparar análisis posteriores cuando cambien el código, los controles de seguridad o
la configuración del análisis.

## Elegir la frecuencia de análisis

Define la frecuencia de los análisis según el riesgo del repositorio y la capacidad de tu equipo
para abordar los hallazgos. Ejecuta análisis en estos momentos:

- **Referencia inicial:** ejecuta un análisis estándar cuando incorpores un repositorio, asumas
  la responsabilidad de un componente o necesites un punto de partida para un nuevo modelo de amenazas.
- **Cambios en el código:** [revisa los cambios
  en el código](/es-419/codex/security/plugin/code-changes) cuando un Pull Request o un Commit
  modifique código sensible para la seguridad o una integración externa.
- **Revisión periódica:** define un intervalo de revisión periódico según la exposición de tu sistema
  y la frecuencia con que cambia el código. Ajústalo a la capacidad de tu equipo para
  abordar los hallazgos.
- **Después de una corrección:** [corrige y verifica el
  hallazgo](/es-419/codex/security/plugin/fix-findings). Confirma que el problema ya no
  se reproduce y conserva el análisis original para compararlo.

Estos activadores de análisis no crean una programación automatizada.

## Volver a abrir un análisis anterior

Abre **Seguridad** y luego selecciona un análisis guardado en **Análisis** para revisar sus
hallazgos, cobertura y artefactos de informe disponibles. Para evaluar el código más reciente,
inicia un análisis nuevo del mismo repositorio. El análisis nuevo no reemplaza al
anterior ni a sus artefactos.

## Usar los resultados

Usa el entorno de trabajo de Seguridad para revisar los hallazgos, la cobertura y las áreas de seguimiento
sin inspeccionar el JSON sin procesar. Cuando esté disponible, abre `report.md` como punto de entrada legible
al directorio completo del análisis. Conserva el directorio completo cuando
lo compartas o archives: el informe incluye enlaces a los informes detallados en `findings/`
y a las directrices de fortalecimiento estructural en `hardening/` cuando esos artefactos opcionales
estén disponibles.

En segundo plano del espacio de trabajo, cada análisis conserva `scan-manifest.json`, `findings.json`,
y `coverage.json` para la automatización y las integraciones. Por lo general, no necesitas
abrir estos archivos.

Para obtener artefactos portátiles o hacer un seguimiento externo de incidencias, consulta [Exportar o dar seguimiento a
los hallazgos](/es-419/codex/security/plugin/export-findings).

## Siguiente paso

Después de aceptar un hallazgo, usa [Corregir y verificar un
hallazgo](/es-419/codex/security/plugin/fix-findings) para generar y revisar un
parche acotado. No le pidas a Codex que corrija todos los hallazgos de un análisis en un solo chat.
