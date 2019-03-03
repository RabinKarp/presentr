from flask import Flask


UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set('*.doc')

app = Flask(__name__)
app.secret_key = b'afasd'
from presentr import views    
