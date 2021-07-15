import csv
import zipfile
import xlrd
import os

class Reader(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def read(self):               #父类先实现该方法
        pass

class CsvReader(Reader):
    def __init__(self, filePath):
        self.filePath = filePath

    def read(self) -> list:
        with open(self.filePath, mode="r", encoding="utf-8") as csvfile:
            csvReader = csv.reader(csvfile)
            rowsData = [row for row in csvReader]

        return  rowsData

class XlsReader(Reader):
    rowAllValues = []
    nrows = 0
    def __init__(self, filePath, sheetIndex):
        self.filePath = filePath
        self.sheetIndex = sheetIndex

    def read(self) -> list:
        with xlrd.open_workbook(self.filePath) as xlsFile:
            xlsSheet = xlsFile.sheet_by_index(self.sheetIndex)         #打开指定的表
            self.nrows = xlsSheet.nrows
            print(type(xlsSheet.row_values(0)))
            for i in range(self.nrows):
                self.rowAllValues.append(xlsSheet.row_values(i))

            return self.rowAllValues

class ZipReader(Reader):

    def __init__(self, filePath, interFileName):
        self.filePath = filePath
        self.interName = interFileName

    def read(self) -> list:
        with zipfile.ZipFile(self.filePath, "r") as zip:
            folder,fileName = os.path.split(self.filePath)
            print(folder)
            zip.extract(self.interName, folder)   #解压指定文件


        if (".csv" in self.interName):
            return CsvReader(folder+'\{0}'.format(self.interName)).read()
        elif (".xls" in self.interName):
            return XlsReader(folder+'\{0}'.format(self.interName), 0).read()