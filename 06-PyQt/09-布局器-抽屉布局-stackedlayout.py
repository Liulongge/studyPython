import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QLabel

class window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉1要显示的内容', self)
        # self.setStyleSheet('background-color:green;')

class window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉2要显示的内容', self)
        # self.setStyleSheet('background-color:red;')


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_stacked_layout()
        self.init_ui()

    # 添加两个要显示的页面
    def create_stacked_layout(self):
        # 创建抽屉时布局
        self.stacked_layout = QStackedLayout()
        win1 = window1()
        win2 = window2()
        # 将创建的两个widget添加到抽屉布局器中
        # 相当于一个列表中有两个元素
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        # 设置widget大小以及固定宽高
        self.setFixedSize(300, 270)
        # 创建整体垂直布局器
        container = QVBoxLayout()
        # 创建1个要显示具体内容的字widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet('background-color:gray;')
        # 创建2个按钮，用来点击进行切换抽屉布局器中的widget
        btn_press1 = QPushButton('抽屉1')
        btn_press2 = QPushButton('抽屉2')
        # 给按钮添加事件(即点击后调用的函数)
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)
        # 将需要显示的空间添加到布局器中
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)
        # 设置当前要显示的widget，从而能够显示这个布局器中的控件
        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个widget
        self.stacked_layout.setCurrentIndex(0)
    
    def btn_press2_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个widget
        self.stacked_layout.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec()



