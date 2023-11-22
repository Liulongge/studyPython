
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class MyWindow(QWidget):
    # 声明一个信号，只能放在函数的外面
    # pyqt的信号只能放在类属性里面定义，不能放在方法中定义
    my_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.init_ui()
        # 用来存放消息
        self.msg_history = list()

    def init_ui(self):
        self.resize(500, 500)
        # 创建一个横踢布局器
        container = QVBoxLayout()
        # 用来显示检测到漏洞的信息
        self.msg = QLabel('')
        self.msg.resize(440, 15)
        # 自动换行
        self.msg.setWordWrap(True)
        # 靠上
        self.msg.setAlignment(Qt.AlignTop)
        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)
        # 创建垂直布局器，用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)
        # 创建水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton('开始检测', self)
        btn.clicked.connect(self.click_my_button)
        # 伸缩器
        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 操作将要显示的控件以及子布局器添加到container
        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 设置布局器
        self.setLayout(container)
        # 绑定信号与槽
        self.my_signal.connect(self.my_slot)


    def my_slot(self, msg):
        # print('num: {}'.format(msg))
        self.msg_history.append(msg)
        self.msg.setText('<br/>'.join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)
        # 更新内容，如果不更新可能没有显示新内筒
        self.msg.repaint()

    def click_my_button(self):
        print('点击按钮啦~')
        for i in range(20):
            time.sleep(0.01)
            self.my_signal.emit(str(i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()