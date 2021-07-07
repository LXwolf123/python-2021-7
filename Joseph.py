
def JosephCalculate(maxNum, stepNum):
    data = []
    delData = []
    num = 0

    for i in range(1, maxNum + 1):
        data.append(i)


    while len(data) > 1:
        num += 1
        temp = data.pop(0)   #取出头部

        if num == stepNum:
            print(num)
            delData.append(temp)
            num = 0
        else:
            data.append(temp)   #是个环 头变尾部

    return {'lastData':data[0], 'delData':delData}   #返回一个字典

def JosephCalculate1(maxNum, stepNum):
    pos = 0
    for i in range(1, maxNum + 1):
        pos = (pos + stepNum) % i

    return pos + 1


if __name__ == '__main__':
        result = JosephCalculate(41, 3)

print('最后淘汰的是第', result['lastData'],'人')
print('淘汰的人的序号为',result['delData'])
print("最后淘汰的序号为", JosephCalculate1(41, 3))

