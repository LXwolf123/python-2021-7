'''date:2021-7-7
   author:潘水根
    第四个版本：这个版本加上了作业里发散的功能，把约瑟夫环封装成了一个容器，用for循环遍历环，同时目标对象从不同文件中获取
        '''

import csv
import xlrd
import zipfile

data = []


#   创建学生类
class Student():

    def __init__(self, name, schoolId, Id):
        self.name = name
        self.schoolId = schoolId
        self.Id = Id

    def sayHello(self):
        print("Hi nice to meet you. i am {0}".format(self.name))


class Reader(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def openfile(self):
        pass


#            读取Csv后缀文件
class CsvReader(Reader):
    def __init__(self, filePath):
        super().__init__(filePath)
        self.filePath = filePath

    def openCsvFile(self, maxNum) -> list:
        with open(self.filePath, mode="r", encoding="utf-8") as csvfile:
            csvReader = csv.reader(csvfile)
            rowsData = [row for row in csvReader]
        assert maxNum < len(rowsData)  # 必须小于行数
        for i in range(1, maxNum + 1):
            data.append(Student(rowsData[i - 1][0], rowsData[i - 1][1], i))

        return data


#         读取 Xls文件
class XlsReader(Reader):
    def __init__(self, filePath):
        super().__init__(filePath)
        self.filePath = filePath

    def openXlsFile(self, maxNum) -> list:
        with xlrd.open_workbook_xls(self.filePath) as xlsfile:
            xlsSheet = xlsfile.sheets()[0]  # 打开第一张表
            nrows = xlsSheet.nrows  # 得到行数
        assert maxNum < nrows

        for i in range(1, maxNum + 1):
            data.append(Student(xlsSheet.row_values(i - 1)[0], xlsSheet.row_values(i - 1)[1], i))

        return data


#          读取 Zip压缩文件
class ZipReader(Reader):
    pos = 0
    strpos = ""
    pathBase = ""

    def __init__(self, filePath, filePathBase):
        super().__init__(filePath)
        self.filePath = filePath
        self.filePathBase = filePathBase

    def openZipFile(self, maxNuM) -> list:
        with zipfile.ZipFile(self.filePath, 'r') as zip:
            self.pos = zip.namelist()[0].index('.')  # 默认只有一个文件
            self.strpos = zip.namelist()[0][self.pos:]
            zip.extractall(self.filePathBase)
            print(self.strpos)

        if (self.strpos == '.csv'):
            print('OK')
            print(self.filePathBase + '.{0}'.format(zip.namelist()[0]))
            return CsvReader(self.filePathBase + '\{0}'.format(zip.namelist()[0])).openCsvFile(maxNuM)
        elif (self.strpos == '.xls'):
            return XlsReader(self.filePath + '\{0}'.format(zip.namelist()[0])).openXlsFile(maxNuM)


def getStudentObject(maxNum):
    for i in range(1, maxNum + 1):
        strName = ""
        strId = ""
        # print(i)
        strName = "潘{0}号".format(i)
        strId = "20170710{0}".format(i)
        data.append(Student(strName, strId, i))
        # print(data[i - 1].name)
        # print(data[i - 1].schoolId)

    return data


def JosephCalculate(studentObj, startNum, maxNum, stepNum) -> list:
    """加上断言，养成良好习惯"""
    assert maxNum > 0
    assert stepNum > 0
    assert startNum > 0

    calData = []
    delData = []
    num = 0

    startNumCopy = startNum

    # 根据开始序号重新排序
    for i in range(startNum, len(studentObj) + 1, 1):
        calData.append(studentObj[i - 1])
    for x in range(startNumCopy - 1):
        calData.append(studentObj[x])

    # for i in range(len(calData)):
    # print(calData[i].Id)

    # print(len(calData))
    # print(len(studentObj))

    studentObj = calData.copy()

    while len(studentObj) > 1:
        num += 1

        temp = studentObj.pop(0)

        if num == stepNum:
            delData.append(temp)
            num = 0
        else:
            studentObj.append(temp)

    # delData.append(studentObj[0])
    # print(studentObj[0])
    # print(delData[-1])

    return [delData, studentObj[0]]  # 封装成容器


if __name__ == '__main__':
    delDataShow = []
    startNum = int(input("请输入开始序号:"))
    maxNum = int(input("请输入总人数："))
    stepNum = int(input("请输入步长值："))
    filePath = input("请输入文件路径：")
    filePathBase = input("请输入文件根目录：")

    #       单独打开CSV文件
    # studentObj = CsvReader(filePath).openCsvFile(maxNum)

    #       单独打开XLS文件
    # studentObj = XlsReader(filePath).openXlsFile(maxNum)

    #       单独打开zip文件
    studentObj = ZipReader(filePath, filePathBase).openZipFile(maxNum)
    # result = JosephCalculate(studentObj, startNum, maxNum, stepNum)

    for obj in JosephCalculate(studentObj, startNum, maxNum, stepNum)[0]:
        print("依次淘汰的人的序号为：{0},  姓名为: {1},  学号为：{2}".format(obj.Id, obj.name, obj.schoolId))

    obj = JosephCalculate(studentObj, startNum, maxNum, stepNum)[1]
    print("最后留下的人的序号为：{0},  姓名为: {1},  学号为：{2}".format(obj.Id, obj.name, obj.schoolId))

