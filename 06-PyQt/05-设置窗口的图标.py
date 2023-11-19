# 不生效
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()
    w.setWindowTitle('设置窗口的图标')

    w.setWindowIcon(QIcon('./icon.jpg'))

    w.show()
    app.exec()