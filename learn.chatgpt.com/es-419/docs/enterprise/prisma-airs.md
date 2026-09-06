<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/prisma-airs -->

Conecta Palo Alto Networks Prisma AIRS para aplicar tus políticas de seguridad a los
prompts de Codex antes de que lleguen al modelo. Los administradores del espacio de
trabajo configuran la integración una sola vez en ese espacio.

Prisma AIRS puede aplicar las protecciones configuradas en tu perfil de seguridad, como
la prevención de pérdida de datos, la detección de inyección de prompts y la detección
de URL maliciosas.

## Antes de comenzar

Necesitas:

- Un espacio de trabajo de ChatGPT con el acceso a Prisma AIRS habilitado. Comunícate con el equipo de OpenAI
a cargo de tu cuenta para solicitar acceso.
- Permisos de administrador del espacio de trabajo.
- Una clave de API de Prisma AIRS, un perfil de seguridad configurado y el punto de acceso del servicio
para tu implementación.

## Conectar Prisma AIRS

1. Abre [Controles de datos de Codex](https://chatgpt.com/codex/cloud/settings/data) como
   administrador del espacio de trabajo.
2. En **Medidas de protección externas**, busca **Prisma AIRS**. Si esta sección no está
   disponible, pide al equipo de OpenAI a cargo de tu cuenta que habilite el acceso para tu espacio de trabajo.
3. Ingresa la **Clave de API**, el nombre o ID del **Perfil de seguridad** y la **URL del
   punto de acceso**.
4. Elige un **Modo de aplicación** y qué hacer **En caso de falla de AIRS**.
5. Selecciona **Guardar conexión**. Codex valida la conexión y cifra tu
   clave de API.
6. Selecciona **Probar conexión** para verificar la configuración guardada.
7. Activa **Habilitar Prisma AIRS** para comenzar a analizar los prompts de todo el
   espacio de trabajo.

Guardar la conexión no habilita el análisis. También debes activar **Habilitar
Prisma AIRS**.

## Elegir un punto de acceso

Usa el punto de acceso aprobado para tu implementación de Prisma AIRS:

| Región        | Punto de acceso                                                 |
| ------------- | -------------------------------------------------------- |
| Estados Unidos | `https://service.api.aisecurity.paloaltonetworks.com`    |
| Alemania       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| India         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| Singapur     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex usa el punto de acceso de Estados Unidos de forma predeterminada. Los requisitos de residencia de datos
del espacio de trabajo pueden restringir el punto de acceso que puedes usar.

## Elegir cómo procesar los prompts

El **Modo de aplicación** determina qué ocurre cuando Prisma AIRS marca un prompt:

- **Bloquear**: detiene el prompt antes de que llegue al modelo. Esta es la opción predeterminada.
- **Solo alertar**: registra la detección y permite que el prompt continúe.

La opción **En caso de falla de AIRS** determina qué ocurre si Prisma AIRS no está disponible o
no responde:

- **Permitir prompts**: permite que el prompt continúe sin que se complete el análisis. Esta es la opción predeterminada.
- **Bloquear prompts**: detiene el prompt hasta que Prisma AIRS pueda analizarlo.

Elige **Bloquear prompts** cuando tu política de seguridad exija que cada prompt sujeto a esa política
reciba una decisión basada en el análisis.

## Entender qué se analiza

Codex envía el texto de los prompts recién enviados al punto de acceso configurado de Prisma AIRS
para su inspección. Esto se aplica a los flujos de trabajo de Codex que abarca la integración, entre ellos la App, la CLI,
la Extensión para IDE y la Nube, cuando los usuarios se autentican en el espacio de trabajo de ChatGPT
configurado. Las sesiones autenticadas con una clave de API de la Plataforma no están incluidas. Consulta
[Exigir un método de inicio de sesión o un espacio de trabajo](/es-419/codex/auth#enforce-a-login-method-or-workspace)
para exigir el método de inicio de sesión y el espacio de trabajo previstos.

Prisma AIRS no analiza las respuestas del asistente, las llamadas a herramientas, los resultados de herramientas, los archivos,
ni las imágenes mediante esta integración. El perfil de seguridad configurado determina
qué amenazas y datos sensibles detecta Prisma AIRS.

Codex cifra tu clave de API y no vuelve a mostrarla después de guardarla. Revisa las políticas de Palo
Alto Networks sobre el manejo, la retención y la residencia de datos antes de habilitar
la inspección de prompts. Esas políticas se aplican a los prompts enviados a Prisma AIRS.

## Administrar la conexión

Vuelve a [Controles de datos de Codex](https://chatgpt.com/codex/cloud/settings/data)
para administrar la integración:

- Selecciona **Probar conexión** para verificar la clave de API, el perfil de seguridad
  y el punto de acceso guardados.
- Ingresa una clave nueva y selecciona **Rotar clave de API** para reemplazar la clave guardada
  sin cambiar el resto de la configuración.
- Desactiva **Habilitar Prisma AIRS** para detener el análisis y conservar la
  configuración guardada.
- Selecciona **Desconectar** y luego confirma para detener el análisis y eliminar la
  conexión guardada y la clave de API.

Para configurar el espacio de trabajo y administrar políticas a mayor escala, consulta la
[Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup) y la
[Configuración administrada](/es-419/codex/enterprise/managed-configuration).
