from PIL import Image

img = Image.open('img/python.png')
new_width  = 200
new_height = 200
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('img/python2.png')