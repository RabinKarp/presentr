# This is a test of PyTesseract's Image-Proccessing Capabilities

from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('img/blackboard.jpg')))
