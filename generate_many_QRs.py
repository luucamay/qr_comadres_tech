# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
from textos import *

# Create PNG files 
# print(data[3])
for i in range(len(data)):
    url = pyqrcode.create(data[i])
    png_name = str(i) + ".text.png"
    url.png(png_name, scale = 8)
'''
s = "Capitulo 5: El codigo femenino \n http://hope.sulabatsu.com/2017/12/12/capitulo-5-el-codigo-femenino/"
url = pyqrcode.create(s)
url.png("5.hope.5.png", scale = 8)
'''
