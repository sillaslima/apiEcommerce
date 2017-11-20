from pprint import pprint
from sys import stdout
import io
import binascii

with open('/home/lima/auto_python/apiEcommerce/fut_branco_100x100.png','rb') as im:
    #print(im.read())
    s = im.read()
    a = bytearray(s)
    #print (a)
    r_data = binascii.unhexlify(s)
    stream = io.BytesIO(r_data)
    print (stream)