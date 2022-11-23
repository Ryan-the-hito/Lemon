class window2(QWidget):  # 增加更新页面（Check for Updates）
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):  # 说明页面内信息

        lbl = QLabel('Current Version: 1.1.1', self)
        lbl.move(110, 75)

        lbl0 = QLabel('Check Now:', self)
        lbl0.move(30, 20)

        bt1 = QPushButton('Check Github', self)
        bt1.clicked.connect(self.upd)
        bt1.move(110, 15)

        bt2 = QPushButton('Check Baidu Net Disk', self)
        bt2.clicked.connect(self.upd2)
        bt2.move(110, 45)

        self.resize(300, 110)
        self.center()
        self.setWindowTitle('Check for Updates')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def upd(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Lemon/releases')

    def upd2(self):
        webbrowser.open('https://pan.baidu.com/s/1CrsGv1BloyFfU37XF6QYTA?pwd=u0cp')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def activate(self):  # 设置窗口显示
        self.show()

class window3(QWidget):  # Remove a word
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):  # 设置窗口内布局
        self.frame1 = QFrame(self)
        self.frame1.setFrameShape(QFrame.Shape.HLine)
        self.frame1.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame1.setGeometry(25, 0, 350, 340)

        self.frame2 = QFrame(self)
        self.frame2.setFrameShape(QFrame.Shape.HLine)
        self.frame2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame2.setGeometry(25, 0, 350, 780)

        lbl0 = QLabel("Decide your fruit blender", self)
        lbl0.move(120, 25)

        font = PyQt6.QtGui.QFont()
        font.setBold(True)
        lbl0.setFont(font)

        lbl1 = QLabel('''Please download 'f1.txt' to 'f8.txt' as well as 'wordlist.txt'.
If you've done this, please select your folder path.''', self)
        lbl1.move(30, 45)

        btn = QPushButton('Check and download', self)
        btn.clicked.connect(self.chkdnld)
        btn.move(40, 85)

        btn2 = QPushButton('Locate your folder', self)
        btn2.clicked.connect(self.locatefile)
        btn2.move(220, 85)

        lbl11 = QLabel('''The folder path you have decided last time was:''', self)
        lbl11.move(30, 120)

        self.lbl12 = QLabel(self)
        self.lbl12.resize(340, 20)
        self.lbl12.move(30, 140)

        lbl2 = QLabel('Remove a lemon', self)
        lbl2.move(150, 180)
        lbl2.setFont(font)

        lbl21 = QLabel('''Please enter the words (if there are many) below with 
Chinese comma (，) in between:''', self)
        lbl21.move(30, 200)

        self.le1 = QLineEdit(self)
        self.le1.resize(180, 25)
        self.le1.move(30, 240)
        self.le1.setPlaceholderText('Enter your text')
        # self.le1.setStyleSheet("border-radius:10px; border: 1px solid gray;")

        btn3 = QPushButton('Search and remove', self)
        btn3.clicked.connect(self.remove)
        btn3.move(225, 237)

        self.lbl3 = QLabel('The results:', self)
        self.lbl3.move(30, 275)

        self.text = QPlainTextEdit(self)
        self.text.setReadOnly(True)
        self.text.move(30, 305)
        self.text.resize(340, 50) 
        # self.text.setStyleSheet("border-radius:10px; border: 2px groove gray; background-color: transparent")

        self.lbl4 = QLabel(self)
        self.lbl4.resize(340, 20)
        self.lbl4.move(30, 360)

        lbl42 = QLabel('Find duplicated Lemons', self)
        lbl42.move(130, 400)
        lbl42.setFont(font)

        btn3 = QPushButton('Search and remove', self)
        btn3.clicked.connect(self.dup)
        btn3.move(133, 430)

        self.text2 = QPlainTextEdit(self)
        self.text2.setReadOnly(True)
        self.text2.move(30, 475)
        self.text2.resize(340, 50)
        # self.text2.setStyleSheet("border-radius:10px; border: 2px groove gray; background-color: transparent")

        self.lbl41 = QLabel(self)
        self.lbl41.resize(340, 20)
        self.lbl41.move(30, 540)

        qbtn = QPushButton('Cancel', self)
        qbtn.clicked.connect(self.cancel)
        qbtn.move(167, 575)

        self.resize(400, 625)
        self.center()
        self.setWindowTitle('Remove a word from list')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def remove(self):
        fj = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if fj == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            fulldir0 = os.path.join(fj, 'wordlist.txt')
            fulldir1 = os.path.join(fj, 'f1.txt')
            fulldir2 = os.path.join(fj, 'f2.txt')
            fulldir3 = os.path.join(fj, 'f3.txt')
            fulldir4 = os.path.join(fj, 'f4.txt')
            fulldir5 = os.path.join(fj, 'f5.txt')
            fulldir6 = os.path.join(fj, 'f6.txt')
            fulldir7 = os.path.join(fj, 'f7.txt')
            fulldir8 = os.path.join(fj, 'f8.txt')
            a = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            a = str(a)
            a = a.replace('\n', '')
            a = a.replace('\r', '')
            a = a.replace('，，', '，')
            a = a.split('，')
            while '' in a:
                a.remove('')
            self.text.appendPlainText('There have been '+str(len(a))+' words on the list.')

            b = str(self.le1.text())
            b = b.split('，')

            i = 0
            while i >= 0 and i <= len(b) - 1:
                n = 0
                while n >= 0 and n <= len(a) - 1:
                    if b[i] == a[n]:
                        if len(b[i]) == 1:
                            f1 = codecs.open(fulldir1, 'r', encoding='utf-8').read()
                            f1 = f1.split('，')
                            while '' in f1:
                                f1.remove('')
                            while b[i] in f1:
                                f1.remove(b[i])
                            f1 = '，'.join(f1)
                            newf1 = codecs.open(fulldir1, 'w', encoding='utf-8')
                            newf1.write(f1 + '，')
                            newf1.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 2:
                            f2 = codecs.open(fulldir2, 'r', encoding='utf-8').read()
                            f2 = f2.split('，')
                            while '' in f2:
                                f2.remove('')
                            while b[i] in f2:
                                f2.remove(b[i])
                            f2 = '，'.join(f2)
                            newf2 = codecs.open(fulldir2, 'w', encoding='utf-8')
                            newf2.write(f2 + '，')
                            newf2.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 3:
                            f3 = codecs.open(fulldir3, 'r', encoding='utf-8').read()
                            f3 = f3.split('，')
                            while '' in f3:
                                f3.remove('')
                            while b[i] in f3:
                                f3.remove(b[i])
                            f3 = '，'.join(f3)
                            newf3 = codecs.open(fulldir3, 'w', encoding='utf-8')
                            newf3.write(f3 + '，')
                            newf3.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 4:
                            f4 = codecs.open(fulldir4, 'r', encoding='utf-8').read()
                            f4 = f4.split('，')
                            while '' in f4:
                                f4.remove('')
                            while b[i] in f4:
                                f4.remove(b[i])
                            f4 = '，'.join(f4)
                            newf4 = codecs.open(fulldir4, 'w', encoding='utf-8')
                            newf4.write(f4 + '，')
                            newf4.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 5:
                            f5 = codecs.open(fulldir5, 'r', encoding='utf-8').read()
                            f5 = f5.split('，')
                            while '' in f5:
                                f5.remove('')
                            while b[i] in f5:
                                f5.remove(b[i])
                            f5 = '，'.join(f5)
                            newf5 = codecs.open(fulldir5, 'w', encoding='utf-8')
                            newf5.write(f5 + '，')
                            newf5.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 6:
                            f6 = codecs.open(fulldir6, 'r', encoding='utf-8').read()
                            f6 = f6.split('，')
                            while '' in f6:
                                f6.remove('')
                            while b[i] in f6:
                                f6.remove(b[i])
                            f6 = '，'.join(f6)
                            newf6 = codecs.open(fulldir6, 'w', encoding='utf-8')
                            newf6.write(f6 + '，')
                            newf6.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 7:
                            f7 = codecs.open(fulldir7, 'r', encoding='utf-8').read()
                            f7 = f7.split('，')
                            while '' in f7:
                                f7.remove('')
                            while b[i] in f7:
                                f7.remove(b[i])
                            f7 = '，'.join(f7)
                            newf7 = codecs.open(fulldir7, 'w', encoding='utf-8')
                            newf7.write(f7 + '，')
                            newf7.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        if len(b[i]) == 8:
                            f8 = codecs.open(fulldir8, 'r', encoding='utf-8').read()
                            f8 = f8.split('，')
                            while '' in f8:
                                f8.remove('')
                            while b[i] in f8:
                                f8.remove(b[i])
                            f8 = '，'.join(f8)
                            newf8 = codecs.open(fulldir8, 'w', encoding='utf-8')
                            newf8.write(f8 + '，')
                            newf8.close()
                            self.text.appendPlainText(b[i] + ' is found and removed!')
                        n = n + 1
                        continue
                    else:
                        n = n + 1
                        continue
                i = i + 1
                continue

            xf1 = codecs.open(fulldir1, 'r', encoding='utf-8').read()
            xf2 = codecs.open(fulldir2, 'r', encoding='utf-8').read()
            xf3 = codecs.open(fulldir3, 'r', encoding='utf-8').read()
            xf4 = codecs.open(fulldir4, 'r', encoding='utf-8').read()
            xf5 = codecs.open(fulldir5, 'r', encoding='utf-8').read()
            xf6 = codecs.open(fulldir6, 'r', encoding='utf-8').read()
            xf7 = codecs.open(fulldir7, 'r', encoding='utf-8').read()
            xf8 = codecs.open(fulldir8, 'r', encoding='utf-8').read()
            full = xf8 + xf7 + xf6 + xf5 + xf4 + xf3 + xf2 + xf1
            ff = codecs.open(fulldir0, 'w', encoding='utf-8')
            ff.write(full)
            ff.close()
            end = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            end = str(end)
            end = end.replace('\n', '')
            end = end.replace('\r', '')
            end = end.replace('，，', '，')
            end = end.split('，')
            while '' in end:
                end.remove('')
            self.lbl4.setText('There are ' + str(len(end)) + ' words on the list now.')
            self.le1.clear()

    def dup(self):
        fj = codecs.open('path.txt', 'r', encoding='utf-8').read()
        fulldir0 = os.path.join(fj, 'wordlist.txt')
        fulldir1 = os.path.join(fj, 'f1.txt')
        fulldir2 = os.path.join(fj, 'f2.txt')
        fulldir3 = os.path.join(fj, 'f3.txt')
        fulldir4 = os.path.join(fj, 'f4.txt')
        fulldir5 = os.path.join(fj, 'f5.txt')
        fulldir6 = os.path.join(fj, 'f6.txt')
        fulldir7 = os.path.join(fj, 'f7.txt')
        fulldir8 = os.path.join(fj, 'f8.txt')
        if fj == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            a = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            a = str(a)
            a = a.replace('\n', '')
            a = a.replace('\r', '')
            a = a.replace('，，', '，')
            a = a.split('，')
            while '' in a:
                a.remove('')
            self.text2.appendPlainText('There have been '+str(len(a))+' words on the list.')

            b = []

            i = 0
            while i >= 0 and i <= len(a) - 1:
                n = 0
                while n >= 0 and n <= len(a) - 1:
                    if a[i] == a[n] and i != n:
                        if len(a[i]) == 1:
                            f1 = codecs.open(fulldir1, 'r', encoding='utf-8').read()
                            f1 = f1.split('，')
                            while '' in f1:
                                f1.remove('')
                            if a[i] not in b:
                                while a[i] in f1:
                                    f1.remove(a[i])
                                f1 = '，'.join(f1)
                                newf1 = codecs.open(fulldir1, 'w', encoding='utf-8')
                                newf1.write(f1+'，')
                                newf1.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 2:
                            f2 = codecs.open(fulldir2, 'r', encoding='utf-8').read()
                            f2 = f2.split('，')
                            while '' in f2:
                                f2.remove('')
                            if a[i] not in b:
                                while a[i] in f2:
                                    f2.remove(a[i])
                                f2 = '，'.join(f2)
                                newf2 = codecs.open(fulldir2, 'w', encoding='utf-8')
                                newf2.write(f2+'，')
                                newf2.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 3:
                            f3 = codecs.open(fulldir3, 'r', encoding='utf-8').read()
                            f3 = f3.split('，')
                            while '' in f3:
                                f3.remove('')
                            if a[i] not in b:
                                while a[i] in f3:
                                    f3.remove(a[i])
                                f3 = '，'.join(f3)
                                newf3 = codecs.open(fulldir3, 'w', encoding='utf-8')
                                newf3.write(f3+'，')
                                newf3.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 4:
                            f4 = codecs.open(fulldir4, 'r', encoding='utf-8').read()
                            f4 = f4.split('，')
                            while '' in f4:
                                f4.remove('')
                            if a[i] not in b:
                                while a[i] in f4:
                                    f4.remove(a[i])
                                f4 = '，'.join(f4)
                                newf4 = codecs.open(fulldir4, 'w', encoding='utf-8')
                                newf4.write(f4+'，')
                                newf4.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 5:
                            f5 = codecs.open(fulldir5, 'r', encoding='utf-8').read()
                            f5 = f5.split('，')
                            while '' in f5:
                                f5.remove('')
                            if a[i] not in b:
                                while a[i] in f5:
                                    f5.remove(a[i])
                                f5 = '，'.join(f5)
                                newf5 = codecs.open(fulldir5, 'w', encoding='utf-8')
                                newf5.write(f5+'，')
                                newf5.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 6:
                            f6 = codecs.open(fulldir6, 'r', encoding='utf-8').read()
                            f6 = f6.split('，')
                            while '' in f6:
                                f6.remove('')
                            if a[i] not in b:
                                while a[i] in f6:
                                    f6.remove(a[i])
                                f6 = '，'.join(f6)
                                newf6 = codecs.open(fulldir6, 'w', encoding='utf-8')
                                newf6.write(f6+'，')
                                newf6.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 7:
                            f7 = codecs.open(fulldir7, 'r', encoding='utf-8').read()
                            f7 = f7.split('，')
                            while '' in f7:
                                f7.remove('')
                            if a[i] not in b:
                                while a[i] in f7:
                                    f7.remove(a[i])
                                f7 = '，'.join(f7)
                                newf7 = codecs.open(fulldir7, 'w', encoding='utf-8')
                                newf7.write(f7+'，')
                                newf7.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        if len(a[i]) == 8:
                            f8 = codecs.open(fulldir8, 'r', encoding='utf-8').read()
                            f8 = f8.split('，')
                            while '' in f8:
                                f8.remove('')
                            if a[i] not in b:
                                while a[i] in f8:
                                    f8.remove(a[i])
                                f8 = '，'.join(f8)
                                newf8 = codecs.open(fulldir8, 'w', encoding='utf-8')
                                newf8.write(f8+'，')
                                newf8.close()
                                b.append(a[i])
                                self.text2.appendPlainText(a[i]+' is found duplicated and removed!')
                        n = n + 1
                        continue
                    else:
                        n = n + 1
                        continue
                i = i + 1
                continue

            i = 0
            while i >= 0 and i <= len(b) - 1:
                if len(b[i]) == 1:
                    f1 = codecs.open(fulldir1, 'a', encoding='utf-8')
                    f1.write(str(b[i])+'，')
                    f1.close()
                    i = i + 1
                    continue
                if len(b[i]) == 2:
                    f2 = codecs.open(fulldir2, 'a', encoding='utf-8')
                    f2.write(str(b[i])+'，')
                    f2.close()
                    i = i + 1
                    continue
                if len(b[i]) == 3:
                    f3 = codecs.open(fulldir3, 'a', encoding='utf-8')
                    f3.write(str(b[i])+'，')
                    f3.close()
                    i = i + 1
                    continue
                if len(b[i]) == 4:
                    f4 = codecs.open(fulldir4, 'a', encoding='utf-8')
                    f4.write(str(b[i])+'，')
                    f4.close()
                    i = i + 1
                    continue
                if len(b[i]) == 5:
                    f5 = codecs.open(fulldir5, 'a', encoding='utf-8')
                    f5.write(str(b[i])+'，')
                    f5.close()
                    i = i + 1
                    continue
                if len(b[i]) == 6:
                    f6 = codecs.open(fulldir6, 'a', encoding='utf-8')
                    f6.write(str(b[i])+'，')
                    f6.close()
                    i = i + 1
                    continue
                if len(b[i]) == 7:
                    f7 = codecs.open(fulldir7, 'a', encoding='utf-8')
                    f7.write(str(b[i])+'，')
                    f7.close()
                    i = i + 1
                    continue
                if len(b[i]) >= 8:
                    f8 = codecs.open(fulldir8, 'a', encoding='utf-8')
                    f8.write(str(b[i])+'，')
                    f8.close()
                    i = i + 1
                    continue

            xf1 = codecs.open(fulldir1, 'r', encoding='utf-8').read()
            xf2 = codecs.open(fulldir2, 'r', encoding='utf-8').read()
            xf3 = codecs.open(fulldir3, 'r', encoding='utf-8').read()
            xf4 = codecs.open(fulldir4, 'r', encoding='utf-8').read()
            xf5 = codecs.open(fulldir5, 'r', encoding='utf-8').read()
            xf6 = codecs.open(fulldir6, 'r', encoding='utf-8').read()
            xf7 = codecs.open(fulldir7, 'r', encoding='utf-8').read()
            xf8 = codecs.open(fulldir8, 'r', encoding='utf-8').read()
            full = xf8 + xf7 + xf6 + xf5 + xf4 + xf3 + xf2 + xf1
            ff = codecs.open(fulldir0, 'w', encoding='utf-8')
            ff.write(full)
            ff.close()
            end = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            end = str(end)
            end = end.replace('\n', '')
            end = end.replace('\r', '')
            end = end.replace('，，', '，')
            end = end.split('，')
            while '' in end:
                end.remove('')
            self.lbl41.setText('There are '+str(len(end))+' words on the list now.')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def cancel(self):  # 设置取消键的功能
        self.text.clear()
        self.text2.clear()
        self.lbl4.clear()
        self.lbl41.clear()
        self.close()

    def activate(self):  # 设置窗口显示
        self.show()
        path = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if path == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            self.lbl12.setText(path)
            self.lbl12.setStyleSheet('color:black')

    def chkdnld(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Lemon/releases')

    def locatefile(self):
        home_dir = str(Path.home())
        fj = QFileDialog.getExistingDirectory(self, 'Open', home_dir)
        pathfile = codecs.open('path.txt', 'w', encoding='utf-8')
        pathfile.write(fj)
        pathfile.close()
        path = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if path == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            self.lbl12.setText(path)
            self.lbl12.setStyleSheet('color:black')

class window4(QWidget):  # Customization settings
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):  # 设置窗口内布局
        self.frame1 = QFrame(self)
        self.frame1.setFrameShape(QFrame.Shape.HLine)
        self.frame1.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame1.setGeometry(25, 0, 350, 340)

        self.frame2 = QFrame(self)
        self.frame2.setFrameShape(QFrame.Shape.HLine)
        self.frame2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame2.setGeometry(25, 0, 350, 780)

        lbl0 = QLabel("Erase your path", self)
        lbl0.move(150, 25)

        font = PyQt6.QtGui.QFont()
        font.setBold(True)
        lbl0.setFont(font)

        lbl1 = QLabel('''This function will help if you want to fully restore your
folder path.''', self)
        lbl1.move(30, 45)

        btn = QPushButton('Erase', self)
        btn.clicked.connect(self.eras)
        btn.move(167, 85)

        lbl11 = QLabel('''The folder path you have decided last time was:''', self)
        lbl11.move(30, 120)

        self.lbl12 = QLabel(self)
        self.lbl12.resize(340, 20)
        self.lbl12.move(30, 140)

        lbl2 = QLabel('Replacement customization', self)
        lbl2.move(110, 180)
        lbl2.setFont(font)

        lbl21 = QLabel('''Please enter the words (if there are many) below with 
Tab in between and line breaks after: (the first is to be 
replaced by the latter)''', self)
        lbl21.move(30, 200)

        self.text = QPlainTextEdit(self)
        self.text.setReadOnly(False)
        self.text.move(30, 255)
        self.text.resize(340, 100)
        # mttxt = codecs.open('replacement.txt', 'r', encoding='utf-8').read()
        # self.text.setPlainText(mttxt)

        btn2 = QPushButton('Save', self)
        btn2.clicked.connect(self.rep_cus)
        btn2.move(170, 357)

        lbl3 = QLabel('Applied websites', self)
        lbl3.move(145, 400)
        lbl3.setFont(font)

        lbl31 = QLabel('''Please enter the websites (if there are many) below with 
line breaks after each one:''', self)
        lbl31.move(30, 420)

        self.text2 = QPlainTextEdit(self)
        self.text2.setReadOnly(False)
        self.text2.move(30, 460)
        self.text2.resize(340, 80)
        # etted = codecs.open('match.txt', 'r', encoding='utf-8').read()
        # self.text2.setPlainText(etted)

        btn3 = QPushButton('Save', self)
        btn3.clicked.connect(self.dup_save)
        btn3.move(170, 545)

        qbtn = QPushButton('Cancel', self)
        qbtn.clicked.connect(self.cancel)
        qbtn.move(165, 575)

        self.resize(400, 625)
        self.center()
        self.setWindowTitle('Customization settings')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def cancel(self):  # 设置取消键的功能
        self.close()

    def activate(self):  # 设置窗口显示
        self.show()
        path = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if path == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            self.lbl12.setText(path)
            self.lbl12.setStyleSheet('color:black')
            fulldir_r = os.path.join(path, 'replacement.txt')
            fulldir_m = os.path.join(path, 'match.txt')
            mttxt = codecs.open(fulldir_r, 'r', encoding='utf-8').read()
            self.text.setPlainText(mttxt)
            etted = codecs.open(fulldir_m, 'r', encoding='utf-8').read()
            self.text2.setPlainText(etted)

    def eras(self):
        pathfile = codecs.open('path.txt', 'w', encoding='utf-8')
        pathfile.write('')
        pathfile.close()
        path = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if path == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
            self.text.clear()
            self.text2.clear()
        else:
            self.lbl12.setText(path)
            self.lbl12.setStyleSheet('color:black')

    def rep_cus(self):
        fj = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if fj == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            fulldir_r = os.path.join(fj, 'replacement.txt')
            mttxt = codecs.open(fulldir_r, 'w', encoding='utf-8')
            mttxt.write(self.text.toPlainText())
            mttxt.close()
            self.close()

    def dup_save(self):
        fj = codecs.open('path.txt', 'r', encoding='utf-8').read()
        if fj == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            fulldir_m = os.path.join(fj, 'match.txt')
            etted = codecs.open(fulldir_m, 'w', encoding='utf-8')
            etted.write(self.text2.toPlainText())
            etted.close()
            self.close()