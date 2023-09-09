import os
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "votre clé"

# Créez un client Cloud Vision
client = vision.ImageAnnotatorClient()

# url = r"c:\Users\ponto\OneDrive\Bureau\--\fleur_lotus.jpg"

def requrl(url):
    # Chargez l'image à analyser
    with open(url, "rb") as image_file:
        content = image_file.read()

    # Créez un objet Image
    image = vision.Image(content=content)

    # Appelez l'API pour l'analyse d'image
    response = client.label_detection(image=image)

    # Initialisez la liste argu
    argu = []

    # Ajoutez les mots détectés à la liste argu
    labels = response.label_annotations
    for label in labels:
        argu.append(label.description)

    return argu
