## URL du Dataset
https://huggingface.co/datasets/hao-li/AIDev

## Objectif du Projet
Déterminer si les reviewers manifestent des attitudes plus positives (sentiment, bienveillance, absence de critique dure) dans leurs commentaires lorsqu'ils évaluent des PRs générées par des agents IA comparées aux PRs humaines.

## Contexte et Motivation
Avec l'essor des agents de codage autonomes alimentés par l'IA, tels que GitHub Copilot et ChatGPT, le paysage du développement logiciel est en pleine transformation. Ces agents IA assistent les développeurs en générant du code, en suggérant des améliorations et en automatisant des tâches répétitives. Cependant, l'intégration de ces agents dans les flux de travail collaboratifs soulève des questions importantes sur la dynamique d'équipe et la communication. En particulier, il est crucial de comprendre comment les développeurs perçoivent et interagissent avec les contributions générées par l'IA, notamment à travers les commentaires et les critiques formulées lors de la revue de code.

## Hypothèse de Recherche
Les reviewers adoptent des attitudes plus positives dans leurs commentaires lorsqu'ils évaluent des PRs générées par des agents IA par rapport aux PRs créées par des développeurs humains.

## Méthodologie
1. **Collecte de Données** : Utiliser le dataset AIDev pour extraire des PRs générées par des agents IA et des PRs humaines, ainsi que les commentaires associés.
2. **Analyse de Sentiment** : Appliquer des techniques de traitement du langage naturel (NLP) pour analyser le sentiment des commentaires des reviewers.
3. **Comparaison Statistiquee** : Effectuer des tests statistiques pour comparer les attitudes exprimées dans les commentaires des deux groupes de PRs.
4. **Contrôle des Variables Confondantes** : Prendre en compte des facteurs tels que la complexité de la PR, le contexte du projet et l'expérience du reviewer.

## Evaluation.

## Resultats Attendus

## Conclusions et Travaux Futurs

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