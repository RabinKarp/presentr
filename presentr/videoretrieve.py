# TODO: This file will interface with the frontend to grab the uploaded video

from presentr import app
import os


def getVideoFile():
    '''
    TODO: Still need to implement functionality!
    '''
    return os.path.join(app.config['UPLOAD_FOLDER'], 'infile') 
