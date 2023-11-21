
# 一、分类
# 在Qt中，生成窗口有三种方式：QWidget | QMainWindow | QDialog
# 1、QWidget
# 控件和窗口的父类，自由度高(什么东西都没有)，没有划分菜单、工具栏、状态栏、主窗口等区域
# 2、QMainWindow
# 是QWidget的子类，包含菜单栏、状态栏、标题栏等，中间部分则为主窗口区域
# 3、QDialog
# 对话框窗口的基类
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('这是一个文字~~')
        label.setStyleSheet('font-size:30px;color:red')

        # 调用父类中的menuBar，从而对菜单栏进行操作
        menu = self.menuBar()
        # 如果Mac的话，菜单栏不会在Window中显示二十屏幕顶部系统菜单位置
        # 下面一行代码是的Mac也按照Windows的那种方式在Window中显示Menu
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu('文件')
        file_menu.addMenu('打开')
        file_menu.addMenu('保存')

        edit_mune = menu.addMenu('编辑')
        edit_mune.addMenu('复制')
        edit_mune.addMenu('粘贴')
        edit_mune.addMenu('剪切')

        # 设置中心内容显示
        self.setCentralWidget(label)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()