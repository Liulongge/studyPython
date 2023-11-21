
# 信号与槽是Qt核心内容
# 1、信号(signal)
# 其实就是事件(按钮点击，内容发生变化，窗口的关闭事件)或是状态(check选中了，togglebutton切换)
# 当程序触发了某种事件(比如：按钮被点击了，内容改变等等)，那么即可发生出来一个信号
# 2、槽(slot)
# 若想捕获这个信号，然后执行相应的逻辑代码，那么就需要使用到槽，槽实际上是一个函数，的那个信号发射出来后，汇之星与之绑定的槽函数
# 3、将信号与槽连接
# 为了能够实现，当点击某个按钮，需要把具体的信号和具体的草函数绑定在一起
# 操作大体如下：对象.信号.connect(槽函数)

import sys
import time
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSignal
class MyWindow(QWidget):
    # 声明一个信号，只能放在函数的外面
    # pyqt的信号只能放在类属性里面定义，不能放在方法中定义
    my_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 500)
        btn = QPushButton('点我', self)
        btn.setGeometry(200, 200, 100, 30)
        # 绑定按钮的点击，点击按钮则开始检测
        btn.clicked.connect(self.click_my_button)
        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)
    
    def my_slot(self, msg):
        print('num: {}'.format(msg))

    def click_my_button(self):
        print('点击按钮啦~')
        for i in range(10):
            time.sleep(0.1)
            self.my_signal.emit(str(i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()