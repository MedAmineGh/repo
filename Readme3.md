#  Détection de Visages avec YOLOv8n

Ce projet utilise YOLOv8n_face pour la détection de visages dans des images.

#  1. Présentation

Le modèle yolov8n-face.pt est un modèle pré-entraîné pour la détection de visages. Ce README explique comment l'utiliser pour prédire les visages sur une image.

#  2. Commande de Prédiction

Pour effectuer une détection de visages sur une image, utilisez la commande suivante :

```bash
yolo task=detect mode=predict model=yolov8n-face.pt conf=0.25 imgsz=1280 line_thickness=1 max_det=1000 source=examples/face.jpg
```

**Explication des paramètres :**

****task=detect :**** Spécifie que la tâche est une détection d'objets.

****mode=predict :**** Indique que nous effectuons une prédiction.

****model=yolov8n-face.pt :**** Modèle pré-entraîné utilisé pour la détection de visages.

****conf=0.25 :**** Seuil de confiance minimum pour afficher une détection.

****imgsz=1280 :**** Taille des images d'entrée en pixels.

****line_thickness=1 :**** Épaisseur des lignes des bounding boxes affichées.

****max_det=1000 :**** Nombre maximum de détections autorisées par image.

****source=examples/face.jpg :**** Chemin de l'image à traiter.

#  3. Installation des dépendances

Avant d'exécuter la commande, assurez-vous d'avoir installé les dépendances requises :
```bash
pip install ultralytics
```
#  4. Exécution

Après l'installation, exécutez la commande de prédiction mentionnée ci-dessus pour détecter les visages dans l'image spécifiée.
