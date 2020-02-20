# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 

# String which represent the QR code 
s = "http://hope.sulabatsu.com/2017/12/07/capitulo-1-el-futuro/"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "hackersfriend.svg" 
url.svg("1.1.hope.svg", scale = 8)

## Create PNG files 
# chapter 2
s = "http://hope.sulabatsu.com/2017/12/08/capitulo-2-viajera-del-tiempo/"
url = pyqrcode.create(s)
url.png("2.hope.2.png", scale = 8)


