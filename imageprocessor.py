from PIL import Image 
from PIL import ImageFilter
from PIL import ImageEnhance

def rotate_box(an_image):
    x,y = an_image.size
    box = (int(x/2), int(y/2), int(x/2) + 150, int(y/2) + 50)
    region = an_image.crop(box)
    region = region.transpose(Image.ROTATE_180)
    an_image.paste(region, box)
    an_image.show()
    return an_image

#im = Image.open("C:\\Users\\DimHackademy\\Desktop\\pictures\\picture1.jpg")

#print(im.format, im.size, im.mode)

#im = rotate_box(im)

#im2 = Image.open("C:\\Users\\DimHackademy\\Desktop\\pictures\\picture2.jpg")

#im2 = rotate_box(im2)
