'''date:2021-7-7
   author:潘水根
    第三个版本：这个版本加上了作业里发散的功能，把约瑟夫环封装成了一个容器，用for循环遍历环
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

    #print(len(calData))
    #print(len(studentObj))

    studentObj = calData.copy()

    while len(studentObj) > 1:
        num += 1

        temp = studentObj.pop(0)

        if num == stepNum:
            delData.append(temp)
            num = 0
        else:
            studentObj.append(temp)
    
    #delData.append(studentObj[0])
    #print(studentObj[0])
    #print(delData[-1])

    return [delData, studentObj[0]]   #封装成容器





if __name__ == '__main__':
    delDataShow = []
    startNum = int(input("请输入开始序号:"))
    maxNum = int(input("请输入总人数："))
    stepNum = int(input("请输入步长值："))

    studentObj = getStudentObject(maxNum)
    #result = JosephCalculate(studentObj, startNum, maxNum, stepNum)

    for obj in JosephCalculate(studentObj, startNum, maxNum, stepNum)[0]:
        print("依次淘汰的人的序号为：{0},  姓名为: {1},  学号为：{2}".format(obj.Id, obj.name, obj.schoolId))
        

    obj = JosephCalculate(studentObj, startNum, maxNum, stepNum)[1]
    print("最后留下的人的序号为：{0},  姓名为: {1},  学号为：{2}".format(obj.Id, obj.name, obj.schoolId))
        
    
        

   
