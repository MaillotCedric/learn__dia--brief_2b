# Objectifs

1. Enrichir le modèle fonctionnel en y ajoutant les catégories `pizza` et `cake`
2. Mise en place d'un monitoring

---

## Objectif 1

Le modèle à enrichir n'étant pas connu, je me suis mis à la recherche de modèles déjà *pre-trained* que je pourrais enrichir avec les catégories souhaitées (`pizza` et `cake`).
L'objectif étant de pouvoir se rendre compte des outils permettant d'enrichir des modèles.

Je me suis concentré sur un modèle de réseaux de neurones convolutionel (CNN) : MobileNet.
Basé sur des millions d'images de la base de données ImageNet, ce modèle permet déjà de reconnaitre près de 1000 catégories d'images.
Après analyse des différentes [catégories](https://github.com/leferrad/tensorflow-mobilenet/blob/master/imagenet/labels.txt) que MobileNet permet d'identifier, je me suis rendu compte que le modèle permettait déjà d'identifier la catégorie `pizza`, mais pas la catégorie `cake`.

### Recherche de datasets

Afin d'avoir de bonnes performances pour le modèle enrichi, l'idée était de rechercher un nombre conséquent d'images pour chaque catégorie à ajouter.

- Cake
  - [Cakey Bakey](https://www.kaggle.com/datasets/rajkumarl/cakey-bakey)
  - [Cakes Dataset](https://www.kaggle.com/datasets/ishikanaik/cakes-dataset)
- Pizza
  - [Pizza or Not Pizza ?](https://www.kaggle.com/datasets/carlosrunner/pizza-not-pizza)
  - [Pizza classification data](https://www.kaggle.com/datasets/projectshs/pizza-classification-data)
  - [Pizza vs Ice Cream](https://www.kaggle.com/datasets/hemendrasr/pizza-vs-ice-cream)

### Data augmentation

Toujours dans l'idée de performance, je me suis orienté vers la `data augmentation` afin d'augmenter mon jeu de données avec des images qui vont être :

- orientées de manières diverses
- élargies ou reduites au travers de zooms

#### Tutorials for data ugmentation

1. [Data augmentation to address overfitting](https://www.youtube.com/watch?v=mTVf7BN7S8w)
2. [Augmentation des données](https://www.tensorflow.org/tutorials/images/data_augmentation?hl=fr)
3. [Efficient Image Classification with Transfer Learning and Image Augmentation with TensorFlow Keras](https://www.youtube.com/watch?v=CLHk6DniYg0)

### Transfer learning

Afin de pouvoir ajouter des nouvelles catégories à un modèle déjà entrainé, j'ai décidé de me pencher sur la technique du `transfer learning`.

#### Tutorials for transfer learning

1. [Transfer Learning](https://www.youtube.com/watch?v=LsdxvjLWkIY)
