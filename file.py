# coding=utf-8
def read_in_chunks(filepath, chunk_size = 1024):
    file_object = open(filepath, "r")

    while True:
        file_data = file_object.read(chunk_size)

        if not file_data:
            break

        yield file_data    #调用生成器


if __name__ == '__main__':
        filepath = input("请输入你需要打开文件的位置：")
        str = ""
        file = open('E:/360MoveData/Users/江西水根/Desktop'+"/3.txt", 'x')
        for chunks in read_in_chunks(filepath):
            str += chunks

        file.write(str)