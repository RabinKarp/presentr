from flask import render_template, request, redirect, flash, send_from_directory, send_file
from werkzeug.utils import secure_filename
from presentr import app
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLD = '../uploads'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)

GENERATED_FOLD = '../generated'
GENERATED_FOLDER = os.path.join(APP_ROOT, GENERATED_FOLD)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER

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
        
        basename = f.filename.split('.')[1]
        
        # TODO: change to a redirect to a page (or flash) that links to the generated files
        # to download -- basename.pdf and basename.tex
        
        return 'file saved successfully'
    return render_template('upload.html')


@app.route('/download/<filename>')
def generated_file(filename):
    return send_file(app.config['GENERATED_FOLDER'] + '/' + filename, attachment_filename=filename)
    #return send_from_directory(app.config['GENERATED_FOLDER'], filename)


if __name__ == '__main__':
    pass
