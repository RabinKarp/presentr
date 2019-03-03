from flask import render_template, request, redirect, flash, send_from_directory, send_file, url_for
from werkzeug.utils import secure_filename
from presentr import app, pipeline
import os
import glob


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLD = '../uploads'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)

GENERATED_FOLD = '../generated'
GENERATED_FOLDER = os.path.join(APP_ROOT, GENERATED_FOLD)

FRAME_FOLD = '../frames'
FRAME_FOLDER = os.path.join(APP_ROOT, FRAME_FOLD)

app.config['APP_ROOT'] = APP_ROOT
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER
app.config['FRAME_FOLDER'] = FRAME_FOLDER


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
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('infile')))
      
        frameFolder = app.config['FRAME_FOLDER']
        #pipeline.complete_pipeline()
        #pipeline.pickle_corpus(frameFolder)
        pipeline.loaded_corpus_pipeline()
        
        files = glob.glob(os.path.join(frameFolder, '*'))
        for f in files:
            os.remove(f)

        flash('output1.tex')
        flash('output1.pdf')
        flash('output1.txt')
        flash('output1_braille.txt')
        return redirect(url_for('upload_file'))
    return render_template('upload.html')


@app.route('/download/<filename>')
def generated_file(filename):
    return send_file(app.config['GENERATED_FOLDER'] + '/' + filename, attachment_filename=filename)
    #return send_from_directory(app.config['GENERATED_FOLDER'], filename)


if __name__ == '__main__':
    pass
