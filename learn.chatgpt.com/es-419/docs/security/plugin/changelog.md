<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/changelog -->

Consulta este registro de cambios para saber qué cambió en el Plugin de Codex Security.

**Versión más reciente del complemento:** `0.1.20`.

Verifica la versión del complemento en tu entorno actual de Codex antes de usar una función de una versión más reciente.

Las entradas del registro de cambios corresponden a la versión del complemento, no a la del paquete. Los usuarios de la CLI y el
SDK pueden ejecutar `npx @openai/codex-security info --json` para consultar juntas las versiones del
paquete y del complemento incluido.

## 0.1.20 (17 de agosto de 2026)

### Ejecuta análisis exhaustivos como auditorías completas e independientes

- Haz que cada worker de análisis exhaustivo realice la misma auditoría integral utilizada en los análisis estándar, que incluye el modelado de amenazas, la validación, el análisis de rutas de ataque y la generación de informes de cobertura.
- Combina en un solo análisis los informes finalizados de los workers y conserva los límites de tiempo configurados, la cobertura parcial, la recuperación tras reinicios y la cancelación.
- Usa cuatro workers simultáneos de forma predeterminada, detén el proceso después de que cuatro análisis completados consecutivos
  no aporten hallazgos nuevos y limita cada análisis exhaustivo a 40 ejecuciones de workers. Las configuraciones existentes de
`workers = "auto"` ahora usan cuatro workers. Consulta
[Configurar el entorno de ejecución de los análisis exhaustivos](/es-419/codex/security/plugin/deep-scans#configure-deep-scan-runtime).
- Reanuda los workers que terminaron de revisar el código fuente, pero perdieron su borrador final, en lugar de repetir la auditoría completa.

### Verifica Trusted Access for Cyber antes de los análisis alojados

- En los hosts de Codex que ofrecen la aplicación Codex Security Access, verifica el estado de Trusted Access antes de iniciar análisis estándar, de cambios y exhaustivos.
- Ve una advertencia destacada cuando los resultados protegidos del análisis puedan no estar disponibles, con un enlace de inscripción si no se concedió acceso.
- Continúa el análisis si la comprobación no puede verificar el estado de Trusted Access o no se concede el acceso; el aviso no determina si se ejecuta el análisis.
- Los paquetes públicos de la CLI y del SDK no realizan esta comprobación informativa en `0.1.20`.

### Ejecuta análisis exhaustivos en más entornos

- Inicia workers de análisis exhaustivos desde instalaciones de los paquetes de la CLI y del SDK, incluidas las
  instalaciones en Windows sin un ejecutable global de `codex`.
- Mantén la configuración de los análisis exhaustivos de las versiones independientes de la CLI y del SDK aislada de otros análisis en ejecución.
- Conserva la configuración de aprobación no interactiva en los workers anidados de análisis exhaustivos.

### Conserva los resultados de los análisis ante más fallas

- Conserva más análisis guardados y resultados de workers que ya finalizaron durante los procesos de recuperación por reinicio, archivado y transferencia.
- Recupera hallazgos válidos a partir de datos de análisis antiguos o incompletos.
- Completa los análisis cuando se superponen informes de cobertura independientes.
- Registra correctamente la entrada en caché en los totales de uso de tokens de las respuestas actuales y anteriores del proveedor.

## 0.1.19 (13 de agosto de 2026)

### Establece un límite de tiempo para los análisis exhaustivos

- Configura `[deep_scan].max_time_hours` con una duración positiva de hasta 96 horas.
  Puedes usar fracciones de hora.
- Conserva los resultados de detección completados cuando venza el plazo y luego continúa con la validación y la generación de informes.
- Marca el informe como parcial si ninguna revisión del código fuente finaliza antes de que venza el plazo.

### Mejora la confiabilidad de los análisis

- Conserva el trabajo de detección completado cuando un worker se detiene o un reducer vuelve a intentarlo.
- Lee archivos de código fuente más grandes y genera informes sin los límites fijos de tamaño anteriores.
- Lee los cambios registrados en commits de la revisión seleccionada y conserva las rutas relativas al repositorio en Windows.
- Transfiere las credenciales de OpenRouter y Fireworks a los workers de los análisis exhaustivos.

## 0.1.18 (7 de agosto de 2026)

### Usa Amazon Bedrock para los análisis de seguridad

- Ejecuta análisis con tokens de portador de Amazon Bedrock y perfiles de AWS, ajustes de región, identidad web o credenciales de contenedores.
- Mantén la autenticación de AWS disponible para los workers delegados de los análisis exhaustivos.

### Ejecuta análisis estándar con menos coordinación

- Usa un flujo de trabajo más sencillo para los análisis estándar de repositorios y de rutas con alcance definido.
- Conserva las instrucciones de los archivos `SECURITY.md` anidados, el alcance exacto del análisis, las actualizaciones de progreso
  y los informes finales del análisis.

### Inicia y completa análisis con mayor confiabilidad

- Permite que los análisis iniciados mediante un prompt dispongan de hasta cinco minutos para inicializar repositorios grandes, en lugar de que el tiempo de espera se agote después de 30 segundos.
- Completa los análisis estándar y exhaustivos cuando un host impone límites a la longitud de los nombres de las herramientas.

### Mantén disponible la remediación después de cambios en el sistema de archivos

- Remedia los hallazgos de los análisis completados después de que el identificador de dispositivo cambie al volver a montar el sistema de archivos.
- Sigue exigiendo el checkout original y la revisión de Git antes de aplicar una corrección.

## 0.1.17 (5 de agosto de 2026)

### Sigue el progreso del análisis en tiempo real

- Monitorea la fase actual del análisis, el tiempo transcurrido, los workers activos, los archivos revisados y el uso de tokens desde una sola vista de progreso en tiempo real.
- Observa cómo se actualiza el progreso de la revisión del repositorio a medida que se terminan de revisar los archivos, en lugar de esperar a que finalice el análisis.

### Reanuda los análisis exhaustivos interrumpidos

- Continúa un análisis exhaustivo en curso después de que se reinicie su coordinador sin repetir revisiones de archivos ya completadas.
- Conserva los resultados de detección completados, la propiedad del análisis y el trabajo pendiente aunque se actualice la aplicación o se interrumpan las sesiones de análisis.

### Inicia y completa análisis con menos sobrecarga

- Inicia análisis estándar, de cambios y exhaustivos directamente en los flujos de trabajo nativos, sin abrir el widget de análisis integrado que se retiró.
- Reutiliza los resúmenes de análisis completados sin volver a cargar cada hallazgo, a menos que solicites los resultados estructurados completos.

## 0.1.16 (4 de agosto de 2026)

### Monitorea las mediciones de uso de los análisis

- Revisa el uso total de tokens y el uso de tokens de entrada, de entrada en caché y de salida, tanto en el análisis principal como en sus workers delegados.
- Distingue entre mediciones completas, parciales y no disponibles, en lugar de mostrar los datos de uso faltantes como cero.

### Ejecuta análisis más exhaustivos con resultados coherentes

- Usa las mismas fases de modelado de amenazas, descubrimiento, validación, análisis de rutas de ataque y generación de informes para los análisis estándar y profundos.
- Configura los workers de los análisis profundos, la delegación por worker, la saturación y los límites de descubrimiento desde la CLI o el SDK.
- Ejecuta análisis profundos con el entorno de ejecución de workers compatible con el modelo y recupera el estado de análisis anteriores sin perder el historial de análisis existente.
- Genera el informe principal para los análisis de cambios y los análisis profundos sin necesidad de informes de vulnerabilidades ni recomendaciones de fortalecimiento por separado.

### Mantener la precisión de las directrices de análisis y los repositorios objetivo

- Actualiza las directrices de seguridad durante un análisis activo y aplícalas a las fases posteriores y a los workers delegados de los análisis profundos.
- Conserva las URL de los repositorios, las referencias a Pull Requests y un contexto de seguridad más extenso sin permitir acceso a la red que no hayas solicitado.
- Haz que los análisis fallen cuando el repositorio o el objetivo del análisis cambie durante la ejecución para que la automatización no acepte hallazgos desactualizados.
- Respeta la configuración del proxy empresarial y de los certificados de confianza en los entornos de red administrados.

### Redactar informes de vulnerabilidades más claros

- Genera informes de vulnerabilidades respaldados por el código fuente que distingan el comportamiento observado de las hipótesis no verificadas.
- Incluye limitaciones realistas de las pruebas de concepto, las versiones afectadas, los límites de seguridad y directrices prácticas de remediación.

## 0.1.15 (30 de julio de 2026)

### Conservar los resultados de los análisis cuando cambia el repositorio

- Mantén los hallazgos y los informes completados vinculados a la revisión original o a la instantánea del árbol de trabajo, incluso si los archivos o la revisión del repositorio cambian durante el análisis.
- Muestra una advertencia al finalizar cuando el código seleccionado cambie o el objetivo deje de estar disponible, en lugar de descartar los resultados del análisis.
- Archiva un análisis existente antes de reutilizar su directorio de salida para otro análisis.

### Aplicar comentarios revisados sobre los hallazgos

- Registra un motivo cuando cierres un hallazgo como falso positivo.
- Aplica las decisiones revisadas sobre falsos positivos a los análisis posteriores del mismo objetivo, sin aplicarlas a otra copia de trabajo ni a un objetivo no relacionado.
- Suprime un hallazgo recurrente solo cuando el motivo anterior siga siendo válido para el código y los controles de seguridad actuales.

### Recuperar hallazgos válidos sin exagerar la cobertura

- Conserva los hallazgos válidos cuando otro hallazgo, informe o artefacto de fortalecimiento tenga un formato incorrecto, y muestra una advertencia sobre los datos omitidos.
- Elimina los hallazgos duplicados y conserva el más sólido según la gravedad, la confianza y la evidencia de respaldo.
- Marca la cobertura como parcial cuando Codex no pueda verificar los hallazgos, los comprobantes de revisión o las áreas de seguimiento.
- Incluye advertencias sobre cobertura incompleta y revisiones pospuestas en las exportaciones SARIF.

### Mantener visibles la configuración y el progreso de los análisis

- Guarda el modelo y el esfuerzo de razonamiento seleccionados junto con los análisis estándar y profundos para que el historial y el progreso de los análisis se mantengan coherentes al volver a cargar.
- Muestra cuántas revisiones independientes de análisis profundos están activas o completadas y cuándo comienza la consolidación de resultados.
- Adapta el descubrimiento de los análisis estándar a la capacidad disponible de los workers, manteniendo una sola lista de archivos incluidos en el alcance y una sola ronda de revisión de candidatos.

### Admitir más estructuras de repositorios y sistemas de archivos

- Incluye los repositorios Git anidados al capturar una instantánea del árbol de trabajo.
- Conserva las rutas literales de los archivos incluidos en el alcance y maneja las rutas de Windows que no distinguen entre mayúsculas y minúsculas.
- Durante la comprobación previa del análisis, expande el valor configurado de `CODEX_HOME` si comienza con `~`.

## 0.1.14 (28 de julio de 2026)

### Revisar el historial de análisis y los hallazgos recurrentes

- Filtra repositorios, hallazgos y el historial de análisis con un número limitado de resultados por página y detalles de estado más claros.
- Vuelve a ejecutar un análisis con su configuración guardada y compara los análisis completados para distinguir los hallazgos nuevos, persistentes, resueltos y no reanalizados.
- Agrupa los worktrees del mismo repositorio y usa identificadores estables de repositorios y hallazgos en todas las vistas.

### Definir la política de seguridad del repositorio

- Usa `$codex-security:define-security-policy` para revisar o actualizar las directrices con alcance definido de
`SECURITY.md` sobre límites de confianza, invariantes de seguridad, hallazgos que se pueden
  informar, gravedad, exclusiones y riesgo aceptado.
- Aplica el archivo de política más cercano, limita su tamaño y rechaza los enlaces simbólicos que apunten fuera del repositorio.

### Revisar los hallazgos antes de darles seguimiento

- Selecciona hasta 25 hallazgos de un análisis completado para darles seguimiento en Linear o en Issues de GitHub.
- Devuelve los hallazgos seleccionados a Codex para su revisión y aprobación en lugar de crear incidencias directamente desde el espacio de trabajo de hallazgos.

### Ejecutar análisis estándar con un flujo de trabajo más sencillo

- Usa una sola lista determinista de archivos incluidos en el alcance y un registro compacto de candidatos para los análisis estándar de repositorios y rutas con alcance definido.
- Conserva el archivo de manifiesto, los hallazgos, la cobertura, el informe y los resultados SARIF existentes mientras reduces las etapas repetidas del análisis.

## 0.1.13 (25 de julio de 2026)

### Revisar hallazgos en más entornos

- Conserva los hallazgos de seguridad reales cuando el código afectado sea local, interno, se use para entrenamiento o no esté desplegado en producción.
- Usa el contexto de despliegue y exposición para calibrar la gravedad y la confianza en lugar de suprimir automáticamente el hallazgo.

## 0.1.12 (23 de julio de 2026)

### Ejecutar análisis más profundos con un seguimiento más claro del progreso

- Ejecuta análisis profundos que coordinan workers en todo un repositorio o en un directorio seleccionado.
- Aplica tu configuración de modelo y razonamiento al trabajo de análisis delegado.
- Consulta los resultados de la comprobación previa, el progreso del análisis, la capacidad disponible de los workers y el comportamiento alternativo antes y durante un análisis.

### Revisar y volver a ejecutar análisis anteriores

- Abre los análisis actuales y anteriores desde la lista de análisis de seguridad.
- Vuelve a abrir un análisis guardado en el espacio de trabajo de hallazgos o ejecútalo de nuevo para actualizar los resultados.
- Consulta estados de finalización más claros y mayor coherencia en los detalles de los hallazgos y el historial de análisis.

### Configurar análisis con menos interrupciones

- Inicia análisis desde el flujo nativo de configuración sin salir de tu tarea actual.
- Mantén la configuración del análisis en el panel lateral, incluso cuando Codex esté en modo de pantalla completa.
- Cierra la configuración cuando no la necesites y conserva esa preferencia para los
análisis posteriores.

### Revisa y corrige los hallazgos validados

- Conserva los hallazgos validados de gravedad baja en los resultados finales.
- Revisa detalles más consistentes sobre los hallazgos en análisis, informes y exportaciones.
- Vuelve a intentar la corrección y conserva el contexto relevante del análisis para las correcciones posteriores.

### Exporta resultados para los flujos de trabajo de seguridad existentes

- Exporta los hallazgos finalizados en formato JSON, CSV o SARIF.
- Genera resultados SARIF localmente para integraciones con herramientas de análisis de código
y de seguridad.
- Mantén la coherencia de los detalles de los hallazgos en los distintos formatos exportados.

## 0.1.11 (10 de julio de 2026)

### Genera informes detallados de hallazgos y fortalecimiento de la seguridad

- Genera un informe de vulnerabilidad respaldado por el código fuente para cada hallazgo del análisis
que deba reportarse, con archivos de prueba de concepto de respaldo cuando estén disponibles.
- Revisa un portafolio de fortalecimiento estructural que analiza el conjunto completo de hallazgos,
las disyuntivas de ingeniería, las opciones de migración y los diagramas de respaldo.
- Usa `report.md` como punto de entrada a estos resultados derivados ubicados en `findings/`
  y `hardening/`. Conserva intacto el directorio completo del análisis al compartir o
  archivar los resultados.

### Ejecuta directamente los flujos de trabajo de generación de informes

- Usa `$codex-security:vulnerability-writeup` para convertir documentos de divulgación,
  hallazgos preliminares, PoCs y código fuente en informes bien elaborados, sin ejecutar
  primero un análisis de Codex Security.
- Usa `$codex-security:propose-security-hardening` para desarrollar opciones estructurales o arquitectónicas
  respaldadas por evidencia a partir de análisis, hallazgos, documentos de incidentes o
  evaluaciones y código fuente.

### Aplica de manera coherente las directrices y la cobertura del repositorio

- Define el contexto del modelo de amenazas, los invariantes de seguridad, los criterios
  para reportar hallazgos, las exclusiones y el contexto de gravedad en archivos `SECURITY.md`
  ubicados en la raíz o en directorios anidados. El archivo aplicable más cercano tiene prioridad.
- Mejora la cobertura de revisión del repositorio antes de la validación y conserva
las superficies cuya revisión se pospuso explícitamente y las brechas de evidencia.
- Revisa los archivos de código fuente eliminados en los análisis de cambios y amplía la cobertura
predeterminada de revisión del repositorio antes de la validación.
- Verifica las habilidades de las fases del análisis profundo, los procesos de trabajo delegados y su capacidad
antes de iniciar un análisis profundo.

## 0.1.10 (23 de junio de 2026)

### Mejora la recepción de tickets de Jira y Linear

- Solicita confirmación antes de importar subincidencias de Linear y conserva las relaciones
entre elementos principales y secundarios en los resultados.
- Distingue entre conexiones faltantes, permisos insuficientes, tickets inaccesibles
y fallas temporales del conector.
- Detén el proceso en lugar de emitir un veredicto cuando el contenido solicitado
del ticket no esté disponible.
- Asigna posiciones únicas con números enteros positivos a partir de `1` dentro de cada cola de elementos confirmados
  o pendientes de revisión.

### Revisa los cambios en el código de forma más confiable

- Compara un commit inspeccionado con su commit padre real y conserva el objetivo del diff
en el espacio de trabajo de hallazgos.
- Informa que el estado del parche no está disponible en lugar de revisar un cambio diferente.
- Revisa resultados de clasificación y contextos de hallazgos más consistentes.

## 0.1.9 (18 de junio de 2026)

### Revisa los análisis en el espacio de trabajo de hallazgos

- Revisa los análisis completados en un espacio de trabajo dedicado que reúne los hallazgos,
la cobertura, la gravedad, la confianza y los artefactos del análisis.
- Filtra y ordena los hallazgos, incluso de mayor a menor nivel de confianza, mientras
conservas el estado de tu espacio de trabajo durante las actualizaciones.
- Abre un hallazgo para revisar en un solo lugar la evidencia del código fuente, los detalles de validación,
la alcanzabilidad, el impacto y las recomendaciones de corrección.

### Ejecuta análisis con menos configuración

- Ejecuta análisis estándar en repositorios Git, carpetas individuales o
bases de código sin historial de Git. Los análisis profundos también pueden enfocarse en una carpeta específica.
- Cancela explícitamente un análisis activo, reanuda uno interrumpido sin que aparezca otro
prompt de configuración y recibe una advertencia antes de iniciar análisis profundos simultáneos.
- Consulta estados de configuración y progreso más claros, con resúmenes de progreso
más compactos y errores que permanecen visibles hasta que los atiendas.

### Exporta resultados portátiles y verificables

- Usa un formato uniforme para los análisis completados, con un archivo de manifiesto, hallazgos estructurados,
datos de cobertura y un informe en Markdown derivado del mismo resultado canónico.
- Exporta los hallazgos como JSON, CSV o SARIF para analizarlos, archivarlos e integrarlos
con otras herramientas de seguridad.
- Completa los análisis de forma más confiable, incluso cuando las rutas de Windows o el bloqueo de los análisis
afecten el acceso al sistema de archivos.

### Clasifica y da seguimiento a los hallazgos existentes

- Clasifica los hallazgos existentes provenientes de escáneres, avisos de seguridad, informes de programas de recompensas por la detección de errores,
GitHub, Jira, Linear o resultados de Codex Security con respecto a la base de código actual.
El flujo de trabajo de clasificación devuelve un veredicto respaldado por evidencia y una cola priorizada
de acciones.
- Da seguimiento en Linear, Jira o Issues de GitHub a los hallazgos validados que selecciones, o crea
un GitHub Security Advisory privado en borrador cuando el repositorio cumpla los
requisitos del aviso.
- Revisa las comprobaciones de duplicados, el contexto de origen, la visibilidad del destino y el
contenido exacto propuesto antes de aprobar una operación de escritura. Codex vuelve a leer el resultado
tras su creación o actualización para verificarlo.

## 0.1.7 (4 de junio de 2026)

### Realiza revisiones de seguridad respaldadas por evidencia

- Analiza un repositorio autorizado o una carpeta seleccionada para detectar
vulnerabilidades de seguridad.
- Ejecuta varias rondas de detección en todo un repositorio cuando necesites una
cobertura más exhaustiva.
- Revisa pull requests, commits, diferencias entre ramas y parches locales para detectar
regresiones de seguridad.
- Haz que cada candidato pase por las etapas de modelado de amenazas, detección de hallazgos, validación
y análisis de impacto antes de generar los informes del análisis.
- Corrige un hallazgo aceptado con un parche puntual, cobertura de pruebas de regresión y
verificación del problema original.
