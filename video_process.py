import cv2
import os

def vid_to_frames(filename):
    path = os.path.dirname(filename)

    vidcap = cv2.VideoCapture(filename)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite('path/frames/frame%d.jpg'% count, image)
        success image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


def frame_to_blackboard(frame):
    # to do 
    pass


def main(filename):
    vid_to_frames(filename)


if __name__ == '__main__':
    main()
