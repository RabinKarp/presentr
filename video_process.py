import cv2
import os
import math

def vid_to_frames(filename):
    path = os.path.dirname(filename)

    vidcap = cv2.VideoCapture(filename)
    framerate = vidcap.get(24)
    
    frame_id = vidcap.get(1)
    success, image = vidcap.read()
    
    count = 0
    while success:
        if frame_id % math.floor(framerate) == 0:
            cv2.imwrite('path/frames/frame%d.jpg'% count, image)
            print('Wrote frame', count)
        
        frame_id = vidcap.get(1)  # current frame number
        success, image = vidcap.read()
        
        print('Read a new frame: ', success)
        count += 1

    vidcap.release()
    cv2.destroyAllWindows()
    print('Done!')


def frame_to_blackboard(frame):
    # to do 
    pass


def main(filename):
    vid_to_frames(filename)


if __name__ == '__main__':
    pass
