## Objectif du Projet
Déterminer si les reviewers manifestent des attitudes plus positives (sentiment, bienveillance, absence de critique dure) dans leurs commentaires lorsqu'ils évaluent des PRs générées par des agents IA comparées aux PRs humaines.

## Contexte et Motivation
Avec l'essor des agents de codage autonomes alimentés par l'IA, tels que GitHub Copilot et ChatGPT, le paysage du développement logiciel est en pleine transformation. Ces agents IA assistent les développeurs en générant du code, en suggérant des améliorations et en automatisant des tâches répétitives. Cependant, l'intégration de ces agents dans les flux de travail collaboratifs soulève des questions importantes sur la dynamique d'équipe et la communication. En particulier, il est crucial de comprendre comment les développeurs perçoivent et interagissent avec les contributions générées par l'IA, notamment à travers les commentaires et les critiques formulées lors de la revue de code.

## Hypothèse de Recherche
H0 — Hypothèse nulle
Il n’y a pas de différence significative dans le ton (sentiment, politesse, bienveillance) des commentaires de review entre les PRs générées par des agents IA et celles générées par des développeurs humains.

H1 — Hypothèse alternative
Les reviewers utilisent un ton plus positif et bienveillant lorsqu’ils commentent les PRs générées par des agents IA que lorsqu’ils commentent des PRs générées par des développeurs humains.

## Méthodologie
1. **Collecte de Données** : Extraction des commentaires provenant du dataset AIDev (plus de 39k commentaires). Tous les PRs étant générés par des agents IA, la distinction IA vs humain est effectuée via la colonne `user_type` qui précise si le commentaire provient d'un Bot ou d'un User.
2. **Analyse de Sentiment** : Application d'une double analyse VADER et TextBlob dans `sentiment_analysis.ipynb` (Étapes 4 à 10) pour enrichir chaque commentaire avec les scores neg/neu/pos/compound, polarity/subjectivity ainsi que la catégorie de sentiment.
3. **Comparaison Statistique** : Constitution d'un échantillon stratifié équilibré (5k commentaires Bot vs 5k User), calcul des statistiques descriptives, puis exécution d'un test de Mann-Whitney U (Étape 13) afin d'évaluer la différence de ton entre les deux groupes.
4. **Contrôle et Limites** : Les colonnes additionnelles (longueur des textes, `user_type`) sont utilisées pour contextualiser les résultats; toutefois, des variables de confusion potentielles (langage, taille de la PR, agent IA spécifique) ne sont pas contrôlées dans cette analyse initiale.

## Évaluation
- Notebook `sentiment_analysis.ipynb` documente l'intégralité du pipeline, de la préparation des données (Étapes 1-3) à la comparaison statistique (Étapes 11-13).

## Résultats
- **Distribution du corpus** : 39 122 commentaires (70.1 % Bot, 29.9 % User).
- **Tonalité moyenne** : Score VADER moyen de 0.1434 pour les Bots vs 0.1000 pour les Users (différence de +0.0433, Mann-Whitney U = 13 052 765.50, p-value = 0.000113 < 0.05).
- **Catégories de sentiment** :
  - Bots : 50.5 % positifs, 36.2 % négatifs, 13.3 % neutres (profil plus polarisé).
  - Users : 39.3 % positifs, 21.6 % négatifs, 39.1 % neutres (profil plus équilibré).
- **Longueur moyenne** : Bots 172 mots vs Users 57 mots (x3).
- **Variabilité** : Ecart-type VADER de 0.5641 pour les Bots contre 0.4494 pour les Users, indiquant un ton automatisé plus variable.
- **Conclusion statistique** : Rejet de H0; les commentaires générés par des Bots sont significativement plus positifs que ceux des utilisateurs humains.

## Conclusions et Travaux Futurs
- **Synthèse** : Les reviewers automatisés maintiennent un ton plus positif et détaillé alors que les humains fournissent des commentaires plus concis et équilibrés. Cela confirme l'hypothèse H1 et suggère que la présence d'agents IA influence la dynamique des revues.
- **Travaux futurs** :
  1. Ajouter des variables de contexte (langage, taille de PR, agent IA précis) pour affiner l'analyse.
  2. Relier le ton des commentaires aux résultats de la PR (acceptation, temps de merge, corrections requises).
  3. Étendre l'analyse à d'autres jeux de données (GitLab, Bitbucket) pour valider la généralisation.

## Références
@misc{li2025aiteammates_se3,
  title={The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering}, 
  author={Hao Li and Haoxiang Zhang and Ahmed E. Hassan},
  year={2025},
  eprint={2507.15003},
  archivePrefix={arXiv},
  primaryClass={cs.SE},
  url={https://arxiv.org/abs/2507.15003}
}