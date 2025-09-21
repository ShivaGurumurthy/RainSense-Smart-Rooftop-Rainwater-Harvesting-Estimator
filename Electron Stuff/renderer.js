document.getElementById('calculateBtn').addEventListener('click', async () => {
  const locality = document.getElementById('locality').value;
  const material = document.getElementById('material').value;
  const area = document.getElementById('area').value || 100;

  document.getElementById('results-text').innerText = 'Calculating...';

  try {
    const result = await window.api.runPython({ locality, material, area });
    document.getElementById('results-text').innerText = result;
  } catch (err) {
    document.getElementById('results-text').innerText = 'Error: ' + err;
  }
});