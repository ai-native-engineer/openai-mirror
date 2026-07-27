<!-- source: https://openai.com/fr-CA/index/introducing-openai-privacy-filter/ -->

22 avril 2026

[Recherche](/news/research/)[Versions](/research/index/release/)[Cybersécurité](/news/security/)

# Présentation de OpenAI Privacy Filter

Notre modèle de pointe pour le masquage des informations personnellement identifiables (PII) au sein des textes

Chargement…

Partager

Aujourd’hui, nous lançons OpenAI Privacy Filter, un modèle à poids ouverts permettant de détecter et de masquer les informations personnelles identifiables (PII) dans un texte. Cette version s’inscrit dans notre démarche plus large visant à soutenir un écosystème logiciel plus résilient, en fournissant aux développeurs une infrastructure concrète pour créer avec l’IA en toute sécurité, notamment grâce à des [outils⁠](https://openai.com/index/codex-security-now-in-research-preview/) et des [modèles⁠](https://openai.com/index/scaling-trusted-access-for-cyber-defense/) qui facilitent la mise en place de solides protections en matière de confidentialité et de sécurité dès le départ.

Privacy Filter est un petit modèle doté d’une capacité de détection des données personnelles de pointe. Il est conçu pour des flux de travail de confidentialité à haut débit et permet une détection des informations personnelles identifiables en tenant compte du contexte dans des textes non structurés. Il peut s’exécuter localement, ce qui signifie que les informations personnelles identifiables peuvent être masquées ou supprimées sans pour autant quitter votre machine. Il traite efficacement de longues entrées, ce qui permet de prendre rapidement des décisions de masquage en un seul passage.

Chez OpenAI, nous utilisons une version ajustée de Privacy Filter dans nos propres flux de travail respectueux de la confidentialité. Nous avons développé Privacy Filter, car nous pensons qu’avec les dernières avancées en IA, il est possible d’élever les normes de confidentialité au-delà de ce qui existe déjà sur le marché. La version de Privacy Filter que nous lançons aujourd’hui atteint des performances de pointe sur le benchmark PII-Masking-300k, après correction des erreurs d’annotation identifiées lors de l’évaluation.

Avec cette version, les développeurs peuvent exécuter Privacy Filter dans leurs propres environnements, l’adapter à leurs cas d’usage et intégrer des protections renforcées de la vie privée dans leurs pipelines d’entraînement, d’indexation, de journalisation et de revue.

## Un petit modèle doté d'une capacité de détection de données personnelles de pointe

La protection de la vie privée dans les systèmes d’intelligence artificielle modernes ne repose pas uniquement sur la reconnaissance de formes. Les outils traditionnels de détection des informations personnelles identifiables (PII) reposent souvent sur des règles déterministes pour des formats tels que les numéros de téléphone et les adresses courriel. Ils peuvent bien fonctionner pour des cas d’usage restreints, mais passent souvent à côté d’informations personnelles plus subtiles et ont du mal à saisir le contexte.

Le filtre de confidentialité est conçu avec une compréhension plus approfondie du langage et du contexte et pour des performances plus nuancées. En combinant une compréhension avancée du langage avec un système d’annotation spécifique à la confidentialité, il peut détecter un éventail plus large d’informations personnelles identifiables dans des textes non structurés, y compris lorsque la décision correcte dépend du contexte. Il peut faire plus efficacement la distinction entre les informations qui doivent être conservées parce qu’elles sont publiques et les informations qui doivent être masquées ou expurgées parce qu’elles se rapportent à un particulier.

Il en résulte un modèle suffisamment performant pour offrir un niveau de filtrage de la confidentialité de pointe. Parallèlement, le modèle est suffisamment léger pour être exécuté localement—ce qui permet de conserver les données qui n'ont pas encore été filtrées sur l’appareil, avec un risque d’exposition réduit, plutôt que de devoir les envoyer vers un serveur pour les dé-identifier.

## Présentation du modèle

Privacy Filter est un modèle bidirectionnel de classification de tokens avec décodage de segments. Il part d’un point de contrôle préentraîné autorégressif, puis est adapté en un classificateur de tokens basé sur une taxonomie fixe d’étiquettes de confidentialité. Au lieu de générer du texte token par token, il annote la séquence d’entrée en une seule passe, puis décode des segments cohérents à l’aide d’une procédure de Viterbi contrainte.

Cette architecture confère à Privacy Filter quelques propriétés utiles pour une utilisation en production :

* **Rapide et efficace :** tous les tokens sont étiquetés en un seul passage.
* **Tient compte du contexte :** l’a priori linguistique permet de détecter les segments d’informations personnelles identifiables en fonction du contexte environnant.
* **Contexte long :** le modèle publié prend en charge jusqu'à 128 000 tokens de contexte.
* **Configurable :** les développeurs peuvent ajuster les points de fonctionnement afin de trouver un compromis entre le rappel et la précision en fonction de leur flux de travail.

Le modèle publié compte 1,5 milliard de paramètres au total, dont 50 millions de paramètres actifs.

Privacy Filter prédit des segments dans huit catégories :

* `personne_privée`
* `adresse_privée`
* `courriel_privé`
* `téléphone_privé`
* `URL_privée`
* `date_privée`
* `numéro_de_compte`
* `secret`

La catégorie `numéro_de_compte` permet de masquer un large éventail de numéros de compte, y compris des informations bancaires telles que les numéros de carte de crédit et les numéros de compte bancaire, tandis que `secret` permet de masquer des éléments comme les mots de passe et les clés API.

Ces étiquettes sont décodées à l'aide de balises d'étendue BIOES, ce qui permet d'obtenir des frontières de masquage plus nettes et plus cohérentes.

## Exemple de texte d'entrée

Objet : suivi de la planification du T2

Bonjour Jordan,

Merci encore de m'avoir rencontré plus tôt dans la journée. Je souhaitais faire un suivi concernant le calendrier révisé du déploiement au T2 et confirmer que le lancement du produit est prévu pour le 18 septembre 2026. Pour référence, le fichier du projet est répertorié sous le numéro 4829-1037-5581. Si quelque chose change de votre côté, n'hésitez pas à répondre à maya.chen@example.com ou à m'appeler au +1 (415) 555-0124.

Cordialement,

Maya Chen

## Texte après masquage des identifiants personnels

Objet : suivi de la planification du T2

Bonjour `[PRIVATE_PERSON]`,

Merci encore de m'avoir rencontré plus tôt dans la journée. Je souhaitais faire un suivi concernant le calendrier révisé du déploiement au T2 et confirmer que le lancement du produit est prévu pour le `[PRIVATE_DATE]`. Pour référence, le fichier du projet est répertorié sous le numéro `[ACCOUNT_NUMBER]`. Si quelque chose change de votre côté, n'hésitez pas à répondre à `[PRIVATE_EMAIL]` ou à m'appeler au `[PRIVATE_PHONE]`.

Cordialement,

**[PRIVATE\_PERSON]**

## Comment nous l'avons conçu

Nous avons développé Privacy Filter en plusieurs étapes.

Tout d'abord, nous avons élaboré une taxonomie de la confidentialité qui définit les types d'extraits que le modèle doit détecter. Cela inclut les identifiants personnels, les coordonnées, les adresses, les dates privées, de nombreux types de numéros de compte, tels que les informations de crédit et bancaires, ainsi que des secrets tels que les clés API et les mots de passe.

Deuxièmement, nous avons transformé un modèle de langage préentraîné en classificateur de tokens bidirectionnel en remplaçant la tête de modélisation du langage par une tête de classification de tokens, puis en le réentraînant avec un objectif de classification supervisée.

Troisièmement, nous avons entraîné le modèle sur un mélange de données publiques et de données synthétiques, conçu pour couvrir à la fois des textes réalistes et des schémas de confidentialité complexes. Dans les portions des données publiques où les annotations étaient incomplètes, nous avons eu recours à une annotation assistée par le modèle et à une relecture afin d’en améliorer la couverture. Nous avons également généré des exemples synthétiques afin d'accroître la diversité dans les formats, les contextes et les sous-types de confidentialité.

Lors de l’inférence, les prédictions au niveau des tokens du modèle sont décodées en segments cohérents à l’aide d’un décodage de séquence contraint. Cette approche préserve la compréhension générale du langage du modèle préentraîné tout en le spécialisant pour la détection des atteintes à la vie privée.

## Performances de Privacy Filter

Nous avons évalué Privacy Filter sur des benchmarks standards ainsi que sur des évaluations supplémentaires, synthétiques et de type conversationnel, conçues pour tester des cas plus difficiles et plus sensibles au contexte.

Dans l’[évaluation PII-Masking-300k⁠(s'ouvre dans une nouvelle fenêtre)](https://huggingface.co/datasets/ai4privacy/pii-masking-300k), Privacy Filter obtient un score F1 de 96 % (94,04 % de précision et 98,04 % de rappel). Sur une version corrigée du benchmark qui tient compte des problèmes d’annotation du jeu de données identifiés lors de la révision, le score F1 a été de 97,43 % (96,79 % de précision et 98,08 % de rappel).

Nous avons également constaté que le modèle peut être adapté efficacement. L'ajustement sur une quantité même limitée de données améliore rapidement la précision sur des tâches propres à un domaine, faisant passer le score F1 de 54 % à 96 %, et atteint presque la saturation sur le benchmark d'adaptation au domaine que nous avons évalué.

Au-delà des performances sur les benchmarks, Privacy Filter est conçu pour un filtrage de la confidentialité efficace dans des textes réels, souvent bruités. Cela inclut de longs documents, des références ambiguës, des chaînes de formats mixtes et des secrets liés aux logiciels. La [fiche modèle ⁠(s'ouvre dans une nouvelle fenêtre)](https://cdn.openai.com/pdf/c66281ed-b638-456a-8ce1-97e9f5264a90/OpenAI-Privacy-Filter-Model-Card.pdf)présente également des évaluations ciblées sur la détection de secrets dans des bases de code, ainsi que des tests de résistance sur des exemples multilingues, hostiles et dépendants du contexte.

## Limites

Privacy Filter n'est pas un outil d'anonymisation, une certification de conformité ni un substitut à l'examen des politiques dans des contextes à forts enjeux. Il s'agit de l'un des composants d'un système plus large de protection de la vie privée dès la conception.

Son comportement reflète la taxonomie des libellés et les frontières décisionnelles sur lesquelles il a été entraîné. Différentes organisations peuvent avoir besoin de politiques de détection ou de masquage différentes, et ces politiques peuvent nécessiter une évaluation dans le domaine ainsi qu’un ajustement supplémentaire du modèle. Les performances peuvent également varier selon les langues, les systèmes d’écriture, les conventions de nommage et les domaines qui s’écartent de la distribution d’entraînement.

Comme tous les modèles, Privacy Filter peut faire des erreurs. Il peut ne pas détecter des identifiants peu courants ou des références privées ambiguës, et il peut sur-masquer ou sous-masquer des entités lorsque le contexte est limité, en particulier dans les séquences courtes. Dans les domaines à forte sensibilité tels que les flux de travail juridiques, médicaux et financiers, la révision humaine ainsi que l'évaluation et l'ajustement spécifiques au domaine restent importants.

## Disponibilité

Nous lançons OpenAI Privacy Filter afin de renforcer la protection de la vie privée dans l'ensemble de l'écosystème.

Le modèle est disponible dès aujourd'hui sous la licence Apache 2.0 sur [Hugging Face⁠(s'ouvre dans une nouvelle fenêtre)](https://huggingface.co/openai/privacy-filter) et [Github⁠(s'ouvre dans une nouvelle fenêtre)](https://github.com/openai/privacy-filter). Il est destiné à l’expérimentation, à la personnalisation et au déploiement commercial, et peut être affiné pour s’adapter à différentes distributions de données et politiques de confidentialité.

Parallèlement au modèle, nous mettons à disposition une documentation couvrant l’architecture du modèle, la taxonomie des labels, les mécanismes de décodage, les cas d’usage prévus, le protocole d’évaluation et les limites connues, afin que les équipes puissent comprendre à la fois les points forts du modèle et les situations pour lesquelles son utilisation doit être prudente.

## Perspectives d’avenir

La protection de la vie privée des systèmes d'IA est un effort continu dans les domaines de la recherche, de la conception des produits, de l'évaluation et du déploiement.

Privacy Filter reflète une orientation que nous jugeons importante : des modèles compacts et efficaces, dotés de capacités de pointe dans des tâches étroitement définies qui comptent pour les systèmes d'IA du monde réel. Nous publions ce modèle, car nous pensons que l’infrastructure respectueuse de la vie privée devrait être plus facile à inspecter, exécuter, adapter et améliorer.

Notre objectif : Les modèles doivent apprendre du monde, pas des individus. Privacy Filter contribue à rendre cela possible.

Nous publions cette version préliminaire de Privacy Filter afin de recueillir les retours de la communauté de recherche et de la protection de la vie privée, et d’améliorer encore les performances du modèle.

* [Éthique et sécurité](/news/?tags=ethics-safety)
* [2026](/news/?tags=2026)

## Auteur

## Poursuivez votre lecture

[Afficher tout](/news/)

![Hugging Face Security Incident 1x1](https://images.ctfassets.net/kftzwdyauwt9/1H0bdkoSFFcqNTx4DSNpal/56f4b7575c012f0698b1be0dafb379f0/Hugging_Face_Security_Incident_1x1.png?w=3840&q=90&fm=webp)

[OpenAI et Hugging Face répondent à un incident de sécurité

Cybersécurité21 juill. 2026](/index/hugging-face-model-evaluation-security-incident/)

![GPT 5-6 > Card](https://images.ctfassets.net/kftzwdyauwt9/1a9IPPV5nXWydTBosgmgYI/8e03f28ca04f26edc8bc81cdba387df1/5-6.jpg?w=3840&q=90&fm=webp)

[GPT-5.6 : une intelligence de pointe à la hauteur de vos ambitions

Produit9 juill. 2026](/index/gpt-5-6/)

![Separating signal from noise > Art Card](https://images.ctfassets.net/kftzwdyauwt9/7j6M3prKIsTmV6cbMaHjhZ/e66f7cdd98c66c99546853cbc22cfe84/Seperating-signal-from-noise-card.png?w=3840&q=90&fm=webp)

[Distinguer le signal du bruit dans les évaluations de code

Recherche8 juill. 2026](/index/separating-signal-from-noise-coding-evaluations/)
