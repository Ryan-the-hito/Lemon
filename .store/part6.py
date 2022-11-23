class window1(QWidget):  # 主程序的代码块（Find a dirty word!）
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
        self.frame2.setGeometry(25, 0, 350, 880)

        lbl0 = QLabel("1. Get your fruit blender", self)
        lbl0.move(120, 25)

        font = PyQt6.QtGui.QFont()
        font.setBold(True)
        lbl0.setFont(font)

        lbl1 = QLabel('''Please download 'f1.txt' to 'f8.txt' as well as 'wordlist.txt',
and store them in a target folder.''', self)
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

        lbl2 = QLabel('2. Put lemons in!!', self)
        lbl2.move(140, 180)
        lbl2.setFont(font)

        lbl3 = QLabel('''Please enter the words (if there are many) below with 
Chinese comma (，) in between:''', self)
        lbl3.move(30, 200)

        self.le1 = QLineEdit(self)
        self.le1.resize(340, 25)
        self.le1.move(30, 240)
        self.le1.setPlaceholderText('Enter your text')
        # self.le1.setStyleSheet("border-radius:10px; border: 1px solid gray;")

        btn3 = QPushButton('Check and update the list', self)
        btn3.clicked.connect(self.findadd)
        btn3.move(110, 275)

        self.lbl30 = QLabel('The results:', self)
        self.lbl30.move(30, 310)

        self.lbl31 = QLabel(self)
        self.lbl31.resize(340, 20)
        self.lbl31.move(30, 330)

        self.text = QPlainTextEdit(self)
        self.text.setReadOnly(True)
        self.text.move(30, 355)
        self.text.resize(340, 50)
        # self.text.setStyleSheet("border-radius:10px; border: 2px groove gray; background-color: transparent")
        '''palette = self.text.palette()
        palette.setBrush(QPalette.Window, QBrush(Qt.transparent))
        self.text.setPalette(palette)'''

        self.lbl33 = QLabel(self)
        self.lbl33.resize(340, 20)
        self.lbl33.move(30, 410)

        lbl4 = QLabel("3. Let's make lemon juice!", self)
        lbl4.move(120, 450)
        lbl4.setFont(font)

        btn4 = QPushButton('Generate .js file', self)
        btn4.clicked.connect(self.makejs)
        btn4.move(140, 475)

        lbl5 = QLabel('''The .js file will be generated. Please check the folder you 
set just now, and install it to your browser with a container 
in browser (e.g. Tampermonkey) installed first.''', self)
        lbl5.move(30, 510)

        qbtn = QPushButton('Cancel', self)
        qbtn.clicked.connect(self.cancel)
        qbtn.move(167, 575)

        self.resize(400, 625)
        self.center()
        self.setWindowTitle('Add a dirty word to list')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def chkdnld(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Lemon/releases')

    def locatefile(self):
        home_dir = str(Path.home())
        fj = QFileDialog.getExistingDirectory(self, 'Open', home_dir)
        pathfile = codecs.open('path.txt', 'w', encoding='utf-8')
        pathfile.write(fj)
        pathfile.close()
        path = codecs.open('path.txt', 'r', encoding='utf-8').read()
        fulldir0 = os.path.join(path, 'wordlist.txt')
        if path == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            self.lbl12.setText(path)
            self.lbl12.setStyleSheet('color:black')
            a = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            a = str(a)
            a = a.replace('\n', '')
            a = a.replace('\r', '')
            a = a.replace('，，', '，')
            a = a.split('，')
            while '' in a:
                a.remove('')
            self.lbl31.setText('There have been ' + str(len(a)) + ' words on the list.')
            self.lbl33.clear()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
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

    def cancel(self):  # 设置取消键的功能
        self.text.clear()
        self.lbl31.clear()
        self.lbl33.clear()
        self.close()

    def findadd(self):
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
            self.lbl31.setText('There have been ' + str(len(a)) + ' words on the list.')

            b = str(self.le1.text())
            b = b.split('，')

            c = []

            i = 0
            while i >= 0 and i <= len(b) - 1:
                n = 0
                while n >= 0 and n <= len(a) - 1:
                    if b[i] == a[n]:
                        self.text.appendPlainText(b[i] + ' is already on the list!')
                        c.append(str(i))
                        n = n + 1
                        continue
                    else:
                        n = n + 1
                        continue
                i = i + 1
                continue

            m = 0
            while m >= 0 and m <= len(c) - 1:
                shan = int(c[m])
                b[shan] = ''
                m = m + 1
                continue
            while '' in b:
                b.remove('')
            b = sorted(b, key=lambda i: len(i), reverse=False)

            i = 0
            while i >= 0 and i <= len(b) - 1:
                if len(b[i]) == 1:
                    f1 = codecs.open(fulldir1, 'a', encoding='utf-8')
                    f1.write(str(b[i]) + '，')
                    f1.close()
                    i = i + 1
                    continue
                if len(b[i]) == 2:
                    f2 = codecs.open(fulldir2, 'a', encoding='utf-8')
                    f2.write(str(b[i]) + '，')
                    f2.close()
                    i = i + 1
                    continue
                if len(b[i]) == 3:
                    f3 = codecs.open(fulldir3, 'a', encoding='utf-8')
                    f3.write(str(b[i]) + '，')
                    f3.close()
                    i = i + 1
                    continue
                if len(b[i]) == 4:
                    f4 = codecs.open(fulldir4, 'a', encoding='utf-8')
                    f4.write(str(b[i]) + '，')
                    f4.close()
                    i = i + 1
                    continue
                if len(b[i]) == 5:
                    f5 = codecs.open(fulldir5, 'a', encoding='utf-8')
                    f5.write(str(b[i]) + '，')
                    f5.close()
                    i = i + 1
                    continue
                if len(b[i]) == 6:
                    f6 = codecs.open(fulldir6, 'a', encoding='utf-8')
                    f6.write(str(b[i]) + '，')
                    f6.close()
                    i = i + 1
                    continue
                if len(b[i]) == 7:
                    f7 = codecs.open(fulldir7, 'a', encoding='utf-8')
                    f7.write(str(b[i]) + '，')
                    f7.close()
                    i = i + 1
                    continue
                if len(b[i]) >= 8:
                    f8 = codecs.open(fulldir8, 'a', encoding='utf-8')
                    f8.write(str(b[i]) + '，')
                    f8.close()
                    i = i + 1
                    continue

            f1 = codecs.open(fulldir1, 'r', encoding='utf-8').read()
            f2 = codecs.open(fulldir2, 'r', encoding='utf-8').read()
            f3 = codecs.open(fulldir3, 'r', encoding='utf-8').read()
            f4 = codecs.open(fulldir4, 'r', encoding='utf-8').read()
            f5 = codecs.open(fulldir5, 'r', encoding='utf-8').read()
            f6 = codecs.open(fulldir6, 'r', encoding='utf-8').read()
            f7 = codecs.open(fulldir7, 'r', encoding='utf-8').read()
            f8 = codecs.open(fulldir8, 'r', encoding='utf-8').read()
            full = f8 + f7 + f6 + f5 + f4 + f3 + f2 + f1
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
            self.lbl33.setText('There are ' + str(len(end)) + ' words on the list now.')
        self.le1.clear()

    def makejs(self):
        fj = codecs.open('path.txt', 'r', encoding='utf-8').read()
        fulldir0 = os.path.join(fj, 'wordlist.txt')
        fulldir9 = os.path.join(fj, 'LemonJuice.js')
        fulldir_r = os.path.join(fj, 'replacement.txt')
        fulldir_m = os.path.join(fj, 'match.txt')
        if fj == '':
            self.lbl12.setText('The directory is empty. Please check!')
            self.lbl12.setStyleSheet('color:red')
        else:
            zong = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            zong = str(zong)
            zong = zong.replace('\n', '')
            zong = zong.replace('\r', '')
            zong = zong.replace('，，', '，')
            zong = zong.split('，')
            while '' in zong:
                zong.remove('')

            i = 0
            while i >= 0 and i <= len(zong) - 1:
                zong[i] = 'v = v.replace("', zong[i], '", "*");', '\n\t'
                zong[i] = ''.join(zong[i])
                i += 1
                continue

            zong = ''.join(zong)

            ax = codecs.open(fulldir_r, 'r', encoding='utf-8').readlines()

            nx = []
            for i in range(len(ax)):
                ax[i] = ax[i].replace('\n', '')
                nx.append(ax[i].split('\t'))

            te = []
            for i in range(len(nx)):
                te.append(nx[i])
            for i in range(len(te)):
                te[i] = 'v = v.replace("', te[i][0], '", "*")'
                te[i] = ''.join(te[i])

            ce = []
            for i in range(len(nx)):
                ce.append(nx[i])
            for i in range(len(ce)):
                ce[i] = 'v = v.replace("', ce[i][0], '", "', ce[i][1], '")'
                ce[i] = ''.join(ce[i])

            for i in range(len(ax)):
                zong = zong.replace(te[i], ce[i])

            mt = codecs.open(fulldir_m, 'r', encoding='utf-8').readlines()

            newma = []
            for i in range(len(mt)):
                mt[i] = mt[i].replace('\n', '')
                newma.append(mt[i])

            for i in range(len(newma)):
                newma[i] = '// @match        ', newma[i]
                newma[i] = ''.join(newma[i])

            endmatch = '\n'.join(newma)

            title = '''// ==UserScript==
// @name         LemonJuice: A Web Tool for Cleaner Chinese
// @namespace    http://tampermonkey.net/
// @version      0.3
// @description  Let Clean Chinese Refresh Your Eyes! 清除中文互联网页面上的“互联网黑话”、“营销号语言”和各种低幼化词汇。
// @author       Ryan-the-hito and everybody
// @icon         https://github.com/Ryan-the-hito/Avocado/raw/main/image/u1fae3_u1f34b.png
// @grant        「Pickle 腌黄瓜」from 脏嘻嘻翻译器
// @license      MIT
// @run-at       document-end'''
            head = '''// ==/UserScript==

function walk(node)
{
    var child, next;

    switch ( node.nodeType )
    {
        case 1:  // Element
        case 9:  // Document
        case 11: // Document fragment
            child = node.firstChild;
            while ( child )
            {
                next = child.nextSibling;
                walk(child);
                child = next;
            }
            break;

        case 3: // Text node
            handleText(node);
            break;
    }
}

function handleText(textNode)
{
    var v = textNode.nodeValue;'''
            end = '''textNode.nodeValue = v;
}

walk(document.body);