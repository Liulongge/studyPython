
# 我们一般将界面的显示用主线程来操作，
# 逻辑功能代码或者耗时的代码都用另外线程进行处理

import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QThread
class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./thread-1.ui')

        lineedit = self.ui.lineEdit
        btn1 = self.ui.pushButton
        btn2 = self.ui.pushButton_2

        btn1.clicked.connect(self.click_1)
        btn2.clicked.connect(self.click_2)

    def click_1(self):
        for i in range(10):
            print('是UI线程中执行......%d' % (i + 1))
            time.sleep(1)
    
    def click_2(self):
        self.my_thread = MyThread() # 线程创建
        self.my_thread.start() # 开始线程


class MyThread(QThread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        for i in range(10):
            print('是MyThread中执行...... %d' % (i + 1))
            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWin()
    myshow.ui.show()
    app.exec()
