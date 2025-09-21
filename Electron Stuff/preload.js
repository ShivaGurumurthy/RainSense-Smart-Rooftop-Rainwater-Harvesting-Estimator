const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  runPython: (args) => ipcRenderer.invoke('run-python', args)
});