import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('第一个PyQt程序')

    # 创建按钮
    btn = QPushButton('按钮')
    # 设置按钮的父亲是当前窗口，等于是添加到窗口中显示
    btn.setParent(w)
    # 展示窗口
    w.show()

    # 程序进行循环等待
    app.exec_()
