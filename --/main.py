#on importe tous les modules 
import openai
from tqdm import tqdm
import reqgpt 
import EXIF 
import reqlens 
import fonctions
import shutil


# chemin = input("Donnez le chemin du dossier à analyser : ")
chemin = r"C:\Users\ponto\OneDrive\Bureau\Nouveau dossier"
# dossier_archivage = input("Donnez le chemin de destination du tri: ")
dossier_archivage = r"C:\Users\ponto\OneDrive\Bureau\Nouveau dossier"

# on rend les chemins utilisable par python
dossier_archivage = fonctions.corriger_url(dossier_archivage)
print(dossier_archivage)

# on crée une liste avec tous les fichiers du dossiers
liste_fichiers = fonctions.dossierliste(chemin)

print(liste_fichiers)


i = 0
n = 0


for i in tqdm(range(i, len(liste_fichiers)), colour = 'WHITE'):
    url = liste_fichiers[n]

    # Appel de la reconnaissance d'image Lens de Google, pas vraiment Lens mais le même moteur en API 
    argu = reqlens.requrl(url)
    
    
    # Appel de GPT 3.5-Turbo pour donner tous les adjectif de Google et trouve le mots parfait pour dessigner (API OpenAi)
    argu = reqgpt.categorisation(argu)
    # Appel de la fonction pour ecrire notre adjectif fais par GPT dans les données EXIF de la photo (ici les mots-clé)
    EXIF.exif_mc(url, argu)
    # On deplace l'image dans le dossiers attitré
    shutil.move(liste_fichiers[i], f"{dossier_archivage}\\{argu}")
    n = n + 1
    

    
# print(f"{n+1} images sur {len(liste_fichiers)}")

#on vas maintenant trier toutes les images dans les dossiers respectif:


    