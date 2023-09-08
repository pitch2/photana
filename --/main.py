#on importe tous les modules de tous les fichiers:

from google.cloud import vision
import piexif
import os
import openai
from tqdm import tqdm
import sys
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#from kivy.graphics import Color, Rectangle
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.dropdown import DropDown
#import interfacekivy     
#pas les modules Kivy car je vais utilisé electron.js, mais leger problème pour lier les script python (----+*--), et j'utilise pyscript.
#---- fichier à importer ----
import reqgpt 
import EXIF 
import reqlens 

chemin = r"C:\\Users\ponto\OneDrive\Bureau\Nouveau dossier"


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

liste_fichiers = dossier(chemin)
print(liste_fichiers)


i = 0




# Début: nous créons une fonction qui corrige les URLs pour éviter les problèmes avec Python
def corriger_url(chemin):
    chemin_corrigé = chemin.replace("\\", "\\\\")
    return chemin_corrigé


for n in range(len(liste_fichiers)):
    url = liste_fichiers[n]

    # Appel de la fonction pour corriger l'URL
    for i in tqdm(range(i, 3), file=sys.stdout, colour = 'MAGENTA'):

        # Appel de la reconnaissance d'image Lens de Google, pas vraiment Lens mais le même moteur en API 
        argu = reqlens.requrl(url)
        i = i+1
        print("a")
        
        # Appel de GPT 3.5-Turbo pour donner tous les adjectif de Google et trouve le mots parfait pour dessigner (API OpenAi)
        argu = reqgpt.categorisation(argu)
        i = i+1

        # Appel de la fonction pour ecrire notre adjectif fais par GPT dans les données EXIF de la photo (ici les mots-clé)
        EXIF.exif_mc(url, argu)
        i = i+1
    print(f"{n+1} images sur {len(liste_fichiers)}")
    n = n + 1

    


