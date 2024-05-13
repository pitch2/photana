### 🛑 Avant, il faut avoir crée le projet sur Google Cloud 
Dans la console Google Cloud, accédez à Menu menu > API et services > Identifiants.
Accéder à [Identifiants](https://console.cloud.google.com/apis)

- Cliquez sur Créer des identifiants > ID client OAuth.
- Cliquez sur Type d'application > Application Web.
- Dans le champ Name (Nom), saisissez un nom pour l'identifiant. Ce nom ne s'affiche que dans la console Google Cloud.
- Ajoutez les URI autorisés associés à votre application :
- Applications côté client (JavaScript) : sous Origines JavaScript autorisées, cliquez sur Ajouter un URI. Saisissez ensuite un URI à utiliser pour les requêtes du navigateur. Ce champ identifie les domaines à partir desquels votre application peut envoyer des requêtes API au serveur OAuth 2.0.
- Applications côté serveur (Java, Python, etc.) : sous URI de redirection autorisés, cliquez sur Ajouter un URI. Saisissez ensuite un URI de point de terminaison auquel le serveur OAuth 2.0 peut envoyer des réponses. (ignorer)
- Cliquez sur Créer. L'écran du client OAuth créé s'affiche, avec l'ID et le code secret du client que vous venez de créer.
- Puis télécharger la clé en cliquant sur le projet
- Cliquez sur OK. Les nouveaux identifiants s'affichent sous ID client OAuth 2.0.

```python
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chemin/vers/votre/fichier-de-clé.json"
``` 

Vous avez maintenant configuré votre fichier JSON de clé pour utiliser les services Google Cloud dans votre application ou script. Assurez-vous de garder ce fichier en sécurité, car il contient des informations d'identification sensibles.
