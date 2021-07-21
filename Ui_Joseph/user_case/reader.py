import csv
import zipfile
import xlrd
import os             #pandas  这个库好用
import pandas as pd

class Reader(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def read(self):               #父类先实现该方法
        pass

class CsvReader(Reader):

    def __init__(self, filePath):
        assert filePath.endswith('.csv')
        self.filePath = filePath

    def read(self) -> list:
        csvFile = pd.read_csv(self.filePath)
        csvDataList = csvFile.values.tolist()
      
        return csvDataList
    
    def saveFile(self, dataList):                   #保存数据
        df = pd.DataFrame(dataList)
        df.to_csv(self.filePath,index=False)

        
class XlsReader(Reader):
   
    def __init__(self, filePath, sheetName):
        assert filePath.endswith('.xls')
        self.filePath = filePath
        self.sheetName = sheetName

    def read(self) -> list:
        xlsFile = pd.read_excel(self.filePath, sheet_name=self.sheetName)
        xlsDataList = xlsFile.values.tolist()
        return xlsDataList

    def saveFile(self, dataList):
        df = pd.DataFrame(dataList)
        df.to_excel(self.filePath, index=False)

            

class ZipReader(Reader):

    def __init__(self, filePath, interFileName):
        assert filePath.endswith('.zip')
        assert interFileName.endswith('.csv') or interFileName.endswith('.xls')
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
            return XlsReader(folder+'\{0}'.format(self.interName), "Sheet1").read()

    def saveFile(self):       #压缩包里的文件不能随便改变， 为了保持程序的完整性，加上
        pass

