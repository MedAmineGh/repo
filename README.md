Deep SORT Realtime

Cette implémentation est une version adaptée de Deep SORT (Simple Online and Realtime Tracking) permettant de suivre des objets en temps réel.
Dépendances

Avant de commencer, assurez-vous d'installer les dépendances nécessaires à votre environnement :

pip install numpy scipy opencv-python
pip install torch torchvision  # Si vous utilisez le modèle MobileNetV2 par défaut
pip install tensorflow  # Si vous utilisez TensorFlow 2+
pip install git+https://github.com/openai/CLIP.git  # Si vous utilisez l'embedder CLIP

Installation

Vous pouvez installer deep-sort-realtime de deux façons :

    Via PyPI :

pip3 install deep-sort-realtime

    Clonez ce repo et installez en tant que package Python :

git clone https://github.com/nwojke/deep_sort.git
cd deep_sort
pip3 install .
