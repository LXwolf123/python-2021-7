from PIL import Image, ImageDraw, ImageFont

#用到了2D绘图模块 PIL


def AddWordToImage(word):
    img = Image.open('001.jpg')
    canvas = ImageDraw.Draw(img)

    fontinfo = ImageFont.truetype('c:/windows/Fonts/Arial.ttf', size = 100)
    fillcolor = "#ff0000"         #红色
    width, height = img.size

    pos = (width - 220, 40)
    canvas.text(pos, word, font=fontinfo,fill=fillcolor)
    img.save('001r.jpg','jpeg')


if __name__ == '__main__':
    AddWordToImage('8')
    print("hello world")