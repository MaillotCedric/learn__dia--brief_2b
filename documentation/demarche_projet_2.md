# Démarche projet

## A. Démarche générale

### A.1. Rappel du projet

Une entreprise fictive (Classifr), souhaite améliorer leur application de classification d'images.

- leur algorithme fonctionne correctement, mais ils aimeraient ajouter deux catégories d'images qui ne sont pas prises en charge actuellement
- l'IA de classification devra être monitorée
- l'application, destinée aux utilisateurs, permet une interaction avec l'IA de classification

### A.2. Démarche envisagée

1. Ajout de nouvelles catégories

   Recherche des différents outils ou techniques permettant d'enrichir des modèles déjà existants

2. Monitoring

   Réflexion sur comment avoir un aperçu du modèle et de ses performances générales

3. Interaction avec l'IA

   Réflexion sur comment l'utilisateur pourra, au travers de différentes interactions, tester et améliorer le modèle

## B. Démarche détaillée

### B.1  Orientations possibles

1. Ajout de nouvelles catégories

   Plusieurs approches sont possibles. Que se soit au travers de solutions IAaaS comme `Custom Vision`, proposé par Azure (Microsoft), ou au travers de librairies Open Source comme `TensorFlow` ou `Keras`.

   L'idée d'utiliser des outils comme `TensorFlow` ou `Keras`, serait de pouvoir prendre avantage de modèles de classification pré-entrainés et dont les performances sont très bonnes.

    `Tensorflow` et `Keras` mettent à disposition tout un tas de fonctions permettant de faire du `Transfer Learning` à partir de modèles très connus comme `EfficientNetV2L`, `MobileNet`, ...

   Le `Transfer Learning` permettrait d'avoir un modèle aux performances comparables sans les temps de calculs élevés et l'utilisation de ressources importantes.

2. Mise en place d'un monitoring

   L'idée derrière la mise en place d'un monitoring serait d'avoir un aperçu du modèle et de ses performances générales.

   - avoir une vue détaillée des bonnes et surtout des mauvaises prédictions
   - pouvoir consulter l'ensemble des métriques qui sont utilisées pour rendre compte des performances du modèle
   - avoir accès aux différentes caractéristiques du modèle
     - les catégories détectées par le modèle
     - les datasets utilisés pour l'entrainement du modèle

3. Interactions avec l'IA

   L'utilisateur pourra interagir avec l'IA afin :

   - d'apporter des précisions importantes dans le cas d'une mauvaise prédiction
     - préciser la catégorie à laquelle appartient réellement l'image
   - d'améliorer les futures prédictions
     - en créant de nouvelles catégories
     - en enrichissant des datasets (upload d'images)
     - en lançant des ré-entrainements

### B.2 Labos