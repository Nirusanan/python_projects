import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("https://www.sab.ac.lk/")
myqr.save("myqr.png", scale = 8)


#Decode
de = decode(Image.open("myqr.png"))
print(de[0].data.decode("ascii"))