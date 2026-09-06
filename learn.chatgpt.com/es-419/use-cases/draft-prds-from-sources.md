<!-- source: https://learn.chatgpt.com/es-419/use-cases/draft-prds-from-sources -->

## Introducción

Antes de trabajar en un producto nuevo o una función nueva, es habitual redactar un documento de requisitos del producto (PRD) para acordar el alcance y los requisitos. Por lo general, el contexto necesario para redactar el PRD ya está disponible en los sistemas internos del equipo: tickets en Linear, conversaciones en Slack, borradores en Notion o Google Drive, etc. ChatGPT puede recopilar este contexto, redactar un PRD que puedas revisar y perfeccionar, y mantener visible la trazabilidad de las fuentes.

## Elige las fuentes

Comienza con las fuentes que quieres que use ChatGPT: el proyecto de Linear, el canal o hilo de planificación de Slack y cualquier documento de Drive, página de Notion, nota de reunión o archivo local que deba citarse en el PRD.
También debes indicar claramente qué secciones esperas en el PRD, como el problema, los usuarios, los requisitos, la UX, los aspectos técnicos, el plan de lanzamiento, el cronograma o las decisiones.

1. Comienza con `$documents` cuando el resultado deba ser un archivo DOCX real.
2. Menciona las fuentes de forma explícita: el proyecto o hito de Linear, el canal o hilo de Slack y los documentos o notas que ChatGPT deba citar.
3. Define para ChatGPT la estructura de secciones del PRD.
4. Revisa primero el apéndice de fuentes y luego los requisitos y las preguntas abiertas.
5. Usa el mismo chat para completar la información que falta, acotar el alcance y preparar el traspaso.

<a id="refine-in-the-same-chat"></a>
<a id="refine-in-the-same-task"></a>

## Perfecciona el PRD en el mismo chat

Usa el prompt inicial de esta página para elaborar el primer borrador. Si falta algo, indícale a ChatGPT la fuente que falta en vez de volver a empezar.

## Verifica la trazabilidad de las fuentes

Antes de compartir el PRD, pídele a ChatGPT que enumere las afirmaciones con respaldo débil o inexistente, las preguntas sin resolver y las decisiones que dio por confirmadas. Si el apéndice de fuentes no permite auditar fácilmente esos elementos, sigue perfeccionando el PRD en el mismo chat antes de exportarlo o publicar algo.

### Prompt sugerido

**Verifica la trazabilidad de las fuentes**
