from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from imagem import enhance_image  # Import the image processing function

app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = os.path.join(app.static_folder, "aigispics")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        return redirect(url_for('gallery'))
    
    images = [f"aigispics/{img}" for img in os.listdir(UPLOAD_FOLDER) if allowed_file(img)]
    return render_template('img.html', images=images)

@app.route('/edit_image', methods=['POST'])
def edit_image():
    image_path = request.form['image_path']
    full_path = os.path.join(app.static_folder, image_path)

    if os.path.exists(full_path):
        enhance_image(full_path)  # Only enhance when the user clicks "Edit Image"
        return redirect(url_for('gallery'))
    else:
        return "Error: Image not found", 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/paint')
def paint():
    return render_template('paint.html')

if __name__ == '__main__':
    app.run(debug=True)
