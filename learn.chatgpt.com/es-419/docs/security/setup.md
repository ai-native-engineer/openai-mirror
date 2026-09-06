<!-- source: https://learn.chatgpt.com/es-419/docs/security/setup -->

Esta página te guía desde el acceso inicial hasta la revisión de hallazgos y los
Pull Requests de corrección en Codex Security en la nube.

  Primero, confirma que configuraste Codex Cloud. Si no es así, consulta [Codex
  Cloud](/es-419/codex/cloud) para comenzar.

## 1. Acceso y entorno

Codex Security en la nube analiza los repositorios de GitHub conectados mediante
[Codex Cloud](/es-419/codex/cloud).

- Confirma que tu espacio de trabajo tenga acceso a Codex Security en la nube.
- Confirma que el repositorio que quieres analizar esté disponible en Codex Cloud.

Ve a [Entornos de Codex](https://chatgpt.com/codex/settings/environments) y verifica si el repositorio ya tiene un entorno. Si no lo tiene, crea uno allí antes de continuar.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 2. Nuevo análisis de seguridad

Una vez que exista el entorno, ve a [Crear un análisis de seguridad](https://chatgpt.com/codex/security/scans/new) y elige el repositorio que acabas de conectar.

Codex Security analiza primero los commits más recientes de los repositorios y luego retrocede en el historial. Usa este proceso para crear y actualizar el contexto del análisis a medida que llegan nuevos commits.

Para configurar un repositorio:

1. Selecciona la organización de GitHub.
2. Selecciona el repositorio.
3. Selecciona la rama que quieres analizar.
4. Selecciona el entorno.
5. Elige una **ventana de historial**. Las ventanas más extensas proporcionan más contexto, pero el procesamiento retroactivo tarda más.
6. Haz clic en **Crear**.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 3. Los análisis iniciales pueden tardar un tiempo

Cuando creas el análisis, Codex Security primero ejecuta una revisión de seguridad a nivel de commit en la ventana de historial seleccionada.
El procesamiento retroactivo inicial puede tardar algunas horas, especialmente en repositorios grandes o con ventanas más extensas.
Es normal que los hallazgos no aparezcan de inmediato. Espera a que termine el análisis inicial antes de abrir un ticket o intentar solucionar problemas.

  La configuración del análisis inicial es automática y exhaustiva. Puede tardar algunas horas. No
te preocupes si el primer conjunto de hallazgos tarda en aparecer.

## 4. Revisar los análisis y mejorar el modelo de amenazas

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

Cuando termine el análisis inicial, abre el análisis y revisa el modelo de amenazas que se generó.
Después de que aparezcan los hallazgos iniciales, actualiza el modelo de amenazas para que se ajuste a tu arquitectura, tus límites de confianza y tu contexto empresarial.
Esto ayuda a Codex Security a priorizar los problemas para tu equipo.

  Si quieres que cambien los resultados del análisis, puedes editar el modelo de amenazas según tu
alcance, tus prioridades y tus supuestos actualizados.

Después de que aparezcan los hallazgos iniciales, vuelve a revisar el modelo para que la orientación del análisis siga alineada con las prioridades actuales.
Mantenerlo actualizado ayuda a Codex Security a generar mejores sugerencias.

Para obtener una explicación más detallada de los modelos de amenazas y de cómo afectan el nivel de criticidad y la priorización, consulta [Mejorar el modelo de amenazas](/es-419/codex/security/threat-model).

## 5. Revisar los hallazgos y aplicar correcciones

Cuando termine el procesamiento retroactivo inicial, revisa los hallazgos en la vista **Hallazgos** .

Puedes usar dos vistas:

- **Hallazgos recomendados**: una lista dinámica de los 10 problemas más críticos del repositorio
- **Todos los hallazgos**: una tabla de hallazgos de todo el repositorio que puedes ordenar y filtrar

  
    
  

Haz clic en un hallazgo para abrir su página de detalles, que incluye:

- una descripción concisa del problema
- metadatos clave, como los detalles del commit y las rutas de los archivos
- razonamiento contextual sobre el impacto
- fragmentos de código relevantes
- contexto de la ruta de llamadas o del flujo de datos, cuando esté disponible
- pasos y resultados de la validación

Puedes revisar cada hallazgo y crear un Pull Request directamente desde la página de detalles del hallazgo.

## Documentación relacionada

- [Codex Security](/es-419/codex/security) ofrece una descripción general del producto.
- [Preguntas frecuentes sobre Codex Security en la nube](/es-419/codex/security/faq) responde preguntas comunes sobre la nube.
- [Mejorar el modelo de amenazas](/es-419/codex/security/threat-model) explica cómo mejorar el contexto del análisis y la priorización de los hallazgos.
