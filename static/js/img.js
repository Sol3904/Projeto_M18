const DeleteEl = document.getElementById('delete-images');

DeleteEl.onclick = function () {
    const images = [];
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            images.push(checkbox.id);  // Pega o valor da imagem (nome)
        }
    });

    if (images.length === 0) {
        alert('Please select at least one image to delete!');
        return;
    }

    fetch('/delete_images', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify({ images })  // Envia o corpo como JSON
    })
    .then(response => response.json())  // Espera a resposta em formato JSON
    .then(result => {
        if (result.message) {
            alert('Imagens removidas com sucesso!');
            window.location.href = '/img';  // Recarrega a página para mostrar as imagens restantes
        }
    })
    .catch(error => {
        console.error('Erro ao deletar imagens:', error);  // Exibe detalhes do erro
        alert('Erro ao deletar imagens');
    });
};
