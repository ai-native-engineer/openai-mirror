<!-- source: https://learn.chatgpt.com/es-419/use-cases/discover-protein-folding-architectures -->

## Explorar una hipótesis sobre una arquitectura de plegamiento de proteínas

Usa el modo Objetivo de Codex cuando tengas una hipótesis sobre el plegamiento de proteínas que requiera más
de una iteración de implementación. Proporciona a Codex una línea científica acotada, una
línea base funcional y un benchmark con puntuación automática. Codex puede implementar
el fork de la arquitectura, hacer seguimiento de los experimentos, diagnosticar fallas y seguir
iterando mientras revisas la evidencia.

Este ejemplo partió de una pregunta concreta: ¿podría un modelo al estilo de AlphaFold2
aprender geometría proteica útil con mayor eficiencia si su tronco representara no
solo residuos y pares de residuos, sino también objetos topológicos explícitos
de orden superior?

## Definir un experimento acotado

AlphaFold2 ya usa un potente razonamiento por pares y basado en triángulos dentro
del Evoformer. Sus operaciones triangulares mejoran las representaciones de las aristas, pero los resultados
siguen volcándose en un tensor de pares. El científico propuso evaluar si las representaciones aprendidas persistentes
de las caras triangulares y las celdas tetraédricas podrían
aportar un sesgo inductivo útil en un entorno con datos limitados.

El repositorio público resultante, [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
agrega estados dispersos de caras `F_ijk` y estados tetraédricos `U_ijkl` junto con la
representación convencional por pares `Z_ij`.

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

Comienza con el prompt inicial de esta página, una línea base mínima al estilo de AlphaFold2
y el benchmark público NanoFold. El benchmark proporciona una base pequeña y depurada,
con datos fijos y puntuación automática, para experimentar en biología estructural.
Mantén la primera implementación lo bastante pequeña como para probarla mediante
pruebas unitarias específicas y microbenchmarks antes de iniciar ejecuciones costosas
de entrenamiento.

## Ejecutar la búsqueda con el modo Objetivo

1. Proporciona una hipótesis científica de alto nivel y falsable en lugar de pedirle al modelo que formule desde cero todo un programa de investigación.
2. Usa GPT-5.5 Pro en ChatGPT para convertir esa línea de investigación en un plan de implementación con restricciones y ablaciones explícitas.
3. Pídele a Codex que implemente la línea base ejecutable más pequeña de [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) y luego verifícala con pruebas unitarias específicas y microbenchmarks.
4. Proporciona el repositorio resultante al modo Objetivo de Codex e indícale que maximice mediante ascenso de colina el `lDDT-Cα` de validación en el benchmark NanoFold, a la vez que conserva los registros de experimentos, los planes y las referencias a los artefactos.
5. Mantén el modo Objetivo en ejecución continua mientras usa la retroalimentación del benchmark para iterar sobre la arquitectura, la estrategia de entrenamiento y el arnés de ejecución experimental. En este ejemplo, el ciclo se ejecutó durante más de 150 horas.

Usa `PLAN.md` para la estrategia actual y los próximos pasos, `EXPERIMENTS.md` para llevar un
registro estructurado de los resultados y `EXPERIMENT_NOTES.md` como bloc de notas continuo.
Estos artefactos permiten auditar una búsqueda prolongada y te ofrecen un lugar estable
desde el cual orientar la siguiente iteración.

El modo Objetivo resulta útil aquí porque la búsqueda requiere ciclos repetidos de implementación,
pruebas, seguimiento de experimentos, diagnóstico de fallas e iteraciones guiadas por el
benchmark. La investigación automatizada sin orientación tendía a desviarse hacia cambios locales conocidos
como funciones de pérdida, optimizadores e hiperparámetros. Una hipótesis concisa sobre la arquitectura,
formulada por un científico, le dio a Codex un espacio de búsqueda más pertinente y, al mismo tiempo,
dejó margen para probar, diagnosticar y perfeccionar la implementación.

Este flujo de trabajo también resulta útil para los equipos que evalúan cómo cambia la calidad de la búsqueda científica con agentes
cuando un científico interviene para orientar el proceso.

## Resultado de ejemplo

El resultado de este flujo de trabajo fue [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
una arquitectura experimental con estados explícitos de símplices de orden superior. Revisa
la topología junto con los registros del benchmark para confirmar que cada iteración siga
poniendo a prueba la idea científica original.

![Comparación de la geometría proteica con símplices de orden 1, 2 y 3.](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

La lección útil no es que Codex haya resuelto de forma autónoma el plegamiento de proteínas. Este
flujo de trabajo muestra cómo el modo Objetivo puede funcionar como un ciclo persistente de ingeniería científica:
un científico aporta la propuesta conceptual y Codex acorta el ciclo de
implementación, experimentación, depuración y búsqueda posterior.

Considera los diagnósticos prometedores como evidencia de que la vía de implementación funciona,
no como prueba de generalización. Revisa periódicamente la trayectoria del agente,
oriéntalo de nuevo hacia preguntas sobre arquitectura que sean científicamente pertinentes si
se limita al ajuste local de hiperparámetros y respalda las afirmaciones solo después de
comparaciones pareadas de validación pública y réplicas adecuadas.

## Recursos

- [Repositorio de SimplexFold](https://github.com/ChrisHayduk/SimplexFold)
- [Plan del benchmark de SimplexFold](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [Competencia NanoFold](https://github.com/ChrisHayduk/nanoFold-Competition)
- [Reglas de la competencia NanoFold](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [Ejecución del modo Objetivo durante más de 150 horas](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [Artículo sobre el modo Objetivo](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)
