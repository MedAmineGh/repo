#  YOLOv8s Training and Inference Script

**Description**

Ce script utilise la bibliothèque Ultralytics YOLO pour charger un modèle YOLOv8s pré-entraîné sur COCO, l'entraîner sur un sous-ensemble de COCO et effectuer une inférence sur une image.

**Prérequis**

Avant d'exécuter ce script, assurez-vous d'avoir installé les dépendances suivantes :

Python 3.8+

ultralytics (YOLOv8)

Les bibliothèques nécessaires pour le traitement d'image (OpenCV, numpy, etc.)

**Installez les dépendances avec la commande :**
```bash
pip install ultralytics 
```
#  Contenu du script

**Chargement du modèle YOLOv8n pré-entraîné**
```bash
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
```
Le modèle YOLOv8n est chargé avec des poids pré-entraînés sur COCO.

**Affichage des informations du modèle (optionnel)**
```bash
model.info()
```
Cette ligne affiche des détails sur l'architecture du modèle.

**Entraînement du modèle**

results = model.train(data="coco8.yaml", epochs=100, imgsz=640)


**Inférence sur une image**
```bash
results = model("path/to/bus.jpg")
```
Cette ligne exécute l'inférence sur une image donnée.

**Exécution du script**

Sauvegardez le script sous yolov8_script.py et exécutez-le avec :
```bash
python yolov8_script.py
```
