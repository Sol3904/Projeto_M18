import os
import base64
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import random
import string

app = Flask(__name__, template_folder="templates", static_folder="static")

# Directory for uploaded images
UPLOAD_FOLDER = os.path.join(app.static_folder, "aigispics")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/img', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('gallery'))
    
    # List all images in the "static/aigispics" directory
    images = [f"aigispics/{img}" for img in os.listdir(UPLOAD_FOLDER) if allowed_file(img)]
    
    return render_template('img.html', images=images)

@app.route('/about')
def about():    
    return render_template('about.html')

@app.route('/delete_images', methods=['POST'])
def delete_images():
    data = request.get_json(force=True)  # Força a leitura do JSON
    image_to_delete = data.get('images', [])  # Obtém a lista de imagens
    
    if not image_to_delete:
        return jsonify({"error": "Nenhuma imagem selecionada"}), 400
    
    for image in image_to_delete:
        image_path = os.path.join(app.static_folder, image)
        print(image_path)
        if os.path.exists(image_path):
            os.remove(image_path)

    return jsonify({"message": "Imagens removidas com sucesso!"}), 200




@app.route('/paint')
def paint():
    return render_template('paint.html')

@app.route('/save', methods=['POST'])
def save_image():
    data = request.json.get("image")
    if not data:
        return {"error": "No image data received"}, 400
    
    # Decodificar imagem base64
    img_data = data.split(",")[1]
    img_bytes = base64.b64decode(img_data)
    
    def generate_unique_filename(folder, extension=".png", length=10):
        while True:
            filename = ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + extension
            file_path = os.path.join(folder, filename)
            if not os.path.exists(file_path):
                return filename
    # Salvar imagem no servidor
    img_path = os.path.join(app.static_folder, "aigispics", generate_unique_filename("aigispics", ".png"))
    with open(img_path, "wb") as img_file:
        img_file.write(img_bytes)    

    return {"message": "Image saved successfully!", "path": f"/static/aigispics/drawing.png"}


if __name__ == "__main__":
    app.run(debug=True)