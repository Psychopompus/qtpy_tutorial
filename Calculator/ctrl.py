class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def generate(self):
        pass

    def connectSignals(self):
        self.view.inputEdit.returnPressed.connect(self.view.setDisplay)
        self.view.btnInsert.clicked.connect(self.view.insertData)
