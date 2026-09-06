<!-- source: https://learn.chatgpt.com/es-419/docs/windows/windows-app -->

# Aplicación de escritorio de ChatGPT para Windows

La [aplicación de escritorio de ChatGPT para Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) te ofrece una única interfaz para
trabajar en distintos proyectos, mantener chats en paralelo y revisar resultados.
La aplicación para Windows admite flujos de trabajo esenciales, como worktrees, tareas programadas, funciones de Git,
el navegador integrado, vistas previas de archivos, complementos y habilidades.
Se ejecuta de forma nativa en Windows mediante PowerShell y el
[sandbox de Windows](/es-419/codex/windows/windows-sandbox#windows-sandbox), o puedes configurarla para que
se ejecute en el [Subsistema de Windows para Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl).

  
    
  

## Descargar la aplicación de escritorio de ChatGPT

Descarga la [aplicación de escritorio de ChatGPT](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) para Windows.

Luego, sigue el [Inicio rápido](/es-419/codex/quickstart?setup=app) para comenzar.

Para conocer las opciones de instalación y actualización para empresas, consulta
[Implementar la aplicación para Windows](/es-419/codex/enterprise/windows-deployment).

Si prefieres instalarla desde la línea de comandos, ejecuta:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## Sandbox nativo

La aplicación de escritorio de ChatGPT en Windows admite un [sandbox de Windows](/es-419/codex/windows/windows-sandbox#windows-sandbox) nativo cuando el agente se ejecuta en PowerShell y usa el entorno aislado de Linux cuando ejecutas el agente en el [Subsistema de Windows para Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl). Para aplicar las protecciones del sandbox en cualquiera de los dos modos, selecciona **Solicitar aprobación** debajo del editor antes de enviar mensajes a Codex.

  Ejecutar Codex en modo de acceso completo significa que no se limita al directorio de tu proyecto
  y podría realizar acciones destructivas involuntarias que pueden provocar
  la pérdida de datos. Mantén los límites del sandbox y usa
[reglas](/es-419/codex/agent-configuration/rules) para excepciones específicas, o establece tu
[política de aprobación en
  never](/es-419/codex/agent-approvals-security#run-without-approval-prompts) para que
  Codex intente resolver problemas sin solicitar permisos elevados,
  según tu [configuración de aprobación y seguridad](/es-419/codex/agent-approvals-security).

## Personalizar tu configuración de desarrollo

<section class="feature-grid">

<div>

### Editor preferido

Elige una aplicación predeterminada para **Abrir**, como Visual Studio, VS Code u otro
editor. Puedes cambiar esa opción para cada proyecto. Si ya elegiste una
aplicación diferente en el menú **Abrir** de un proyecto, la opción específica de ese
proyecto tendrá prioridad.

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### Terminal integrada

También puedes elegir la terminal integrada predeterminada. Según lo que tengas
instalado, las opciones incluyen:

- PowerShell
- Símbolo del sistema
- Git Bash
- WSL

Este cambio solo se aplica a las sesiones nuevas de la terminal. Si ya tienes una
terminal integrada abierta, reinicia la aplicación o inicia un chat nuevo para que
aparezca la nueva terminal predeterminada.

</div>

  
    
  

</section>

## Subsistema de Windows para Linux (WSL)

De forma predeterminada, la aplicación de escritorio de ChatGPT usa el agente de Codex nativo de Windows. Esto significa que el agente
ejecuta comandos en PowerShell. La aplicación también puede trabajar con proyectos almacenados en el
Subsistema de Windows para Linux 2 (WSL2) mediante la CLI `wsl` cuando sea necesario.

Si quieres agregar un proyecto desde el sistema de archivos de WSL, haz clic en **Agregar proyecto nuevo**
o presiona <kbd>Ctrl</kbd>+<kbd>O</kbd>; luego, escribe `\\wsl$\` en la ventana del
Explorador de archivos. Allí, elige tu distribución de Linux y la carpeta que
quieras abrir.

Si planeas seguir usando el agente nativo de Windows, conviene almacenar los proyectos en
el sistema de archivos de Windows y acceder a ellos desde WSL mediante
`/mnt/<drive>/...`. Esta configuración es más confiable que abrir los proyectos
directamente desde el sistema de archivos de WSL.

Si quieres que el propio agente se ejecute en WSL2, abre **[Configuración](codex://settings)**,
cambia el agente de Nativo de Windows a WSL y **reinicia la aplicación**. El
cambio no se aplica hasta que la reinicias. Tus proyectos deberían conservarse
después del reinicio.

WSL1 fue compatible hasta Codex `0.114`. A partir de Codex `0.115`, el sandbox de Linux
pasó a usar `bubblewrap`, por lo que WSL1 ya no es compatible.

  
    
  

La terminal integrada se configura de manera independiente del agente. Consulta
[Personalizar tu configuración de desarrollo](#customize-for-your-dev-setup) para conocer las
opciones de terminal. Puedes mantener el agente en WSL y seguir usando PowerShell en la
terminal, o usar WSL para ambos, según tu flujo de trabajo.

## Herramientas útiles para desarrolladores

Codex funciona mejor si ya tienes instaladas algunas herramientas comunes para desarrolladores:

- **Git**: habilita el panel de revisión en la aplicación de escritorio de ChatGPT y te permite inspeccionar o
  revertir cambios.
- **Node.js**: una herramienta común que el agente usa para realizar tareas con mayor
  eficiencia.
- **Python**: una herramienta común que el agente usa para realizar tareas con mayor
  eficiencia.
- **.NET SDK**: útil para crear aplicaciones nativas para Windows.
- **GitHub CLI**: habilita las funciones específicas de GitHub en la aplicación de escritorio de ChatGPT.

Instálalas con el administrador de paquetes predeterminado de Windows, `winget`, pegando lo siguiente
en la [terminal integrada](/es-419/codex/integrated-terminal) o
pidiéndole a Codex que las instale:

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

Después de instalar GitHub CLI, ejecuta `gh auth login` para habilitar las funciones de GitHub en
la aplicación.

Si necesitas otra versión de Python o .NET, cambia los identificadores de paquete por los de la
versión que quieras.

## Solución de problemas y preguntas frecuentes

### Ejecutar comandos con permisos elevados

Si necesitas que Codex ejecute comandos con permisos elevados, inicia la propia aplicación
de escritorio de ChatGPT como administrador. Después de instalarla, abre el menú Inicio,
busca la aplicación y elige **Ejecutar como administrador**. El agente de Codex hereda ese
nivel de permisos.

### La directiva de ejecución de PowerShell bloquea comandos

Si nunca has usado herramientas como Node.js o `npm` en PowerShell, pueden aparecer errores relacionados con la directiva de ejecución en el
agente de Codex o en la terminal integrada.

Esto también puede ocurrir si Codex crea scripts de PowerShell para ti. En ese caso,
quizá necesites una directiva de ejecución menos restrictiva para que PowerShell pueda
ejecutarlos.

Un error puede verse así:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

Una solución común es establecer la directiva de ejecución en `RemoteSigned`:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Para conocer los detalles y otras opciones, consulta la
[guía sobre la directiva de ejecución](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) de Microsoft
antes de cambiar la directiva.

### Scripts del entorno local en Windows

Si tu [entorno local](/es-419/codex/environments/local-environment) usa comandos multiplataforma,
como scripts de `npm`, puedes mantener un mismo script de configuración o un
conjunto de acciones para todas las plataformas.

Si necesitas un comportamiento específico de Windows, crea scripts de configuración específicos de Windows o
acciones específicas de Windows.

Las acciones se ejecutan en el entorno que usa tu terminal integrada. Consulta
[Personalizar tu configuración de desarrollo](#customize-for-your-dev-setup).

Los scripts de configuración local se ejecutan en el entorno del agente: WSL si el agente usa WSL,
y PowerShell en caso contrario.

### Compartir la configuración, la autenticación y las sesiones con WSL

La aplicación para Windows usa el mismo directorio de inicio de Codex que Codex nativo en Windows:
`%USERPROFILE%\.codex`.

Si también ejecutas Codex CLI dentro de WSL, la CLI usa de forma predeterminada el directorio de inicio
de Linux, por lo que no comparte automáticamente la configuración, la autenticación en caché
ni el historial de sesiones con la aplicación para Windows.

Para compartirlos, usa uno de estos métodos:

- Sincroniza `~/.codex` de WSL con `%USERPROFILE%\.codex` en tu sistema de archivos.
- Configura `CODEX_HOME` para que WSL use el directorio principal de Codex en Windows:

```bash

```

Si quieres usar esa configuración en cada shell, agrégala al perfil de tu shell de WSL, como
`~/.bashrc` o `~/.zshrc`.

### Las funciones de Git no están disponibles

Si no tienes Git instalado de forma nativa en Windows, la app no puede usar algunas
funciones. Instálalo con `winget install Git.Git` desde PowerShell o `cmd.exe`.

### Git no se detecta en los proyectos abiertos desde `\\wsl$`

Por ahora, si quieres usar el agente nativo de Windows con un proyecto que también sea
accesible desde WSL, la solución alternativa más confiable es almacenar el proyecto
en la unidad nativa de Windows y acceder a él desde WSL mediante `/mnt/<drive>/...`.

### `Cmder` no aparece en el cuadro de diálogo Abrir

Si `Cmder` está instalado pero no aparece en el cuadro de diálogo Abrir de Codex, agrégalo al
menú Inicio de Windows: haz clic con el botón derecho en `Cmder` y elige **Agregar a Inicio**; luego,
reinicia Codex o la computadora.
