from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
class Captcha(object):
    def __init__(self, width, height):
        assert width > 0
        assert  height > 0
        
        self.width = width
        self.height = height

    def getBackRandChar(self):
        return chr(random.randint(65, 90))
    def getBackRandColor(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    def getBackWorkRandColor(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def createCaptcha(self):
        image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        #创建字体对象
        font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 36)
        canvas = ImageDraw.Draw(image)

        for x in range(self.width):
            for y in range(self.height):
                canvas.point((x, y), fill = self.getBackRandColor())
        for i in range(4):
            canvas.text((60 * i + 10, 10), self.getBackRandChar(), font=font, fill=self.getBackWorkRandColor())

        image = image.filter(ImageFilter.BLUR)
        image.save('code.jpg', 'jpeg')


if __name__ == '__main__':
    captcha = Captcha(240, 60)
    captcha.createCaptcha()