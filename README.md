# Photana

Photana est un programme python qui permet de tier des photos dans des catégories. A l'aide de plusieurs API (Google ainsi que OpenAi). 

---
### Installation et initilisation: 

- Vous devez déjà télécharger l'archive:
```
git clone https://github.com/pitch2/photana.git
```

- Ensuite, télécharger les modules nécessaires au fonctionnement du programme:
```
pip install -r requirements.txt
```

- Ensuite, vous devrez recupérer votre API de OpenAI (assez simple), et dans le fichier ```reqgpt.py```, vous mettez les informations (organisation & clé API), 
    - 0,002 dollars pour 1000 tokens = 750 mots (le programme ne vous couteras cassiment rien)
      
- Enfin il faut configurer Google Vision, comme la manipulation est assez longue je vous laisse regarder dans le fichier ```explication_google.txt```

### Bugs:
Si tous est bien configurer tous fonctionne correment, aucun bugs. Il y a juste un probleme certaines fois avec OpenAI, je vous conseil de mettre votre CB (et un plafond de consommation pour aucun dépassement involontaire.                                         

### Suite:
J'ai comme idée de faire une suite de programme destiné aux photographes, de plus, d'autres features arriveront prochainements (comme d'autres manière de trier)

### Credits :
Made 100% by Adrien Pichon. The beginning of the project dated 8/09/23.
