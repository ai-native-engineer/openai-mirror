<!-- source: https://learn.chatgpt.com/es-419/docs/security/security-review -->

La Revisión de Codex Security está disponible como versión preliminar de investigación.
Está disponible para clientes de ChatGPT Enterprise, Business, Edu y Pro, pero
no está disponible en Plus. Durante el período introductorio, la Revisión de Codex Security
no consume créditos de ChatGPT. Pueden aplicarse límites de uso.

La Revisión de Codex Security es una revisión adicional para los clientes que desean
prestar especial atención a los problemas de seguridad en los pull requests.

La Revisión de Codex Security analiza los riesgos específicos de seguridad con mayor profundidad que la [Revisión
de código](/es-419/codex/third-party/github) mediante el análisis del
diff del pull request, el contexto complementario del repositorio y los modelos de amenazas
o lineamientos de seguridad configurados. La Revisión de código también puede identificar problemas relacionados con la seguridad
como parte de su revisión general, por lo que es posible que algunos hallazgos coincidan.

## Antes de comenzar

Para configurar la ejecución automática de la Revisión de Codex Security, necesitas:

- Acceso de tu espacio de trabajo a la versión preliminar de investigación de la Revisión de Codex Security
- [Codex Cloud](/es-419/codex/cloud) configurado con un repositorio de GitHub conectado
- Permiso de push o de administrador en GitHub para la configuración del repositorio

Contar con un análisis existente de Codex Security es opcional.

<a id="configure-security-review"></a>

## Configurar la Revisión de Codex Security

1. Ve a [Configuración de Codex](https://chatgpt.com/codex/settings/code-review).
2. En **Preferencias del repositorio**, elige qué pull requests recibirán una
   Revisión de Codex Security:
   - **Usar configuración personal** permite que cada colaborador elija participar según su configuración personal de la
     Revisión de Codex Security.
   - **Revisar todos los Pull requests** se aplica a todos los pull requests del repositorio.
   - **Revisar los Pull requests del equipo**, cuando esté disponible, se aplica a los pull requests abiertos por
     miembros de tu espacio de trabajo de ChatGPT, no por miembros de un equipo de GitHub.
3. Elige cuándo se ejecutará la Revisión de Codex Security:
   - **Al abrir un Pull Request** se ejecuta de forma independiente cuando se abre un pull request.
   - **Con cada push** se ejecuta de forma independiente después de hacer push de commits nuevos.
   - La opción **Cada vez que se ejecute la revisión de código** requiere que se ejecute la Revisión de código y ejecuta al mismo tiempo la
     Revisión de Codex Security.

## Agregar contexto del modelo de amenazas

Puedes configurar un modelo de amenazas para proporcionar a Codex contexto sobre tu aplicación: sus
activos, límites de confianza, supuestos de seguridad y riesgos específicos del repositorio.
Si el repositorio tiene una configuración existente de análisis de Codex Security, puedes usar
su modelo de amenazas. De lo contrario, proporciona la ruta a un archivo de modelo de amenazas incluido
en el repositorio. Si no especificas una fuente, Codex vuelve a generar el
modelo de amenazas para cada revisión.

## Establecer los umbrales de reporte

De forma predeterminada, las revisiones automáticas de Codex Security reportan hallazgos de gravedad **Alta** y **Crítica**,
mientras que las revisiones solicitadas manualmente reportan hallazgos de gravedad **Media**, **Alta** y
**Crítica**. Puedes cambiar la gravedad mínima por separado para
las revisiones automáticas y manuales, además de agregar excepciones basadas en rutas.

Los hallazgos publicados en un pull request heredan la visibilidad en GitHub
de ese pull request. Cualquier persona que pueda ver el pull request puede ver esos hallazgos,
incluso en repositorios públicos o en pull requests de colaboradores que no pertenecen
a tu espacio de trabajo. Elige con cuidado los umbrales de reporte en los repositorios donde
los comentarios de los pull requests podrían tener amplia visibilidad. El umbral de reporte controla
qué publica Codex en GitHub; el informe completo de la Revisión de Codex Security permanece en
Codex.

<a id="request-a-security-review"></a>

## Solicitar una Revisión de Codex Security

Para solicitar manualmente una Revisión de Codex Security, agrega este comentario a un pull request:

`@codex security review`

Codex agrega una reacción mientras se ejecuta la revisión y luego publica directamente en el pull request los hallazgos que cumplen con tu
umbral de reporte manual. Abre la tarea de Codex asociada
y selecciona la pestaña **Informe de seguridad** para ver el informe completo,
que incluye la gravedad, la ruta de ataque, la evidencia de respaldo, la validación y
la orientación para la remediación. Si no hay problemas que cumplan con el umbral de reporte, Codex no
publica hallazgos en el pull request.

## Documentación relacionada

- [Revisar pull requests de GitHub con Codex](/es-419/codex/third-party/github) explica la Revisión de código y la integración con GitHub.
- [Codex Security](/es-419/codex/security) presenta una descripción general del producto.
- [Configuración de Codex Security en la nube](/es-419/codex/security/setup) explica los análisis de repositorios y la revisión de hallazgos.
- [Mejorar el modelo de amenazas](/es-419/codex/security/threat-model) explica cómo ajustar el contexto del repositorio.
