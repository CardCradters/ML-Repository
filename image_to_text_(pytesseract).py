# -*- coding: utf-8 -*-
"""Image to text (pytesseract).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fJSdJGDRHjnCLo2Hbsiw6LVrIFZ8kOXP
"""

!pip install pytesseract

!apt install tesseract-ocr
!apt install libtesseract-dev

import pytesseract
from PIL import Image

from google.colab import drive

# Accessing My Google Drive
drive.mount('/content/drive')

foto = '/content/drive/MyDrive/Capstone/namecard1.jpg' # minta storage ke andi: link

image = Image.open(foto)

# Perform OCR using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)