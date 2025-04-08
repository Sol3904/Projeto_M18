const $ = (id) => document.getElementById(id);

const canvasEl = $('paintCanvas');
const canvas = new fabric.Canvas(canvasEl);

// Predefinir o modo de desenho para falso
canvas.isDrawingMode = false;

// Criar pincel
const pencilBrush = new fabric.PencilBrush(canvas);
pencilBrush.color = '#000'; // Cor do desenho preta
pencilBrush.width = 5; // Largura do desenho

// Atribuir o pincel ao quadro de desenho quando em modo de desenho
canvas.freeDrawingBrush = pencilBrush;

// Preparar o botão para o modo de desenho
const toggleDrawingModeEl = $('toggle-drawing-mode');
const clearEl = $('clear-canvas');
const saveEl = $('save-canvas');

/**
 * Esta função permite trocar entre o modo de desenho e o modo de edição do Quadro.
 */
toggleDrawingModeEl.onclick = function () {
    if (canvas.isDrawingMode) {
        canvas.isDrawingMode = false;
        toggleDrawingModeEl.innerHTML = 'Desenhar';
    } else {
        canvas.isDrawingMode = true;
        toggleDrawingModeEl.innerHTML = 'Sair do desenho';
    }
};

/**
 * Esta função permite que, ao clicar no botão "Apagar quadro", o desenho seja apagado do quadro.
 */
clearEl.onclick = function () {
    canvas.clear();
};

/**
 * Esta função permite a deteção do clique do rato
 */
canvasEl.addEventListener('mousedown', function(event) {
    console.log('Mouse click detected on canvas!');
    console.log('Mouse X: ' + event.offsetX + ', Mouse Y: ' + event.offsetY);
});



/**
 * Esta função permite que, ao clicar no botão "salvar desenho", o desenho seja salvo na galeria.
 */
saveEl.onclick = async () => {
    const imageData = canvas.toDataURL('image/png');
    
    const response = await fetch('/save', 
    {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    });
    
    const result = await response.json();
    if (result.message) 
    {
        alert('Imagem salva com sucesso!');
        // Opcional: Atualizar a página para exibir a nova imagem na galeria
        window.location.href = '/img';
    }
};

$('saveButton').addEventListener('click', saveDrawing);