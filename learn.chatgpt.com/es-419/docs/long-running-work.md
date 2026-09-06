<!-- source: https://learn.chatgpt.com/es-419/docs/long-running-work -->

Para el trabajo que puede requerir muchos pasos, proporciona a ChatGPT un resultado claro, las restricciones
y una definición de cuándo se considera terminado. Mantén el trabajo relacionado en el mismo chat para que
ChatGPT pueda usar el mismo contexto para elegir el siguiente paso y determinar cuándo
se completó el trabajo.

En la aplicación de escritorio de ChatGPT, ingresa `/goal` para iniciar el modo Objetivo. La fila de progreso
te permite pausar, reanudar, editar o eliminar el objetivo mientras ChatGPT trabaja.

Para el trabajo de larga duración alojado en la versión web de ChatGPT, usa ChatGPT Work e incluye el
resultado, las restricciones y los criterios de revisión directamente en tu prompt.

Continúa en el mismo chat web para agregar contexto, cambiar las restricciones o
pedir una actualización de estado. Usa chats separados cuando las tareas independientes puedan ejecutarse en
paralelo y evita otorgar a dos tareas acceso de escritura a la misma fuente conectada.
Para el trabajo relacionado, mantén juntos los chats y los archivos fuente en un
[proyecto](/es-419/codex/projects).

En una sesión interactiva de Codex CLI, ingresa `/goal` para iniciar el modo Objetivo. Continúa
en la misma sesión para orientar el trabajo o pedir una actualización de estado.

En el chat de la extensión para IDE, ingresa `/goal` para iniciar el modo Objetivo en el
espacio de trabajo abierto. Continúa en el mismo chat para orientar la tarea mientras se ejecuta.

  
    
  

<a id="start-a-goal"></a>
<a id="define-what-done-means"></a>
<a id="steer-a-running-goal"></a>
<a id="run-goals-in-parallel"></a>
<a id="related-docs"></a>

## Iniciar un objetivo

Escribe `/goal` en la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE. El
texto del objetivo se convierte tanto en el primer prompt como en los criterios de finalización de la
tarea.

Si el resultado aún no está claro, comienza con `/plan`. Pide a ChatGPT que te entreviste,
identifique las restricciones y convierta el resultado en un objetivo con criterios de éxito
medibles. Luego, inicia el objetivo mejor definido con `/goal`.

## Definir qué significa completar el trabajo

Escribe un objetivo que permita a ChatGPT verificar su propio progreso. Incluye estos tres elementos cuando
sean pertinentes:

| Elemento del objetivo     | Qué incluir                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **Resultado**      | Describe el resultado que quieres, no solo la actividad que ChatGPT debe realizar.   |
| **Restricciones**  | Indica las herramientas necesarias, los límites, los requisitos de compatibilidad o los enfoques que deben evitarse. |
| **Verificación** | Agrega pruebas, mediciones o criterios de revisión que demuestren que se completó el trabajo.  |

Por ejemplo:

```text
Migrate this codebase from JavaScript to TypeScript. Preserve existing behavior,
compile in strict mode without explicit `any` types, and make the full test suite pass.

## Orientar un objetivo en curso

En la aplicación de escritorio de ChatGPT, la fila de progreso del objetivo aparece sobre el editor. Úsala para
pausar o reanudar el trabajo, editar el objetivo o eliminarlo. También puedes enviar mensajes de
seguimiento mientras el objetivo está en curso para agregar contexto o ajustar las restricciones.

Usa un chat secundario cuando quieras un resumen del estado o una explicación sin
interrumpir el chat principal. Si prevés perder la
conectividad, pausa el objetivo antes de que ocurra y reanúdalo cuando quieras que ChatGPT continúe.

<a id="steer-a-running-task"></a>

## Orientar el trabajo en curso

Continúa en el mismo chat para agregar contexto, ajustar las restricciones o pedir
un resumen del estado. Inicia otro chat cuando una tarea distinta pueda ejecutarse
de forma independiente.

## Orientar un objetivo en curso

Envía un mensaje de seguimiento en la misma sesión interactiva para agregar contexto o
ajustar las restricciones. Pide un resumen del estado cuando quieras que Codex resuma el
progreso antes de que continúe.

## Orientar un objetivo en curso

Continúa en el mismo chat del IDE para agregar contexto, ajustar las restricciones o pedir un
resumen del estado. Mantén disponible el espacio de trabajo mientras el objetivo esté en curso.

Al iniciar un objetivo, ChatGPT no obtiene más acceso. Conserva el mismo
[sandbox y la misma política de aprobación](/es-419/codex/sandboxing) y se pone en pausa cuando
necesita una decisión. Con las [revisiones automáticas
de aprobación](/es-419/codex/sandboxing/auto-review), un revisor distinto puede
evaluar las solicitudes que cumplan los requisitos sin ampliar esos límites.

## Ejecutar objetivos en paralelo

Cada chat conserva su propio contexto, mensajes, resultados y objetivo. Ejecuta los chats
de forma simultánea, pero evita que dos chats modifiquen los mismos archivos. Usa
[worktrees](/es-419/codex/environments/git-worktrees) para que los chats de programación en paralelo tengan copias de trabajo
separadas.

Para el trabajo local, activa **Evitar el reposo durante la ejecución** en Configuración para que tu Mac
no entre en reposo. Usa [Mascotas](/es-419/codex/pets?surface=app) o las [notificaciones
del sistema](/es-419/codex/notifications?surface=app) para saber cuándo un chat necesita que intervengas
o está listo para revisión.

## Documentación relacionada

- [Proyectos y chats](/es-419/codex/projects)
- [Modo Objetivo y diseño de prompts](/es-419/codex/prompting#goal-mode)
- [Worktrees de Git](/es-419/codex/environments/git-worktrees)

## Documentación relacionada

- [Proyectos y chats](/es-419/codex/projects)
- [Tareas programadas](/es-419/codex/automations)
- [Sandbox y permisos](/es-419/codex/sandboxing)
