import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QLabel

class window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉1要显示的内容', self)
        self.setStyleSheet('background-color:green;')

class window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉2要显示的内容', self)
        self.setStyleSheet('background-color:red;')


class window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        self.stacked_layout = QStackedLayout()
        win1 = window1()
        win2 = window2()

        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        self.setFixedSize(300, 270)
        container = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet('background-color:gray;')

        btn_press1 = QPushButton('抽屉1')
        btn_press2 = QPushButton('抽屉2')
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)

        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        self.setLayout(container)
        



