const $ = (id) => document.getElementById(id);

// Initialize the Fabric.js canvas
const canvasEl = $('paintCanvas');
const canvas = new fabric.Canvas(canvasEl);

// Default to not drawing
canvas.isDrawingMode = false;

// Create Pencil Brush
const pencilBrush = new fabric.PencilBrush(canvas);
pencilBrush.color = '#000'; // Black color for drawing
pencilBrush.width = 5; // Set the default drawing width

// Assign the brush to the canvas when entering drawing mode
canvas.freeDrawingBrush = pencilBrush;

// Set up the button to toggle drawing mode
const toggleDrawingModeEl = $('toggle-drawing-mode');
const clearEl = $('clear-canvas');
const saveEl = $('save-canvas');

// Toggle drawing mode on button click (cancel or activate)
toggleDrawingModeEl.onclick = function () {
    if (canvas.isDrawingMode) {
        canvas.isDrawingMode = false;
        toggleDrawingModeEl.innerHTML = 'Cancel Drawing Mode';
    } else {
        canvas.isDrawingMode = true;
        toggleDrawingModeEl.innerHTML = 'Exit Drawing Mode';
    }
};

// Clear canvas button
clearEl.onclick = function () {
    canvas.clear();
};

// Debug: Mouse click detection
canvasEl.addEventListener('mousedown', function(event) {
    console.log('Mouse click detected on canvas!');
    console.log('Mouse X: ' + event.offsetX + ', Mouse Y: ' + event.offsetY);
});



// Function to save the canvas drawing
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