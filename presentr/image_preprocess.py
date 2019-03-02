# This is a test of PyTesseract's Image-Proccessing Capabilities

from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import pytesseract

# im = Image.open('img/blackboard_original.jpg')
def preprocess(im):
    '''
    Inverts and grayscales the given image.
    '''
    im = ImageOps.invert(ImageOps.grayscale(im))
    return im

# The preprocessed image
# prep = preprocess(im)
# prep.show()