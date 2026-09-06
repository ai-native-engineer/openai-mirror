<!-- source: https://learn.chatgpt.com/es-419/use-cases/qa-your-app-with-computer-use -->

## Introducción

Uso de la computadora es ideal para las sesiones de QA porque puede ver la interfaz, recorrer los flujos haciendo clic, escribir en los campos y registrar lo que falla. Esto permite detectar tanto errores funcionales como problemas de la interfaz de usuario durante recorridos de usuario realistas.

La clave es indicarle a Codex qué entorno debe probar, cuáles son los flujos más importantes y qué tipo de informe quieres que genere.

## Cómo usarlo

1. Instala el [complemento de Uso de la computadora](/es-419/codex/computer-use).
2. Indícale a Codex qué app, compilación o entorno debe probar.
3. Indica los flujos o casos de uso clave que más te importan.
4. Solicita un informe estructurado para facilitar la priorización o el traspaso de los resultados.

Puedes formular la solicitud en términos generales:

- `@Computer Test my app. Find any major issues and give me a report.`

O puedes ser más específico:

- `@Computer Test my app in staging. Cover signup, invite a teammate, and upgrade billing. Log every bug with repro steps, expected result, actual result, and severity.`

Si ya mantienes un archivo con el plan de pruebas en el repositorio, adjúntalo al chat o indícale a Codex dónde encontrarlo para que la sesión de QA siga tus flujos actuales.

## Consejos prácticos

### Detalla la configuración

Si el estado de la cuenta, los datos de prueba, los flags de funcionalidades o la elección del entorno afectan el flujo, incluye esa información desde el principio. Codex dará resultados mucho mejores si sabe si las pruebas son locales, de preproducción o en condiciones similares a las de producción.

### Indica qué tipos de problemas te interesan

Especifica si quieres que Codex se centre en funcionalidades que no funcionan, problemas de diseño, textos confusos, regresiones visuales o todo lo anterior.

### Decide si detener o continuar la ejecución

Si un solo problema que bloquee el flujo debe poner fin a la ejecución, indícalo. De lo contrario, dile a Codex que continúe con el resto del flujo y recopile todos los problemas que no lo bloqueen antes de resumirlos.

## Siguientes pasos recomendados

Después de la sesión de QA, mantén abierto el mismo chat y pídele a Codex que corrija uno de los errores que encontró, convierta los hallazgos en borradores listos para Linear o GitHub, o centre la siguiente sesión en un flujo específico que esté fallando.

## Prompt sugerido

**Realiza una sesión estructurada de QA**
