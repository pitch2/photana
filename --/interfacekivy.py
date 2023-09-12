import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.dropdown import DropDown

class Interface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        # Couleur de fond pastel
        r, g, b = 201 / 255.0, 224 / 255.0, 229 / 255.0
        a = 1.0  # Alpha (transparence) à 1

        # Créer un rectangle de couleur de fond
        with self.canvas.before:
            Color(r, g, b, a)  # Couleur pastel
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Mettre à jour le rectangle en cas de changement de taille ou de position
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Créer un layout d'ancrage pour le bouton principal
        anchor_layout = AnchorLayout(anchor_x="left", anchor_y="top")
        
        # Créer le bouton principal avec un style pastel et un texte
        self.btn_main = Button(
            text="Menu",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.976, 0.741, 0.765, 1),  # Couleur pastel du bouton
            color=(0, 0, 0, 1),  # Couleur foncée du texte
        )
        
        # Créer le menu dépliant
        self.dropdown = DropDown()
        
        # Créer un bouton pour le dossier Téléchargements
        btn_download = Button(
            text="Téléchargements",
            size_hint_y=None,
            height=44,
            background_color=(0.976, 0.741, 0.765, 1),  # Couleur pastel du bouton
            color=(0, 0, 0, 1),  # Couleur foncée du texte
        )
        btn_download.bind(on_release=self.open_download_folder)
        self.dropdown.add_widget(btn_download)
        
        # Créer un bouton pour le dossier Bureau
        btn_desktop = Button(
            text="Bureau",
            size_hint_y=None,
            height=44,
            background_color=(0.976, 0.741, 0.765, 1),  # Couleur pastel du bouton
            color=(0, 0, 0, 1),  # Couleur foncée du texte
        )
        btn_desktop.bind(on_release=self.open_desktop_folder)
        self.dropdown.add_widget(btn_desktop)
        
        # Lier l'affichage du menu dépliant au bouton principal
        self.btn_main.bind(on_release=self.dropdown.open)
        
        # Ajouter le bouton principal au layout d'ancrage et ce dernier à l'interface
        anchor_layout.add_widget(self.btn_main)
        self.add_widget(anchor_layout)

    # Mettre à jour la position et la taille du rectangle de fond
    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    # Ouvrir le dossier Téléchargements
    def open_download_folder(self, instance):
        download_folder = "C:\\Users\\ponto\\OneDrive\\Bureau\\PHOTO"
        os.system(f"explorer {download_folder}")

    # Ouvrir le dossier Bureau
    def open_desktop_folder(self, instance):
        desktop_folder = os.path.expanduser("~") + os.sep + "Desktop"
        os.system(f"explorer {desktop_folder}")

class MinimalApp(App):
    def build(self):
        app = Interface()
        return app

if __name__ == "__main__":
    MinimalApp().run()
