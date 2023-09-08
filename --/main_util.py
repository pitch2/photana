
from google.cloud import vision
import piexif
import os
import openai
from tqdm import tqdm
import reqgpt 
import EXIF 
import reqlens 



i = 0
# On prend l'url de la photo que on à besoin, pour l'instant c'est une photo de test, bientôt une fonction pour generer cette URL
url = r"C:\Users\ponto\OneDrive\Bureau\--\fleur_lotus.jpg"

# Début: nous créons une fonction qui corrige les URLs pour éviter les problèmes avec Python
def corriger_url(chemin):
    chemin_corrigé = chemin.replace("\\", "\\\\")
    return chemin_corrigé
# Appel de la fonction pour corriger l'URL
for i in tqdm(range(0, 3)):

    url = corriger_url(url)
    i = i+1

    # Appel de la reconnaissance d'image Lens de Google, pas vraiment Lens mais le même moteur en API 
    argu = reqlens.requrl(url)
    i = i+1
    
    # Appel de GPT 3.5-Turbo pour donner tous les adjectif de Google et trouve le mots parfait pour dessigner (API OpenAi)
    argu = reqgpt.categorisation(argu)
    i = i+1

    # Appel de la fonction pour ecrire notre adjectif fais par GPT dans les données EXIF de la photo (ici les mots-clé)
    EXIF.exif_mc(url, argu)
    i = i+1


