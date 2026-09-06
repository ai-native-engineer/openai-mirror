<!-- source: https://learn.chatgpt.com/es-419/use-cases/analyze-data-export -->

## Antes de comenzar

Adjunta un archivo CSV o una hoja de cálculo, o conecta Google Drive y pega en el chat la URL exacta de Google Drive o Google Sheets. Sites puede convertir esas fuentes en un panel privado e interactivo sin publicarlo ni hacer públicos tus datos.

Puedes crear el panel en ChatGPT Work desde el navegador o la aplicación de escritorio. Para que una revisión programada continúe cuando tu laptop esté apagada, inicia la tarea en el navegador. Una tarea ejecutada desde la aplicación de escritorio requiere que la computadora esté encendida y que la aplicación esté en ejecución.

## Qué esperar

ChatGPT revisa los datos de origen, crea un panel y muestra las cifras en las que se basan los gráficos. Este ejemplo usa archivos ficticios de exportación trimestral de ventas, un mapa de segmentos de clientes y una vista previa representativa del panel. Distingue el mayor cambio en dólares del mayor cambio porcentual y señala un pedido que no puede asignarse a un segmento de clientes.

<div data-use-case-export-only>

### Panel de ejemplo

| Segmento de clientes | Ingresos del T1 | Ingresos del T2 |         Cambio |
| ---------------- | ---------: | ---------: | -------------: |
| Empresas       |     $3000 |     $2450 | -$550 (-18,3 %) |
| Mercado medio       |     $1000 |     $1170 |   +$170 (+17 %) |
| PyMEs              |       $400 |       $520 |   +$120 (+30 %) |

El segmento Empresas tuvo el mayor cambio en dólares, y el segmento PyMEs tuvo el mayor cambio porcentual. Un pedido del T2 por un valor de $160 no coincidió con el mapa de segmentos de clientes y se excluyó de los totales por segmento. El panel privado incluye un gráfico comparativo, filtros de segmento y fecha, la fecha de la última actualización de la fuente y los cálculos subyacentes.

Cuando le pides a ChatGPT que revise la fuente todas las mañanas de lunes a viernes, actualiza el panel cuando cambian los datos aprobados y señala los cambios importantes o los registros faltantes. No publica ni comparte el panel sin aprobación.

</div>

## Cómo funciona

- **Conecta la fuente:** adjunta un archivo de exportación de ventas o una hoja de cálculo, o pega el enlace exacto a una hoja aprobada de Google Sheets o a un archivo aprobado de Google Drive. ChatGPT revisa las columnas, las fechas y los registros de clientes antes de sacar conclusiones.
- **Crea el panel:** Sites convierte los resultados en un panel privado e interactivo con gráficos, filtros, la fecha de la última actualización de la fuente y los cálculos que respaldan los resultados.
- **Mantenlo actualizado:** una tarea programada de ChatGPT Work revisa la fuente aprobada cada día de lunes a viernes y actualiza el panel cuando cambian los datos. El sitio no ejecuta por sí mismo la tarea programada.
- **Muestra solo lo importante:** pídele a ChatGPT que señale cambios inusuales, registros faltantes o decisiones que requieren revisión. Si no cambia nada importante, no debería notificarte.
- **Revisa antes de compartir:** primero, inspecciona el panel. Pídele a ChatGPT que lo comparta con personas específicas solo después de que apruebes el cambio de acceso.

## Compartir el panel

Después de revisar el panel, pídele a ChatGPT que lo comparta con personas específicas o lo ponga a disposición de tu espacio de trabajo. También puedes administrar el acceso directamente en [Sites](https://chatgpt.com/sites). Pídele a ChatGPT que muestre la configuración actual de uso compartido y espere tu aprobación antes de invitar a alguien, publicar el panel o cambiar su visibilidad.

Consulta la [documentación de Sites](/es-419/codex/sites) para conocer las opciones de uso compartido y de acceso al espacio de trabajo.

## Ir más allá

**Cambia lo que monitorea el panel**

**Configura una alerta más útil**

**Prepara una actualización semanal**
