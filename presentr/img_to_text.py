from google.cloud import vision
from google.cloud.vision import types
import io, os

client = vision.ImageAnnotatorClient()

def getTextFromFrame(fpath):
    '''
    Returns the text within a give frame as a list of lines tokenized into words.

    fPath: The filename of the image to get text from
    '''
    bname = os.path.basename(fpath)
    with io.open(fpath, 'rb') as image_file:
        content = image_file.read()
        image = vision.types.Image(content=content)
        response = client.document_text_detection(image=image)

    # Tokenize the annotation based on the \n separator, then by spaces. Affix the frame number to every line
    linelists = response.full_text_annotation.text.split("\n")
    wordlists = [line.split(" ") for line in linelists]
    wordlists = [int(bname[5:-4]), wordlists]

    print(wordlists) # Aesthetic but jenk debug print
    return wordlists 

# Test
# print(getTextFromFrame("/Users/Vivek/Desktop/presentr/tests/img/blackboard_original.jpg"))

def getFrameStack(folderpath):
    '''
    Get the filepaths of all jpegs within a given folder. 
    '''
    files = os.listdir(folderpath)
    
    try:
        files.remove('.DS_Store')
    except:
        pass
    try:
        files.remove('.empty')
    except:
        pass
    return ["{}/{}".format(folderpath, file) for file in files]
