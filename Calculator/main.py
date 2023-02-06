import sys
from PyQt5.QtWidgets import (QApplication, QWidget,     # 애플리케이션 핸들러와 빈 GUI 위젯
                             QPushButton, QVBoxLayout,
                             QMessageBox,               # 메시지 박스 위젯
                             QPlainTextEdit)            # QplainTextEdit 추가

from PyQt5.QtGui import QIcon                           # icon을 추가하기 위한 라이브러리

class Calculator(QWidget): # QWidget 클래스를 상속받아서 클래스를 정의
    def __init__(self):
        super().__init__()  # 부모 클래스 QWidget을 초기화
        self.initUI()       # 나머지 초기화는 initUI함수에 정의

    def initUI(self):
        self.te1 = QPlainTextEdit()     # 텟스트 에디트 위젯 생성
        self.te1.setReadOnly(True)      # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self)        # 버튼 추가
        self.btn1.clicked.connect(self.activateWindow)  # 버튼 클릭시 핸들러 함수 연결

        vbox = QVBoxLayout()        # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)    # 수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addWidget(self.btn1)   # 버튼 위치
        vbox.addStretch(1)          # 빈 공간

        self.setLayout(vbox)        # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')       # 윈도우에 포시되는 타이틀 설정
        self.setWindowIcon(QIcon('icon.png'))   # 윈도우 아이콘 추가
        self.resize(256,256)                    # 윈도우 사이즈
        self.show()                             # 윈도우 화면이 표시되도록 호출

    def activateWindow(self):           # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        #QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

if __name__=='__main__':            # pyqt는 애플리케이션 당 1개의 QApplication이 필요함
    app = QApplication(sys.argv)    # QApplication 인스턴스 생성
    view = Calculator()             # Calculator 위도우 인스턴스 생성
    sys.exit(app.exec_())           # 애플리케이션이 이벤트 처리를 하도록 루프 구동
    