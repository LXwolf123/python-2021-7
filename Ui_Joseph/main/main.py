import reader
from PyQt5.QtWidgets import *
from ui import  JosephUi
import sys




if __name__ == "__main__":
    choice = int(input("请输入你想选择何种界面(1:QT界面 2:控制台界面):"))
    if choice == 1:
        app = QApplication(sys.argv)
        myWin = JosephUi.MyMainForm()
        myWin.show()
        sys.exit(app.exec_())
    else:
        JosephUi.MyConsoleUi().buildUi()

