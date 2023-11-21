
# 一、分类
# 在Qt中，生成窗口有三种方式：QWidget | QMainWindow | QDialog
# 1、QWidget
# 控件和窗口的父类，自由度高(什么东西都没有)，没有划分菜单、工具栏、状态栏、主窗口等区域
# 2、QMainWindow
# 是QWidget的子类，包含菜单栏、状态栏、标题栏等，中间部分则为主窗口区域
# 3、QDialog
# 对话框窗口的基类
# 对话框一般不应该作为主窗口存在，而是通过点击操作弹出，起到提示作用

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton('确定', self)
        ok_btn.setGeometry(50, 50, 100, 30)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('对话框')
    w.show()
    app.exec()