# Code for resize image
from PIL import Image
# Image
img = Image.open('img/python.png')
# Sizes
new_width, new_height = 200, 200
img = img.resize((new_width, new_height), Image.ANTIALIAS)
# Save image
img.save('img/python2.png')