'''date:2021-7-7
   author:潘水根
    第二个版本：这个版本把学生对象容器作为传入参数，基本传入参数有起始序号，步长，总人数，实现第二次布置的约瑟夫环的基本任务
        '''

data = []
#   创建学生类
class Student():

    def __init__(self, name, schoolId, Id):
        self.name = name
        self.schoolId = schoolId
        self.Id = Id

    def sayHello(self):
        print("Hi nice to meet you. i am {0}".format(self.name))

def getStudentObject(maxNum):

    for i in range(1, maxNum + 1):
        strName = ""
        strId = ""
       # print(i)
        strName = "潘{0}号".format(i)
        strId = "20170710{0}".format(i)
        data.append(Student(strName, strId, i))
        #print(data[i - 1].name)
        #print(data[i - 1].schoolId)

    return data


def JosephCalculate(studentObj, startNum, maxNum, stepNum):

    """加上断言，养成良好习惯"""
    assert maxNum > 0
    assert  stepNum > 0
    assert startNum > 0

    calData = []
    delData = []
    num = 0

    startNumCopy = startNum



    for i in range(startNum, len(studentObj) + 1, 1):
        calData.append(studentObj[i - 1])
    for x in range(startNumCopy - 1):
        calData.append(studentObj[x])

    #for i in range(len(calData)):
        #print(calData[i].Id)

    print(len(calData))
    print(len(studentObj))

    studentObj = calData.copy()

    while len(studentObj) > 1:
        num += 1

        temp = studentObj.pop(0)

        if num == stepNum:
            delData.append(temp)
            num = 0
        else:
            studentObj.append(temp)


    return {'lastData':studentObj[0], 'deldata':delData}





if __name__ == '__main__':
    delDataShow = []
    startNum = int(input("请输入开始序号:"))
    maxNum = int(input("请输入总人数："))
    stepNum = int(input("请输入步长值："))

    studentObj = getStudentObject(maxNum)
    result = JosephCalculate(studentObj, startNum, maxNum, stepNum)

    print('最后淘汰的人的序号为：', result['lastData'].Id)
    print('最后淘汰的人的学号为：', result['lastData'].schoolId)
    print('最后淘汰的人的姓名为：', result['lastData'].name)
    result['lastData'].sayHello()



    for i in range(len(result['deldata'])):
        delDataShow.append(result['deldata'][i].Id)

    print('依次淘汰的人序号为：',delDataShow)






















