import os
import base64
import random
import string
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from imagem import enhance_image  # Importa a função de processamento de imagem

# Configuração do Flask
app = Flask(__name__, template_folder="templates", static_folder="static")

# Diretório para imagens enviadas
UPLOAD_FOLDER = os.path.join(app.static_folder, "aigispics")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configuração do aplicativo
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """Verifica se o arquivo tem uma extensão permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Rotas principais
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/paint')
def paint():
    return render_template('paint.html')

# Rota para galeria de imagens
def list_images():
    """Lista todas as imagens no diretório 'static/aigispics'."""
    return [f"aigispics/{img}" for img in os.listdir(UPLOAD_FOLDER) if allowed_file(img)]

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
    
    return render_template('img.html', images=list_images())

@app.route('/edit_image', methods=['GET', 'POST'])
def edit_image():
    try:
        data = request.get_json(force=True)
        print("Recebido:", data)

        original_image_path = os.path.join(app.static_folder, data['image'])
        if not os.path.exists(original_image_path):
            return jsonify({"error": "Imagem não encontrada"}), 404

        edited_image_path = os.path.join(app.static_folder, "aigispics", "edited_" + os.path.basename(original_image_path))
        
        # Cópia da imagem se não existir
        if not os.path.exists(edited_image_path):
            from shutil import copyfile
            copyfile(original_image_path, edited_image_path)

        # Aplicar efeitos
        enhance_image(
            edited_image_path,
            float(data['sharpness']),
            float(data['brightness']),
            float(data['contrast']),
            float(data['color'])
        )

        return jsonify({"success": True, "new_image": f"aigispics/edited_{os.path.basename(original_image_path)}"}), 200

    except Exception as e:
        print("Erro no edit_image:", str(e))
        return jsonify({"error": "Erro interno ao processar imagem"}), 500




# Rota para deletar imagens
@app.route('/delete_images', methods=['POST'])
def delete_images():
    data = request.get_json(force=True)
    images_to_delete = data.get('images', [])
    
    if not images_to_delete:
        return jsonify({"error": "Nenhuma imagem selecionada"}), 400
    
    for image in images_to_delete:
        image_path = os.path.join(app.static_folder, image)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    return jsonify({"message": "Imagens removidas com sucesso!"}), 200

# Rota para salvar imagens desenhadas
@app.route('/save', methods=['POST'])
def save_image():
    data = request.json.get("image")
    if not data:
        return {"error": "No image data received"}, 400
    
    img_data = data.split(",")[1]
    img_bytes = base64.b64decode(img_data)
    
    def generate_unique_filename(folder, extension=".png", length=10):
        while True:
            filename = ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + extension
            file_path = os.path.join(folder, filename)
            if not os.path.exists(file_path):
                return filename
    
    filename = generate_unique_filename(UPLOAD_FOLDER, ".png")
    img_path = os.path.join(UPLOAD_FOLDER, filename)
    
    with open(img_path, "wb") as img_file:
        img_file.write(img_bytes)
    
    return {"message": "Image saved successfully!", "path": f"/static/aigispics/{filename}"}

if __name__ == "__main__":
    app.run(debug=True)
