
# 纯靠代码编写界面，效率有点低，可以使用辅助设计图形化页面Qt Designer
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        # self.setWindowTitle('login')
        self.ui = uic.loadUi('./login.ui')
        print(self.ui) # ui文件找你最顶层的对象(Form)
        print(self.ui.__dir__) # 最顶层对象的所有属性(key:value)
        print(self.ui.label) # 最顶层对象嵌套的QLabel
        print(self.ui.label.text()) # 最顶层对象中嵌套的QLabel的文本
        self.user_name = self.ui.lineEdit # 用户名输入框
        self.password = self.ui.lineEdit_2 # 密码输入框
        self.login_btn = self.ui.pushButton # 登录按钮
        self.forget_btn = self.ui.pushButton_2 # 忘记密码按钮
        self.text_browser = self.ui.textBrowser # 文本提示区域

        # 给登录按钮被点击绑定函数
        self.login_btn.clicked.connect(self.login)

    def login(self):
        # 实现登录逻辑
        print('正在登录......')
        # 获取用户名和密码
        user_name = self.user_name.text()
        password = self.password.text()
        print('用户名: {}'.format(user_name))
        print('密码: {}'.format(password))
        if user_name == 'admin' and password == 'admin':
            self.text_browser.setText('欢迎{}'.format(user_name))
            self.text_browser.repaint()
        else:
            self.text_browser.setText('用户名或密码错误...请重试')
            self.text_browser.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MyWindow()
    w.ui.show()
    app.exec()