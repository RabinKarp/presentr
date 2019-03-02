from flask import render_template, Blueprint
from presentr.main import *

bp = Blueprint('main', __name__, url_prefix='')

@bp.route('/')
def index():
    return render_template('index.html')
