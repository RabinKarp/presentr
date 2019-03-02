from flask import render_template, Blueprint
import videoretrieve, video_process, image_preprocess, img_to_text

def complete_pipeline():
    '''
    Converts a video into a presentation from start to finish.
    '''
    vFile = videoretrieve.getVideoFile()
    frameFolder = video_process.vid_to_frames(vFile, 100) # Only process the first 100 seconds
    shortened_pipeline(frameFolder)

def shortened_pipeline(frameFolder):
    '''
    Assumes that we have the frames in the given folder, and then
    just performs the text analysis.
    '''
    frames = img_to_text.getFrameStack(frameFolder)

    # Currently just prints out the contents of the first two frames
    for i in range(2):
        print(img_to_text.getTextFromFrame(frames[i])) 

bp = Blueprint('main', __name__, url_prefix='')

@bp.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # complete_pipeline()
    # shortened_pipeline("/Users/Vivek/Desktop/presentr/tests/vid/frames")
    shortened_pipeline("/Users/Vivek/Desktop/presentr/tests/img")
