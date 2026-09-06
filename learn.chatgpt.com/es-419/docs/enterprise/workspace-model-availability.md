<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/workspace-model-availability -->

Los modelos disponibles para una persona dependen de la interfaz del producto y de cómo
inició sesión. Una configuración de modelos de tu espacio de trabajo de ChatGPT no se aplica
automáticamente a Codex en la aplicación de escritorio de ChatGPT, Codex CLI, la extensión
para IDE, Codex Cloud ni la API de OpenAI.

Para conocer el modelo de administración completo, consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).

## Identificar el ámbito de acceso a los modelos

| Producto o ámbito de autenticación                                                         | El acceso a los modelos se rige por                                                                                  | Fuente actual                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Espacio de trabajo de ChatGPT                                                                          | El plan del espacio de trabajo, el acceso de los miembros, la configuración del espacio de trabajo y los permisos de rol admitidos                 | [Modelos y límites de ChatGPT Enterprise y Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| Codex en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE con inicio de sesión mediante ChatGPT        | Los modelos compatibles con el cliente específico y el acceso disponible para la identidad de ChatGPT con la que se inició sesión    | [Modelos de Codex](/es-419/codex/models) y las indicaciones vigentes para el espacio de trabajo                                                                  |
| Codex Cloud                                                                                | Los modelos compatibles con los flujos de trabajo alojados de Codex y el acceso disponible para la identidad de ChatGPT con la que se inició sesión | [Modelos de Codex](/es-419/codex/models) y [Codex Cloud](/es-419/codex/cloud)                                                                 |
| Codex en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE con autenticación mediante clave de API | La organización y el proyecto de la API de OpenAI asociados con la clave                                       | [Autenticación](/es-419/codex/auth) y la [Plataforma API](https://platform.openai.com/docs/overview)                        |

Consulta la fuente actual correspondiente a la interfaz que realmente utiliza el usuario. No
copies un catálogo de modelos ni supongas que una configuración del selector de modelos de ChatGPT
tiene el mismo efecto en Codex en la aplicación de escritorio de ChatGPT, Codex CLI, la extensión
para IDE, Codex Cloud y la Plataforma API.

## Definir una experiencia inicial clara para los empleados

Revisa la [configuración de modelos](https://help.openai.com/en/articles/8411955) de tu
espacio de trabajo antes de invitar a un grupo piloto. Los propietarios y administradores del espacio de trabajo pueden
configurar valores iniciales predeterminados por separado para Chat y para Work y Codex. Cuando la interfaz lo
permita, elige un modelo inicial, un nivel de razonamiento, una velocidad y el comportamiento de los
chats nuevos para Chat, Work y las interfaces locales de Codex.

Considera estas opciones valores predeterminados, no permisos. Los modelos disponibles siguen dependiendo
de la licencia y el rol del miembro, de su identidad en el espacio de trabajo o la API,
de los requisitos obligatorios del espacio de trabajo y de la interfaz específica que utiliza.
Los valores iniciales predeterminados no otorgan acceso a modelos no disponibles ni anulan
esos requisitos. Codex Cloud no permite cambiar su modelo predeterminado.

La disponibilidad del Modo rápido depende del espacio de trabajo, de la interfaz del producto y de cualquier
configuración obligatoria de `features.fast_mode` en
[`requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml).
Esta configuración puede mantener el Modo rápido activado o desactivado para los clientes locales administrados de Codex;
no es un valor inicial predeterminado y no puede anular las restricciones de disponibilidad del espacio de trabajo o del producto.

## GPT-6 Astra en Enterprise

Durante la implementación inicial, tu organización debe tener acceso a Daybreak antes de que
un administrador pueda habilitar Astra. Astra está desactivado de forma predeterminada en ChatGPT Enterprise
durante las dos primeras semanas después del lanzamiento. Los administradores de los espacios de trabajo que cumplan los requisitos
pueden habilitar Astra para usuarios o grupos
en Chat, Work y Codex. Los requisitos de acceso existentes de cada producto siguen vigentes. Revisa la
[configuración de modelos de tu espacio de trabajo](https://help.openai.com/en/articles/8411955) y
confirma la disponibilidad en cada cliente que utilice tu grupo piloto.

Habilitar el acceso y elegir un modelo inicial son decisiones independientes. Verifica la
licencia, el rol y las condiciones de facturación aplicables antes de establecer Astra como modelo predeterminado.
Consulta [precios](/es-419/codex/pricing) para obtener orientación sobre el uso incluido y la facturación,
y [monitoreo de seguridad](/es-419/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)
para las tareas que se pausan para su revisión.

Al iniciar sesión con una clave de API, el acceso a Astra se rige por la organización y el proyecto de la API
asociados con la clave. Habilitar Astra en un espacio de trabajo de ChatGPT no otorga
acceso a la API. El acceso anticipado con una clave de API también requiere configurar el cliente;
solicita las instrucciones de configuración al equipo de OpenAI que gestiona tu cuenta. Seleccionar un
modelo o cambiar la configuración local no otorga acceso por sí solo.

## Prepararse para el retiro de GPT-5.4

El 31 de agosto de 2026, GPT-5.4 y GPT-5.4 mini dejarán de estar disponibles en Codex para los usuarios que hayan iniciado
sesión con ChatGPT. Antes de esa fecha, actualiza los valores predeterminados afectados del espacio de trabajo, las configuraciones de modelos guardadas,
las configuraciones administradas, los agentes personalizados y las tareas programadas:

- Reemplaza `gpt-5.4` por `gpt-5.6-terra` (GPT-5.6 Terra).
- Reemplaza `gpt-5.4-mini` por `gpt-5.6-luna` (GPT-5.6 Luna).

Ni la API de OpenAI ni Codex, cuando se autentica con tu propia clave de API, se ven afectados.
Consulta [Modelos de Codex](/es-419/codex/models#deprecated-codex-models) y
[configuración administrada](/es-419/codex/enterprise/managed-configuration)
para conocer los detalles de la migración.

## Diferenciar el acceso de los permisos en tiempo de ejecución

El acceso a los modelos determina si un modelo está disponible para el usuario autenticado
en una interfaz compatible. Los perfiles de permisos locales y los requisitos administrados
determinan qué puede hacer un agente una vez iniciada una ejecución local, por ejemplo, qué archivos
puede modificar o a qué destinos de red puede acceder.

Un perfil de permisos no puede otorgar acceso a los modelos. El acceso a los modelos tampoco puede debilitar
el sandbox, la política de aprobación, los controles de red ni los permisos del sistema de origen
que se aplican a una ejecución.

## Solucionar problemas de acceso a los modelos

Si un usuario no puede seleccionar un modelo que espera tener disponible:

- Confirma la interfaz del producto y el método de inicio de sesión.
- Confirma el espacio de trabajo de ChatGPT o la organización y el proyecto de la Plataforma API.
- Revisa los controles de acceso actuales para ese ámbito de autenticación.
- Verifica si el cliente local seleccionado o Codex Cloud son compatibles con el modelo.

## Fuentes actuales

- [Modelos y límites de ChatGPT Enterprise y Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [Administrar la configuración del espacio de trabajo](https://help.openai.com/en/articles/8411955)
- [Control de acceso basado en roles](https://help.openai.com/en/articles/11750701-rbac)
- [Modelos de Codex](/es-419/codex/models)
- [Disponibilidad de las funciones de Codex según el plan](/es-419/codex/pricing#feature-availability)
- [Autenticación](/es-419/codex/auth)

## Documentación relacionada

- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
- [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
- [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
