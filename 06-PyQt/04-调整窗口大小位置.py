import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget
from PyQt5 import QtCore
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    # 设置窗口大小
    w.resize(400, 200)
    # 设置窗口title
    w.setWindowTitle('QLineEdit控件')
    # 将窗口设置在屏幕的左上角
    w.move(0, 0)

    # 设置窗口再屏幕中央显示
    # 获取屏幕可用区域中心坐标
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    print(w.frameGeometry().getRect())
    old_x, old_y, width, hight = w.frameGeometry().getRect()
    # 移动到中心区域
    w.move(x - int(width / 2), y - int(hight / 2))

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