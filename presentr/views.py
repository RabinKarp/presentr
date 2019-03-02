from flask import render_template, Blueprint, request, redirect, flash
from werkzeug.utils import secure_filename
from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))


if __name__ == '__main__':
    pass
