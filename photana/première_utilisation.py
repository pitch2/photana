import os

print("Vous êtes dans le fichiers de première utilisation, vous pourrez supprimé ce fichier après")

dossier_archivage = input("Saisir le chemin de destination du classement: ")

def corriger_url(chemin):
    chemin_corrigé = chemin.replace("\\", "\\\\")
    return chemin_corrigé

dossier_archivage = corriger_url(dossier_archivage)

dossier_a_crée = ["Paysages", "Fleurs", "Animaux", "Voitures", "Bateaux", "Personnes", "Bâtiments", "Illustration", "Divers", "Nourriture", "Art abstrait", "Événements spéciaux", "Sport", "Loisirs", "Mode", "Musique", "Voyages"]

for dossier in dossier_a_crée:
    # Create the full path for the subdirectory
    sous_dossier = os.path.join(dossier_archivage, dossier)
    os.makedirs(sous_dossier)

print("Tout est bien initalisé")