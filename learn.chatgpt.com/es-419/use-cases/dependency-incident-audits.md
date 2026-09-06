<!-- source: https://learn.chatgpt.com/es-419/use-cases/dependency-incident-audits -->

## Comenzar con un plan de auditoría seguro

Cuando un incidente relacionado con una dependencia o la cadena de suministro evoluciona rápidamente, el primer resultado útil no es un parche apresurado. Es un plan de auditoría claro: qué cambió, qué paquetes o flujos de trabajo podrían verse afectados y qué evidencia demostraría que tu repositorio está expuesto.

Usa Codex para convertir el aviso en una lista de verificación prudente y de solo lectura antes de instalar, compilar, probar o ejecutar cualquier cosa.

## Mantener la primera revisión en modo de solo lectura

1. Proporciónale a Codex el aviso público, el informe del incidente o la lista de paquetes afectados.
2. Pídele que distinga las fuentes oficiales de los comentarios más generales.
3. Pídele que defina qué evidencia demostraría o descartaría la exposición.
4. Deja que inspeccione los archivos de manifiesto y de bloqueo, los flujos de trabajo de CI, los scripts y los archivos relevantes del repositorio.
5. Pídele que agrupe los hallazgos por estado de la evidencia, gravedad y próximo paso recomendado.

En los incidentes relacionados con paquetes, evita ejecutar comandos para instalar, compilar, probar o importar, así como comandos del ciclo de vida, hasta saber a qué afecta el aviso. Codex puede buscar en los archivos de bloqueo y los flujos de trabajo sin ejecutar código que no sea de confianza.

## Informar el estado de la evidencia por separado de la gravedad

Un resultado de auditoría útil debe mostrar tanto qué tan grave sería un hallazgo como qué tan sólida es la evidencia:

  <p>
    <strong>Exposición confirmada:</strong> el archivo de bloqueo contiene un paquete con una versión afectada
    en una ruta de dependencias de producción.
  </p>
  <p>
    <strong>Requiere verificación:</strong> una tarea de CI tiene permisos de publicación, pero
    el flujo de trabajo no parece instalar directamente el paquete afectado.
  </p>
  <p>
    <strong>Exposición descartada:</strong> el nombre del paquete solo aparece en la documentación y no
    figura en los archivos de manifiesto ni de bloqueo.
  </p>
  <p>
    <strong>Próximo paso:</strong> revisa la propuesta de actualización de dependencias y el plan para rotar tokens
    antes de realizar cualquier acción destructiva.
  </p>

Una vez finalizada la revisión de solo lectura, puedes pedirle a Codex que prepare un Pull Request de remediación, actualice los permisos de CI o redacte una nota de seguimiento del incidente. Mantén esas acciones separadas de la auditoría inicial.
