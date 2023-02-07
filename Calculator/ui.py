from PyQt5.QtWidgets import (QApplication, QWidget,     # 애플리케이션 핸들러와 빈 GUI 위젯
                             QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox)

from PyQt5.QtGui import QIcon                           # icon을 추가하기 위한 라이브러리
from PyQt5.QtCore import Qt

class View(QWidget):
    def __init__(self):
        super().__init__()  # 부모 클래스 QWidget을 초기화
        self.initUI()       # 나머지 초기화는 initUI함수에 정의

    def initUI(self):
        self.te1 = QPlainTextEdit()     # 텟스트 에디트 위젯 생성
        self.te1.setReadOnly(True)      # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.le1=QLineEdit('0', self)
        self.le1.setAlignment(Qt.AlignRight)
        self.le1.setFocus(True)         # 포커스 설정
        self.le1.selectAll()            # 텍스트 전체 선택

        self.le2=QLineEdit('0', self)
        self.le2.setAlignment(Qt.AlignRight)

        self.cb=QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/'])

        hbox_fomular = QHBoxLayout()
        hbox_fomular.addWidget(self.le1)
        hbox_fomular.addWidget(self.cb)
        hbox_fomular.addWidget(self.le2)

        self.btn1 = QPushButton('Calc', self)        # 버튼 이름 변경
        self.btn2 = QPushButton('Clear', self)          # 버튼2 추가

        hbox = QHBoxLayout()
        hbox.addStretch(1)          # 공백
        hbox.addWidget(self.btn1)   # 버튼1 배치
        hbox.addWidget(self.btn2)   # 버튼2 배치

        vbox = QVBoxLayout()        # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)    # 수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addLayout(hbox_fomular)
        vbox.addLayout(hbox)        # btn1 위치에 hbox를 배치
        vbox.addStretch(1)          # 빈 공간

        self.setLayout(vbox)        # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')       # 윈도우에 포시되는 타이틀 설정
        self.setWindowIcon(QIcon('icon.png'))   # 윈도우 아이콘 추가
        self.resize(256,256)                    # 윈도우 사이즈
        self.show()                             # 윈도우 화면이 표시되도록 호출

    def setDisplay(self):           # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        self.te1.appendPlainText("Button clicked!")

    def clearWindow(self):
        self.te1.clear()
