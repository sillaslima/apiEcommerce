
import base64
with open('photo4943226265427617822.jpg','rb') as im:
    #print(im.read())
    s = im.read()
    a = base64.b64encode(s)
    print (a)
    #print(s)



