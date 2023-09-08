import os
import tqdm


# Spécifiez le chemin du dossier que vous souhaitez parcourir
chemin = "C:\\Users\ponto\OneDrive\Bureau\my-electron-app"


def dossier (dossier_cible):
    # Liste pour stocker les liens (chemins complets) des fichiers
    liste_liens_fichiers = []

    # Parcourez le dossier cible
    for nom_fichier in os.listdir(dossier_cible):
        # Créez le chemin complet du fichier en utilisant os.path.join
        chemin_complet = os.path.join(dossier_cible, nom_fichier)
        
        # Vérifiez si l'élément est un fichier (et non un sous-dossier)
        if os.path.isfile(chemin_complet):
            liste_liens_fichiers.append(chemin_complet)

    # Maintenant, la liste contient les liens (chemins complets) de tous les fichiers du dossier cible
    return(liste_liens_fichiers)


from tqdm import tqdm
from time import sleep
import sys
 
i = 0
for i in tqdm(range(0, 5)):
    for k in tqdm(range(0,3), file=sys.stdout, colour = 'MAGENTA'):
        sleep(.9)
        
    i = i +1
    sleep(.5)