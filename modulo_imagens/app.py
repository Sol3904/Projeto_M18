import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/img')
def gallery():
    # List all images in the "static/aigispics" directory
    img_folder = os.path.join(app.static_folder, "aigispics")
    images = [f"aigispics/{img}" for img in os.listdir(img_folder) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    return render_template('img.html', images=images)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
