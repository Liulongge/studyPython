
# 纯靠代码编写界面，效率有点低，可以使用辅助设计图形化页面Qt Designer
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi('./test.ui')
    ui.show()
    app.exec()