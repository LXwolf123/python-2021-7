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

        assert stepNum >= 0
        assert startId >= 0

        #   在约瑟夫环对象创建时就实例化学生对象
        for i in range(0, self.maxNum):
            self._objList.append(Student(self.fileData[i][0], self.fileData[i][1], i))         #得到学生娃儿的所有实例化对象

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._objList) > 0:
            outPos = (self.startId+self.stepNum - 1) % len(self._objList)
            outStudent = self._objList.pop(outPos)
            self.startId = outPos
            return outStudent

        else:
            raise StopIteration




