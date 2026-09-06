<!-- source: https://learn.chatgpt.com/es-419/docs/sandboxing/auto-review -->

La Revisión automática sustituye la aprobación manual en el límite del sandbox por un
agente revisor independiente. El agente principal de Codex sigue ejecutándose en el mismo sandbox, con
la misma política de aprobación y los mismos límites de red y del sistema de archivos. La
diferencia radica en quién revisa las solicitudes de escalamiento que cumplen los requisitos.

  La Revisión automática solo se aplica cuando las aprobaciones son interactivas. En la práctica, esto
  significa usar `approval_policy = "on-request"` o una política de aprobación granular que
  siga mostrando la categoría de prompt correspondiente. Con `approval_policy = "never"`,
  no hay nada que revisar.

En la aplicación de escritorio de ChatGPT, seleccionar un modelo Daybreak aprobado
cambia automáticamente el control de permisos a **Aprobar por mí** cuando ese
modo está disponible para tu cuenta y lo permite la política de la organización. Esto
también se aplica cuando usas el comando `/model` de la aplicación de escritorio. Si ese modo
no está disponible, el modo de permisos actual no cambia. La selección del modelo
nunca anula los requisitos administrados de la organización.

Antes de habilitar **Acceso completo** para un modelo de seguridad aprobado, la
aplicación de escritorio de ChatGPT muestra una advertencia específica del modelo sobre acciones peligrosas. La
advertencia recomienda usar **Aprobar por mí** en su lugar e incluye un enlace a la
[configuración de la política del revisor](#configuration). La advertencia no restablece
el límite del sandbox ni anula la política de la organización.

## Cómo funciona la revisión automática

En términos generales, el flujo es el siguiente:

1. El agente principal opera en `read-only` o `workspace-write`.
2. Cuando necesita cruzar el límite del sandbox, solicita aprobación.
3. Si se establece `approvals_reviewer = "auto_review"`, Codex dirige esa solicitud de aprobación
   a un agente revisor independiente en lugar de detenerse para que intervenga una persona.
4. El revisor decide si la acción debe ejecutarse y devuelve una justificación.
5. Si se aprueba la acción, la ejecución continúa. Si se rechaza, se indica al agente
principal que busque una alternativa considerablemente más segura o que se detenga y pregunte al
usuario.

La Revisión automática cambia quién revisa; no concede permisos. No amplía
`writable_roots`, no habilita el acceso a la red ni debilita las rutas protegidas. Solo
cambia la forma en que Codex gestiona las acciones que ya necesitan aprobación.

## Cuándo se activa

La Revisión automática evalúa las solicitudes de aprobación que, de otro modo, quedarían en pausa a la espera de una persona.
Entre ellas se incluyen:

- Llamadas a herramientas shell o exec que solicitan permisos elevados del sandbox.
- Solicitudes de red bloqueadas por el sandbox o la política vigentes.
- Ediciones de archivos fuera de las raíces de escritura permitidas.
- Llamadas a herramientas MCP o de aplicaciones que requieren aprobación según sus anotaciones de herramienta
o el modo de aprobación configurado.
- Acceso a un sitio web o dominio nuevo mediante Uso de la computadora.

La Revisión automática no se ejecuta para las acciones habituales que ya se permiten dentro del
sandbox. Si un comando puede ejecutarse con el `sandbox_mode` activo, o si una llamada a una herramienta
se mantiene dentro de lo permitido por la política, el agente principal continúa sin revisión.

El Uso de la computadora es un caso aparte. Las aprobaciones de la App para Uso de la computadora siguen mostrándose
directamente al usuario, por lo que la Revisión automática no sustituye esos prompts de la App.

## Qué bloquea la revisión automática

En términos generales, la Revisión automática está diseñada para bloquear acciones como las siguientes:

- enviar datos privados, secretos o credenciales a destinos que no son de confianza
- sondear en busca de credenciales, tokens, cookies o material de sesión
- debilitar la seguridad de forma generalizada o persistente
- realizar acciones destructivas con un riesgo considerable de causar daños irreversibles

La política exacta se encuentra en el repositorio de código abierto de Codex:
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
y
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Esta política puede personalizarse para cada empresa con `guardian_policy_config` o
para cada usuario mediante la configuración local [`[auto_review].policy`](/es-419/codex/config-file/config-advanced#approval-policies-and-sandbox-modes).

## Qué ve el revisor

El revisor es, a su vez, un agente de Codex con una función más específica que la del agente principal:
decidir si debe ejecutarse una acción concreta que cruza el límite.

El revisor ve una transcripción compacta junto con la solicitud exacta de aprobación. Por lo
general, esto incluye los mensajes del usuario, las actualizaciones visibles del asistente, las llamadas pertinentes a
herramientas y sus resultados, y la acción que ahora se propone aprobar. También puede
realizar comprobaciones de solo lectura para obtener el contexto faltante, pero rara vez lo hace.

El razonamiento oculto del asistente no se incluye. La Revisión automática ve los elementos conservados del
chat y la evidencia de las herramientas, no la cadena de pensamiento privada.

## Rechazos y comportamiento ante fallas

Un rechazo explícito no se trata como un error común del sandbox. Codex devuelve
la justificación de la revisión al agente principal y agrega una instrucción más estricta:

- No intentes lograr el mismo resultado mediante una solución alternativa, ejecución indirecta o
la elusión de la política.
- Continúa solo con una alternativa considerablemente más segura.
- De lo contrario, detente y pregunta al usuario.

Codex también aplica un mecanismo de corte por rechazos para cada turno. En la implementación actual
de código abierto, la Revisión automática interrumpe el turno después de `3`
rechazos consecutivos o `10` rechazos dentro de una ventana móvil de las últimas `50`
revisiones del mismo turno.

Cualquier resultado que no sea un rechazo restablece el contador de rechazos consecutivos. Cuando se activa el mecanismo de corte,
Codex emite una advertencia y aborta el turno actual mediante una interrupción, en lugar de
permitir que el agente entre en un bucle de nuevos intentos de escalamiento.

Los tiempos de espera se presentan por separado de los rechazos explícitos, y se informa al agente principal
que un tiempo de espera por sí solo no demuestra que la acción sea insegura.

También existe una vía explícita para anular el rechazo de acciones. En la TUI actual
de código abierto, ejecuta `/approve` para abrir el selector **Rechazos de la revisión automática** y, luego,
selecciona una acción rechazada recientemente y apruébala para un único reintento. Codex registra hasta 10
rechazos recientes por tarea. Esa aprobación tiene un alcance limitado: se aplica a la acción
exacta que se rechazó, no a acciones futuras similares; se registra para un reintento en el
mismo contexto; y el reintento aún pasa por la Revisión automática. Internamente,
Codex inserta un marcador de aprobación con alcance de desarrollador para esa acción exacta. El
revisor ve entonces esa anulación explícita del usuario como parte del contexto, pero sigue cumpliendo la
política y puede volver a rechazarla si la política establece que el usuario no puede anular esa clase de
rechazo.

## Configuración

Para obtener detalles sobre la configuración, consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration#configure-automatic-review-policy).

La política predeterminada del revisor se encuentra en el repositorio de código abierto de Codex:
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Las empresas pueden sustituir su sección específica del tenant por
`guardian_policy_config` en los requisitos administrados. Los usuarios individuales también pueden configurar
una política local mediante
[`[auto_review].policy`](/es-419/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
en su archivo `config.toml`, pero los requisitos administrados tienen prioridad:

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

Para personalizar la política, primero copia todo el texto de la política predeterminada y, luego,
ajústalo de forma iterativa según tu perfil de riesgo individual.

## Configurar una actividad de ciberseguridad autorizada

Para trabajos de seguridad autorizados, combina la revisión automática con un alcance
por escrito de la actividad y un [perfil de permisos](/es-419/codex/permissions) con privilegios mínimos.
Usa un objetivo de laboratorio aprobado, documenta las acciones y el periodo de la actividad, y
mantén fuera del alcance los sistemas de producción, los hosts no relacionados, las credenciales y los cambios persistentes,
a menos que estén autorizados explícitamente.

Tanto `[auto_review].policy` como `guardian_policy_config` sustituyen tu política actual
del revisor. No se combinan con las políticas incluidas con tu modelo ni con las
administradas por tu organización. Se siguen aplicando las instrucciones de revisión y el formato
de respuesta integrados. Antes de usar cualquiera de los ejemplos, copia la política actual
completa, conserva todas las reglas existentes y agrega las reglas para el trabajo aprobado.
Sustituye el marcador de posición en mayúsculas por esa política completa. Si no puedes
acceder a la política actual, no la reemplaces.

La siguiente plantilla local de `config.toml` habilita la revisión y agrega condiciones con alcance definido
después de la política existente del revisor:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

Sustituye el objetivo y las acciones permitidas del ejemplo por el alcance aprobado real.
Haz cumplir las restricciones del objetivo mediante reglas independientes del sistema de archivos y de red;
las instrucciones del revisor no sustituyen esos límites.

Las organizaciones pueden aplicar las mismas condiciones en el archivo administrado `requirements.toml`:

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` controla los perfiles de permisos actuales.
`allowed_sandbox_modes` también impide el acceso completo en implementaciones que aún usan
el valor heredado `sandbox_mode`.

La configuración administrada `guardian_policy_config` tiene prioridad sobre la configuración local
`[auto_review].policy` de un usuario. Conserva `approval_policy = "on-request"` u otra
política de aprobación interactiva apta y mantén un límite del sandbox que pueda hacerse cumplir.
Con `approval_policy = "never"`, `:danger-full-access` o `--yolo`, una acción
puede evitar que se genere la solicitud de aprobación para cruzar el límite que necesita la revisión.

Un destino de red incluido en la lista de destinos permitidos no activa la revisión por sí solo. Agrega
[reglas de comandos](/es-419/codex/agent-configuration/rules) explícitas con
`decision = "prompt"`, o configura las herramientas MCP sensibles para que requieran aprobación,
cuando las acciones dentro del sandbox deban llegar de todos modos al revisor.

Consulta [Modelos y acceso de confianza](/es-419/codex/cyber-safety) y la [configuración
recomendada](/es-419/codex/cyber-safety/recommended-configuration) para obtener información sobre el acceso a modelos,
la configuración de la actividad y los flujos de trabajo personalizados de agentes. Consulta [Configuración administrada](/es-419/codex/enterprise/managed-configuration#configure-automatic-review-policy)
para conocer la precedencia en empresas y las versiones de cliente compatibles. Para arneses de ejecución personalizados de la API o del
Agents SDK, usa [Medidas de protección y revisión humana](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution).

## Reducir el volumen de revisiones sin debilitar la seguridad

La Revisión automática funciona mejor cuando el sandbox ya abarca tus flujos de trabajo seguros
habituales. Si demasiadas acciones rutinarias necesitan revisión, corrige primero el límite
en lugar de enseñarle al revisor a aprobar indefinidamente solicitudes de escalamiento triviales.

En la práctica, los cambios con mayor impacto son:

- Agrega valores específicos a
[`writable_roots`](/es-419/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  para los directorios temporales o repositorios adyacentes que uses intencionalmente.
- Agrega [reglas de prefijos](/es-419/codex/agent-configuration/rules) con un alcance limitado. Prefiere prefijos de comandos
  precisos como `["cargo", "test"]` o `["pnpm", "run", "lint"]` en lugar de patrones
  amplios como `["python"]` o `["curl"]`. Las reglas amplias suelen eliminar precisamente el
  límite que la Revisión automática debe proteger.

Las transcripciones de las sesiones de Revisión automática se conservan en `~/.codex/sessions` de
forma predeterminada, por lo que puedes pedirle a Codex que analice allí el tráfico anterior antes de cambiar
la política o los permisos.

## Límites

La Revisión automática mejora las condiciones operativas predeterminadas para las tareas prolongadas con agentes,
pero no es una garantía de seguridad determinista.

- Solo evalúa las acciones que solicitan traspasar un límite.
- Aun así, puede cometer errores, especialmente en contextos adversariales o inusuales.
- Debe complementar, no reemplazar, un buen diseño del sandbox, el monitoreo y
una política específica de la organización.

Para conocer los fundamentos de la investigación y los resultados de evaluación publicados, consulta la
[publicación de Alignment Research sobre la Revisión automática](https://alignment.openai.com/auto-review/).
