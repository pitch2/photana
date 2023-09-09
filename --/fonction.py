#on retrouve ici des fonctions basique pour pas surchargé main.py
import os 


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


# Début: nous créons une fonction qui corrige les URLs pour éviter les problèmes avec Python
def corriger_url(chemin):
    chemin_corrigé = chemin.replace("\\", "\\\\")
    return chemin_corrigé