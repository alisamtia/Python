# Install Pillow module:pip install Pillow
from PIL import Image, ImageEnhance, ImageFilter
import os
# Change image Extention
img1=Image.open('file.jpg')
# img1.save('file.png')

# Show image here
# img1.show()

# Resize Image
# max_size=(250,250)
# img1.thumbnail(max_size)
# img1.save("small_dog.png")



# Change all files
# for item in os.listdir():
#     if item.endswith('.jpg') or item.endswith('.png'):
#         img1=Image.open(item)
#         filename,ext=os.path.splitext(item)
#         img1.save(f'{filename}.png')

# -----------------------------Sharpness---------------------------------------------------
# 0: Blurry
# 1: Orignal Image
# 2: image with increased sharpness
# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(3).save('edited_image.png')

# ------------------------------Color---------------------------------------------------------
# 0:Black and white
# 1:Orignal Image
# 2:Increase color
# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(2).save('edited_image_color_2.png')

# ----------------------------------brightness-------------------------------------------------
# 0:black
# 1:Orignal
# 2:High Brightness
# enhancer=ImageEnhance.Brightness(img1)
# enhancer.enhance(1.5).save('edited_image_color_2.png')

# ----------------------------------contrast--------------------------------------------------------
# Same as back
# enhancer=ImageEnhance.Contrast(img1)
# enhancer.enhance(2).save('edited_image_contrast.png')


# -------------------------------------------blurness--------------------------------------------------------
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('Blurness.jpg')