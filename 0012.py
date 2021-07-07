#coding "utf-8"

splitdata = []

def dealSensitiveWord(filepath):

    with open(filepath, "r", encoding="UTF-8") as file:
        data = file.read()
        splitdata = data.split("\n")
        print(splitdata)
        file.close()


        while True:
            replace = ""
            chatData = input("请您输入你需要输入的内容：")

            for data in splitdata:

                if (data in chatData):
                    for i in range(len(data)):
                        replace += "*"
                    chatData = chatData.replace(data, replace)
                    print("have find {0}".format(chatData))
                    break



if __name__ == '__main__':


    filepath = input("请您输入需要打开的文件地址:")
    dealSensitiveWord(filepath)