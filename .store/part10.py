w0 = window0()
w1 = window1()
w2 = window2()
w3 = window3()
w4 = window4()
action1.triggered.connect(w1.activate)
action3.triggered.connect(w0.activate)
action4.triggered.connect(w3.activate)
action5.triggered.connect(w2.activate)
action6.triggered.connect(w4.activate)
app.setStyleSheet(style_sheet)
app.exec()
