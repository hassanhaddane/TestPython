
# OpenCV (Open Computer Vision) est une bibliothèque graphique. Elle est spécialisée dans le traitement d'images, que ce soit pour de la photo ou de la vidéo.

import cv2

# NumPy est très utile pour effectuer des calculs logiques et mathématiques sur des tableaux et des matrices.
# Cet outil permet d'effectuer ces opérations bien plus rapidement et efficacement que les listes Python
import numpy as np

img = cv2.imread("image1.png")
cv2.imshow('Image', img)

number_of_white_pix = np.sum(img == 255)

print(' le nombre de pixels blancs sur cette image:', number_of_white_pix)
