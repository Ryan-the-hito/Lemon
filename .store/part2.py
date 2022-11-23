class window0(QWidget):  # 增加说明页面(About)
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):  # 说明页面内信息
        lbl0 = QLabel('Lemon', self)
        lbl0.move(165, 140)

        lbl = QLabel('''

                                        Version 1.1.1

                              This app is open-sourced. 
                        Please do not use it for business.
                                      本软件免费开源，
                                           请勿商用。