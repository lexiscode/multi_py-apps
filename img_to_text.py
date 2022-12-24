# install tesseract and pytesseract packages
# download and install tesseract on windows https://digi.bib.uni-mannheim.de/tesseract/

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nwoko\AppData\Local\Programs\Tesseract-OCR\tesseract.exe" #path to its installation

def convert():
    img = Image.open('img.png')
    text = pytesseract.image_to_string(img) #img to strings
    print(text)

convert()
