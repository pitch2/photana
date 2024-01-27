# Photana

### 📷 Présentation :
Photana est un programme en Python qui permet de trier des photos dans des catégories à l'aide de plusieurs API, notamment Google et OpenAI. Pour le moment, le programme fonctionne uniquement avec les formats jpg et jpeg, et la version Tkinter n'a pas encore toutes les fonctionnalités (elle fonctionne, mais le libellé EXIF n'est pas pris en compte).

---
### ⚙️ Installation et initialisation:

1. Téléchargez l'archive en exécutant la commande suivante dans votre terminal :
   ```
   git clone https://github.com/pitch2/photana.git
   ```

2. Ensuite, installez les modules nécessaires au fonctionnement du programme :
   ```
   pip install -r requirements.txt
   ```

3. Récupérez votre API OpenAI (c'est assez simple). Dans le fichier ```reqgpt.py```, saisissez les informations de votre organisation et de la clé API.
    - Coût : 0,002 dollars pour 1000 tokens, équivalent à 750 mots (le programme vous coûtera presque rien).

4. Configurez Google Vision. La procédure étant assez longue, consultez le fichier ```explication_google.txt``` pour plus de détails.

### 🛑 Bugs :
Si tout est bien configuré, le programme fonctionne correctement, sans aucun bug. Cependant, il peut y avoir des problèmes occasionnels avec OpenAI. Je vous conseille de configurer votre carte bancaire avec un plafond de consommation pour éviter tout dépassement involontaire.

### ➡️ Suite :
J'ai l'intention de créer une suite de programmes destinée aux photographes. De plus, d'autres fonctionnalités seront ajoutées prochainement, notamment de nouvelles méthodes de tri.

### ©️ Crédits :
Réalisé à 100% par Adrien Pichon. Le début du projet date du 8/09/23.
