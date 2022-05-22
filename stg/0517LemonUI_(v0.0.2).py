#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSystemTrayIcon, QMenu, QComboBox, QDialog,
                             QDialogButtonBox, QMenuBar, QFrame, QFileDialog, QPlainTextEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
import PyQt6.QtGui
import sys
import webbrowser
import os
from pathlib import Path

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("lemonicon.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()
action1 = QAction("🧐 Add a dirty word to list!")
menu.addAction(action1)

action4 = QAction("🤔️ Remove a word from list")
menu.addAction(action4)

menu.addSeparator()

action5 = QAction("🆕 Check for Updates")
menu.addAction(action5)

action3 = QAction("ℹ️ About")
menu.addAction(action3)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)


class window0(QWidget):  # 增加说明页面(About)
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):  # 说明页面内信息
        lbl0 = QLabel('Lemon', self)
        lbl0.move(165, 140)

        lbl = QLabel('''

                                        Version 0.0.2

                              This app is open-sourced. 
                        Please do not use it for business.
                                      本软件免费开源，
                                           请勿商用。






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


class CustomDialog(QDialog):  # (About)
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thank you for your support!")

        buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('')

        m1 = QLabel('''
        Thank you for your kind support! 😊
        I will write more interesting apps! 🥳''', self)
        m1.move(10, 190)
        m1.resize(300, 60)

        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('wechat_full.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setGeometry(20, 20, 180, 200)
        l1.setScaledContents(True)

        l2 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('alipay_full.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l2.setGeometry(200, 20, 180, 200)
        l2.setScaledContents(True)

        self.resize(400, 300)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.center()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


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
            fulldir0 = os.path.join(path, 'wordlist.txt')
            a = codecs.open(fulldir0, 'r', encoding='utf-8').read()
            a = str(a)
            a = a.replace('\n', '')
            a = a.replace('\r', '')
            a = a.replace('，，', '，')
            a = a.split('，')
            while '' in a:
                a.remove('')
            self.lbl31.setText('There have been ' + str(len(a)) + ' words on the list.')

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
            self.lbl31.setText('The directory is empty. Please do step 1.')
            self.lbl33.setText('The directory is empty. Please do step 1.')
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
        if fj == '':
            self.lbl31.setText('The directory is empty. Please do step 1.')
            self.lbl33.setText('The directory is empty. Please do step 1.')
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

            title = '''// ==UserScript==
// @name         LemonJuice: A Web Tool for Cleaner Chinese
// @namespace    http://tampermonkey.net/
// @version      0.3
// @description  Let Clean Chinese Refresh Your Eyes! 清除中文互联网页面上的“互联网黑话”、“营销号语言”和各种低幼化词汇。
// @author       Ryan-the-hito
// @match        *://*/*
// @icon         https://github.com/Ryan-the-hito/Avocado/raw/main/image/u1fae3_u1f34b.png
// @grant        none
// @license      MIT
// @run-at       document-end
// ==/UserScript==

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




new MutationObserver(function() {
    walk(document.body);
}).observe(document.body, {
    childList: true
});'''

            with open(fulldir9, 'w', encoding='utf-8') as f:
                f.write(title + '\n\n\t' + zong + '\n\t' + end)


class window2(QWidget):  # 增加更新页面（Check for Updates）
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):  # 说明页面内信息

        lbl = QLabel('Current Version: 0.0.2', self)
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

        btn3 = QPushButton('Search and remove', self)
        btn3.clicked.connect(self.remove)
        btn3.move(225, 237)

        self.lbl3 = QLabel('The results:', self)
        self.lbl3.move(30, 275)

        self.text = QPlainTextEdit(self)
        self.text.setReadOnly(True)
        self.text.move(30, 305)
        self.text.resize(340, 50)

        self.lbl4 = QLabel(self)
        self.lbl4.resize(340, 20)
        self.lbl4.move(30, 360)

        lbl42 = QLabel('Find duplicated Lemons', self)
        lbl42.move(130, 400)
        lbl42.setFont(font)

        btn3 = QPushButton('Search and remove', self)
        btn3.clicked.connect(self.dup)
        btn3.move(133, 420)

        self.text2 = QPlainTextEdit(self)
        self.text2.setReadOnly(True)
        self.text2.move(30, 455)
        self.text2.resize(340, 50)

        self.lbl41 = QLabel(self)
        self.lbl41.resize(340, 20)
        self.lbl41.move(30, 510)

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


w0 = window0()
w1 = window1()
w2 = window2()
w3 = window3()
action1.triggered.connect(w1.activate)
action3.triggered.connect(w0.activate)
action4.triggered.connect(w3.activate)
action5.triggered.connect(w2.activate)
app.exec()
