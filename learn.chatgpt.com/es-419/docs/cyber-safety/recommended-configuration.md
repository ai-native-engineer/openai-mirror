<!-- source: https://learn.chatgpt.com/es-419/docs/cyber-safety/recommended-configuration -->

Los controles de seguridad adecuados para un flujo de trabajo de ciberseguridad dependen del modelo, de las acciones que puede realizar, de los sistemas a los que puede acceder y de la sensibilidad de los datos involucrados.

En la mayoría de los flujos de trabajo de Daybreak Blue, las prácticas de seguridad que tu organización ya aplica —como los controles de acceso, la protección de credenciales y la revisión de acciones sensibles— pueden ser suficientes.

Los flujos de trabajo de Daybreak Red, las pruebas de seguridad autónomas y las actividades que involucren sistemas de producción, datos sensibles o herramientas externas pueden requerir salvaguardas más estrictas. Las siguientes recomendaciones están destinadas principalmente a estos casos de mayor riesgo.

  Eres responsable de evaluar los riesgos de tu flujo de trabajo específico e
implementar los controles de seguridad adecuados. Las salvaguardas del modelo y Trusted
Access no reemplazan las prácticas de seguridad, monitoreo y
supervisión de tu organización.

Trusted Access controla el acceso aprobado al modelo, pero no configura tu entorno ni impone límites a los sistemas y las acciones aprobados. Tu equipo debe establecer controles adecuados de aislamiento, permisos, revisión, monitoreo y supervisión humana. Supón que el modelo, sus herramientas y todos los sistemas conectados podrían estar comprometidos y configura el entorno para que, aun así, no puedan acceder a sistemas no autorizados, exponer credenciales, desactivar salvaguardas ni persistir una vez finalizado el trabajo.

## Aislar el entorno

Ejecuta el trabajo de seguridad ofensiva en un laboratorio dedicado o un sandbox. Empieza sin acceso irrestricto a Internet ni a sistemas sensibles de producción, redes corporativas, cargas de trabajo no relacionadas o interfaces de administración del host. Mantén fuera del alcance los secretos, las credenciales, el acceso persistente y los cambios duraderos en el sistema, a menos que el trabajo aprobado los requiera y autorice explícitamente.

Para trabajos de mayor riesgo o con menos salvaguardas, usa un entorno nuevo con aislamiento estricto para cada intento. Separa el cómputo, el almacenamiento, la red y las identidades, y destruye el entorno al finalizar en lugar de restablecerlo o reutilizarlo.

Pon a prueba los límites del sistema de archivos y de la red antes de iniciar trabajos de mayor riesgo. Incluye todos los hosts accesibles, las herramientas conectadas, los agentes delegados y los servicios posteriores de la cadena. Mantén aislado el entorno del host incluso cuando el modelo o el revisor aprueben una acción individual.

## Definir y hacer cumplir los límites aprobados

Antes de que el modelo comience, documenta los sistemas, las herramientas, las acciones y los límites de tiempo aprobados para el trabajo. Incluye:

- Los sistemas, hosts y entornos de destino aprobados.
- Los sistemas excluidos, incluidos los sistemas de producción y la infraestructura no relacionada.
- Las herramientas y los servicios conectados aprobados.
- Las acciones aprobadas y prohibidas.
- Las horas aprobadas de inicio y finalización y los requisitos para el manejo de datos.
- La divulgación de vulnerabilidades, la aprobación de parches y la coordinación con los responsables de mantenimiento.
- Las condiciones de detención y las acciones que requieren aprobación humana explícita.

Proporciona al agente estos límites aprobados como contexto de la tarea. La documentación por sí sola no permite hacerlos cumplir: aplica controles independientes sobre el sistema de archivos, la red, las identidades y las herramientas para imposibilitar las acciones no autorizadas siempre que sea viable.

Usa los [perfiles de permisos](/es-419/codex/permissions) de Codex para crear un límite de privilegios mínimos. Elige `:read-only` cuando la tarea no requiera cambios o amplía `:workspace` cuando el trabajo requiera modificar el espacio de trabajo. Por ejemplo:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = "cyber-lab"

[features]
network_proxy = true

[permissions.cyber-lab]
description = "Limit security testing to the approved lab and workspace."
extends = ":workspace"

[permissions.cyber-lab.filesystem]
glob_scan_max_depth = 3

[permissions.cyber-lab.filesystem.":workspace_roots"]
"**/.env*" = "deny"
"**/*.pem" = "deny"

[permissions.cyber-lab.network]
enabled = true
# Uncomment only for an approved host that resolves to a private address.
# allow_local_binding = true

[permissions.cyber-lab.network.domains]
"lab.example.com" = "allow"

La función `network_proxy` limita el acceso al dominio aprobado. Sin ella,
`network.enabled = true` permite el acceso directo a la red y la lista de permitidos del laboratorio
no restringe los destinos. La búsqueda web, las apps, los conectores, los servidores MCP,
la actividad del navegador y Codex Cloud usan controles independientes; restringe o desactiva
cada superficie que no requiera tu flujo de trabajo aprobado.

Reemplaza `lab.example.com` por un destino aprobado. El análisis acotado del sistema de archivos está diseñado para evitar búsquedas en todo el espacio de trabajo en Linux, WSL y Windows; aumenta la profundidad o usa rutas de denegación exactas si hay archivos sensibles a mayor profundidad. No combines los perfiles de permisos con la configuración heredada de `sandbox_mode`; sigue las [indicaciones para configurar perfiles de permisos](/es-419/codex/permissions#define-and-select-a-profile).

Si el host de laboratorio aprobado se resuelve en una dirección privada, Codex lo bloquea de forma predeterminada aunque esté en la lista de permitidos. Configura `allow_local_binding = true` solo para trabajos en redes privadas que se hayan aprobado explícitamente, mantén limitada la lista de destinos permitidos y consulta las [indicaciones sobre redes locales y privadas](/es-419/codex/permissions#local-and-private-networks). También puedes agregar a la lista de permitidos la dirección IP privada exacta aprobada.

Bloquea de forma predeterminada el acceso a Internet sin restricciones y a las redes de producción. Si necesitas acceso externo, canalízalo a través de una puerta de enlace o un proxy sujetos a controles independientes, con listas de permitidos restringidas, inspección de solicitudes y registro. Aplica las mismas restricciones a las conexiones indirectas mediante administradores de paquetes, webhooks, servicios de obtención de URL, redireccionamientos, API de la nube y herramientas conectadas. Carga las dependencias antes de la ejecución o usa dependencias aprobadas por un administrador.

## Proteger las credenciales y los datos sensibles

No incluyas claves de API reutilizables, credenciales de la nube, contraseñas ni tokens de cuentas de servicio en prompts, repositorios, variables de entorno, sistemas de archivos compartidos o registros accesibles para el modelo. Cuando se requiera autenticación, usa un intermediario o una puerta de enlace independiente para proporcionar credenciales de corta duración cuyo alcance se limite al destino exacto y a la acción permitida, sin exponerlas al modelo.

Proporciona solo los datos necesarios para la tarea aprobada. Elimina la información sensible innecesaria, bloquea el acceso a los metadatos de la nube y a los puntos de acceso de credenciales, y trata como no confiables los archivos generados por el modelo.

Evita `:danger-full-access` y `--yolo` en los flujos de trabajo de ciberseguridad. Acceso completo elimina el límite del sandbox que se puede hacer cumplir y del que depende la revisión automática. Las organizaciones administradas pueden excluir `:danger-full-access` y `--yolo`, limitar las políticas de aprobación permitidas y exigir la revisión automática mediante la [configuración administrada por la empresa](/es-419/codex/enterprise/managed-configuration#configure-automatic-review-policy).

Antes de habilitar **Acceso completo** para un modelo de seguridad aprobado, la aplicación de escritorio de ChatGPT muestra una advertencia específica del modelo sobre acciones peligrosas. En su lugar, la advertencia recomienda **Aprobar por mí** e incluye un enlace a la [configuración de la política del revisor](/es-419/codex/sandboxing/auto-review#configuration). La advertencia no restablece el límite del sandbox ni anula la política de la organización.

Las medidas de protección incorporan una revisión basada en políticas a un flujo de trabajo de ciberseguridad controlado. No reemplazan el aislamiento del entorno, los permisos con privilegios mínimos, los límites claramente definidos, el monitoreo ni la supervisión humana.

## Revisar las acciones sensibles de Codex

La [Revisión automática](/es-419/codex/sandboxing/auto-review) envía las solicitudes de aprobación aptas que surgen en el límite del sandbox a un revisor distinto antes de ejecutar la acción propuesta. El revisor evalúa la acción propuesta, el contexto delimitado de la tarea y la política aplicable, y luego permite o rechaza la solicitud. Las organizaciones pueden adaptar esa política según sus destinos aprobados, acciones prohibidas y condiciones que requieran revisión humana.

Exige aprobación humana explícita para las acciones que afecten la producción, los sistemas externos, los datos sensibles, la elevación de privilegios, el acceso persistente o los cambios irreversibles. Considera no confiables las instrucciones integradas en sitios web, repositorios, documentos y resultados de herramientas; no pueden ampliar el alcance autorizado ni anular los controles de acceso.

En la aplicación de escritorio de ChatGPT, al seleccionar un modelo Daybreak aprobado, el control de permisos cambia automáticamente a **Aprobar por mí** cuando ese modo está disponible para tu cuenta y lo permite la política de la organización. Esto también se aplica cuando usas el comando `/model` de la aplicación de escritorio. Si ese modo no está disponible, el modo de permisos actual no cambia. La selección del modelo nunca anula los requisitos administrados por la organización.

Para que se ejecute la revisión automática, mantén activos los tres controles:

1. Usa una política de aprobación interactiva, como `approval_policy = "on-request"`.
2. Configura `approvals_reviewer = "auto_review"`.
3. Mantén un límite de sandbox o de perfil de permisos que pueda hacerse cumplir.

Las solicitudes a un destino incluido en la lista de permitidos de la red permanecen dentro del límite de la red y no activan automáticamente la Revisión automática. Para revisar un comando sensible aunque su destino esté en la lista de permitidos, crea una [regla de comando](/es-419/codex/agent-configuration/rules) explícita en `~/.codex/rules/`:

```python
prefix_rule(
    pattern = ["curl"],
    decision = "prompt",
    justification = "Review requests to the approved cybersecurity target.",
)

Reinicia Codex después de agregar la regla. Con `approvals_reviewer = "auto_review"`, los comandos que coincidan se envían al revisor antes de ejecutarse. Agrega las reglas de prompt correspondientes para cada comando sensible o usa `approval_mode = "prompt"` para [herramientas MCP](/es-419/codex/extend/mcp) individuales. Las acciones que requieran la decisión de una persona aún necesitan aprobación humana explícita.

La Revisión automática no inspecciona las acciones rutinarias que ya están permitidas dentro del sandbox. Con `approval_policy = "never"` o Acceso completo, es posible que una acción sensible no genere una solicitud de aprobación que se pueda revisar. La revisión automática puede cometer errores y no reemplaza el aislamiento, los límites claramente definidos, el monitoreo ni la supervisión humana explícita.

Para conocer una política con alcance definido y su aplicación en toda la organización, consulta [Configurar un flujo de trabajo de ciberseguridad autorizado](/es-419/codex/sandboxing/auto-review#configure-an-authorized-cybersecurity-engagement).

## Monitorear de forma independiente y bloquear ante fallas

Registra las solicitudes al modelo, las llamadas a herramientas, la actividad de red, el uso de credenciales y los cambios relevantes para la seguridad. Mantén los registros y los sistemas de monitoreo fuera del entorno controlado por el modelo. Genera alertas ante destinos no autorizados, solicitudes de red inesperadas, credenciales expuestas, cambios en las políticas, registros faltantes e intentos de eludir las salvaguardas.

Mantén la aplicación de políticas, los intermediarios de credenciales, los sistemas de revisión y los controles de apagado de emergencia independientes del agente. Detén el flujo de trabajo si falla un control esencial o un sistema de monitoreo.

## Agregar medidas de protección a los flujos de trabajo de agentes personalizados

Si desarrollas con Responses API, Agents SDK u otro arnés de ejecución, agrega una revisión en el límite de ejecución de las herramientas. Antes de ejecutar las acciones sensibles propuestas, comprueba que se ajusten a los sistemas, las acciones y los límites de tiempo aprobados; deriva a una persona las acciones ambiguas o de alto riesgo, aplica restricciones independientes al sistema de archivos y a la red, conserva registros de auditoría y bloquea la ejecución si el revisor o la política no están disponibles.

La Revisión automática de Codex no protege automáticamente las herramientas personalizadas ni los arneses de ejecución externos. Usa [Medidas de protección y revisión humana](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution) para el patrón de Agents SDK y toma como referencia la [política del revisor de código abierto](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).

El entorno aislado y la revisión propios del producto Codex son independientes de las [comprobaciones de ciberseguridad de la API](/api/docs/guides/safety-checks/cybersecurity). Las salvaguardas de la API pueden devolver errores `cyber_policy`, y los valores de `safety_identifier` de cada usuario pueden ayudar a limitar el impacto de una acción de salvaguarda.

## Limpiar y validar los resultados

Cuando termine el trabajo, revoca las credenciales temporales, finaliza los procesos en segundo plano, elimina el acceso persistente y destruye los entornos de mayor riesgo. Verifica que no queden conexiones de retorno, artefactos expuestos, estados compartidos ni acceso entre ejecuciones, y mantén aislados entre sí a los distintos usuarios, sesiones y evaluaciones.

Valida los hallazgos antes de actuar en función de ellos, sigue prácticas de divulgación coordinada y asegúrate de que haya personas responsables de la remediación y los cambios.

## Antes de comenzar

Confirma los sistemas y las acciones aprobados, el modelo adecuado, el entorno aislado, los permisos con privilegios mínimos, el acceso restringido a la red, las credenciales protegidas, la revisión de acciones, el monitoreo independiente, la detención de emergencia y el plan de limpieza. Las salvaguardas del modelo, el aislamiento, los permisos con alcance limitado, la revisión de acciones, el monitoreo y la supervisión humana se complementan; ningún elemento debe ser el único control.
