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

document.querySelectorAll(".slider").forEach(slider => {
    slider.addEventListener("input", function () {
        const image = this.dataset.image;
        const sliders = document.querySelectorAll(`.slider[data-image="${image}"]`);
        
        const values = {
            image: image,
            sharpness: sliders[0].value,
            brightness: sliders[1].value,
            contrast: sliders[2].value,
            color: sliders[3].value
        };

        fetch('/edit_image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(values)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Atualizar a imagem na interface com a nova cópia editada
                const imgElement = document.querySelector(`img[src*="${image}"]`);
                imgElement.src = `/static/${data.new_image}?t=${new Date().getTime()}`; // Força a atualização da imagem
                imgElement.dataset.image = data.new_image; // Atualiza o atributo para os próximos ajustes
            }
        })
        .catch(error => console.error('Erro ao modificar a imagem:', error));
    });
});


