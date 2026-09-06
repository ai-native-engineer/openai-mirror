<!-- source: https://learn.chatgpt.com/es-419/docs/build-plugins -->

Para crear o enviar un complemento, consulta la documentación completa
[para crear complementos en developers.openai.com](/plugins).

<div className="not-prose my-6">
  
    Crear y enviar un complemento
  
</div>

Esta página ofrece una breve introducción. Un complemento es un paquete instalable
que puede incluir habilidades, un Servidor MCP o ambos. Un Servidor MCP también puede devolver
una interfaz de usuario opcional.

ChatGPT y Codex comparten un único directorio universal de complementos. Publica un complemento público
una sola vez para que una misma ficha se pueda encontrar en las interfaces compatibles de ambos
productos. Durante el desarrollo, usa un Marketplace local para probar el paquete
antes de enviarlo al directorio universal.

Para distribuir complementos en un espacio de trabajo a través de GitHub, consulta
[Administración de complementos](/es-419/codex/enterprise/plugin-management).

Empieza con una habilidad mientras sigues perfeccionando un flujo de trabajo personal.
Crea un complemento cuando quieras compartir ese flujo de trabajo, empaquetar habilidades relacionadas,
conectarte a un servicio externo o distribuir una capacidad estable a un equipo.

## Crear un complemento con `@plugin-creator`

Para completar la configuración lo más rápido posible, usa la habilidad integrada `@plugin-creator` en el modo Work
de ChatGPT o `$plugin-creator` en Codex.

  
    
  

Describe el resultado, las habilidades o el Servidor MCP que quieras incluir y si deseas
una ficha en un Marketplace local para hacer pruebas. Por ejemplo:

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

La habilidad crea el archivo de manifiesto obligatorio `.codex-plugin/plugin.json`, organiza
la carpeta del complemento y puede agregar el complemento a un Marketplace local.

  
    
  

Cuando termine:

1. Revisa `.codex-plugin/plugin.json`.
2. Verifica cada habilidad incluida en `skills/`.
3. Vuelve a cargar ChatGPT o Codex e instala el complemento desde su Marketplace local
de origen.
4. Prueba el complemento en una conversación nueva con solicitudes representativas.

Si el complemento incluye un Servidor MCP, primero crea y prueba ese servidor y luego
proporciona a `@plugin-creator` los detalles de la conexión registrada. Sigue el
[flujo de trabajo completo del Servidor MCP](https://developers.openai.com/plugins/build/mcp-server)
para las herramientas, la autenticación, el despliegue y las pruebas.

## Crear manualmente un complemento solo con habilidades

Un complemento mínimo contiene un archivo de manifiesto y al menos una habilidad:

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

Crea `.codex-plugin/plugin.json`:

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

Luego, agrega `skills/meeting-follow-up/SKILL.md`:

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

Usa un nombre estable para el complemento en kebab case. La descripción de la habilidad debe ser lo bastante específica
para que ChatGPT y Codex reconozcan cuándo corresponde usar el flujo de trabajo.

Usa `@plugin-creator` para agregar la carpeta a un Marketplace local; luego, instala y
prueba el complemento antes de compartirlo.

## Continuar con la documentación para crear complementos

Para acceder a la documentación completa sobre cómo crear complementos, consulta la
[documentación de Complementos](https://developers.openai.com/plugins/). Abarca:

- [Arquitectura de complementos](https://developers.openai.com/plugins/concepts/plugins)
- [Crear habilidades](https://developers.openai.com/plugins/build/skills)
- [Crear un Servidor MCP](https://developers.openai.com/plugins/build/mcp-server)
- [Agregar una interfaz de usuario opcional](https://developers.openai.com/plugins/build/chatgpt-ui)
- [Empaquetar un complemento](https://developers.openai.com/plugins/build/plugins)
- [Probar un complemento](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Enviar y publicar](https://developers.openai.com/plugins/deploy/submission)

Para explorar, instalar, habilitar o quitar complementos, consulta [Usar
complementos](/es-419/codex/plugins).
