<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/groups-and-provisioning -->

Los grupos organizan a las personas en un espacio de trabajo de ChatGPT y pueden tener roles personalizados. La
pertenencia a un grupo no sustituye las asignaciones de licencias, no otorga por sí sola permisos para las funciones del
espacio de trabajo, no anula la política del entorno de ejecución local ni proporciona acceso a la Plataforma API
o a los sistemas conectados.

Para conocer el modelo de control completo, consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).

## Compara las fuentes de pertenencia

Usa grupos para personas con una misma necesidad de acceso, como un grupo piloto,
los operadores del espacio de trabajo o los miembros que necesitan la misma función compatible.

### Crea un grupo para una necesidad de acceso compartida

Los propietarios y administradores del espacio de trabajo pueden crear y administrar grupos. Crea un grupo administrado
manualmente para un conjunto pequeño o temporal de personas, o sincroniza un grupo existente
de tu proveedor de identidad cuando la pertenencia deba regirse por tu directorio.

Cada grupo tiene una única fuente de referencia para la pertenencia:

| Tipo de grupo                | Fuente de pertenencia                   | Cuándo se aplica                                                                  |
| ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| Administrado manualmente          | Administración del espacio de trabajo de ChatGPT    | El grupo es pequeño, temporal o no se administra mediante la sincronización de directorios             |
| Administrado por un proveedor de identidad | Tu proveedor de identidad mediante SCIM | La pertenencia debe regirse por el directorio de la organización y su proceso de baja de miembros |

Los grupos administrados manualmente pueden coexistir con los administrados por un proveedor de identidad. En los grupos
sincronizados, el proveedor de identidad es la fuente de pertenencia; las actualizaciones posteriores de aprovisionamiento
pueden sobrescribir los cambios realizados en el espacio de trabajo. El Centro de ayuda es la fuente de referencia sobre el comportamiento actual de SCIM,
los atributos compatibles y los pasos de configuración.

## Comprende los límites del acceso

La pertenencia a un grupo no otorga por sí sola permisos para las funciones del espacio de trabajo.

### Vincula un grupo con los permisos adecuados

Los propietarios del espacio de trabajo pueden asignar roles personalizados a grupos o, cuando esa opción esté disponible, directamente
a los miembros. Revisa todos los roles aplicables: un valor explícito de **Desactivado** en cualquier rol
deniega ese permiso, incluso si otro rol lo otorga. El tipo de licencia del miembro
y su elegibilidad para el producto siguen aplicándose.

SCIM aprovisiona la pertenencia al espacio de trabajo y las asignaciones a grupos. No otorga
permisos en GitHub, Google Drive, Slack ni ningún otro sistema conectado. Tampoco
sustituye los requisitos del entorno de ejecución local ni el acceso a la organización de la Plataforma API.

El RBAC del espacio de trabajo y los requisitos del entorno de ejecución local son sistemas de control independientes. Un
grupo puede ser relevante para ambos, pero no deduzcas una regla de coincidencia
o precedencia para los requisitos administrados a partir del orden de los grupos del espacio de trabajo. Consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration) para conocer las
reglas documentadas de distribución y precedencia local.

## Usa los procedimientos de configuración vigentes

Los detalles de administración del espacio de trabajo pueden cambiar. Consulta estas fuentes para conocer los pasos vigentes en la interfaz de usuario,
la disponibilidad y los límites:

- [Administrar miembros, tipos de licencia, roles y acceso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Administrar grupos](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)
- [Preguntas frecuentes sobre la integración con SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
- [Administrar la configuración del espacio de trabajo](https://help.openai.com/en/articles/8411955)

### Verifica las altas, los cambios y las bajas

- **Altas:** confirma que el miembro acepte cualquier invitación pendiente al espacio de trabajo y
  reciba la licencia prevista, se incorpore a los grupos correspondientes y obtenga los permisos y las funciones compatibles
  previstos.
- **Cambios:** actualiza la fuente de referencia para la pertenencia y verifica los
  permisos efectivos del miembro en todos los roles aplicables.
- **Bajas:** revoca el acceso de un miembro administrado mediante SCIM a través del proveedor
  de identidad y confirma que ya no pueda acceder al espacio de trabajo. Si
  solo eliminas al miembro del espacio de trabajo, una sincronización posterior puede restablecer
  su acceso.

## Documentación relacionada

- [Gestión del ciclo de vida de los usuarios](/es-419/codex/enterprise/user-lifecycle)
- [Autenticación](/es-419/codex/auth)
- [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
- [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
