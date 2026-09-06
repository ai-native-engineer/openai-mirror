<!-- source: https://learn.chatgpt.com/es-419/docs/amazon-bedrock -->

Configura las interfaces locales de ChatGPT Work y Codex para usar los modelos de OpenAI disponibles
a través de Amazon Bedrock. En esta configuración, el cliente local envía solicitudes de modelos a
Bedrock mediante la autenticación y los controles de acceso administrados por AWS.

## Cómo funciona

Cuando configuras una interfaz local de ChatGPT Work o Codex con Amazon Bedrock como
proveedor de modelos, la Responses API alojada por OpenAI no forma parte de la ruta de solicitud.
El cliente local envía las solicitudes de modelos a Amazon Bedrock, y Bedrock proporciona una
implementación de Responses API compatible con OpenAI para los modelos de OpenAI admitidos.

  La autenticación es nativa de AWS. Los usuarios se autentican con una clave de API de Bedrock o credenciales de AWS
  IAM. No usan el inicio de sesión de ChatGPT ni `OPENAI_API_KEY` para este
  proveedor.

## Antes de comenzar

Asegúrate de tener:

- Acceso a modelos de OpenAI compatibles en Amazon Bedrock.
- Una región de AWS donde esté disponible el modelo seleccionado.
- Autenticación para la ruta de Amazon Bedrock Mantle configurada para la cuenta de
AWS.

## Configurar el proveedor

Agrega el proveedor de modelos `amazon-bedrock` para la ruta de Amazon Bedrock Mantle a
`~/.codex/config.toml`. La aplicación de escritorio de ChatGPT, Codex CLI, la extensión para IDE y el
SDK leen las mismas capas de configuración local. Especificar un modelo es opcional.
Selecciona explícitamente un modelo compatible cuando sea necesario.

```toml
model_provider = "amazon-bedrock"

  Esta guía abarca la ruta de Amazon Bedrock Mantle en las regiones comerciales de AWS
compatibles. Las interfaces locales de ChatGPT Work y Codex no admiten puntos de acceso de Bedrock Mantle
en las regiones de AWS GovCloud.

## Opciones de autenticación

Las interfaces locales de ChatGPT Work y Codex admiten dos métodos de autenticación de Bedrock.
Los comprueban en este orden:

1. Clave de API de Bedrock.
2. Cadena de credenciales del SDK de AWS.

### Opción 1: clave de API de Bedrock

Configura la clave de API de Bedrock en el entorno que lee el cliente local. Debes
especificar una región cuando uses la autenticación mediante clave de API.

```shell

### Opción 2: credenciales del SDK de AWS

Usa este método cuando tu organización administre el acceso a Bedrock mediante la cadena de credenciales del SDK
de AWS. El cliente local puede usar estas fuentes estándar de credenciales del SDK de
AWS:

#### Archivos de configuración compartidos de AWS

Configura los archivos compartidos `config` y `credentials` de AWS:

```shell
aws configure

#### Variables de entorno

Configura las variables de entorno estándar para las credenciales del SDK de AWS:

```shell

#### Credenciales de AWS Management Console

Inicia sesión con credenciales de AWS Management Console:

```shell
aws login

#### AWS SSO o un perfil con nombre

Inicia sesión con AWS SSO y selecciona el perfil con nombre:

```shell
aws sso login --profile codex-bedrock

#### Identidad federada

Para el SSO corporativo o la federación OIDC, configura una identidad federada con
`credential_process` fuera del cliente local y permite que el SDK de AWS resuelva las
credenciales. Incluye el inicio de sesión en el navegador, el intercambio de tokens, el almacenamiento en caché y la renovación en la
utilidad auxiliar `credential_process` de tu perfil de AWS.

## App de escritorio y extensión para IDE

Es posible que las aplicaciones de escritorio y las extensiones para IDE no hereden las variables de entorno del
shell. Coloca los valores necesarios en `~/.codex/.env` y, luego, reinicia la aplicación o la
extensión.

```shell

## Verificar la configuración

- En Codex CLI, abre `/status` y confirma que Codex usa el proveedor de modelos
`amazon-bedrock`.
- En la aplicación de escritorio de ChatGPT, selecciona Work o Codex e inicia una tarea nueva después de
reiniciar la aplicación.
- En la extensión para IDE, inicia una sesión nueva después de reiniciar la extensión.
- Confirma que el modelo seleccionado esté disponible en la región de AWS configurada y que
la identidad de AWS tenga permiso para acceder a él.

## Modelos compatibles

Usa los ID exactos de los modelos:

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

La disponibilidad de los modelos varía según la región de AWS. Antes de seleccionar un modelo, consulta [la compatibilidad de los modelos
por región
de AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html).

## Disponibilidad de funciones

Esta configuración admite flujos de trabajo locales de ChatGPT Work y Codex. ChatGPT Work alojado
en la web, Codex Cloud y las funciones que dependen de servicios en la nube alojados por OpenAI,
herramientas alojadas o descubrimiento administrado en la nube no están disponibles
actualmente.

  El Modo rápido no está disponible con Amazon Bedrock. El Modo rápido usa procesamiento
prioritario, y la oferta inicial de Amazon Bedrock solo admite inferencia
bajo demanda.

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> Actualmente, esta función solo está disponible en regiones específicas. Consulta
    la documentación de cada función para obtener más información sobre las restricciones geográficas.
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> Están disponibles los paquetes locales de complementos y los complementos seleccionados por OpenAI que no
    requieren autenticación de ChatGPT, incluido Codex Security.
    No están disponibles los complementos que requieren autenticación de ChatGPT, conectores o uso compartido
    alojado en la nube.
  </div>

## Solución de problemas

Si la configuración falla, verifica lo siguiente:

- El ID del modelo coincide exactamente con un modelo compatible.
- Especificas una región de AWS donde el modelo está disponible.
- La clave de API de Bedrock o las credenciales de AWS son válidas y no han caducado.
- La identidad de AWS tiene permiso para acceder al modelo de Bedrock seleccionado.
- `AWS_BEARER_TOKEN_BEDROCK` no está configurado con una clave caducada o incorrecta.
- Para usar la app de escritorio o la extensión para IDE, las variables de entorno necesarias están
  presentes en `~/.codex/.env`.

## Alcance del soporte

El Soporte de OpenAI puede ayudar con la puesta en marcha y la configuración del cliente de ChatGPT Work y Codex,
el funcionamiento local de la CLI, el funcionamiento de la app de escritorio y de la extensión para IDE,
y la experiencia local del producto.

Para consultas sobre credenciales de AWS, permisos de IAM, acceso a modelos de Bedrock, cuotas, facturación,
disponibilidad regional, errores en las solicitudes de Bedrock, registros de servicios de AWS o el funcionamiento del servicio de Bedrock,
comunícate con el administrador de AWS del cliente o con AWS Support.
