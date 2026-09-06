<!-- source: https://learn.chatgpt.com/es-419/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Elige un modelo

En la aplicación de escritorio de ChatGPT, usa el control de modelo y razonamiento que aparece debajo del
editor para elegir un modelo disponible y ajustar su esfuerzo de razonamiento.

Un mayor esfuerzo de razonamiento puede mejorar los resultados en tareas complejas, pero requiere
más tiempo y usa más tokens. Comienza con el esfuerzo predeterminado y auméntalo cuando
la tarea requiera una planificación o un análisis más profundos.

El modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> va
más allá de una ejecución con un solo agente. Usa
[subagentes](/codex/agent-configuration/subagents) para acelerar el trabajo complejo,
por lo que resulta útil para tareas de mayor alcance que pueden dividirse entre subagentes.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Elige un modelo

Estas recomendaciones se aplican a **ChatGPT Work** en la web. Usa el
control de modelo y razonamiento que aparece debajo del editor para elegir un modelo disponible
y ajustar su esfuerzo de razonamiento.

Un mayor esfuerzo de razonamiento puede mejorar los resultados en tareas complejas, pero requiere
más tiempo y usa más tokens. Comienza con el esfuerzo predeterminado y auméntalo cuando
la tarea requiera una planificación o un análisis más profundos.

El modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> va
más allá de una ejecución con un solo agente. Usa
[subagentes](/codex/agent-configuration/subagents) para acelerar el trabajo complejo,
por lo que resulta útil para tareas de mayor alcance que pueden dividirse entre subagentes.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## Elige un modelo

En una sesión interactiva de la CLI, usa `/model` para cambiar de modelo o ajustar
el esfuerzo de razonamiento. También puedes elegir un modelo al iniciar Codex con
`--model` o con su alias `-m`:

La misma opción funciona con ejecuciones no interactivas. Por ejemplo:

Un mayor esfuerzo de razonamiento puede mejorar los resultados en tareas complejas, pero requiere
más tiempo y usa más tokens. Comienza con el esfuerzo predeterminado y auméntalo cuando
la tarea requiera una planificación o un análisis más profundos.

El modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> va
más allá de una ejecución con un solo agente. Usa
[subagentes](/codex/agent-configuration/subagents) para acelerar el trabajo complejo,
por lo que resulta útil para tareas de mayor alcance que pueden dividirse entre subagentes.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Elige un modelo

Usa el selector de modelos debajo del editor para elegir un modelo disponible y
un esfuerzo de razonamiento.

Un mayor esfuerzo de razonamiento puede mejorar los resultados en tareas complejas, pero requiere
más tiempo y usa más tokens. Comienza con el esfuerzo predeterminado y auméntalo cuando
la tarea requiera una planificación o un análisis más profundos.

El modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> va
más allá de una ejecución con un solo agente. Usa
[subagentes](/codex/agent-configuration/subagents) para acelerar el trabajo complejo,
por lo que resulta útil para tareas de mayor alcance que pueden dividirse entre subagentes.

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## Modelos recomendados

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

La disponibilidad depende del despliegue gradual, tu método de inicio de sesión y el cliente que uses.
Consulta los [precios](/es-419/codex/pricing) para conocer el acceso y el consumo según el plan, y la
[disponibilidad de modelos en el espacio de trabajo](/es-419/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise)
para conocer el acceso en Enterprise.

  Empieza con el ajuste predeterminado de Potencia disponible para tu cuenta. Muévelo hacia
**Más inteligente** para un razonamiento más profundo o hacia **Más rápido** para trabajar con mayor rapidez y a menor costo.
  Abre **Avanzado** cuando quieras usar `gpt-5.6-luna` o elegir un modelo, un nivel de esfuerzo de razonamiento
  o una velocidad específicos.

Las ilustraciones del selector muestran los controles de GPT-5.6. Para las cuentas Pro, Business
($100) y Enterprise que cumplan los requisitos, el despliegue gradual de Astra actualiza las opciones de Potencia
a Terra Ligera, Sol Ligera, Sol Media, Astra Ligera, Astra Media y Astra
Muy alta. Las opciones pueden variar según el plan y la etapa del despliegue.

### Gestión experimental del contexto

En los clientes de Codex compatibles, los usuarios que inicien sesión con ChatGPT Plus o Pro pueden activar
la gestión experimental del contexto. Astra conserva notas entre ventanas de contexto
y puede buscar mensajes anteriores y resultados de herramientas de la misma tarea.
Este experimento está desactivado de forma predeterminada y, en su lanzamiento, no está disponible con Business, Enterprise ni
con el inicio de sesión mediante una clave de API.

Para activarla, establece `features.context_management.experimental_mode = true` en tu archivo
`config.toml` y luego inicia una tarea nueva. Consulta la [referencia de configuración](/es-419/codex/config-file/config-reference)
para conocer el ajuste y los [conceptos básicos de configuración](/es-419/codex/config-file/config-basic)
para encontrar la ubicación del archivo. Los requisitos del espacio de trabajo siguen vigentes.

<a id="choosing-sol-terra-and-luna"></a>

## Elegir entre Astra, Sol, Terra y Luna

Elige **Astra** cuando una tarea requiera la mayor capacidad para trabajar con múltiples
pasos y herramientas. **Sol** ofrece profundidad y resultados refinados, **Terra** es adecuado para el trabajo cotidiano
y **Luna** para tareas claras y repetibles.

### En qué destaca cada modelo

- **Astra, para los trabajos más difíciles de principio a fin.** Elige Astra para flujos de trabajo completos
  que abarquen código, aplicaciones e investigación y requieran razonamiento y criterio sostenidos.
  Proporciónale las fuentes, las plantillas, las restricciones y las verificaciones que definan un resultado
  útil. Astra tiene mayor capacidad para hacer preguntas concretas e incorporar tus
  indicaciones sin perder de vista el objetivo y las restricciones originales.
- **Sol, para trabajos complejos y de alcance abierto.** Elige Sol para tareas ambiguas, difíciles o
  de alto valor que requieran análisis, criterio o refinamiento adicionales, como
  cambios complejos en el código, investigación profunda o documentos bien elaborados. Para tareas más acotadas,
  define qué se necesita para darlas por terminadas y mantener el trabajo enfocado.
- **Terra, el modelo versátil y pragmático.** Elige Terra para el trabajo cotidiano que
  requiera un razonamiento sólido y el uso de herramientas cuando no necesites toda la profundidad que ofrece Sol.
  Es un punto de partida natural para el trabajo que antes asignabas a GPT-5.5.
- **Luna, para tareas claras y repetibles.** Elige Luna para tareas específicas y de gran volumen
  cuando tengas claro cómo debe ser un buen resultado, como la extracción,
  la clasificación, la transformación y los resúmenes estructurados.

### Elige un nivel de esfuerzo de razonamiento

Usa el nivel de esfuerzo de razonamiento más bajo que te dé el resultado que necesitas. Auméntalo
para las tareas que requieran más planificación, análisis o verificación.

- La opción **Ligera** en la aplicación de escritorio de ChatGPT, ChatGPT Work en la web y la extensión para IDE, o **Baja** en la
  CLI, es adecuada para tareas rápidas y bien delimitadas.
- **Media** equilibra la velocidad y la profundidad para las tareas que requieren más planificación.
- **Alta** y **Muy alta** son adecuadas para trabajos difíciles con varios pasos, fuentes
  o decisiones que exigen sopesar ventajas y desventajas.

No hay una correspondencia exacta entre los niveles de esfuerzo de razonamiento de GPT-5.5 y los de GPT-5.6. Prueba una
tarea conocida con un nivel más bajo y ajústalo según el resultado.

### Cuándo usar Max o Ultra

**Max** le da al modelo seleccionado más tiempo para razonar sobre una sola tarea. Úsalo
para los problemas más difíciles, cuando la profundidad importe más que la velocidad o el consumo. Si
Max no aparece entre tus opciones, tendrás que activarlo en la configuración de la aplicación.

**Ultra** usa [subagentes](/es-419/codex/agent-configuration/subagents) para abordar
en paralelo distintas partes de una tarea compleja. Elígelo cuando puedas dividir el
trabajo en partes coherentes. La mayoría de las tareas no requiere Max ni Ultra.

Si Ultra no aparece en el control deslizante de modelos de la aplicación de escritorio, ve a
**Configuración** \> **Configuración** y luego activa **Ultra en el control deslizante del selector de modelos**.

## Otros modelos

Cuando inicias sesión con ChatGPT, Codex funciona mejor con los modelos recomendados que se indican arriba.

  <strong>
    GPT-5.4 y GPT-5.4 mini se retiran de Codex el 31 de agosto de 2026.
  </strong>{" "}
  Si inicias sesión con ChatGPT, reemplaza `gpt-5.4` por `gpt-5.6-terra` y
`gpt-5.4-mini` por `gpt-5.6-luna` en las configuraciones guardadas, los agentes personalizados y
  las tareas programadas. La API de OpenAI y Codex con autenticación mediante tu propia clave de API
  no se ven afectados.

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

También puedes configurar Codex para usar cualquier modelo y proveedor que admita la [API Chat Completions](https://platform.openai.com/docs/api-reference/chat) o la [API Responses](https://platform.openai.com/docs/api-reference/responses), según tu caso de uso específico.

  La compatibilidad con la API Chat Completions está obsoleta y se eliminará en
futuras versiones de Codex.

## Modelos obsoletos de Codex

Los modelos `gpt-5.4` y `gpt-5.4-mini` se retiran de Codex para quienes inician sesión con ChatGPT
el 31 de agosto de 2026. Reemplaza `gpt-5.4` por `gpt-5.6-terra` y
`gpt-5.4-mini` por `gpt-5.6-luna` en los valores predeterminados del espacio de trabajo, la configuración guardada
del modelo, las configuraciones administradas, los agentes personalizados y las tareas programadas.

Los modelos `gpt-5.2` y `gpt-5.3-codex` ya están obsoletos en Codex cuando
inicias sesión con ChatGPT. Actualiza los scripts, los archivos de configuración y
los comandos `codex exec --model` que aún hagan referencia a esos modelos.

La API de OpenAI y Codex con autenticación mediante tu propia clave de API no se ven afectados
por el retiro de GPT-5.4. Para conocer la disponibilidad actual de los modelos en la API, consulta la
[página de modelos de la API](/api/docs/models).

## Configura tu modelo local predeterminado

La aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE usan el mismo [archivo de configuración](/es-419/codex/config-file/config-basic)
`config.toml`. Para especificar un modelo, agrega una entrada
`model` a tu archivo de configuración. Si no especificas un modelo, la
aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE usa un modelo recomendado.

## Elige un modelo para los chats en la nube

Actualmente, no puedes cambiar el modelo predeterminado para los chats de Codex Cloud.
