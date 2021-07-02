import os
from PIL import Image

imageWidth = 1136
imageHeight = 640
fileinfo = "G:/python/practise/"
mylist = os.listdir(fileinfo)

# resize方法是返回修改后的对象
for n in mylist:
    if (".jpg" in n or ".png" in n):
        im = Image.open(fileinfo+n)
        out = im.resize((imageWidth, imageHeight))
        out.save('new'+n)
        print(n)












