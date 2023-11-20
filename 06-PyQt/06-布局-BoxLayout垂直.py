import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QGroupBox, QMainWindow
from PyQt5 import QtCore

class MyWindow(QWidget):
    def __init__(self):
        # 调用父类的__init__方法，因为它里面有很多对UI空间的初始化操作
        super().__init__()

        # 设置大小
        self.resize(300, 300)
        # 设置标题
        self.setWindowTitle('垂直布局')

        # 创建一个布局器，垂直布局
        layout = QVBoxLayout()
 
        # 添加弹簧
        layout.addStretch(10)

        btn1 = QPushButton('按钮1')
        layout.addWidget(btn1)

        btn2 = QPushButton('按钮2')
        layout.addWidget(btn2)

        btn3 = QPushButton('按钮2')
        layout.addWidget(btn3)

        # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为0
        # 会将在你放在的layout中的空间压缩成默认大小
        layout.addStretch(10)

        # 让当前的窗口使用这个排雷的规则(布局器)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = MyWindow()

    w.show()
    app.exec()