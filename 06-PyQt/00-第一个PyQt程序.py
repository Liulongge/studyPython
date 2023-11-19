import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建对象，有且只有一个
    app = QApplication(sys.argv)

    # 创建一个QWidget对象
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")
    w.show()
    # 程序进行循环等待状态
    app.exec_()