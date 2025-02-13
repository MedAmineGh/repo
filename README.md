#    Deep SORT Realtime

Cette implémentation est une version adaptée de Deep SORT (Simple Online and Realtime Tracking) permettant de suivre des objets en temps réel.
Dépendances

Avant de commencer, assurez-vous d'installer les dépendances nécessaires à votre environnement :
```bash
pip install numpy scipy opencv-python
pip install torch torchvision  # Si vous utilisez le modèle MobileNetV2 par défaut
pip install tensorflow  # Si vous utilisez TensorFlow 2+
pip install git+https://github.com/openai/CLIP.git  # Si vous utilisez l'embedder CLIP
```
#    Installation

Vous pouvez installer deep-sort-realtime de deux façons :

**Via PyPI :**
```bash
pip3 install deep-sort-realtime
```
**Clonez ce repo et installez en tant que package Python :**
```bash
git clone https://github.com/nwojke/deep_sort.git
cd deep_sort
pip3 install .
```
#    Utilisation
Exemple de script : ObjectTracker_infer.py

Le script ObjectTracker_infer.py utilise Deep SORT pour effectuer un suivi d'objets en temps réel à partir d'un flux vidéo. Ce script prend en entrée une vidéo ou une source d'image et applique un suivi d'objets en utilisant un détecteur d'objets que vous fournissez.
#    Fonctionnement :

***Initialisation de Deep SORT :***
Le tracker est initialisé avec une configuration par défaut, y compris le paramètre max_age qui contrôle combien de frames une piste peut exister sans mises à jour avant d'être supprimée.

***Chargement du détecteur d'objets :***
Le script inclut une fonction de détection d'objets. Cela peut être n'importe quel détecteur comme YOLO, SSD ou Faster-RCNN qui renvoie des boîtes englobantes dans un format spécifique attendu par Deep SORT (coordonnées des boîtes, confiance, et classe de détection).

***Mise à jour du suivi :***
Le script passe chaque frame de la vidéo dans le tracker pour mettre à jour et suivre les objets détectés. Chaque boîte de détection est associée à une piste unique. Le suivi continue même si les objets se déplacent d'une frame à l'autre.

***Affichage des résultats :***
Le script dessine les boîtes de suivi sur chaque frame, associées à un identifiant unique de la piste (ID). Ces informations sont affichées à l'écran en temps réel.



#    Conclusion

Le script ObjectTracker_infer.py montre comment intégrer Deep SORT avec un détecteur d'objets pour suivre des objets en temps réel. Ce modèle est conçu pour être flexible et peut être adapté pour utiliser différents types de détecteurs en fonction de vos besoins.
