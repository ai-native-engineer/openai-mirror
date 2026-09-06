<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/admin-setup -->

Usa esta guía para planificar una implementación de ChatGPT Enterprise en estos ámbitos
administrativos:

- Acceso al espacio de trabajo.
- Política de ejecución local para las funciones incluidas en la aplicación de escritorio de ChatGPT,
Codex CLI y la extensión para IDE.
- Codex Cloud.
- Acceso a la Plataforma API.
- Acceso a complementos y conectores.
- Permisos en los sistemas conectados.

Completa los pasos en orden para una implementación nueva o usa las páginas vinculadas para modificar
un solo ámbito.

En la configuración del espacio de trabajo, **Codex y Work locales** combina el acceso local a Codex y Work
bajo **Permitir que los miembros usen Codex y Work de forma local**. Algunos espacios de trabajo
ofrecen, en cambio, secciones independientes de **Codex local** y **Work local** . En
esa distribución, **Permitir que los miembros usen Codex de forma local** controla Codex, y **Usar
Work de forma local** controla Work. Habilitar uno no habilita el otro.
Estas etiquetas identifican permisos del espacio de trabajo, no productos ni clientes independientes.
Los permisos de los tokens y los límites de vigencia de las credenciales aparecen en la sección **Tokens de
acceso** o en la sección de acceso local, según el espacio de trabajo.
La configuración administrada es una capa de políticas independiente que puede restringir el comportamiento durante la ejecución de
las funciones compatibles incluidas en esos clientes. Esta guía menciona
cada interfaz por separado cuando el comportamiento o la disponibilidad difieren.

Comienza con el mapa de referencia de
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).
Consulta las indicaciones del Centro de ayuda para conocer los procedimientos vigentes del espacio de trabajo de ChatGPT y la
documentación para desarrolladores vinculada sobre el comportamiento de las ejecuciones locales y alojadas.

<a id="enterprise-grade-security-and-privacy"></a>

Para obtener información sobre seguridad empresarial, privacidad y protecciones durante la ejecución, consulta
[Aprobaciones y seguridad de agentes](/es-419/codex/agent-approvals-security) y el
[informe técnico sobre la seguridad de Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## Paso 1: asignar responsables y elegir un plan de implementación

Asigna una persona responsable a cada parte de la implementación:

- **Acceso al espacio de trabajo:** membresía, licencias, roles y funciones compatibles del
  espacio de trabajo.
- **Política de ejecución local:** aprobaciones, perfiles de permisos, acceso al sistema de archivos y
  a la red, y otros requisitos para clientes locales compatibles.
- **Codex Cloud:** entornos alojados, conexiones a repositorios y política de
  ejecución en la nube.
- **Sistemas conectados:** instalación de la aplicación en el proveedor, cuentas y
  permisos.
- **Informes y cumplimiento:** acceso a datos analíticos, exportaciones de auditoría y tratamiento posterior de
  datos.

Decide si cada grupo de usuarios necesita las funciones locales incluidas en la aplicación de escritorio de ChatGPT,
Codex CLI, la extensión para IDE, Codex Cloud o una combinación. Considera
el acceso a la Plataforma API como un ámbito independiente de organización y proyecto cuando un
flujo de trabajo use autenticación mediante claves de API.

## Paso 2: configurar el acceso al espacio de trabajo y la identidad

Usa la membresía, las licencias y los grupos del espacio de trabajo de ChatGPT, así como los permisos RBAC compatibles,
para dar a los grupos de usuarios previstos acceso a las funciones compatibles del espacio de trabajo. Verifica el acceso a los
clientes locales y a Codex Cloud según las indicaciones vigentes del espacio de trabajo, en lugar
de suponer que el mismo rol controla todas las interfaces. Limita los roles
administrativos integrados a las personas que administran el espacio de trabajo.

Los controles y las etiquetas del espacio de trabajo cambian con el tiempo. Consulta estas fuentes para conocer los
procedimientos vigentes:

- [Administrar miembros, tipos de licencia, roles y acceso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Configurar el control de acceso basado en roles](https://help.openai.com/en/articles/11750701-rbac)
- [Administrar la configuración del espacio de trabajo](https://help.openai.com/en/articles/8411955)
- [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
- [Gestión del ciclo de vida de los usuarios](/es-419/codex/enterprise/user-lifecycle)
- [Autenticación](/es-419/codex/auth)

Prueba el inicio de sesión y el acceso a las funciones con un miembro representativo antes de ampliar
la implementación. El acceso al espacio de trabajo no otorga acceso a repositorios, archivos ni acciones
en un servicio conectado.

## Paso 3: configurar los requisitos de ejecución local

Los requisitos locales limitan el comportamiento durante la ejecución cuando un usuario inicia una ejecución
local compatible en la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE. Distribuye
`requirements.toml` mediante un canal compatible en la nube, en el dispositivo o en el sistema. Mantén
esta política separada de los roles y grupos del espacio de trabajo de ChatGPT.

Usa perfiles de permisos para los clientes locales compatibles en lugar de crear nuevas
implementaciones basadas en restricciones heredadas del modo sandbox. Por ejemplo:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

Para deshabilitar Uso de la computadora en todas las interfaces compatibles del navegador y de la aplicación de escritorio,
restringe cada clave pública de función que participa en la experiencia:

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

Para consultar la lista oficial de claves, el funcionamiento de la distribución, la precedencia y más
ejemplos, consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration) y la
[referencia de `requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml).

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## Paso 4: estandarizar la configuración del repositorio

Usa una configuración específica del repositorio para compartir los valores predeterminados, las reglas y las
habilidades del proyecto sin duplicar la configuración para cada usuario. Incorpora la configuración al repositorio en
`.codex` o `.agents`, según la ubicación documentada de la función:

| Tipo          | Fuente                                           | Úsalo para                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| Configuración | [Configuración básica](/es-419/codex/config-file/config-basic) | Establecer valores predeterminados del repositorio para los clientes locales compatibles        |
| Reglas         | [Reglas](/es-419/codex/agent-configuration/rules)        | Controlar los comandos que requieren aprobación fuera del sandbox |
| Habilidades        | [Crear habilidades](/es-419/codex/build-skills)              | Poner los flujos de trabajo del repositorio a disposición de los clientes compatibles   |

La configuración del repositorio puede proporcionar valores predeterminados y flujos de trabajo reutilizables. No puede
otorgar acceso al espacio de trabajo, a modelos, a la Plataforma API ni a sistemas conectados.

## Paso 5: configurar Codex Cloud

Codex Cloud usa entornos alojados y repositorios de código fuente conectados. Planifica
cada ámbito:

1. Otorga al grupo de usuarios previsto acceso a Codex Cloud mediante los controles compatibles del espacio de
trabajo.
2. Instala y configura la integración compatible con el sistema de origen.
3. En el sistema de origen, limita el acceso a los repositorios que cada
grupo de usuarios necesite.
4. Configura los entornos en la nube, los secretos y el acceso a Internet para esos
repositorios.
5. Configura flujos de trabajo alojados opcionales, como la revisión de código.
6. Realiza pruebas con un usuario representativo que tenga los permisos previstos del espacio de trabajo y del
repositorio.

Codex Cloud respeta los permisos y las protecciones del repositorio que proporciona el
sistema de origen conectado. El acceso al espacio de trabajo no permite eludir esos controles. Consulta
[Entornos en la nube](/es-419/codex/environments/cloud-environment),
[Integración con GitHub](/es-419/codex/third-party/github) y
[Aprobaciones y seguridad de agentes](/es-419/codex/agent-approvals-security) para obtener instrucciones sobre la
configuración y la ejecución de Codex Cloud.

## Paso 6: configurar complementos y funciones conectadas

Evalúa como decisiones independientes la instalación de complementos, las habilidades incluidas, las funciones que dependen de conectores,
las acciones de conectores y la autorización del sistema de origen.
Deshabilitar una función que depende de un conector no necesariamente desinstala el
complemento ni sus habilidades incluidas.

Antes de incluir un complemento o una habilidad en la implementación:

1. Confirma su origen, quién es responsable, el grupo de usuarios previsto y la fecha de revisión.
2. Revisa las habilidades incluidas, los conectores, los servidores MCP, los hooks y los datos y
las acciones que requiere cada capacidad.
3. Pruébalo con datos no confidenciales y el nivel mínimo de acceso que necesita.
4. Registra quién es responsable de volver a revisarlo y retirarlo.

Los complementos funcionan en Chat y Work en las versiones web, de escritorio y para dispositivos móviles de ChatGPT,
en Codex dentro de la aplicación de escritorio de ChatGPT y mediante el explorador de complementos de Codex CLI.
No están disponibles en la extensión para IDE.
ChatGPT y Codex comparten un único directorio público universal de complementos; los controles del espacio de trabajo
determinan a cuáles de esos complementos pueden acceder los miembros.

Consulta [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors) y
[Controles de habilidades](/es-419/codex/enterprise/skills) para conocer el modelo completo.

## Paso 7: configurar la gobernanza y la observabilidad

Elige la opción de informes que corresponda a la pregunta:

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- Usa [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics) para
  consultar de forma interactiva la analítica del espacio de trabajo de ChatGPT y la analítica de Codex.
- Usa la [API de análisis](/es-419/codex/enterprise/analytics-api) para generar informes agregados de forma programática
  mediante la API de análisis de Codex.
- Usa la [API de Cumplimiento](/es-419/codex/enterprise/compliance-api) para acceder a registros de auditoría e
  investigación.
- Usa [Límites de uso y controles de gasto de ChatGPT](/es-419/codex/enterprise/usage-limits)
  cuando la actividad de Codex que depende del plan consuma créditos elegibles
  del espacio de trabajo de ChatGPT.

Consulta las referencias de la API que requieren autenticación para obtener información actualizada sobre los requisitos de acceso, los esquemas,
los campos, la retención y el comportamiento de las solicitudes. No desarrolles una integración a partir de una
copia del contrato incluida en esta guía.

Protege el perímetro de integración:

- Almacena las claves de API y otras credenciales de integración en el sistema de gestión
de secretos de la organización.
- Limita el acceso a los sistemas de destino y a los datos conservados
al grupo de usuarios autorizado.
- Protege los registros exportados de la API de Cumplimiento según su nivel de sensibilidad y
la política de retención de la organización, y prueba los flujos de trabajo de recopilación y eliminación
para verificar que cumplan el contrato vigente.

## Paso 8: verificar y mantener la implementación

Verifica todos los ámbitos aplicables con identidades representativas:

- Membresía, licencia y permisos de rol admitidos en el espacio de trabajo de ChatGPT.
- Capacidades locales incluidas en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión
para IDE, incluidos el inicio de sesión y los requisitos de ejecución que se aplican.
- Acceso a Codex Cloud, configuración del entorno y permisos del repositorio.
- Acceso a la organización y al proyecto de la Plataforma API para flujos de trabajo con claves de API.
- Instalación de complementos, habilidades incluidas, acceso a conectores y acciones admitidas.
- Autorización y acceso a datos en sistemas conectados.
- Acceso de los administradores responsables a las funciones de análisis y cumplimiento.

Registra quién es el responsable y cuál es la fuente vigente del procedimiento de cada control. Este registro
permite a los administradores actualizar los procedimientos cuando haya cambios en la interfaz de usuario o en la política sin
cambiar el modelo de administración.

Después de la implementación inicial, revisa el acceso, las capacidades conectadas, el uso de créditos,
los comentarios de soporte y los flujos de trabajo que los equipos realmente usan. Ajusta el alcance de la implementación
y la guía para administradores cuando cambien esos indicadores.
