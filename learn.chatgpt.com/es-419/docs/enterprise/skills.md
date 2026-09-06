<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/skills -->

Las habilidades son flujos de trabajo reutilizables compuestos por instrucciones y recursos de apoyo.
Las habilidades del espacio de trabajo de ChatGPT, las habilidades del sistema de archivos utilizadas por las capacidades locales incluidas
en la app de escritorio de ChatGPT, Codex CLI o la extensión para IDE, y los complementos que
empaquetan habilidades tienen controles independientes de ciclo de vida y acceso.

Para conocer el modelo de administración completo, consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).

<a id="distinguish-the-distribution-models"></a>

## Distribución y administración de habilidades

| Modelo de distribución      | Para qué usarlo                                                                                           | Ámbito de administración                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Habilidad del espacio de trabajo de ChatGPT | Compartir o instalar un flujo de trabajo aprobado mediante las funciones del espacio de trabajo de ChatGPT que permiten hacerlo              | Permisos y controles del ciclo de vida para las habilidades del espacio de trabajo de ChatGPT                                    |
| Habilidad del sistema de archivos local  | Cargar un flujo de trabajo instalado desde una ubicación del repositorio, del usuario o del administrador, o desde una ubicación incluida con el sistema     | Distribución mediante el sistema de archivos, configuración del cliente local y permisos en tiempo de ejecución                  |
| Complemento                  | Empaquetar una o más habilidades con conectores, servidores MCP, hooks y metadatos de presentación opcionales | Disponibilidad e instalación de complementos, además de los controles independientes para cada capacidad incluida |

La distribución de habilidades del espacio de trabajo de ChatGPT, la instalación de habilidades en el sistema de archivos local y
la instalación de complementos específica de cada entorno son procesos independientes. Mover una habilidad no
transfiere su propiedad, la configuración de uso compartido ni sus asignaciones de roles en el espacio de trabajo de ChatGPT; tampoco transfiere el estado de
instalación del complemento ni la autorización del conector.

Los complementos funcionan en Chat y Work en las versiones web, de escritorio y para dispositivos móviles de ChatGPT,
en Codex dentro de la app de escritorio de ChatGPT y mediante el navegador de complementos de Codex CLI.
No están disponibles en la extensión para IDE.
Esos entornos compatibles obtienen los complementos públicos de un único directorio universal
que comparten ChatGPT y Codex.

## Controles correspondientes

Consulta [Crear habilidades](/es-419/codex/build-skills) para obtener información sobre las ubicaciones en el sistema de archivos y cómo crear habilidades,
[Habilidades en ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
para conocer los procedimientos vigentes del espacio de trabajo y [Crear plugins](https://developers.openai.com/plugins/build/plugins) para
saber cómo empaquetar complementos.

Los controles del espacio de trabajo de ChatGPT no instalan habilidades del sistema de archivos local ni complementos.
La distribución mediante el sistema de archivos no asigna la propiedad ni roles dentro del espacio de trabajo de ChatGPT.
La instalación de complementos no concede acceso a un conector, un servidor MCP ni un
servicio conectado. Configura cada capacidad mediante la interfaz de control que le
corresponda.

## Documentación relacionada

- [Habilidades y complementos](/es-419/codex/skills-and-plugins)
- [Complementos](/es-419/codex/plugins)
- [Crear habilidades](/es-419/codex/build-skills)
- [Crear plugins](https://developers.openai.com/plugins/build/plugins)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors)
