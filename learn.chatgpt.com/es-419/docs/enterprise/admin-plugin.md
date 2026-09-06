<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/admin-plugin -->

Consulta esta guía para entender cómo el complemento Admin facilita las tareas habituales de administración, prepararte para una tarea y probar prompts para casos de uso clave con las aprobaciones y el contexto adecuados.

## 1. Entiende para qué sirve el complemento Admin

El complemento Admin está diseñado para ayudar a gestionar la configuración, los permisos y los controles directamente en ChatGPT Work. Describes el objetivo en lenguaje cotidiano y el complemento reúne los datos necesarios, consulta el estado actual, explica lo que encuentra y te orienta sobre el siguiente paso admitido.

### Qué busca resolver el complemento Admin

- Convertir una solicitud administrativa en un flujo de trabajo claro sin que tengas que escribir una solicitud a una API.
- Revisar el estado actual del espacio de trabajo antes de tomar una decisión o aprobar un cambio.
- Mostrar qué fuentes y campos autorizados respaldan la respuesta, junto con todo lo que no pudo verificar.
- Detenerse para una revisión antes de realizar un cambio admitido y luego volver a consultar el registro para confirmar el resultado.

El complemento utiliza internamente determinadas API de administración y fuentes de datos conectadas y aprobadas. No integra todos los sistemas de administración, amplía tus permisos ni permite realizar todas las acciones de las API en ChatGPT. El sistema responsable de los datos sigue controlando lo que el complemento puede leer o cambiar.

### Qué buscan resolver las API de administración

Una API de administración ofrece al software una forma estructurada de solicitar datos o una acción admitida. Las organizaciones pueden usar las API de administración para crear procesos internos o herramientas externas. Algunos ejemplos comunes son los informes programados, las tareas repetitivas en numerosos registros y las conexiones con sistemas aprobados. Estos flujos de trabajo suelen requerir una revisión de ingeniería, seguridad y gobernanza.

No necesitas crear un flujo de trabajo con una API para usar esta guía. El resto de la guía se centra en el complemento Admin. La administración de espacios de trabajo de ChatGPT y la administración de la Plataforma API de OpenAI también siguen siendo independientes, cada una con sus propios permisos y requisitos de autenticación.

### Mantén las credenciales en privado

Usa solo las conexiones y los sistemas de almacenamiento de secretos aprobados por tu organización. Nunca pegues una clave real de una API de administración en ChatGPT, Codex, un documento o un archivo de código fuente.

## 2. Prepárate para usar el complemento Admin

Usa el complemento Admin para una tarea puntual admitida cuando quieras resolver la solicitud en lenguaje cotidiano. Describe el objetivo y proporciona los ID estables o el contexto aprobado para los informes. El complemento muestra lo que encontró o lo que planea cambiar antes de que decidas si quieres continuar.

El complemento usa únicamente las fuentes, las credenciales y las acciones autorizadas para esa tarea. No integra todos los sistemas de administración ni te otorga permisos más amplios. El sistema original sigue siendo la fuente de referencia.

### Antes de empezar

1. Busca el área de administración donde se encuentran los registros.
2. Reúne los datos necesarios y obtén la aprobación requerida.
3. Empieza con una solicitud de solo lectura.
4. Pregunta al complemento qué fuentes y campos utilizó y qué no pudo verificar.
5. Para un cambio admitido, revisa el plan antes de aprobarlo. Luego pide al complemento que vuelva a consultar el registro y confirme el resultado.

Confirma que el complemento esté disponible en tu espacio de trabajo y que tengas los permisos necesarios. Los casos de uso de roles y acceso que se presentan a continuación reflejan el alcance documentado actual del complemento. El complemento puede revisar roles, permisos de funciones y asignaciones de usuarios o grupos. Después de que confirmes, también puede asignar un rol existente a un grupo existente.

El complemento no puede crear roles, cambiar los permisos de un rol ni confirmar el acceso a un conector específico.

Los casos de uso de análisis necesitan acceso a fuentes de datos conectadas y aprobadas. El análisis del ROI también requiere resultados de negocio o de ingeniería aprobados; los registros de uso por sí solos no bastan.

## 3. Explora los casos de uso clave del complemento Admin

Elige un caso de uso, reemplaza cada marcador de posición con un valor de tu solicitud aprobada y sigue los pasos en orden. Empieza con una solicitud de solo lectura, a menos que la tarea sea un cambio admitido que ya cuente con aprobación.

### Enumera los roles del espacio de trabajo

**Prompt para probar**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**Pasos**

1. **Recopila:** confirma el ID del espacio de trabajo y que tengas permiso para consultar esta información.
2. **Ejecuta:** solicita la lista de roles en modo de solo lectura.
3. **Revisa:** comprueba los tipos de roles, el acceso a las funciones y las asignaciones.
4. **Verifica:** investiga cualquier resultado inesperado sin realizar cambios.

### Revisa un rol

**Prompt para probar**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**Pasos**

1. **Recopila:** confirma el ID del rol y el espacio de trabajo.
2. **Ejecuta:** solicita la revisión del rol en modo de solo lectura.
3. **Revisa:** comprueba que los permisos y las asignaciones correspondan a la función prevista del rol.
4. **Verifica:** anota las preguntas que tengas para la persona responsable del rol. Recuerda que el complemento no puede crear el rol ni editar sus permisos.

### Comprende el acceso de un usuario o grupo

**Prompt para probar**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**Pasos**

1. **Recopila:** usa el ID estable del usuario o grupo.
2. **Ejecuta:** pide al complemento que explique el acceso.
3. **Revisa:** comprueba qué roles están asignados y qué acceso otorgan. Toma nota de cualquier acceso superpuesto o faltante.
4. **Verifica:** si el complemento no puede ver algo, márcalo como desconocido en lugar de hacer suposiciones.

### Asigna un rol existente a un grupo

**Prompt para probar**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**Pasos**

1. **Recopila:** confirma los ID del grupo y del rol. Revisa la solicitud aprobada y quién figura como responsable de la aprobación.
2. **Ejecuta:** pide al complemento que muestre los roles actuales y lo que cambiaría.
3. **Revisa:** aprueba solo si el plan coincide con la solicitud aprobada.
4. **Verifica:** después de la asignación, vuelve a revisar el grupo para confirmar que el rol existente se agregó según lo aprobado.

### Verifica el permiso general para conectores

**Prompt para probar**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**Pasos**

1. **Recopila:** confirma el ID del usuario y que tengas permiso para revisar su acceso.
2. **Ejecuta:** solicita la verificación del permiso general.
3. **Revisión:** comprueba el rol asignado y el permiso utilizado para responder.
4. **Verificación:** usa esto solo como una comprobación general. No demuestra el acceso a un conector específico ni a un elemento conectado.

### Resolver problemas con un cambio aprobado

**Prompt para probar**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**Pasos**

1. **Recopilación:** confirma el registro del cambio aprobado y el resultado previsto.
2. **Ejecución:** pide al complemento que compare la solicitud con el espacio de trabajo actual.
3. **Revisión:** comprueba el espacio de trabajo y el rol. Luego, verifica quién es el propietario del registro.
4. **Verificación:** usa el estado actual del espacio de trabajo como fuente de referencia antes de elegir el siguiente paso.

### Optimizar los costos y la combinación de modelos

**Prompt para probar**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**Pasos**

1. **Recopilación:** confirma el espacio de trabajo, el rango de fechas y que los datos de costos cubran todo el período. Comprueba qué campos aprobados de rendimiento o resultados están disponibles.
2. **Ejecución:** solicita la comparación de costos y modelos.
3. **Revisión:** distingue lo que muestran los datos de las suposiciones, la información faltante y las ventajas y desventajas.
4. **Verificación:** revisa los posibles ahorros con Finanzas y los responsables de los flujos de trabajo antes de actuar.

### Conocer el uso y la adopción

**Prompt para probar**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**Pasos**

1. **Recopilación:** comprueba el espacio de trabajo, el rango de fechas y las correspondencias de equipos. Asegúrate de que la generación de informes por usuario esté aprobada.
2. **Ejecución:** solicita el análisis de uso y adopción.
3. **Revisión:** comprueba cuáles de los campos solicitados están disponibles. Omite la actividad para la que no haya datos en lugar de hacer suposiciones.
4. **Verificación:** un uso elevado no demuestra un uso avanzado, valor para el negocio ni desempeño individual.

### Medir el valor para el negocio y el ROI

**Prompt para probar**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**Pasos**

1. **Recopilación:** comprueba el espacio de trabajo y el rango de fechas; luego, confirma los resultados aprobados. Revisa la fórmula y las reglas de privacidad.
2. **Ejecución:** solicita el análisis de ROI.
3. **Revisión:** comprueba cada fuente y suposición. Anota cada limitación o dato faltante.
4. **Verificación:** el uso por sí solo no puede demostrar el ROI ni la causalidad. Revisa el resultado con Finanzas y los responsables del negocio.

### Evaluar el ROI de Codex

**Prompt para probar**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**Pasos**

1. **Recopilación:** confirma el espacio de trabajo y el período del informe. Revisa las correspondencias de equipos y repositorios y los datos de referencia aprobados.
2. **Ejecución:** solicita el análisis de ROI de Codex.
3. **Revisión:** distingue los patrones observados de las suposiciones. Protege los datos de usuarios y repositorios.
4. **Verificación:** revisa las recomendaciones y los valores de referencia de los resultados con Ingeniería.

## 4. Cuándo puede convenir un flujo de trabajo con API

Algunas organizaciones crean sus propios procesos administrativos o herramientas externas con las API. Este enfoque puede servir para realizar tareas programadas o continuas. También puede ser útil cuando un proceso abarca muchos registros o necesita conectarse a un sistema interno aprobado. Esto es independiente de la experiencia guiada del complemento Admin.

Empieza por una tarea administrativa definida: identifica los datos de entrada y los permisos necesarios, los puntos de revisión, el resultado esperado y cómo se registrará ese resultado. Si tu organización la automatiza, involucra a los equipos de ingeniería, seguridad y gobernanza correspondientes; guarda las credenciales en un sistema aprobado de almacenamiento de secretos; y prueba el flujo de trabajo antes de desplegarlo.

### Recursos relacionados

- [Referencia de la API de administración del espacio de trabajo de ChatGPT](https://chatgpt.com/public/admin/api-reference)
- [Límites de la administración](/es-419/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [Analytics API del espacio de trabajo de ChatGPT](/es-419/codex/enterprise/analytics-api)
- [API de Cumplimiento del espacio de trabajo de ChatGPT](/es-419/codex/enterprise/compliance-api)
