const { ipcRenderer } = require('electron');

// Ajoutez un gestionnaire d'événements au bouton HTML
document.getElementById('runPythonButton').addEventListener('click', () => {
  // Déclenchez l'exécution du script Python en envoyant un message au processus principal
  ipcRenderer.send('run-python-script');
});
