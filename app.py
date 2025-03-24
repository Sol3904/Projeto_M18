import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates", static_folder="static")

# Directory for uploaded images
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
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('gallery'))
    
    images = [f"aigispics/{img}" for img in os.listdir(UPLOAD_FOLDER) if allowed_file(img)]
    return render_template('img.html', images=images)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/paint')
def paint():
    return render_template('paint.html')

if __name__ == '__main__':
    app.run(debug=True)