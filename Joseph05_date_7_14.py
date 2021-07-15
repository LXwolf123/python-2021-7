import reader


class Student():

    def __init__(self, name, schoolId, Id):
        self.name = name
        self.schoolId = schoolId
        self.Id = Id

    def sayHello(self):
        print("Hi nice to meet you. i am {0}".format(self.name))


class JosephCricle(object):
    _objList = []               #对象列表
    _originObjList = []
    delObjList = []

    def __init__(self, reader, startId, maxNum, stepNum):
        self.startId = startId
        self.maxNum = maxNum
        self.stepNum = stepNum
        self.fileData = reader
        assert stepNum > 0
        assert startId > 0

        #   在约瑟夫环对象创建时就实例化学生对象
        for i in range(1, self.maxNum + 1):
            self._objList.append(Student(self.fileData[i - 1][0], self.fileData[i - 1][1], i))         #得到学生娃儿的所有实例化对象

    def getJosephCricle(self):
        startIdCopy = self.startId
        num = 0
        for i in range(self.startId, len(self._objList) + 1, 1):
            self._originObjList.append(self._objList[i - 1])
        for j in range(startIdCopy - 1):
            self._originObjList.append(self._objList[j])

        self._objList = self._originObjList.copy()

        while len(self._objList) > 1:
            num += 1
            temp = self._objList.pop(0)
            if num == self.stepNum:
                self.delObjList.append(temp)
                num = 0
            else:
                self._objList.append(temp)

        self.delObjList.append(self._objList[0])      #最后留下的人也要加上

        return  self.delObjList                       #把依次删除的人返回



if __name__ == '__main__':

    startNum = int(input("请输入开始序号:"))
    maxNum = int(input("请输入总人数："))
    stepNum = int(input("请输入步长值："))
    filePath = input("请输入文件路径：")
    interFileName = input("请输入需要解压缩文件名字：")

    #obj = reader.XlsReader(filePath, 0)        #excel格式实现
    #reader = obj.read()
    #obj = reader.CsvReader(filePath)           #Csv表格格式实现
    #reader = obj.read()
    obj = reader.ZipReader(filePath, interFileName)      #压缩包方式实现
    reader = obj.read()
    #josephObjList = JosephCricle(reader, startNum, maxNum, stepNum).getJosephCricle()

    for obj in JosephCricle(reader, startNum, maxNum, stepNum).getJosephCricle():               #for循环遍历整个约瑟夫环
       print("依次删除的学生姓名为：{0}，学号为：{1}，序号为：{2}".format(obj.name, obj.schoolId, obj.Id))