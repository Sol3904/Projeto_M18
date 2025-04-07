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

document.querySelectorAll(".apply-filters").forEach(button => {
    button.addEventListener("click", function (event) {
        event.preventDefault();  // <- Isto evita que o botão envie o form
        
        const image = this.dataset.image;

        const sliders = document.querySelectorAll(`.slider[data-image="${image}"]`);
        const values = {
            image: image,
            sharpness: sliders[0].value,
            brightness: sliders[1].value,
            contrast: sliders[2].value,
            color: sliders[3].value
        };

        console.log(values); // Para debug


        fetch('/edit_image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(values)
        })
        .then(async response => {
            const contentType = response.headers.get("content-type");
            
            if (contentType && contentType.includes("application/json")) {
                const data = await response.json();
                if (data.success) {
                    const imgElement = document.querySelector(`img[src*="${image}"]`);
                    imgElement.src = `/static/${data.new_image}?t=${new Date().getTime()}`;
                    imgElement.dataset.image = data.new_image;
                }
            } else {
                const text = await response.text();
                console.error("Resposta não é JSON:", text);
            }
            window.location.reload();
        })
        .catch(error => console.error('Erro ao aplicar filtros:', error));
        
    });
});



