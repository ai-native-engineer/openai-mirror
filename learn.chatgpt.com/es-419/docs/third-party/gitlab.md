<!-- source: https://learn.chatgpt.com/es-419/docs/third-party/gitlab -->

Usa la revisión de código de Codex para obtener una revisión adicional centrada en lo importante de las solicitudes de fusión de GitLab. Codex analiza el diff de la solicitud de fusión, sigue las pautas de tu repositorio y publica una revisión de código estándar de GitLab enfocada en problemas graves.

La compatibilidad con GitLab está en fase beta y se encuentra disponible en todos los planes de ChatGPT. La integración de Codex
se ejecuta en Codex Cloud. Los controles de repositorio similares a los de GitHub en la
app de escritorio, como **Crear Pull Request**, no están incluidos en esta versión beta.

## Antes de comenzar

Asegúrate de tener:

- Una cuenta de GitLab conectada. GitLab.com requiere el
[flujo de conexión estándar](https://help.openai.com/articles/20001486);
  las instancias de GitLab autogestionado o GitLab Dedicated requieren la
[configuración de una plantilla por parte de un administrador del espacio de trabajo](https://help.openai.com/articles/20001487).
- Un archivo `AGENTS.md` si quieres que Codex siga las pautas de revisión
  específicas del repositorio.

## Configura la revisión de código de Codex

### Configura la conexión con GitLab y la identidad de revisión de Codex

Para GitLab.com, conecta tu cuenta de GitLab en Codex una vez que te hayas
[conectado a GitLab en ChatGPT](https://help.openai.com/articles/20001486).
En GitLab autogestionado o GitLab Dedicated, cada revisor debe conectarse después de que la
[plantilla del administrador del espacio de trabajo](https://help.openai.com/articles/20001487) haya sido
publicada.

Para GitLab autogestionado o GitLab Dedicated, abre **Codex Cloud** → **Configuración** →
[**Conectores**](https://chatgpt.com/codex/cloud/settings/connectors). Un
administrador del espacio de trabajo puede permitir que Codex cree una cuenta de servicio o guardar el token de acceso personal de una cuenta
de servicio existente.

#### Permite que Codex cree la cuenta

En **Codex Cloud** → **Configuración** → **Conectores**, selecciona la app correspondiente a tu
host de GitLab autogestionado o GitLab Dedicated → selecciona **Configurar cuenta de servicio** →
**Crear una cuenta de servicio**. El administrador del espacio de trabajo que complete la configuración debe tener
acceso de administrador a la instancia de GitLab. Elige **Grupos seleccionados**
o **Solo proyectos seleccionados**, selecciona dónde debe operar Codex y crea
la cuenta. La opción de grupos otorga acceso Developer a cada grupo seleccionado,
y sus proyectos y subgrupos lo heredan; la opción de proyectos otorga acceso Developer
solo a los proyectos individuales que selecciones. Codex creará la cuenta de servicio de instancia ChatGPT
Codex Connector con un token de acceso personal con el alcance
`api`.

#### Usa una cuenta existente

En GitLab, crea o elige una cuenta de servicio y concédele acceso Developer
solo en los grupos o proyectos donde debe operar Codex. En la página **Cuentas
de servicio** , selecciona la cuenta → **Administrar tokens de acceso** → **Agregar un
token nuevo** para
[crear un token de acceso personal](https://docs.gitlab.com/user/profile/service_accounts/#create-a-personal-access-token-for-a-service-account)
con el alcance `api` y una fecha de vencimiento dentro de 30 días o más. Regresa a
Codex, elige **Usar una cuenta de servicio existente**, pega el token y selecciona
**Guardar token**. El token se cifra cuando se guarda y nunca vuelve a mostrarse.

#### Administra el token de la cuenta de servicio

Los administradores del espacio de trabajo pueden gestionar la cuenta de servicio en **Codex Cloud** →
**Configuración** → **Conectores**. Si Codex creó la cuenta, los administradores pueden revocar
el token actual y generar uno nuevo. Si la cuenta ya existía, pueden
reemplazar o eliminar el token guardado en Codex y revocarlo por separado
en GitLab si es necesario. Codex no puede responder a la actividad de GitLab hasta que se haya
configurado un token válido.

### Elige cómo llega a Codex la actividad de GitLab

#### Crea un entorno de proyecto para tareas de programación o la configuración específica del proyecto

En **Codex Cloud** → **Configuración** → **Entornos**, selecciona el proyecto de GitLab
y crea un entorno de proyecto cuando quieras que Codex escriba o ejecute código
para ese proyecto —por ejemplo, para editar archivos, hacer commit de los cambios o enviar actualizaciones a
la rama de una solicitud de fusión— o cuando una revisión dependa de secretos específicos del proyecto,
acceso a la red o comandos de configuración.

En GitLab.com, también se requiere un entorno de proyecto para habilitar las revisiones de Codex.

Mientras creas el entorno, activa **Habilitar la actividad de Codex desde GitLab**
para instalar el webhook del proyecto que envía a Codex eventos de solicitudes de fusión, comentarios e
incidencias. Para crear el webhook del proyecto, se requiere acceso Maintainer u Owner,
acceso de administrador o un rol personalizado con permisos para administrar los webhooks
del proyecto. Los webhooks firmados de proyectos y grupos requieren GitLab 19.0 o una versión posterior. En
GitLab 19.0 autogestionado, confirma que el indicador de función `webhook_signing_token` esté
habilitado; está habilitado de forma predeterminada y se eliminó en GitLab 19.1.

#### Habilita la actividad de revisiones de Codex para los proyectos de un grupo de GitLab

En GitLab autogestionado o GitLab Dedicated, los administradores del espacio de trabajo pueden abrir **Entornos**
→ **Actividad de GitLab** → **Administrar grupos** para habilitar las revisiones de Codex en un grupo
y sus subgrupos. Codex instalará un webhook de grupo que abarcará los proyectos
de todo ese grupo. El usuario de GitLab conectado debe tener el rol Owner del grupo, y los
webhooks de grupo requieren GitLab Premium o Ultimate y GitLab 19.0 o una versión posterior.

La actividad de grupo habilita las revisiones de código, pero no crea entornos de proyecto. Para ejecutar tareas de programación activadas desde GitLab, como editar archivos, ejecutar comandos, hacer commit de los cambios o enviar actualizaciones a una solicitud de fusión, crea un entorno de proyecto.

### Configura las políticas de revisión de código

Configura las políticas de revisión de código en la
[configuración de revisiones de Codex](https://chatgpt.com/codex/cloud/settings/code-review?provider=gitlab).
Elige la política del repositorio: `Review my MRs`, `Review team MRs`,
`Review all MRs` o `Follow personal`. Luego, elige entre **Al abrir una MR**,
**Con cada push** o **Activador inteligente (experimental)** para definir cuándo se ejecutan las revisiones. La configuración del repositorio puede
prevalecer sobre los valores predeterminados personales.

## Solicita una revisión de Codex

1. En un comentario de la solicitud de fusión, menciona `@codex review`.
2. Espera a que Codex reaccione (👀) y publique una revisión.

Codex publica discusiones y notas de GitLab en la solicitud de fusión, como lo haría un compañero de equipo. De forma predeterminada, las revisiones solicitadas manualmente pueden incluir hallazgos P0, P1 y P2, mientras que las revisiones automáticas se centran en hallazgos P0 y P1.

## Habilita las revisiones automáticas

Para revisar automáticamente las solicitudes de fusión que cumplan los requisitos, activa **Revisiones
automáticas** en la configuración de Codex, elige la política del repositorio de GitLab y selecciona un
activador entre **Al abrir una MR**, **Con cada push** o **Activador inteligente (experimental)**.
Codex se ejecuta sin un comentario `@codex review` cuando el evento de la solicitud de fusión
coincide con esa política y ese activador.

La actividad de GitLab debe estar habilitada mediante un webhook de proyecto o de un grupo antecesor. En GitLab autogestionado o GitLab Dedicated, la cuenta de servicio configurada también debe tener acceso para escribir en el proyecto. Codex utiliza un entorno de proyecto configurado cuando está disponible. Si un grupo antecesor ya tiene la actividad habilitada, los proyectos descendientes heredan esa cobertura.

## Personaliza lo que revisa Codex

Codex busca archivos `AGENTS.md` en tu repositorio y sigue las reglas de revisión de código
correspondientes. Agrega una sección `## Code Review Rules` al archivo más cercano
al código al que se aplican esas reglas. Usa encabezados `###` para agrupar verificaciones relacionadas cuando
resulte útil.

Por ejemplo, un servicio de informes de experimentos puede evitar que el comportamiento posterior a la exposición modifique una cohorte de comparación:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Coloca las reglas de todo el repositorio en el archivo `AGENTS.md` de la raíz y las reglas específicas del servicio en
un archivo anidado, como `services/experiment_reporting/AGENTS.md`. Codex aplica
las pautas de la raíz y las más específicas que correspondan a cada archivo modificado, de modo que los
cambios no relacionados no tengan que incluir contexto específico del servicio.

Comienza con dos o tres reglas concisas que definan las verificaciones que los revisores suelen explicar. Reglas útiles:

- **Concéntrate en comportamientos importantes y específicos del repositorio.** Describe la
  restricción de compatibilidad, el límite de datos o el efecto secundario inseguro que se debe señalar y
  explica por qué es importante.
- **Indica la alternativa segura o la excepción.** Da a Codex contexto suficiente para distinguir
  un problema real del comportamiento esperado.
- **Mantén las reglas acotadas y duraderas.** Prioriza los resultados sobre los nombres de funciones que
  pueden cambiar y coloca las pautas cerca del código al que se aplican.
- **Deja las verificaciones mecánicas en CI.** Excluye de las reglas de revisión el formato, el lint y otras
  verificaciones deterministas.

Abre una solicitud de fusión representativa y solicita una revisión con `@codex review`.
Perfecciona las reglas según los hallazgos y los comentarios recibidos, y acota o
elimina las pautas que generen ruido.

Las reglas de revisión de código orientan a Codex; no reemplazan las pruebas, las protecciones de las ramas ni las aprobaciones obligatorias.

Para centrarte en un aspecto puntual, agrégalo al comentario de tu solicitud de fusión:

`@codex review for issues in the database migration`

## Atiende los hallazgos de la revisión

Para corregir los hallazgos de la revisión, se necesita un **entorno de proyecto configurado**; la actividad de
grupo, por sí sola, permite realizar revisiones, pero no ejecutar tareas de programación. Si el proyecto tiene
un entorno, pídele a Codex que corrija un problema en la misma solicitud de fusión dejando
otro comentario:

```md
@codex fix the P1 issue

Codex inicia un [chat en la nube](/es-419/codex/cloud) con la solicitud de fusión como contexto y
puede enviar una corrección a la rama cuando tenga permiso para hacerlo.

## Asígnale otras tareas a Codex

Otras tareas de programación también requieren un **entorno de proyecto configurado**; la actividad de
grupo, por sí sola, permite realizar revisiones. Si mencionas a `@codex` en un comentario con
cualquier texto distinto de `review`, Codex inicia un [chat en la nube](/es-419/codex/cloud) usando
tu solicitud de fusión como contexto.

```md
@codex fix the CI failures

## Soluciona problemas con la revisión de código

Si Codex no reacciona ni publica una revisión:

- Confirma que esté seleccionada la app de GitLab prevista; si usas una configuración específica del proyecto, confirma que este tenga el entorno de Codex Cloud previsto.
- Confirma que haya actividad para el proyecto o un grupo antecesor. En GitLab, revisa
**Webhooks** →
[**Eventos recientes**](https://docs.gitlab.com/user/project/integrations/webhooks/)
  y comprueba que los eventos de solicitudes de fusión y notas se entreguen correctamente.
- En GitLab autogestionado o GitLab Dedicated, confirma que el webhook del proyecto o grupo esté
  firmado, que la verificación SSL esté habilitada y que la instancia utilice GitLab 19.0 o una versión
  posterior. En GitLab 19.0 autogestionado, confirma que el indicador de función `webhook_signing_token`
  esté habilitado; repara los hooks deshabilitados automáticamente después de fallas.
- En GitLab autogestionado o GitLab Dedicated, confirma que un token de acceso personal existente de una cuenta de servicio
  esté activo y tenga el alcance `api`. Si Codex creó la
  cuenta de servicio, confirma que esté configurada correctamente en la
[configuración de conectores de Codex](https://chatgpt.com/codex/cloud/settings/connectors)
  y que el proyecto o grupo esté habilitado.
- En GitLab autogestionado o GitLab Dedicated, confirma que la cuenta de servicio del espacio de trabajo —y no solo el usuario de GitLab conectado— tenga acceso Developer al proyecto o a un grupo superior para que Codex pueda publicar revisiones y reacciones. La pertenencia se hereda; la actividad y el acceso de la cuenta de servicio son independientes.
- Confirma que se haya habilitado **Revisión de código** o **Revisiones automáticas** y que la MR cumpla
  con la política y el activador del repositorio.
- Usa `@codex review`.
