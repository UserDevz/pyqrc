# Gerador de qrcodes em Python;
# Criador: UserDevz;
# Bibliotecas:
#      *PyQRCode;
#      *png;
#
# Para entender o funcionamento, leia o readme;

import PyQRCode
import png

qrcode = PyQRCode.create('')
qrcode.png('', scale=6)


