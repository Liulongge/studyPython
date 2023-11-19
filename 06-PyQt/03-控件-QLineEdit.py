import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5 import QtCore
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 创建QLlabel组件
    label = QLabel('账号:', w)
    label.setGeometry(20, 20, 30, 20)

    # 创建QLineEdit组件
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号')
    edit.setGeometry(55, 20, 200, 20)

    # 创建QPushButton组件
    btn = QPushButton('注册', w)
    btn.setGeometry(50, 80, 70, 30)

    w.show()
    app.exec()