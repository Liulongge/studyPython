# Qt
        Qt是一个跨平台的C++开发库，主要用来开发图像用户界面程序。PyQt是Python语言的GUI编程解决方案之一，可以用来替代Python内置的Tkinter，其他替代还有PyGTK，wxPython等，与QT一样PyQt是一个自由软件。
        Qt(C++语言GUI)
        PyQt = Python + Qt技术

## Python GUI开发选择
        1.Tkinter
        Python官方采用的标准库，优点是作为Python标准库、稳定、发布程序小，缺点是控件相对较小。
        2.wxPython
        基于wxWidgets的Python库，优点是控件比较丰富，缺点是稳定性相对差点、文档少、用户少。
        3.PySide2、PyQt5
        基于Qt的Python库，优点是控件比较丰富、跨平台体验好、文档完善、用户对。缺点库比较大，发布出来的程序比较大。
        PyQt5的开发者是英国的Riverbank Computing公司，而PySide2则是Qt专门针对Python语言提供的。

## 网址
        https://wiki.python.org/moin/PyQt

## 安装
        conda create -n pyqt python=3.9.16
        pip install pyqt5

## 模块介绍
        QtCore: 包含了核心的非GUI功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件夹、进程与线程一起使用；
        QtGui: 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类；
        QtWidget: 包含了一系列创建桌面应用的UI元素。

   