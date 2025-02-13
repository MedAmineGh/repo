README - Entraînement de YOLO pour l'Estimation de l'Âge

Ce projet propose deux approches pour estimer l'âge à l'aide du modèle YOLO :

Régression : Prédit un âge sous forme d'une valeur continue.

Classification : Catégorise l'âge en classes prédéfinies.

1. Entraînement avec Régression

Le premier script utilise une approche de régression pour estimer l'âge.

Fichier : train_age_regression.py

Explication :

Utilise YOLOv8 avec un fichier de configuration yolov8n-regress.yaml.

Le dataset est défini dans imdb10-age.yaml.

Entraînement sur 3 epochs.

Après l'entraînement, le modèle est sauvegardé sous trained_yolov8n_age_model.pt.

Exécution :

python train_age_regression.py

2. Entraînement avec Classification

Le second script utilise une approche de classification pour estimer l'âge.

Fichier : train_age_classification.py

Explication :

Utilise YOLOv8 avec un fichier de configuration relu6-yolov11-cls.yaml.

Le dataset est défini dans data.yaml.

Entraînement sur 50 epochs avec un batch size de 16 et une taille d'image de 640.

Ne sauvegarde pas explicitement le modèle mais termine l'entraînement avec un message de confirmation.

Exécution :

python train_age_classification.py

Comparaison des deux méthodes

Méthode

Type de Sortie

Modèle Utilisé

Epochs

Taille Image

Batch Size

Régression

Valeur continue

yolov8n-regress.yaml

3

Par défaut

Par défaut

Classification

Catégorie (âge en classe)

relu6-yolov11-cls.yaml

50

640

16

Prérequis

Python 3.8+

Bibliothèque ultralytics

GPU (fortement recommandé pour accélérer l'entraînement)

Installation des dépendances

pip install ultralytics

Conclusion

| Méthode       | Type de Sortie          | Modèle Utilisé         | Epochs | Taille Image | Batch Size |
|--------------:|:-----------------------:|-----------------------:|-------:|-------------:|-----------:|
| Régression    | Valeur continue         | `yolov8n-regress.yaml` |      3 | Par défaut   | Par défaut |
| Classification| Catégorie (âge en classe)| `relu6-yolov11-cls.yaml` |     50 | 640         | 16        |

Le choix dépend du besoin de votre application.
