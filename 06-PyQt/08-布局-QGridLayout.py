import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('计算器')
        # 准备数据
        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['1', '2', '3', '*', '<-'],
            3: ['', '8', '9', '/', 'C'],
        }
        # 垂直布局
        layout = QVBoxLayout()
        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText('请输入内容')
        # 把输入框放到容器中
        layout.addWidget(edit)

        # 网格布局
        grid = QGridLayout()
        for line_number, line_data in data.items():
            for col_number, number in enumerate(line_data):
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)
        
        # 创建的是widget调用addWidget
        # 创建的是layout调用addLayout
        layout.addLayout(grid)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    app.exec()

