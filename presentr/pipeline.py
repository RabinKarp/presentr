import videoretrieve, video_process, image_preprocess, img_to_text, stich
import os
import pickle

def complete_pipeline():
    '''
    Converts a video into a presentation from start to finish.
    '''
    vFile = videoretrieve.getVideoFile()
    frameFolder = video_process.vid_to_frames(vFile, 420) # Process 420 seconds of video 
    shortened_pipeline(frameFolder)


def shortened_pipeline(frameFolder):
    '''
    Assumes that we have the frames in the given folder, and then
    just performs the text analysis.
    '''
    frames = img_to_text.getFrameStack(frameFolder)

    corpus = []
    for f in frames:
        corpus.append(img_to_text.getTextFromFrame(f)) 

    return corpus

def pickle_corpus(frameFolder):
    '''
    Pickles the corpus so we don't have to recompute it every time.
    '''
    corpus = shortened_pipeline(frameFolder)
    corpus = sorted(corpus, key=lambda x: x[0])
    f = open('pickles/corpus.pkl', 'wb')
    pickle.dump(corpus, f)
    f.close()

def loaded_corpus_pipeline():
    '''
    Loads the corpus from the Pickle and proceeds with the Pipeline
    '''
    f = open('pickles/corpus.pkl', 'rb')

    # This line not strictly necessary
    corpus = sorted(pickle.load(f), key=lambda x : x[0])
    f.close()

    stich.stich(corpus)

if __name__ == '__main__':
    # complete_pipeline()
    
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLD = '../tests/vid/frames'
    UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
    print(UPLOAD_FOLDER)

    # pickle_corpus(UPLOAD_FOLDER)
    loaded_corpus_pipeline()
