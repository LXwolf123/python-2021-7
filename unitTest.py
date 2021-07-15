from datetime import date
import unittest
import reader
import Joseph05_date_7_14

#             缺乏测试经验不知道测些啥
class CsvReaderFunctionTest(unittest.TestCase):

    def testFunctionCsvRead(self):
        data = reader.CsvReader("G:\python\csvdemo1.csv").read() 
        print(len(data))
        
        self.assertEqual(len(data), 53)
        for i in range(50):
            self.assertEqual(data[i][0], "潘{0}号".format(i + 1))
        #self.assertNotAlmostEqual(type(data), lui)

class XlsReaderFunctionTest(unittest.TestCase):

    def testFunctionXlsRead(self):
        data = reader.XlsReader("G:\python\csvdemo1.xls", 0).read()

        self.assertEqual(len(data), 100)
        for i in range(50):
            self.assertEqual(data[i][0], "潘{0}号".format(i + 1))

class ZipReaderFunctionTest(unittest.TestCase):

    def testFunctionZipRead(self):
        data = reader.ZipReader("G:\python\csvdemo1.zip", "csvdemo1.xls").read()

        self.assertEqual(len(data), 150)
        for i in range(50):
            self.assertEqual(data[i][0], "潘{0}号".format(i + 1))


class JosephFunctionTest(unittest.TestCase):

    def testFunctionJosephCricle(self):
        obj = Joseph05_date_7_14.JosephCricle(reader.ZipReader("G:\python\csvdemo1.zip", "csvdemo1.xls").read(), 1, 20, 2).getJosephCricle()

        self.assertEqual(type(obj), list)
        self.assertEqual(obj[19].Id, 9)


unittest.main()