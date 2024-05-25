import qrcode

myqr = qrcode.make("https://www.sab.ac.lk/")
myqr.save("myqr.png", scale = 8)

