<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/apps-and-connectors -->

Los complementos agrupan flujos de trabajo reutilizables y pueden incluir habilidades y apps que se conectan
a otras herramientas. ChatGPT y Codex usan el mismo directorio público de complementos en las
interfaces compatibles, mientras que los administradores deciden qué complementos están disponibles en su espacio de trabajo.
Obtén más información sobre [complementos](/es-419/codex/plugins),
[habilidades](/es-419/codex/skills-and-plugins) y
[apps y conectores](https://help.openai.com/en/articles/11487775).

Un miembro puede usar una capacidad basada en un conector solo cuando el complemento y la app
están disponibles para su rol y tiene acceso al servicio conectado.

Los complementos funcionan en Chat y Work en las versiones web, de escritorio y para dispositivos móviles de ChatGPT,
en Codex dentro de la aplicación de escritorio de ChatGPT y mediante el navegador de complementos de Codex CLI.
No están disponibles en la extensión para IDE.

Para ver cómo se relacionan estos controles con los roles y permisos del espacio de trabajo, consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).

## Comprender la cadena de capacidades

Un complemento puede abarcar estas capas de control:

| Capa                   | Qué determina                                                           | Dónde se administra                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Disponibilidad            | Si el paquete del complemento está disponible para el usuario                           | [Configuración del espacio de trabajo](https://chatgpt.com/admin/settings) para las interfaces web y de escritorio compatibles; el navegador de complementos de la CLI para la CLI |
| Habilidades incluidas         | Qué instrucciones reutilizables aporta el complemento instalado                 | El paquete del complemento y los [Controles de habilidades](/es-419/codex/enterprise/skills)                                                               |
| Acceso a la App              | Si los usuarios pueden usar una capacidad basada en un conector                          | [Apps del espacio de trabajo](https://chatgpt.com/admin/ca) y [Permisos y roles](https://chatgpt.com/admin/settings)                    |
| Acciones y permisos | Qué acciones pueden ejecutar los usuarios y cuándo ChatGPT solicita confirmación antes de usar el conector | El Control de acciones del conector y los Permisos de App en [Apps del espacio de trabajo](https://chatgpt.com/admin/ca)                            |
| Autorización del servicio   | A qué datos y acciones externos puede acceder la identidad autenticada        | El servicio conectado y su proveedor de identidad                                                                                 |
| Permisos del entorno de ejecución     | Qué puede hacer un agente después de recibir datos o una herramienta                        | Los controles del entorno de ejecución, del sandbox y de aprobación para la interfaz activa                                                              |

Usa estas capas para una implementación en dos pasos: primero, pon a disposición los complementos adecuados;
luego, configura las capacidades y los permisos que necesita cada flujo de trabajo.

## Paso 1: habilitar la disponibilidad de los complementos

En las interfaces web y de escritorio compatibles, los controles de complementos del espacio de trabajo determinan
qué roles pueden usar o instalar un complemento. Codex CLI usa su propio navegador de
complementos para la instalación. Consulta
[Crear plugins](https://developers.openai.com/plugins/build/plugins) para obtener información sobre
el empaquetado y la distribución.

Para importar complementos de GitHub al espacio de trabajo y mantenerlos actualizados, consulta
[Administración de complementos](/es-419/codex/enterprise/plugin-management).

### Exportar el catálogo público para su revisión

Los propietarios y administradores de espacios de trabajo de ChatGPT Enterprise que cumplan los requisitos pueden descargar un CSV de
los complementos públicos disponibles en su espacio de trabajo. Usa la exportación para revisar
los metadatos de complementos, apps y habilidades antes de cambiar la disponibilidad de los complementos.

1. Abre [Administración \> Complementos](https://chatgpt.com/admin/plugins).
2. Selecciona **Públicos**.
3. Selecciona el ícono de descarga (**Exportar CSV**) en el encabezado de la página.

El archivo descargado se llama `public-plugins-security-review.csv` e incluye:

- Metadatos del complemento: `Plugin Name`, `Plugin Description`, `Date Added (UTC)`,
`OpenAI Verified`, `Developer Name` y `Version`.
- Metadatos de la App: `App Name(s)` y `App Description(s)`.
- Metadatos de las habilidades de Chat: `Skill Name(s)` y `Skill Description(s)`.

Cuando un complemento incluye más de una app o habilidad, los valores correspondientes
se separan con punto y coma. La exportación usa una instantánea del catálogo público que puede tener
hasta 48 horas de antigüedad,
incluye únicamente los complementos públicos visibles para el espacio de trabajo actual y no
incluye los complementos creados para ese espacio de trabajo. No está disponible en los espacios de trabajo
de FedRAMP.

## Paso 2: administrar las capacidades

  Poner una app o un complemento a disposición en ChatGPT no otorga acceso a archivos,
registros ni acciones en el servicio conectado. Antes de solucionar problemas o
ampliar el acceso, verifica el rol del miembro en el espacio de trabajo y la configuración de las acciones
aprobadas. Luego, confirma que la cuenta autenticada o la conexión compartida tenga los
permisos previstos en el servicio conectado.

Los complementos de ChatGPT y Codex pueden incluir conectores que permiten buscar, recuperar o sincronizar información,
o actuar sobre sistemas externos. La disponibilidad de los complementos y el acceso y las acciones
permitidos para cada conector se controlan por separado.

Administra las capacidades basadas en conectores desde
[Apps del espacio de trabajo](https://chatgpt.com/admin/ca) y
[Permisos y roles](https://chatgpt.com/admin/settings). Los controles disponibles
permiten a los administradores:

- Habilitar apps o conectores y asignar el acceso según el rol del espacio de trabajo.
- Para los conectores que admiten Control de acciones, permitir acciones de solo lectura o un
conjunto personalizado aprobado y definir cómo el espacio de trabajo gestiona las acciones recién agregadas.
- Configurar los Permisos de App que determinan cuándo ChatGPT solicita confirmación antes de usar una app.
- Mantener el acceso dentro de los alcances y permisos otorgados por cada servicio
conectado y cada usuario autenticado.

Para conocer la disponibilidad y los procedimientos vigentes, consulta
[Controles de administración, seguridad y cumplimiento en apps](https://help.openai.com/en/articles/11509118).

<a id="choose-a-starting-set-of-apps"></a>

## Elegir un conjunto inicial con un objetivo claro

Comienza con complementos que respondan a una necesidad empresarial concreta. Decide si cada complemento
estará disponible para todos, se limitará a un rol o grupo piloto, o requerirá
una revisión adicional.

Para cada servicio conectado, registra el responsable en la empresa, los datos permitidos, las acciones de lectura o escritura
aprobadas, el método de autenticación y un contacto para soporte o solicitudes de eliminación.

Antes de habilitar acciones de escritura o publicar una nueva capacidad conectada, verifica
a qué roles se aplica y realiza pruebas con una cuenta que solo tenga los permisos previstos
en el servicio conectado.

Para una implementación amplia, comienza con categorías que los equipos usan a diario, como el correo electrónico,
el calendario y los sistemas de archivos o documentos. Usa el
[Directorio de complementos](https://chatgpt.com/apps) para confirmar la disponibilidad
y las capacidades actuales en las interfaces compatibles de ChatGPT y Codex.

Sin importar el conjunto inicial, comienza con acciones de lectura. Antes de habilitar acciones de escritura,
identifica al responsable del complemento, revisa los alcances del conector y los permisos del servicio,
confirma el acceso a los datos y documenta los efectos externos y una vía
de recuperación.

## Comprender el flujo de datos y la seguridad

Cuando ChatGPT usa una app o un conector incluidos en un complemento, envía una solicitud
al servicio conectado y devuelve datos o resultados de acciones autorizados por los
permisos del usuario autenticado en ese servicio.

ChatGPT gestiona los datos de las apps conectadas de dos maneras:

- **Sin sincronización:** ChatGPT procesa de forma transitoria los datos de Chat y de investigación profunda
  y no los indexa.
- **Con sincronización:** ChatGPT indexa de antemano el contenido seleccionado de las fuentes conectadas. Puedes consultar
  en la página del complemento si una app admite la sincronización.

El modo cambia la forma en que ChatGPT indexa el contenido de las fuentes conectadas; no reemplaza
los controles habituales de retención de chats. Las conversaciones de ChatGPT que usan apps siguen
disponibles a través de la API de Cumplimiento.

La documentación de OpenAI sobre apps detalla el cifrado en tránsito y en reposo, la autorización por usuario, los controles de roles y acciones y el acceso restringido a la red para las conversaciones que usan apps. También indica que, para los clientes de Business, Enterprise y Edu, la información a la que se accede a través de apps no se usa para entrenar modelos. Cuando una solicitud llega a un servicio conectado, también se aplican los alcances, la retención, la residencia de datos y las demás políticas de ese servicio.

Consulta [seguridad y cumplimiento de las apps](https://help.openai.com/en/articles/11509118)
y [apps con sincronización](https://help.openai.com/en/articles/10847137) para obtener información actualizada sobre el
manejo de datos. Para los servidores MCP configurados localmente en la app de escritorio
de ChatGPT, Codex CLI o la extensión para IDE, consulta la
[configuración de MCP en Codex](/es-419/codex/extend/mcp).

## Usa procedimientos y referencias actualizados

- [Controles de administración, seguridad y cumplimiento en apps](https://help.openai.com/en/articles/11509118)
- [Apps en ChatGPT](https://help.openai.com/en/articles/11487775)
- [Apps con sincronización](https://help.openai.com/en/articles/10847137)
- [Administrar la configuración del espacio de trabajo](https://help.openai.com/en/articles/8411955)
- [Complementos](/es-419/codex/plugins)
- [Habilidades y complementos](/es-419/codex/skills-and-plugins)
- [Crear plugins](https://developers.openai.com/plugins/build/plugins)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
