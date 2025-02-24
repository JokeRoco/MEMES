const dropzone = document.getElementById('dropzone');

dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];

    const formData = new FormData();
    formData.append("file", file);

    fetch('/download', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(result => alert('Datei heruntergeladen: ' + result))
    .catch(error => console.error('FEHLER:', error));
    window.location.reload();

});