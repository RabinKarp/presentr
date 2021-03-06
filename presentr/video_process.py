import cv2
import os
import math
from presentr import app


def vid_to_frames(filename, num_seconds):
    path = os.path.dirname(filename)

    vidcap = cv2.VideoCapture(filename)
    framerate = 24
    frameperiod = 3 # This constrains the program to only collect a frame every 3 seconds

    success, image = vidcap.read()

    count = 0
    while success and count <= num_seconds * 24:
        if count % (24 * frameperiod) == 0:
            frame_name = os.path.join(app.config['FRAME_FOLDER'], 'frame%d.jpg' % count)
            print(frame_name)
            cv2.imwrite(frame_name, image)
            print('Wrote ', frame_name)
        
        success, image = vidcap.read()
        
        print('Read a new frame: ', success)
        count += 1

    vidcap.release()
    cv2.destroyAllWindows()
    print('Done!')
    
    # Returns the folder of the newly constructed frame stack
    return app.config['FRAME_FOLDER']

def frame_to_blackboard(frame):
    # to do 
    pass


if __name__ == '__main__':
    pass
