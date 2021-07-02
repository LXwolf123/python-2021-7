import re

#  正则表达式库
def getWordNum(place):
    num = 0
    with open(place,'r') as f:
        data = f.read()
    result = re.split("[^a-zA-Z]", data)     #  以字母以外的任意字符分割字符串
    print(result)
    for i in result:
        if i != ' ':
            num += len(i)
    return num

if __name__ == '__main__':
    print(getWordNum('G:/python/practise/004.txt'))