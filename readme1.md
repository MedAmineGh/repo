#  YOLOv11 Relu6 classfication Training Script

Ce script permet d'entraîner un modèle YOLOv8 en utilisant la bibliothèque Ultralytics.

#  **Prérequis**

Avant d'exécuter ce script, assurez-vous d'avoir installé les dépendances requises :

```bash
pip install ultralytics
```

#  Utilisation

Le script train_yolo.py est conçu pour entraîner un modèle YOLOv11 Relu6 classfication en utilisant un fichier de configuration et un dataset défini.

#  Exécution du script

Pour lancer l'entraînement, exécutez la commande suivante :

```bash
python train_yolo.py
```

#  Paramètres

Le script prend les paramètres suivants :

**model_path:** Chemin vers le modèle YOLO (pré-entraîné ou fichier YAML pour un entraînement à partir de zéro). Par défaut : relu6-yolov11-cls.yaml.

**data_path:** Chemin vers le fichier YAML contenant les informations du dataset. Par défaut : data.yaml.

**epochs:** Nombre d'époques d'entraînement. Par défaut : 50.

**batch_size:** Taille du batch. Par défaut : 16.

**img_size:** Taille des images d'entrée. Par défaut : 640.

#  Résultats de l'entraînement

Après l'entraînement, les résultats seront sauvegardés dans un dossier généré par la bibliothèque Ultralytics, contenant :

  -Les poids du modèle entraîné.

  -Les logs d'entraînement.

  -Les graphiques de performance.

#  Remarque

Assurez-vous que votre dataset est correctement structuré et défini dans data.yaml.
