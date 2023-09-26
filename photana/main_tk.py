import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tqdm import tqdm
import reqgpt
import EXIF
import reqlens
import fonctions
import shutil
import os

# Function to select a folder and populate the entry field
def browse_folder(entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)

# Function to start processing
def start_processing():
    chemin = entry_chemin.get()
    dossier_archivage = entry_dossier_archivage.get()
    dossier_archivage = fonctions.corriger_url(dossier_archivage)

    liste_fichiers = fonctions.dossierliste(chemin)
    total_images = len(liste_fichiers)
    progress_bar["maximum"] = total_images

    for i in tqdm(range(total_images), colour='WHITE'):
        url = liste_fichiers[i]

        argu = reqlens.requrl(url)

        # Get the adjective from GPT
        argu = reqgpt.categorisation(argu)

        # Create a directory for the adjective if it doesn't exist
        adjective_dir = os.path.join(dossier_archivage, argu)
        if not os.path.exists(adjective_dir):
            os.makedirs(adjective_dir)

        # Move the image to the appropriate directory
        filename = os.path.basename(url)
        destination = os.path.join(adjective_dir, filename)
        shutil.move(url, destination)

        # Add the adjective to the image's EXIF data
        # Uncomment the line below to actually write to EXIF
        # EXIF.exif_mc(url, argu)

        progress_bar["value"] = i + 1
        root.update_idletasks()

    messagebox.showinfo("Traitement terminé", "Le traitement des images est terminé.")

# Create the main application window
root = tk.Tk()
root.title("Image Processing Tool")
root.geometry("500x300")
root.configure(bg="black")

# Create and place the widgets
label_chemin = tk.Label(root, text="Chemin du dossier à analyser:")
label_chemin.pack()

entry_chemin = tk.Entry(root)
entry_chemin.pack(fill=tk.X, padx=10, pady=(0, 10))

browse_button_chemin = tk.Button(root, text="Parcourir", command=lambda: browse_folder(entry_chemin))
browse_button_chemin.pack(pady=(0, 10))

label_dossier_archivage = tk.Label(root, text="Chemin de destination du tri:")
label_dossier_archivage.pack()

entry_dossier_archivage = tk.Entry(root)
entry_dossier_archivage.pack(fill=tk.X, padx=10, pady=(0, 10))

browse_button_dossier = tk.Button(root, text="Parcourir", command=lambda: browse_folder(entry_dossier_archivage))
browse_button_dossier.pack(pady=(0, 10))

start_button = tk.Button(root, text="Start Processing", command=start_processing)
start_button.pack(pady=(0, 10))

progress_bar = ttk.Progressbar(root, length=300)
progress_bar.pack(pady=(0, 10))

# Run the main event loop
root.mainloop()
