import piexif
import os



def exif_mc(url_fichier, argu):
    nom_fichier = os.path.basename(url_fichier)  # Utilisez os.path.basename pour obtenir le nom du fichier
    extension = nom_fichier.split(".")[-1]

    if extension.lower() != "jpg":  # Vérifiez l'extension en ignorant la casse
        os.rename(url_fichier, f"{os.path.splitext(url_fichier)[0]}.jpg")

    exif_dict = piexif.load(url_fichier)
    exif_dict["0th"][piexif.ImageIFD.XPKeywords] = argu.encode("utf-16le")
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, url_fichier)

