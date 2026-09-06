<!-- source: https://learn.chatgpt.com/es-419/docs/cyber-safety -->

OpenAI Daybreak ayuda a los usuarios que cuentan con aprobación a realizar tareas autorizadas de ciberseguridad defensiva. Daybreak Blue brinda acceso a modelos insignia que rechazan menos solicitudes en los flujos de trabajo defensivos autorizados. Daybreak Red brinda acceso, previa aprobación por separado, a modelos especializados en ciberseguridad para investigaciones de seguridad más avanzadas.

Combina tu modelo aprobado con un entorno controlado, límites claros para los sistemas y las acciones aprobados, permisos con privilegios mínimos y una revisión automática antes de que se ejecuten acciones sensibles. Usa el modelo solo con la identidad, el espacio de trabajo o la organización y el proyecto de la API, y la interfaz del producto que se hayan aprobado.

## Elige el modelo adecuado

Comienza con **GPT-Daybreak-Blue** para la mayoría de las tareas defensivas autorizadas. Este modelo brinda acceso a capacidades avanzadas y rechaza menos solicitudes en flujos de trabajo de seguridad defensiva, como:

- Descubrimiento y priorización de vulnerabilidades.
- Revisión de la seguridad del código y modelado de amenazas.
- Ingeniería de detección y respuesta a incidentes.
- Análisis de malware en un entorno controlado.
- Remediación y validación de parches.

**GPT-Daybreak-Red** es un modelo especializado en ciberseguridad para flujos de trabajo aprobados por separado y autorizados explícitamente, como la reproducción controlada de vulnerabilidades, la validación de pruebas de concepto o exploits, las pruebas de penetración, el red teaming y el análisis de sistemas complejos. No es la opción predeterminada para tareas rutinarias de seguridad, y el acceso no se concede automáticamente ni está disponible en todas las interfaces.

Estos flujos de trabajo avanzados pueden parecer actividades maliciosas cuando no existe una autorización clara. Usa el modelo y la interfaz aprobados únicamente en sistemas de tu propiedad o que tengas autorización explícita para evaluar, y mantén una supervisión humana adecuada.

Por ejemplo:

- **GPT-Daybreak-Blue:** revisa el repositorio aprobado del laboratorio en busca de debilidades de autenticación, ordena los hallazgos según la evidencia y el impacto, y propón parches sin acceder a sistemas externos.
- **GPT-Daybreak-Red:** dentro del laboratorio aprobado y durante el período de pruebas autorizado, reproduce la falla de autenticación documentada, valida una prueba de concepto mínima y detente antes de acceder a credenciales, establecer persistencia o realizar cambios en producción.

## Trusted Access for Cyber

Solicita **acceso a Daybreak** mediante [Trusted Access for Cyber](https://help.openai.com/en/articles/20001258-trusted-access-for-cyber). El acceso depende de la aprobación y del aprovisionamiento para tu identidad o servicio específicos, tu espacio de trabajo de ChatGPT o tu organización y proyecto de la API, la oferta y el modelo autorizados, y la interfaz permitida del producto.

- Las personas pueden solicitar acceso mediante la [solicitud individual de Trusted Access](https://chatgpt.com/cyber).
- Las organizaciones pueden enviar el [formulario de solicitud de Trusted Access para empresas](https://openai.com/form/enterprise-trusted-access-for-cyber/) y coordinarse con su representante de OpenAI.

Presentar una solicitud o completar la verificación de identidad no garantiza la aprobación.

  Presentar una solicitud, verificar tu identidad o recibir la aprobación para Daybreak Blue
no te da acceso a Daybreak Red ni a GPT-Daybreak-Red. La oferta especializada
requiere aprobación y aprovisionamiento por separado.

Para el acceso empresarial, usa el espacio de trabajo, la organización de la API o el proyecto aprobados únicamente para el trabajo interno autorizado de tu organización. No extiendas ese acceso a usuarios externos, clientes de terceros, servicios ofrecidos externamente, funciones de productos que dependan de ese acceso ni sistemas ajenos al trabajo aprobado. Si no tienes claro qué identidad, espacio de trabajo, organización de la API, proyecto, modelo o interfaz están aprobados, detente y confírmalo con tu representante de OpenAI.

Trusted Access no otorga automáticamente la [retención cero de datos](/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring). Antes de comenzar, confirma los controles de retención que se hayan aprobado por separado para la organización específica de la API y el punto de acceso correspondiente.

## Falsos positivos

Las actividades legítimas de ciberseguridad o las que no están relacionadas con ella también pueden activar una medida de protección. Si una medida de protección bloquea, redirige o limita una solicitud, revisa el aviso disponible en el cliente y los registros de solicitudes. Consulta [Problemas comunes y solución de problemas](https://help.openai.com/en/articles/20001259) para saber qué información recopilar y qué pasos seguir. Reporta los posibles falsos positivos de Codex mediante `/feedback` cuando esté disponible. Para conocer las restricciones de acceso a la API y cómo apelarlas, sigue la [guía sobre las comprobaciones de ciberseguridad de la API](/api/docs/guides/safety-checks/cybersecurity#appeals).

Todos los usuarios siguen sujetos a las [Políticas de uso](https://openai.com/policies/usage-policies/) y a los [Términos de uso](https://openai.com/policies/row-terms-of-use/).

## Configura tu flujo de trabajo de seguridad

Trusted Access regula el acceso aprobado a los modelos, pero no configura tu entorno, no hace cumplir los límites para los sistemas y las acciones aprobados ni revisa las acciones propuestas.

- [Usa la configuración recomendada](/es-419/codex/cyber-safety/recommended-configuration) para establecer aislamiento, permisos con privilegios mínimos, límites claramente definidos y medidas de protección para las acciones sensibles.
