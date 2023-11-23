
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import QThread
from PyQt5 import uic
import time
from PyQt5.QtCore import pyqtSignal
import json

class LoginThread(QThread):
    start_login_signal = pyqtSignal(str)
    def __init__(self):
       super().__init__()

    def login_by_requests(self, user_password_json):
        user_password_json = json.loads(user_password_json)
        print(user_password_json.get('user_name'))
        print(user_password_json.get('password'))

    def run(self):
        # 通过while True的方式让子线程一直在运行，而不是结束
        # 通过这种方式，我们让子线程一直活着，从而有能力接受来自主线程(UI线程)的任务
        while True:
            print('子线程正在执行......')
            time.sleep(1)
 
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.ui = uic.loadUi('./login.ui')

        self.user_name_Qwidget = self.ui.lineEdit
        self.password_Qwidget = self.ui.lineEdit_2
        self.login_btn = self.ui.pushButton
        self.forget_password_btn = self.ui.pushButton_2
        self.textBrowser = self.ui.textBrowser

        self.login_btn.clicked.connect(self.login)
        self.login_thread = LoginThread()
        # 将要创建的线程与
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        # 让子线程开始工作
        self.login_thread.start()

    def login(self):
        # 登录按钮的槽函数
        user_name = self.user_name_Qwidget.text()
        password = self.password_Qwidget.text()
        self.login_thread.start_login_signal.emit(json.dumps({'user_name' : user_name, 'password' : password}))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()