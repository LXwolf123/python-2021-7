import xlwt
from xlwt.Worksheet import Worksheet


def addTxtToExcel(filePath):
    workSpace = xlwt.Workbook(encoding="utf-8")  # 创建一个excel表格

    workSheet = workSpace.add_sheet("sheet0")  # 添加表格

    with open(filePath, "r", encoding="utf-8") as txtFile:
        txtData = txtFile.read()
        print(txtData)
        txtDataDict = eval(txtData)  # 将读出的字符串数据转换成Dict

    keyList = [str(i) for i in txtDataDict]

    for i in range(len(keyList)):
        workSheet.write(i, 0, keyList[i])

    for i in range(len(keyList)):
       workSheet.write(i, 1, txtDataDict[keyList[i]])

    workSpace.save("test3.xls")


if __name__ == '__main__':
    filePath = input("请输入要打开TXT文件的路径：")
    addTxtToExcel(filePath)