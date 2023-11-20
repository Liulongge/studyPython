import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QGroupBox, QHBoxLayout, QRadioButton
from PyQt5 import QtCore

# 最外层一个布局器
# 创建group, 显示到布局器1
# 创建group, 显示到布局器2
# 将布局器1/2显示到最外层布局器
# 最外层布局器显示到窗口上
class MyWindow(QWidget):
    def __init__(self):
        # 调用父类的__init__方法，因为它里面有很多对UI空间的初始化操作
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 创建一个布局器，垂直布局
        container = QVBoxLayout()
 
        # ---- 创建第1个组，添加多个组件 ----
        hobby_box = QGroupBox('爱好')
        v_layout = QVBoxLayout()
        btn1 = QRadioButton('抽烟')
        btn2 = QRadioButton('喝酒')
        btn3 = QRadioButton('烫头')
        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        hobby_box.setLayout(v_layout)

        # ---- 创建第2个组，添加多个组件 ----
        # 性别组
        gender_box = QGroupBox('性别')
        # 性别容器
        h_layout = QHBoxLayout()
        # 性别选型
        btn4 = QRadioButton('男')
        btn5 = QRadioButton('女')
        # 追加到性别容器中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 添加到box中
        gender_box.setLayout(h_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示内容是最外层容器
        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = MyWindow()

    w.show()
    app.exec()