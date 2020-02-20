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
