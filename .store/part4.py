
                © 2022 Ryan-the-hito. All rights reserved.
                ''', self)
        lbl.move(20, 135)

        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('lemonicon.icns')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setGeometry(150, 40, 100, 100)
        l1.setScaledContents(True)

        bt1 = QPushButton('The Author', self)
        bt1.clicked.connect(self.intro)
        bt1.move(205, 280)

        bt2 = QPushButton('Github Page', self)
        bt2.clicked.connect(self.homepage)
        bt2.move(100, 280)

        bt3 = QPushButton('Buy me a cup of coffee ☕', self)
        bt3.clicked.connect(self.donate)
        bt3.move(110, 310)

        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(20)
        lbl0.setFont(font)

        self.resize(400, 380)
        self.center()
        self.setWindowTitle('About')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def intro(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

    def homepage(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Lemon')

    def donate(self):
        dlg = CustomDialog()
        dlg.exec()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def activate(self):  # 设置窗口显示
        self.show()