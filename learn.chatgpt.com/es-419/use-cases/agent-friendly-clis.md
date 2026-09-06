<!-- source: https://learn.chatgpt.com/es-419/use-cases/agent-friendly-clis -->

## Introducción

Cuando Codex trabaja repetidamente con la misma API, fuente de registros, bandeja de entrada exportada, base de datos local o script del equipo, proporciona una interfaz componible para ese trabajo: un comando que pueda ejecutar desde cualquier carpeta, cuyos resultados pueda inspeccionar y acotar, y que pueda combinar con `git`, `gh`, `rg`, pruebas y scripts del repositorio.

Agrega una habilidad complementaria que registre cuándo Codex debe usar la CLI, qué debe ejecutar primero, cómo mantener breve la salida, dónde se guardan los archivos descargados y qué comandos de escritura requieren aprobación.

En este flujo de trabajo, `$cli-creator` ayuda a Codex a crear el comando. `$skill-creator` ayuda a Codex a guardar una habilidad reutilizable, como `$ci-logs`, que se puede invocar por nombre en tareas futuras.

## Cómo usar

1. [Decide si la tarea necesita una CLI](#choose-what-the-cli-should-do)
2. [Comparte la fuente de la que Codex debe aprender](#share-the-docs-files-or-commands)
3. [Ejecuta `$cli-creator`](#ask-codex-to-build-the-cli-and-skill)
4. [Prueba el comando instalado](#verify-the-command-works-from-any-folder)
5. [Invoca la habilidad guardada más adelante](#use-the-skill-later)

## Elige qué debe hacer la CLI

Empieza por lo que quieres que haga Codex, no por la tecnología en la que quieres que lo programe. Una buena CLI convierte una operación recurrente de lectura, búsqueda, descarga, exportación, creación de borradores, carga, consulta de estado o escritura segura en un comando que Codex puede ejecutar desde cualquier repositorio.

| Situación                                              | Qué puede hacer Codex con la CLI                                                                                              |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Solo se puede acceder a los registros de CI a través de una página de compilación.**                  | Aceptar una URL de compilación, descargar en `./logs` los registros de los trabajos fallidos y devolver las rutas de los archivos junto con fragmentos breves.                          |
| **Los tickets de soporte llegan en una exportación semanal.**         | Indexar la exportación CSV o JSON más reciente, hacer búsquedas por cliente o frase y leer un ticket por su ID estable.                        |
| **Una respuesta de una API es demasiado grande para caber en el contexto.**          | Enumerar solo los campos que necesita, leer el objeto completo por ID y exportar la respuesta completa a un archivo.                      |
| **Una exportación de Slack contiene hilos largos.**                   | Buscar con `--limit`, leer un hilo y devolver el contexto cercano en vez de todo el archivo.                             |
| **Un script del equipo ejecuta cuatro pasos distintos.**           | Dividir la configuración, el descubrimiento, la descarga, la creación de borradores, la carga, la consulta de estado y la escritura en vivo en comandos separados.                               |
| **Un complemento encuentra el registro, pero Codex necesita un archivo.** | Seguir usando el complemento en el chat; usar una CLI para descargar el archivo adjunto, la traza, el informe, el video o el paquete de registros y devolver la ruta. |

## Comparte la documentación, los archivos o los comandos

Codex necesita algo concreto de lo cual aprender: documentación o una especificación OpenAPI, un comando curl con la información confidencial eliminada, una ruta de exportación o base de datos, una carpeta de registros o un script existente. Si quieres que la CLI siga un estilo conocido, pega una salida breve de `--help` generada por `gh`, `kubectl` o la propia herramienta de tu equipo.

Si el comando necesita autenticación, indícale a Codex el nombre de la variable de entorno, la ruta del archivo de configuración o el flujo de inicio de sesión que debe admitir. Configura tú mismo el secreto en tu shell o archivo de configuración. No pegues secretos en el chat. Pídele a Codex que la comprobación de configuración de la CLI muestre un error claro cuando falte la autenticación.

## Pídele a Codex que cree la CLI y la habilidad

Usa el prompt inicial de esta página. Indica la fuente de la que Codex debe aprender y la primera tarea que la CLI debe admitir.

Antes de que Codex escriba código, debe mostrar la interfaz de comandos propuesta y preguntar solo por los detalles faltantes que impedirían crearla.

## Verifica que el comando funcione desde cualquier carpeta

Codex no debe detenerse tras ejecutar `cargo run`, `python path/to/script.py` o un comando de un paquete que no esté instalado. Pídele que pruebe el comando instalado desde otro repositorio o una carpeta temporal, tal como se usaría en una tarea posterior.

**Prueba la CLI como lo haría un agente en el futuro**

Si Codex devuelve un bloque JSON enorme, pídele que acote la respuesta predeterminada y agregue la opción de exportar las cargas útiles completas a un archivo. Si olvida el límite de aprobación, pídele que actualice la habilidad complementaria antes de usarla en otra tarea.

## Usa la habilidad más adelante

Cuando vuelvas a necesitar la CLI, invoca la habilidad en vez de volver a pegar la documentación:

Para trabajos recurrentes, prueba la habilidad una vez en un chat y luego pídele a Codex que [programe una tarea para esa misma invocación desde el chat](/es-419/codex/automations#schedule-a-task-inside-a-chat).
