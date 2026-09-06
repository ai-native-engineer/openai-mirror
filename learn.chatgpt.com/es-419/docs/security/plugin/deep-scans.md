<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/deep-scans -->

Ejecuta un análisis profundo cuando necesites una revisión más exhaustiva y puedas permitir un mayor
tiempo de ejecución. Los análisis profundos examinan un repositorio con mayor profundidad y pueden reducir
la variabilidad entre ejecuciones.

Comienza con un [análisis estándar](/es-419/codex/security/plugin/scans) para comprobar el alcance
y los resultados. Luego, usa un análisis profundo cuando necesites una evaluación más exhaustiva.

## Elegir entre análisis estándar y profundos

|                         | Análisis estándar                                      | Análisis profundo                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| Ideal para                | Primeras ejecuciones y revisiones habituales de repositorios o carpetas | Revisiones más exhaustivas después de un análisis estándar           |
| Variabilidad             | Estándar                                           | Reducida                                               |
| Alcance                   | Repositorio o carpeta indicada explícitamente                      | Repositorio o carpeta indicada explícitamente                         |
| Tiempo de ejecución y recursos   | Menores                                              | Mayores                                                |
| Pull requests y diffs | Usa el flujo de trabajo de revisión de cambios                     | No se admite; usa en su lugar el flujo de trabajo de revisión de cambios |

## Configurar el tiempo de ejecución de los análisis profundos

Para controlar la concurrencia y la duración de un análisis profundo, crea o edita
`~/.codex/codex-security/config.toml`. Si estableces `CODEX_HOME`, usa
`$CODEX_HOME/codex-security/config.toml` en su lugar.

Por ejemplo, este perfil ejecuta un análisis más corto con concurrencia limitada:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

| Parámetro                         | Valor predeterminado | Descripción                                                                                                        |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `workers`                       | `4`     | Cantidad de workers de análisis estándar independientes que pueden ejecutarse al mismo tiempo. El valor heredado `"auto"` también se interpreta como `4`. |
| `subagents`                     | `3`     | Cantidad de subagentes que puede iniciar cada worker. Establece `0` para desactivarlos.                                                |
| `stop_after_no_new`             | `4`     | Detén el análisis después de que esta cantidad de análisis consecutivos completados por workers no genere nuevos hallazgos.                                   |
| `stop_after_consecutive_errors` | `3`     | Detén el análisis después de esta cantidad de errores consecutivos de los workers.                                                                    |
| `max_discovery_runs`            | `40`    | Limita la cantidad de ejecuciones independientes de análisis estándar antes de la consolidación.                                             |
| `max_time_hours`                | `96`    | Limita la ejecución de los workers a una cantidad positiva de horas, hasta un máximo de `96`; usa fracciones si es necesario.                          |

Los valores más bajos pueden reducir el tiempo de análisis y el uso de tokens, pero pueden hacer que se pasen por alto hallazgos.
Los cambios de configuración se aplican a los nuevos análisis profundos, no a los que ya están en curso.

Cuando se alcanza el límite de tiempo, Codex Security detiene los workers que no hayan finalizado,
conserva los resultados de los análisis completados y los consolida en el informe final. Si ningún worker
termina la revisión del código fuente antes del plazo, el informe registra una cobertura
parcial.

El parámetro `max_time_hours` requiere la versión `0.1.19` del complemento o una versión posterior. Consulta el
[registro de cambios del complemento](/es-419/codex/security/plugin/changelog) para conocer los detalles de la versión.

## Iniciar el análisis profundo

En la App de escritorio, abre **Seguridad**, selecciona **Análisis** y selecciona **+ Análisis**.
Elige un repositorio u otra carpeta, selecciona **Base de código** y activa
**Análisis profundo**. El análisis abarca todo el repositorio o toda la carpeta seleccionada.

También puedes iniciar un análisis profundo de todo el repositorio desde una conversación de Codex:

```text
Use $codex-security:deep-security-scan to run a deep security scan of this repository.

Para un componente de un monorepo, indica explícitamente la carpeta:

```text
Use $codex-security:deep-security-scan to run a deep security scan of /absolute/path/to/repository/services/payments.

Para realizar un análisis profundo de alcance específico en la App de escritorio, selecciona la carpeta como base de código.
El análisis abarca toda la carpeta seleccionada.

## Confirmar la configuración y las comprobaciones previas

Para obtener la mejor calidad de análisis, usa <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
con un nivel de razonamiento `xhigh`.

1. Selecciona **Base de código** y activa **Análisis profundo**.
2. Confirma que el repositorio o la carpeta seleccionada corresponda al código que quieres
analizar.
3. Elige un modelo y un nivel de razonamiento.
4. Abre **Contexto adicional** para agregar vectores de ataque concretos, áreas sensibles
   de la aplicación o contexto del repositorio que el código no pueda revelar.
5. Selecciona **Iniciar análisis**.

Los workers de análisis profundo heredan el modelo y la configuración de razonamiento que seleccionaste. Cada
worker ejecuta un análisis estándar completo y Codex Security consolida los
resultados de los análisis completados. Sigue el análisis guardado desde **Análisis** o selecciona **Ver
actividad** para inspeccionar su tarea de Codex. Consulta el [registro de cambios
del complemento](/es-419/codex/security/plugin/changelog) antes de actualizar el complemento o
iniciar un análisis de larga duración.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Sigue la fase activa del análisis profundo e inspecciona su actividad en Codex antes de
revisar el resultado final.
  </figcaption>
</figure>

## Revisar el resultado

Los análisis profundos usan los mismos detalles guardados y el mismo directorio completo del análisis que
los análisis estándar. Abre el análisis completado en **Análisis** o revisa sus hallazgos en
**Hallazgos**. El archivo `report.md` generado incluye enlaces a informes detallados de vulnerabilidades
o recomendaciones de refuerzo estructural cuando solicitas esos resultados.
Conserva junto con el informe los directorios vinculados `findings/` y `hardening/` cuando
compartas o archives el resultado.

Revisa el resumen de cobertura antes de los hallazgos. Incluso un análisis profundo tiene límites,
así que comprueba las superficies pendientes y las lagunas de evidencia restantes antes de llegar a una
conclusión. Si aceptas un hallazgo, continúa con [Corregir y verificar un
hallazgo](/es-419/codex/security/plugin/fix-findings).

Para revisar una pull request, un commit, un rango de ramas o un parche local, usa [Revisar cambios
de código](/es-419/codex/security/plugin/code-changes). Un análisis profundo nunca reemplaza
el flujo de trabajo centrado en diffs.
