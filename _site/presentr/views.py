from flask import render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from presentr import app
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/home/yvette/code/presentr/uploads'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file saved successfully'
    return render_template('upload.html')

if __name__ == '__main__':
    pass
