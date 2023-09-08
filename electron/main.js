const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'index.html'));

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  // Exposez la fonction runPythonScript() au processus de rendu
  ipcMain.on('run-python-script', () => {
    runPythonScript();
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// Fonction pour exécuter le script Python
function runPythonScript() {
  const scriptPath = path.join(__dirname, 'my_script.py'); // Assurez-vous que le chemin est correct
  const pythonProcess = spawn('python', [scriptPath]);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Sortie Python : ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Erreur Python : ${data}`);
  });

  pythonProcess.on('error', (error) => {
    console.error('Erreur lors de l\'exécution du processus Python :', error);
  });
}
