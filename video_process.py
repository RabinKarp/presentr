import cv2
import os
import math

def vid_to_frames(filename, num_frames):
    path = os.path.dirname(filename)

    vidcap = cv2.VideoCapture(filename)
    framerate = 24
    
    success, image = vidcap.read()

    count = 0
    while success and count <= num_frames * 24:
        if count % 24 == 0:
            frame_name = path + '/frames/frame%d.jpg' % count
            print(frame_name)
            cv2.imwrite(frame_name, image)
            print('Wrote ', frame_name)
        
        success, image = vidcap.read()
        
        print('Read a new frame: ', success)
        count += 1

    vidcap.release()
    cv2.destroyAllWindows()
    print('Done!')


def frame_to_blackboard(frame):
    # to do 
    pass


if __name__ == '__main__':
    vid_to_frames('tests/vid/IMG_2645.MOV', 100)
