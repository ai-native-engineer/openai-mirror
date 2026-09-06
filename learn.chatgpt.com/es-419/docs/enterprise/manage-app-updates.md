<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/manage-app-updates -->

La app de escritorio de ChatGPT normalmente busca e instala actualizaciones por sí sola. Si
tu organización necesita revisar las nuevas versiones antes de que los usuarios las reciban,
puedes desactivar el actualizador integrado de la app e implementar versiones aprobadas mediante
tu plataforma de administración de dispositivos.

El actualizador de la app permanece habilitado de forma predeterminada. Desactivarlo no impide que
Microsoft Store, Microsoft Intune, la administración de dispositivos móviles (MDM), los administradores de
paquetes u otras herramientas externas de implementación instalen actualizaciones.

## Antes de comenzar

Confirma que cuentas con:

- Acceso de administrador de Codex a
[Configuración administrada](https://chatgpt.com/codex/settings/managed-configs)
  para tu espacio de trabajo.
- Una versión de la app de escritorio de ChatGPT para macOS o Windows que admita
actualizaciones administradas por la organización.
- Una plataforma de MDM o implementación de software que pueda instalar paquetes aprobados de la app
en tus dispositivos administrados.
- Un proceso para probar nuevas versiones, implementar actualizaciones de seguridad y hacer seguimiento de
las versiones instaladas de la app.

Si aún no implementaste la app en Windows, comienza con
[Implementar la app para Windows](/es-419/codex/enterprise/windows-deployment).

## Desactivar las actualizaciones en la app

  Cuando desactivas las actualizaciones en la app, queda a cargo de tu organización
implementar con rapidez las nuevas versiones de la app y las correcciones de seguridad. Retrasar las actualizaciones puede
dejar la app y sus componentes incluidos expuestos a vulnerabilidades de seguridad
conocidas. Las versiones anteriores de la app no reciben parches de seguridad independientes ni
soporte extendido.

Crea una política administrada que desactive el actualizador propio de la app de escritorio:

1. Abre
[Configuración administrada](https://chatgpt.com/codex/settings/managed-configs).
2. Selecciona **Agregar política** o abre una política existente para los usuarios, grupos o
   plataformas que quieras administrar.
3. En **Objetivos**, selecciona **Agregar objetivo** para asignar la política a
**Grupos**, **Usuarios** o **Plataformas** específicos. Siempre que sea
   posible, comienza con un grupo piloto pequeño.
4. Abre **TOML sin procesar** y busca el editor de **requirements.toml**.
5. Agrega la siguiente política:

   ```toml
   [features]
   in_app_updates = false

   Si tu política ya contiene una tabla `[features]`, agrega
`in_app_updates = false` a esa tabla. No agregues una segunda tabla `[features]`
   ni coloques la configuración en **config.toml**.

6. Selecciona **Guardar cambios**.
7. Pide a los usuarios afectados que cierren por completo y vuelvan a abrir la app de escritorio de ChatGPT. Cerrar
la ventana de la app no siempre basta para reiniciar la aplicación.

Algunos espacios de trabajo muestran un editor de listas de políticas en lugar de la pestaña **TOML sin procesar**. En
esa interfaz, agrega el mismo bloque TOML directamente a la política correspondiente, usa
**Grupos** para asignarla, si esa opción está disponible, y selecciona **Guardar**.

Para obtener más información sobre la entrega y la precedencia de las políticas administradas, consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration).

## Verificar la configuración administrada

Después de que se reinicie la app, verifica la política desde el dispositivo de un usuario afectado:

1. Inicia sesión en la app de escritorio de ChatGPT con una cuenta a la que se aplique la política.
2. Abre **Configuración** \> **General**.
3. Busca **Actualizaciones en la app** y confirma que muestre **Administrado** y el mensaje
   “Tu organización desactivó las actualizaciones en la app”.
4. Confirma que tu plataforma de administración de dispositivos aún pueda implementar una versión aprobada de la
app.

La opción de menú **Buscar actualizaciones** puede seguir visible aunque la política
bloquee las actualizaciones en la app. Usa el indicador **Administrado** para verificar la política
en lugar de comprobar si aparece esa opción de menú.

Si el indicador no aparece después del primer reinicio, es posible que la app aún
use una política almacenada en caché. Deja que la política se actualice y, luego, cierra por completo y vuelve a abrir la
app. No confíes en la restricción de actualizaciones hasta que aparezca **Administrado**.

## Implementar versiones aprobadas de la app

Después de desactivar las actualizaciones en la app, usa tu proceso actual de administración de dispositivos
para distribuir nuevas versiones:

1. Elige una versión de la app que tu organización planee implementar.
2. Obtén el paquete de instalación compatible con cada sistema operativo y
arquitectura de dispositivo de tu flota.
3. Prueba la versión con un grupo pequeño de usuarios representativos.
4. Implementa el paquete aprobado mediante Microsoft Intune, tu plataforma de MDM u
otra herramienta de implementación de software.
5. Revisa el inventario de dispositivos para confirmar que tu plataforma instaló la versión
prevista y luego amplía la implementación a otros grupos.

Tu plataforma de administración determina cómo implementas las versiones por etapas, seleccionas versiones
y realizas la recuperación cuando una implementación no se completa. Si tu plataforma permite
una reversión, volver a una versión anterior no extiende el soporte ni garantiza
la compatibilidad con el servicio.

Para macOS, descarga el
[instalador de la app de escritorio de ChatGPT](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg).
Para conocer los métodos de instalación en Windows y los paquetes específicos de cada arquitectura, consulta
[Implementar la app para Windows](/es-419/codex/enterprise/windows-deployment).

## Volver a activar las actualizaciones en la app

Para restablecer el comportamiento normal de actualización de la app:

1. Identifica las políticas administradas, los archivos `requirements.toml` del sistema y los perfiles de MDM
   que desactivan las actualizaciones para los usuarios afectados.
2. Elimina `in_app_updates = false` de cada tabla `[features]` correspondiente.
3. Guarda los cambios de la política y vuelve a implementar los requisitos actualizados mediante la administración de dispositivos.
4. Pide a los usuarios afectados que cierren por completo y vuelvan a abrir la app de escritorio de ChatGPT.
5. Revisa **Configuración** \> **General** para confirmar que la fila administrada correspondiente a **Actualizaciones en la app**
   ya no aparezca.

Cuando ninguna política aplicable establece `in_app_updates = false`, el actualizador integrado de la app
funciona con normalidad. Si el indicador **Administrado** aún
aparece, revisa las demás políticas del espacio de trabajo, los perfiles de MDM y los archivos
`requirements.toml` del sistema. Consulta
[Ubicaciones y precedencia](/es-419/codex/enterprise/managed-configuration#locations-and-precedence)
para conocer el orden en que se aplican las fuentes administradas.

## Comprender las responsabilidades de seguridad y soporte

Una vez que la app recibe y aplica la política administrada de actualizaciones, esta:

- Impide que la app de escritorio busque, descargue o instale actualizaciones
mediante su propio actualizador.
- No proporciona fijación de versiones administrada por OpenAI ni un canal de versiones independiente,
y tampoco garantiza que las versiones anteriores sean compatibles con el servicio.
- Se aplica a la app de escritorio de ChatGPT en las compilaciones compatibles para macOS y Windows. No
administra las actualizaciones de apps para dispositivos móviles, Codex CLI ni la extensión para IDE.

## Solucionar problemas comunes

Si un problema de autenticación, conexión o tiempo de espera impide que la app
obtenga o aplique la política administrada, su actualizador integrado puede
permanecer habilitado. No des por hecho que la app bloquea las actualizaciones a menos que aparezca **Administrado**.

Si el indicador **Administrado** no aparece, confirma que:

- El usuario afectado seleccionó el espacio de trabajo correcto.
- La política está asignada a ese usuario, grupo o plataforma.
- El dispositivo ejecuta una versión compatible de la app.
- La app puede conectarse al servicio que distribuye las políticas administradas.
- La configuración se encuentra en **requirements.toml**, no en **config.toml**.
- El usuario cerró por completo y volvió a abrir la app después de que guardaste la política.

Si no puedes abrir Configuración administrada o guardar una política, confirma que tienes
acceso de administrador de Codex para el espacio de trabajo.

Si la versión de la app cambia después de desactivar las actualizaciones en la app, verifica si
Microsoft Store, Intune, MDM, un administrador de paquetes u otro sistema de implementación
instaló la actualización. La política solo controla el actualizador integrado de la app.

## Documentación relacionada

- [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
- [Implementar la app para Windows](/es-419/codex/enterprise/windows-deployment)
- [Referencia de configuración de `requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
