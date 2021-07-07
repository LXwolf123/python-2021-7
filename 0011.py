#coding "utf-8"

splitdata = []

def dealSensitiveWord(filepath):
    with open(filepath, "r", encoding="UTF-8") as file:
        data = file.read()
        splitdata = data.split("\n")
        print(splitdata)
        file.close()
        while True:
            chartData = input("请您输入你需要输入的内容：")

            if (chartData in splitdata):
                print("Freedom")
            else:
                print("Human Rights")

if __name__ == '__main__':


    filepath = input("请您输入需要打开的文件地址:")
    dealSensitiveWord(filepath)






