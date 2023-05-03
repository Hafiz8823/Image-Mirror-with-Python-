from PIL import Image
Image.open("Image.jpg")
img = Image.open("Image.jpg")
Mirror_Image=img.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_Image.save(r'binod_mirror.png')
Image.open('binod_mirror.png')
