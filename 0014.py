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
        for j in range(1, len(txtDataDict[keyList[i]]) + 1):

            workSheet.write(i, j, txtDataDict[keyList[i]][j - 1])

    workSpace.save("test2.xls")


if __name__ == '__main__':
    filePath = input("请输入要打开TXT文件的路径：")
    addTxtToExcel(filePath)