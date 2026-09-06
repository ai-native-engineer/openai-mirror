<!-- source: https://learn.chatgpt.com/es-419/docs/third-party/github -->

Usa la revisión de código de Codex para realizar una revisión adicional centrada en hallazgos relevantes en los pull
requests de GitHub. Codex revisa el diff del pull request, sigue las pautas de tu repositorio
y publica una revisión de código estándar en GitHub centrada en problemas graves. La Revisión
de seguridad, disponible en versión preliminar de investigación, ofrece un análisis más profundo de
los posibles problemas de seguridad en un pull request.

<br />

## Antes de comenzar

Asegúrate de contar con:

- [Codex Cloud](/es-419/codex/cloud) configurado para el repositorio que quieres revisar.
- Acceso a la [configuración de revisión de código de Codex](https://chatgpt.com/codex/settings/code-review).
- Un archivo `AGENTS.md` si quieres que Codex siga pautas de revisión específicas del repositorio.

## Configurar la revisión de código de Codex

Para configurar las revisiones automáticas, necesitas un repositorio de GitHub conectado y
permisos de push o de administrador en GitHub para modificar su configuración.

1. Configura [Codex Cloud](/es-419/codex/cloud).
2. Ve a la [configuración de Codex](https://chatgpt.com/codex/settings/code-review).
3. Activa **Revisión de código** para tu repositorio.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Solicitar una revisión de Codex

1. En un comentario del pull request, menciona `@codex review`.
2. Espera a que Codex reaccione (👀) y publique una revisión.

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex publica una revisión en el pull request, tal como lo haría alguien de tu equipo. En
GitHub, Codex solo señala problemas P0 y P1 para que los comentarios de revisión se centren en
los riesgos de alta prioridad.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Activar las revisiones automáticas

Si quieres que Codex revise automáticamente cada pull request, activa
**Revisiones automáticas** en la [configuración de Codex](https://chatgpt.com/codex/settings/code-review).
Codex publicará una revisión cada vez que alguien abra un nuevo PR para revisión, sin
tener que incluir un comentario con `@codex review`.

## Personalizar lo que revisa Codex

Codex busca archivos `AGENTS.md` en tu repositorio y sigue las reglas aplicables de
revisión de código. Agrega una sección `## Code Review Rules` al archivo más cercano
al código al que se aplican las reglas. Usa encabezados `###` para agrupar verificaciones relacionadas cuando
resulte útil.

Por ejemplo, un servicio de generación de informes de experimentos puede evitar que el comportamiento posterior a la exposición
altere una cohorte de comparación:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Coloca las reglas de todo el repositorio en el archivo `AGENTS.md` de la raíz y las reglas específicas del servicio
en un archivo anidado, como `services/experiment_reporting/AGENTS.md`. Codex
aplica las pautas del archivo raíz y las pautas más específicas que correspondan a cada archivo modificado, para que
los cambios no relacionados no tengan que incluir contexto específico del servicio.

Comienza con dos o tres reglas concisas que incorporen verificaciones que los revisores suelen explicar. Reglas útiles:

- **Céntrate en comportamientos de alto impacto específicos del repositorio.** Describe la
  restricción de compatibilidad, el límite de datos o el efecto secundario inseguro que se debe señalar y
  por qué es importante.
- **Indica la alternativa segura o la excepción.** Proporciona a Codex suficiente contexto para distinguir
  un problema real del comportamiento esperado.
- **Mantén las reglas acotadas y duraderas.** Prefiere describir resultados en lugar de nombres de funciones que
  pueden cambiar y coloca las pautas cerca del código al que se aplican.
- **Deja las verificaciones mecánicas en CI.** Excluye el formato, el lint y otras
  verificaciones deterministas de las reglas de revisión.

Abre un pull request representativo y solicita una revisión con `@codex review`.
Ajusta las reglas según los hallazgos y comentarios que observes; acota o
elimina las pautas que generen ruido.

Las reglas de revisión de código orientan a Codex; no sustituyen las pruebas, las protecciones de rama ni
las aprobaciones obligatorias.

Para enfocarte en un aspecto específico solo una vez, agrégalo al comentario de tu pull request:

`@codex review for issues in the database migration`

## Revisión de seguridad

La Revisión de seguridad es una revisión adicional para los clientes que quieren
prestar especial atención a los problemas de seguridad en los pull requests. Ofrece un análisis de los riesgos específicos de seguridad más profundo
que el de la Revisión de código al analizar el diff del pull request,
el contexto pertinente del repositorio y los modelos de amenazas configurados o las pautas de
seguridad configuradas.

La Revisión de código también puede identificar problemas de seguridad como parte de su revisión
general, por lo que puedes encontrar coincidencias ocasionales entre los hallazgos de la Revisión de código y la Revisión
de seguridad.

### Configurar la Revisión de seguridad

Para obtener instrucciones y opciones de configuración más detalladas, consulta [Revisión de
seguridad](/es-419/codex/security/security-review).

1. Configura [Codex Cloud](/es-419/codex/cloud).
2. Ve a la [configuración de Codex](https://chatgpt.com/codex/settings/code-review).
3. En **Preferencias del repositorio**, elige a qué pull requests se les aplicará la Revisión de
   seguridad y cuándo se ejecutará. Selecciona **Siempre que se ejecute la revisión de código** para ejecutarla
   junto con la Revisión de código.

### Solicitar una Revisión de seguridad

Para solicitar manualmente una Revisión de seguridad, agrega este comentario a un pull request:

`@codex security review`

Codex reacciona mientras se ejecuta la revisión y luego publica los hallazgos de seguridad directamente
en el pull request. Abre la tarea de Codex asociada y selecciona la pestaña **Informe de
seguridad** para ver el informe completo.

## Abordar los hallazgos de la revisión

Después de que Codex publique una revisión, puedes pedirle que corrija los problemas en el mismo pull
request mediante otro comentario:

```md
@codex fix the P1 issue

Codex inicia un chat en la nube con el pull request como contexto y puede enviar una corrección
a la rama cuando tenga permiso para hacerlo.

## Asignar otras tareas a Codex

Si mencionas `@codex` en un comentario con cualquier texto distinto de `review`, Codex inicia un [chat en la nube](/es-419/codex/cloud) con tu pull request como contexto.

```md
@codex fix the CI failures

## Solucionar problemas con la revisión de código

Si Codex no reacciona ni publica una revisión:

- Confirma que activaste **Revisión de código** para el repositorio en la [configuración de Codex](https://chatgpt.com/codex/settings/code-review).
- Confirma que el pull request pertenece a un repositorio con [Codex Cloud](/es-419/codex/cloud) configurado.
- Usa el activador exacto `@codex review` en un comentario del pull request.
- Para las revisiones automáticas, comprueba que activaste **Revisiones automáticas** y que
  el evento del pull request coincide con la configuración del activador de revisión.
