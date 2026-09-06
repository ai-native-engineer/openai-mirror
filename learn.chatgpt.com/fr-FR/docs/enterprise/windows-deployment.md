<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/windows-deployment -->

Les utilisateurs peuvent installer eux-mêmes l’application de bureau ChatGPT, ou votre équipe informatique peut
la déployer à l’aide d’un outil de gestion d’entreprise. L’application est signée par le Store, mais
les utilisateurs n’ont pas besoin d’ouvrir le Microsoft Store pour l’installer ou la mettre à jour.

## Permettre aux utilisateurs d’installer et de mettre à jour l’application

Si les utilisateurs peuvent gérer eux-mêmes leurs applications, orientez-les vers le
[programme d’installation web](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi).
Celui-ci offre l’expérience standard d’installation et de mise à jour
automatique. Des composants du Microsoft Store peuvent apparaître pendant l’installation ou
les mises à jour, mais les utilisateurs n’ont pas besoin d’accéder eux-mêmes au Store.

Vous pouvez également installer l’application depuis la ligne de commande :

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## Déployer l’application à l’aide d’un outil de gestion d’entreprise

Si votre organisation gère les logiciels de manière centralisée, utilisez Microsoft Intune ou
une autre plateforme compatible de gestion des appareils mobiles (MDM) ou de déploiement
de logiciels. Si votre plateforme prend en charge le déploiement d’applications du Microsoft Store, recherchez
ChatGPT from OpenAI dans le processus de déploiement d’applications du Store, ou utilisez cet ID de produit du Store :

```text
9PLM9XGG6VKS

Pour plus de détails sur la configuration, consultez la documentation Microsoft suivante :

- [Guide de déploiement en entreprise](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Guide de déploiement avec Intune](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [Guide de déploiement avec MECM](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [Ajouter des applications du Microsoft Store à Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### Gérer les mises à jour de l’application

Pour obtenir des instructions de configuration et des recommandations de déploiement, consultez
[Gérer les mises à jour de l’application](/fr-FR/codex/enterprise/manage-app-updates).

## Installer l’application sans les services de distribution Microsoft

Si votre environnement ne permet pas d’utiliser les services Microsoft de distribution d’applications pour
l’installation initiale, téléchargez le package MSIX signé par le Store pour chaque
architecture d’appareil :

| Architecture de l’appareil | Package                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

Ces liens stables renvoient à la dernière version publiée du package signé par le Store pour chaque
architecture. Pour les flux de travail de déploiement hors ligne nécessitant un fichier de licence,
téléchargez également la
[licence hors ligne (`ChatGPT-License.xml`)](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml).
Importez le package MSIX approprié et, si nécessaire, le fichier de licence dans votre solution MDM
ou votre plateforme de déploiement de logiciels.

Après l’installation initiale, les appareils pouvant accéder à
`persistent.oaistatic.com` peuvent installer automatiquement les mises à jour, sauf si la
configuration gérée désactive l’outil de mise à jour intégré à l’application. Si vous désactivez les mises à jour
depuis l’application, déployez des packages plus récents à l’aide de votre solution MDM ou de votre outil de déploiement de logiciels.

Cette méthode de déploiement :

- Prend en charge l’installation initiale dans les environnements restreints.
- Prend en charge les appareils x64 et Arm64.
- Ne fournit ni package MSI autonome ni fichier EXE distribué hors du Store.

## Ressources connexes

- [Gérer les mises à jour de l’application](/fr-FR/codex/enterprise/manage-app-updates)
- [Application de bureau ChatGPT pour Windows](/fr-FR/codex/app/windows)
