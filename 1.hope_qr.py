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
# chapter 1
s = "http://hope.sulabatsu.com/2017/12/07/capitulo-1-el-futuro/"
url = pyqrcode.create(s) 
url.png("1.hope.1.png", scale = 8)
# chapter 2
s = "http://hope.sulabatsu.com/2017/12/08/capitulo-2-viajera-del-tiempo/"
url = pyqrcode.create(s)
url.png("2.hope.2.png", scale = 8)

# C3
s = "Capitulo 3: Una chica perdidad \n http://hope.sulabatsu.com/2017/12/09/capitulo-3-una-chica-perdida-en-el-tiempo/"
url = pyqrcode.create(s)
url.png("3.hope.3.png", scale = 8)

# C4
s = "Capitulo 4: El codigo nos necesita \n  http://hope.sulabatsu.com/2017/12/11/capitulo-4-la-tecnologia-nos-necesita/"
url = pyqrcode.create(s)
url.png("4.hope.4.png", scale = 8)

# C5
s = "Capitulo 5: El codigo femenino \n http://hope.sulabatsu.com/2017/12/12/capitulo-5-el-codigo-femenino/"
url = pyqrcode.create(s)
url.png("5.hope.5.png", scale = 8)

