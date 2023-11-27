# pip install pyqrcode
# pip install qrcode
# pip install pypng
# pip install pyzbar
# pip install pillow

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# QR Code Maker
# content="https://remotesol.com/wp-admin"
# a=pyqrcode.create(content)
# a.png("MyWebsite.png",scale=5)
# print("Qr Code Generated Successfully")

# Scannner
img=Image.open("MyWebsite.png")
cont=decode(img)
print(cont[0].data.decode())