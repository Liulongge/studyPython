import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('QLable控件')

    # 创建QLable组件

    # 1.创建时带父亲
    label = QLabel('账号:', w)
    # 2.创建时不带父亲
    # label = QLabel('账号:')
    # label.setParent(w)

    # 设置显示位置与大小：x, y, w, h
    label.setGeometry(20, 20, 400, 400)

    w.show()

    app.exec()

