<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/windows-deployment -->

Los usuarios pueden instalar la app de escritorio de ChatGPT por su cuenta, o tu equipo de TI puede
implementarla con una herramienta de administración para empresas. La app cuenta con firma de Store, pero
los usuarios no necesitan abrir Microsoft Store para instalarla ni actualizarla.

## Permitir que los usuarios instalen y actualicen la app

Si los usuarios pueden administrar sus propias aplicaciones, indícales que usen el
[instalador web](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi).
El instalador ofrece la experiencia estándar de instalación y actualización
automática. Es posible que aparezcan componentes de Microsoft Store durante la instalación o
las actualizaciones, pero los usuarios no necesitan navegar por la Store.

También puedes instalar la app desde la línea de comandos:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## Implementar la app con una herramienta de administración para empresas

Si tu organización administra el software de forma centralizada, usa Microsoft Intune u
otra plataforma compatible para la administración de dispositivos móviles (MDM) o la implementación de
software. Si tu plataforma admite la implementación de apps de Microsoft Store, busca
ChatGPT de OpenAI en el flujo de apps de Store o usa este identificador de producto de Store:

```text
9PLM9XGG6VKS

Para conocer los detalles de configuración, consulta la siguiente documentación de Microsoft:

- [Guía de implementación para empresas](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Guía de implementación de Intune](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [Guía de implementación de MECM](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [Agregar apps de Microsoft Store a Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### Administrar las actualizaciones de la app

Para obtener instrucciones de configuración y recomendaciones para la implementación, consulta
[Administrar las actualizaciones de la app](/es-419/codex/enterprise/manage-app-updates).

## Instalar sin los servicios de distribución de Microsoft

Si tu entorno no puede usar los servicios de Microsoft para distribuir apps durante la
instalación inicial, descarga el paquete MSIX con firma de Store correspondiente a cada
arquitectura de dispositivo:

| Arquitectura del dispositivo | Paquete                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

Estos enlaces estables apuntan al paquete con firma de Store publicado más recientemente para cada
arquitectura. Para los flujos de trabajo de implementación sin conexión que requieren un archivo de licencia,
descarga también la
[licencia sin conexión (`ChatGPT-License.xml`)](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml).
Importa el MSIX correspondiente y, cuando sea necesario, el archivo de licencia en tu MDM
o plataforma de implementación de software.

Después de la instalación inicial, los dispositivos con acceso a
`persistent.oaistatic.com` pueden instalar actualizaciones automáticamente, a menos que la
configuración administrada desactive el actualizador integrado de la app. Si desactivas las actualizaciones
desde la app, implementa paquetes más recientes mediante tu MDM o herramienta de implementación de software.

Este método de implementación:

- Permite realizar la instalación inicial en entornos restringidos.
- Es compatible con dispositivos x64 y Arm64.
- No proporciona un MSI independiente ni un EXE que no provenga de Store.

## Recursos relacionados

- [Administrar las actualizaciones de la app](/es-419/codex/enterprise/manage-app-updates)
- [App de escritorio de ChatGPT para Windows](/es-419/codex/app/windows)
