import random

#常量大写

def getRandomStr(length = 8):    #8位长度
    str = ""
    for i in range(length):
        str += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    return  str

actCode = []  #创建一个列表

if __name__ == '__main__':
        for num in range(200):
             actCode.append(getRandomStr(8))

print(actCode)

