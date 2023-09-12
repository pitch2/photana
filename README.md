# Photoana

Photoana, comme son nom l'indique, est un analyseur de photos qui permet ensuite de les étiqueter et de les trier dans des dossiers.

En ce qui concerne la forme, j'utilise le framework Electron.js et j'exécute mon script à l'aide de PyScript, un framework HTML. Pour l'instant, je rencontre un problème lors de l'exécution du script... (Pour l'instant, le script n'est pas disponible sur le référentiel).

Le programme est assez simple, mais je n'ai pas trouvé d'équivalent sur Internet. Le programme d'analyse fonctionne avec deux API.

Si vous souhaitez l'utiliser, il faudra exécuter le script "premier_démarrage" et également configurer votre API OpenAI, ainsi qu'une clé en format .json pour l'Google Vision.

Le fichier requirements arrive...

---
### Google Vision

Étape 1 : Accéder à la Console Google Cloud

  - Accédez à Google Cloud Console.
  
  - Connectez-vous à votre compte Google ou créez un compte si vous n'en avez pas.

Étape 2 : Créer un projet

  - Si vous n'avez pas déjà un projet, créez-en un en cliquant sur le sélecteur de projet en haut de la page, puis en cliquant sur "Nouveau projet". Donnez-lui un nom et appuyez   sur "Créer".
  
Étape 3 : Activer les API Google Cloud

  - Dans le menu de navigation à gauche, cliquez sur "API & Services" > "Tableau de bord".
  
  - Cliquez sur le bouton "+ Activer les APIs et les services" en haut de la page.
  
  - Dans la barre de recherche, tapez le nom de l'API que vous souhaitez utiliser (par exemple, "Cloud Vision API" ou "Google Sheets API").
  
  - Cliquez sur le résultat de l'API que vous souhaitez utiliser.

Étape 4 : Activer l'API

  - Cliquez sur le bouton "Activer" pour activer l'API que vous avez sélectionnée.

Étape 5 : Créer un compte de service

  - Dans le menu de navigation à gauche, sous "API & Services", cliquez sur "Identifiants".
  
  - Cliquez sur le bouton "Créer des identifiants" en haut de la page, puis sélectionnez "Compte de service".
  
  - Donnez un nom à votre compte de service, attribuez-lui un rôle (par exemple, "Lecteur" ou "Administrateur", selon les besoins), puis cliquez sur "Continuer".

Étape 6 : Créer une clé de compte de service

  - Sur la page suivante, cliquez sur "Créer une clé de compte de service" pour générer une nouvelle clé.
  
  - Sélectionnez le type de clé JSON.
  
  - Cliquez sur "Créer" pour télécharger la clé JSON sur votre ordinateur.

Étape 7 : Configurer la variable d'environnement
  
  - Une fois que vous avez téléchargé la clé JSON, configurez la variable d'environnement GOOGLE_APPLICATION_CREDENTIALS dans votre code pour qu'elle pointe vers le chemin du      fichier JSON de clé que vous venez de télécharger.
  
Exemple en Python :
```
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chemin/vers/votre/fichier-de-clé.json"
```

Si ça ne fonctionne toujours pas, je conseil d'installer le logiciel GCloud
