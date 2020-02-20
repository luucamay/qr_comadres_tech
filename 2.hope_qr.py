# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 


# String which represent the QR code 
s = "http://hope.sulabatsu.com/2017/12/07/capitulo-1-el-futuro/"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "hackersfriend.svg" 
url.svg("1.1.hope.svg", scale = 8)
