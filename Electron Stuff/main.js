// main.js
const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');


process.env.SSL_CERT_FILE = '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/certifi/cacert.pem';

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 900,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  win.loadFile('index.html');
}

app.whenReady().then(createWindow);

ipcMain.handle('run-python', async (event, args) => {
  return new Promise((resolve, reject) => {
    const pyProcess = spawn(
      '/Library/Frameworks/Python.framework/Versions/3.13/bin/python3',
      [path.join(__dirname, 'rainsense-files', 'main.py')],
      { cwd: path.join(__dirname, 'rainsense-files') }
    );

    let output = '';
    let errorOutput = '';

    pyProcess.stdout.on('data', (data) => {
      output += data.toString();
    });

    pyProcess.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });

    pyProcess.on('close', (code) => {
      if (code === 0) {
        resolve(output);
      } else {
        resolve(`ERROR: ${errorOutput}`);
      }
    });

    // Send user inputs to Python
    pyProcess.stdin.write(`${args.locality}\n`);
    pyProcess.stdin.write(`${args.material}\n`);
    pyProcess.stdin.write(`${args.area}\n`);
    pyProcess.stdin.end();
  });
});