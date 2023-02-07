class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def calculate(self):
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)  # 버튼 1 연결을 변경
        self.view.btn2.clicked.connect(self.view.clearWindow)    # 버튼2 핸들러 함수 연결
