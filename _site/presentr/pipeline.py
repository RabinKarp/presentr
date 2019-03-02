import videoretrieve, video_process, image_preprocess, img_to_text


def complete_pipeline():
    '''
    Converts a video into a presentation from start to finish.
    '''
    vFile = videoretrieve.getVideoFile()
    frameFolder = video_process.vid_to_frames(vFile, 420) # Only process the first 100 seconds
    shortened_pipeline(frameFolder)


def shortened_pipeline(frameFolder):
    '''
    Assumes that we have the frames in the given folder, and then
    just performs the text analysis.
    '''
    frames = img_to_text.getFrameStack(frameFolder)

    corpus = []
    for f in frames: 
        print(img_to_text.getTextFromFrame(f)) 

def pickled_corpus_pipeline():
    '''
    TODO: Implement here!
    '''
    pass

if __name__ == '__main__':
    # complete_pipeline()
    shortened_pipeline("/Users/Vivek/Desktop/presentr/tests/vid/frames")

    # Just a very short unit test
    # shortened_pipeline("/Users/Vivek/Desktop/presentr/tests/img")