<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/fix-findings -->

Usa Codex Security para convertir un hallazgo de seguridad aceptado en un parche específico y
verificado. Puedes trabajar en el entorno de trabajo de seguridad o ejecutar el flujo de
corrección desde un prompt, la línea de comandos o CI/CD. Codex valida el problema
y, cuando las pruebas son seguras y viables, agrega una prueba de regresión específica que
falla antes de la corrección y pasa después de aplicarla. También comprueba que el comportamiento
legítimo siga funcionando. Si una prueba de regresión no es segura o viable, Codex
registra la brecha de evidencia y proporciona el artefacto de validación repetible
más sólido en su lugar.

Comienza con un hallazgo aceptado y revisa el parche propuesto y la evidencia de
verificación. Si el flujo cumple con tus estándares, procesa los demás hallazgos
aceptados de uno en uno en tareas de Codex o jobs de CI/CD independientes. Limitar el alcance de cada tarea
facilita la revisión de sus cambios en el código y su evidencia.

## Corregir un hallazgo en la interfaz

Abre un hallazgo aceptado en **Hallazgos** o un análisis completado en **Análisis**.
Revisa su evidencia y, luego, usa **Parche** para generar, revisar, aplicar y verificar
una corrección específica.

1. Genera un parche específico

   Abre el hallazgo, selecciona la pestaña **Parche** y selecciona **Generar parche**.
   Cuando sea viable, Codex valida o reproduce el problema y crea un artefacto de parche
   sin modificar el checkout seleccionado.

2. Revisa el diff propuesto

   Revisa todos los archivos fuente, todas las pruebas de regresión y todos los artefactos de validación modificados. Rechaza
las refactorizaciones amplias, las tareas de limpieza no relacionadas o los cambios que debiliten otro
control de seguridad.

3. Aplica el parche localmente

   Selecciona **Aplicar parche** solo cuando el diff sea aceptable. Codex aplica exactamente el
   parche generado al árbol de trabajo y registra ese estado. Revisa el diff del
   árbol de trabajo antes de continuar.

4. Verifica la corrección

   Selecciona **Verificar corrección**. Codex vuelve a ejecutar el caso de reproducción original o la comprobación de explotación más sólida
   disponible. Si una prueba de regresión es segura y viable, Codex
   comprueba que falle antes de la corrección y pase después de aplicarla. Si la prueba no es
   segura o viable, Codex registra la brecha de evidencia y proporciona en su lugar el
   artefacto de validación repetible más sólido. También comprueba
   el comportamiento legítimo, las evasiones relacionadas y las pruebas pertinentes del repositorio.

5. Cierra el hallazgo de forma deliberada

   La verificación no cierra automáticamente un hallazgo. Revisa los comandos,
los resultados y la brecha de evidencia restante; luego, cierra el hallazgo con un motivo
preciso o mantenlo abierto para seguir trabajando.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revisa la corrección de seguridad generada antes de aplicarla a tu checkout.
  </figcaption>
</figure>

## Corregir un hallazgo desde la CLI

Usa la CLI de Codex para un hallazgo aceptado proveniente de un análisis, ticket, aviso de seguridad,
divulgación, evaluación de seguridad o revisión interna.

Instala Codex Security en el `CODEX_HOME` que usa `codex exec` antes de
ejecutar estos comandos. Un runner de CI nuevo no incluye complementos del Marketplace de forma
predeterminada.

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

Incluye la fuente y el sumidero conocidos, la entrada del atacante, el impacto, el invariante esperado,
el caso de reproducción, los archivos afectados y el comando de validación. Codex puede inspeccionar el
repositorio para obtener los detalles técnicos que falten. Debería preguntar antes de dar por supuesta una
política del producto o un invariante de seguridad previsto.

Para una ejecución automatizada, haz checkout del código, deja disponible el informe del hallazgo
e instala el complemento en el `CODEX_HOME` del runner. Luego, habilita la escritura en el espacio de trabajo
y pasa el prompt a `codex exec`:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## Analizar y corregir hallazgos en CI/CD

Instala Codex Security en el `CODEX_HOME` del runner antes de invocar cualquiera de las dos
habilidades. Los comandos siguientes usan el complemento instalado; no lo instalan.

En CI/CD, separa el análisis de cambios de la corrección y exige que el análisis
deje el checkout sin cambios. Conserva el directorio del análisis completado como artefacto del
job, revisa los hallazgos e inicia una tarea de Codex o un job por separado para cada
hallazgo aceptado para corrección.

De forma predeterminada, `codex exec` usa un sandbox de solo lectura. Ejecuta tanto el análisis de cambios como
la corrección con `--sandbox workspace-write`. El análisis necesita ese permiso
para guardar artefactos temporales, pero su prompt debe seguir exigiendo `Do not modify
the checkout`. La corrección necesita el mismo permiso para escribir
el parche específico y la evidencia de verificación. Consulta [Permisos y
seguridad](/es-419/codex/non-interactive-mode#permissions-and-safety).

Para cada análisis y cada hallazgo aceptado:

1. Determina las revisiones base y head del cambio.
2. Ejecuta `$codex-security:security-diff-scan` sobre ese diff sin modificar
   el checkout.
3. Conserva el directorio completo del análisis y selecciona los hallazgos que quieras corregir.
4. Invoca `$codex-security:fix-finding` una vez por cada hallazgo aceptado y pasa
   su ID de hallazgo y el directorio del análisis completado.
5. Genera un solo parche específico y agrega una prueba de regresión que falle antes de la
corrección y pase después de aplicarla. Si esa prueba no es segura o viable, registra la
brecha de evidencia y usa en su lugar el artefacto de validación repetible más sólido.
6. Verifica el problema original y el comportamiento legítimo. Devuelve cada parche, prueba
o artefacto de validación alternativo, comando de verificación y cualquier brecha de evidencia
de forma independiente.

Primero, analiza el cambio sin modificar el checkout:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

Luego, corrige un hallazgo aceptado a partir del análisis completado:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

Repite el segundo comando en una tarea independiente o un job independiente para cada
hallazgo aceptado restante. Después de la verificación, integra cada parche mediante tu proceso habitual
de revisión de código y lanzamiento. Para transferir los hallazgos a otro equipo antes de la
corrección, consulta [Exportar o dar seguimiento a los
hallazgos](/es-419/codex/security/plugin/export-findings).
