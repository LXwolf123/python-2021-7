from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from user_case import Joseph06, reader


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 561)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 20, 471, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)
        self.fileDirLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.fileDirLineEdit.setObjectName("fileDirLineEdit")
        self.gridLayout.addWidget(self.fileDirLineEdit, 0, 2, 1, 1)
        self.savePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout.addWidget(self.savePushButton, 2, 0, 1, 1)
        self.openFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openFileButton.setObjectName("openFileButton")
        self.gridLayout.addWidget(self.openFileButton, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 3)
        self.calPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.calPushButton.setObjectName("calPushButton")
        self.gridLayout.addWidget(self.calPushButton, 2, 2, 1, 1)
        self.mesInputLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.mesInputLineEdit.setObjectName("mesInputLineEdit")
        self.gridLayout.addWidget(self.mesInputLineEdit, 1, 2, 1, 1)
        self.josephDataInputEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.josephDataInputEdit.setObjectName("josephDataInputEdit")
        self.gridLayout.addWidget(self.josephDataInputEdit, 3, 0, 1, 1)
        self.inputInterFilename = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputInterFilename.setObjectName("inputInterFilename")
        self.gridLayout.addWidget(self.inputInterFilename, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mesInputLineEdit.setPlaceholderText(_translate("Form", "请按照格式输入（姓名，学号）"))
        self.savePushButton.setText(_translate("Form", "保存"))
        self.openFileButton.setText(_translate("Form", "打开文件"))
        self.fileDirLineEdit.setPlaceholderText(_translate("Form", "文件路径"))
        self.calPushButton.setText(_translate("Form", "计算"))
        self.josephDataInputEdit.setPlaceholderText(_translate("Form", "按格式输入:(开始序号,总人数，步长值)"))
        self.inputInterFilename.setPlaceholderText(_translate("Form", "请输入要打开内部文件名"))


class MyMainForm(QMainWindow, Ui_Form):
    reader = []
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        #  建立信号和槽的绑定
        self.openFileButton.clicked.connect(self.openFile)
        self.savePushButton.clicked.connect(self.saveDataToFile)
        self.calPushButton.clicked.connect(self.calJosePh)

    def fileDataShow(self):
        self.textBrowser.clear()
        for i in self.reader:  # 更新显示方法
            self.textBrowser.append(str(i))

    def openFile(self):
        # 要供外部使用的才写到属性里头
        self.filenamePath, ok = QFileDialog.getOpenFileName(self, "选取单个文件", "c:/",
                                                            "All Files (*);;Text Files (*.txt)")
        if (ok):
            self.fileDirLineEdit.setText(str(self.filenamePath))

            if ".csv" in self.filenamePath:                            #打开的是CSV文件
                self.obj = reader.CsvReader(self.filenamePath)         #对象也得设置成属性外部要使用
                self.reader =  self.obj.read()
                self.fileDataShow()
            if ".xls" in self.filenamePath:
                self.obj = reader.XlsReader(self.filenamePath, "Sheet1")
                self.reader = self.obj.read()
                self.fileDataShow()
            if ".zip" in self.filenamePath:
                self.interFilename = self.inputInterFilename.text()
                self.obj = reader.ZipReader(self.filenamePath, self.interFilename)
                self.reader = self.obj.read()
                self.fileDataShow()



    def saveDataToFile(self):
        self.mesInputData = self.mesInputLineEdit.text()
        self.mesList = self.mesInputData.split(",")
        self.index = self.spinBox.value()
        self.reader[self.index][0] = self.mesList[0]
        self.reader[self.index][1] = self.mesList[1]
        self.obj.saveFile(self.reader)
        self.fileDataShow()


    def calJosePh(self):
        dataList = self.josephDataInputEdit.text().split(",")
        dataList = list(map(int, dataList))
        startId = dataList[0]        #开始值
        maxNum = dataList[1]
        stepNum = dataList[2]
        print("the data is {0}, {1}, {2}".format(startId,maxNum,stepNum))
        self.textBrowser.clear()
        for obj in Joseph06.JosephCricle(self.reader, startId, maxNum, stepNum):  # for循环遍历整个约瑟夫环
            self.textBrowser.append("依次删除的同学的姓名为：{0}，学号为：{1}，序号为：{2}".format(obj.name, obj.schoolId, obj.Id))

class MyConsoleUi(object):
    def __init__(self):
        pass

    def buildUi(self):
        while True:
            print("*****************这是开始******************")
            filepath = input("请输入需要打开的文件路径:")

            while True:
                if filepath.endswith(".csv"):
                    print("***********您打开的是csv表格文件*********************")
                    obj = reader.CsvReader(filepath)
                    readerData = obj.read()

                    command = int(input("请问您现在需要干什么（1：输出表格数据 2：编辑表格数据 3：计算约瑟夫环 4:退出）请根据意愿进行选择，祝您愉快："))
                    if command == 1:
                        print("***********为您输出表格内部数据***********************")
                        for i in range(len(readerData)):
                            print("学生的姓名为：{0}，学号为：{1}".format(readerData[i][0], readerData[i][1]))
                    elif command == 2:
                        print("**************现在您想编辑信息*****************")
                        data = input("请按格式输入（序号,姓名,学号）：")
                        str = data.split(",")
                        readerData[int(str[0])][0] = str[1]
                        readerData[int(str[0])][1] = str[2]  # 得到需要保存的数据
                        obj.saveFile(readerData)
                    elif command == 3:
                        josephInfo = input("请您输入对应的开始序号,总人数,步长值。请按格式输入（开始序号,总人数,步长值）：")
                        infoList = josephInfo.split(",")
                        startId = int(infoList[0])
                        maxNum = int(infoList[1])
                        stepNum = int(infoList[2])
                        print("******************现在为您输出约瑟夫环数据****************")
                        for stuobj in Joseph06.JosephCricle(readerData, startId, maxNum, stepNum):  # for循环遍历整个约瑟夫环
                            print("依次删除的同学的姓名为：{0}，学号为：{1}，序号为：{2}".format(stuobj.name, stuobj.schoolId, stuobj.Id))

                    else:
                        break
                else:
                    break

            while True:
                if filepath.endswith(".xls"):
                    print("***********您打开的是xls表格文件*********************")
                    obj = reader.XlsReader(filepath, "Sheet1")
                    readerData = obj.read()

                    command = int(input("请问您现在需要干什么（1：输出表格数据 2：编辑表格数据 3：计算约瑟夫环 4:退出）请根据意愿进行选择，祝您愉快："))
                    if command == 1:
                        print("***********为您输出表格内部数据***********************")
                        for i in range(len(readerData)):
                            print("学生的姓名为：{0}，学号为：{1}".format(readerData[i][0], readerData[i][1]))
                    elif command == 2:
                        print("**************现在您想编辑信息*****************")
                        data = input("请按格式输入（序号,姓名,学号）：")
                        str = data.split(",")
                        readerData[int(str[0])][0] = str[1]
                        readerData[int(str[0])][1] = str[2]  # 得到需要保存的数据
                        obj.saveFile(readerData)
                    elif command == 3:
                        josephInfo = input("请您输入对应的开始序号,总人数,步长值。请按格式输入（开始序号,总人数,步长值）：")
                        infoList = josephInfo.split(",")
                        startId = int(infoList[0])
                        maxNum = int(infoList[1])
                        stepNum = int(infoList[2])
                        print("******************现在为您输出约瑟夫环数据****************")
                        for stuobj in Joseph06.JosephCricle(readerData, startId, maxNum, stepNum):  # for循环遍历整个约瑟夫环
                            print("依次删除的同学的姓名为：{0}，学号为：{1}，序号为：{2}".format(stuobj.name, stuobj.schoolId, stuobj.Id))

                    else:
                        break

                else:
                    break

            while True:
                if filepath.endswith(".zip"):
                    print("***********您打开的是zip压缩包文件*********************")
                    obj = reader.ZipReader(filepath, "demo6.csv")
                    readerData = obj.read()

                    command = int(input("请问您现在需要干什么（1：输出表格数据 2：计算约瑟夫环 3:退出）请根据意愿进行选择，祝您愉快："))
                    if command == 1:
                        print("***********为您输出表格内部数据***********************")
                        for i in range(len(readerData)):
                            print("学生的姓名为：{0}，学号为：{1}".format(readerData[i][0], readerData[i][1]))

                    elif command == 2:
                        josephInfo = input("请您输入对应的开始序号,总人数,步长值。请按格式输入（开始序号,总人数,步长值）：")
                        infoList = josephInfo.split(",")
                        startId = int(infoList[0])
                        maxNum = int(infoList[1])
                        stepNum = int(infoList[2])
                        print("******************现在为您输出约瑟夫环数据****************")
                        for stuobj in Joseph06.JosephCricle(readerData, startId, maxNum, stepNum):  # for循环遍历整个约瑟夫环
                            print("依次删除的同学的姓名为：{0}，学号为：{1}，序号为：{2}".format(stuobj.name, stuobj.schoolId, stuobj.Id))

                    else:
                        break

                else:
                    break




