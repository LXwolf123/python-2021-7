from PIL import Image, ImageDraw, ImageFont

#用到了2D绘图模块 PIL


def AddWordImage(word):
    img = Image.open('001.jpg')
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('c:/windows/Fonts/Arial.ttf', size = 100)
    fillcolor = "#ff0000"         #红色
    width, height = img.size
    draw.text((width - 220, 40), word, font=myfont,fill=fillcolor)
    img.save('001r.jpg','jpeg')

if __name__ == '__main__':
    AddWordImage('hello')
    print("hello world")