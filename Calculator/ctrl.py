class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateWindow)  # 버튼 클릭시 핸들러 함수 연결
        self.view.btn2.clicked.connect(self.view.clearWindow)    # 버튼2 핸들러 함수 연결
