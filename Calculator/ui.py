from PyQt5.QtWidgets import (QApplication, QWidget,  # 애플리케이션 핸들러와 빈 GUI 위젯
                             QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox, QLabel)

from PyQt5.QtGui import QIcon  # icon을 추가하기 위한 라이브러리
from PyQt5.QtCore import Qt


class View(QWidget):
    def __init__(self, db):
        super().__init__()  # 부모 클래스 QWidget을 초기화
        self.initUI()  # 나머지 초기화는 initUI함수에 정의
        self.db = db

    def initUI(self):
        self.inputEdit = QLineEdit('한글단어 입력', self)
        self.inputEdit.setFocus(True)
        self.inputEdit.selectAll()
        self.inputEdit.returnPressed.connect(self.setDisplay)
        self.inputEdit.textEdited.connect(self.setDisplay)

        self.le1_L = QLineEdit()
        self.le2_L = QLineEdit()
        self.le3_L = QLineEdit()
        self.le4_L = QLineEdit()
        self.le4_L.setDisabled(True)
        self.le5_L = QLineEdit()
        self.le5_L.setDisabled(True)
        self.le6_L = QLineEdit()
        self.le6_L.setDisabled(True)

        self.le1_R = QLineEdit()
        self.le2_R = QLineEdit()
        self.le3_R = QLineEdit()
        self.le4_R = QLineEdit()
        self.le5_R = QLineEdit()
        self.le6_R = QLineEdit()

        hbox0 = QHBoxLayout()
        hbox0.addWidget(QLabel("영어약어", self))
        hbox0.addWidget(QLabel("접두사 + 영어약어", self))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.le1_L)
        hbox1.addWidget(self.le1_R)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.le2_L)
        hbox2.addWidget(self.le2_R)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.le3_L)
        hbox3.addWidget(self.le3_R)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.le4_L)
        hbox4.addWidget(self.le4_R)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.le5_L)
        hbox5.addWidget(self.le5_R)
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.le6_L)
        hbox6.addWidget(self.le6_R)

        self.leInput1 = QLineEdit('한글', self)
        self.leInput2 = QLineEdit('영문약어', self)
        self.btnInsert = QPushButton('Insert', self)
        self.btnInsert.clicked.connect(self.insertData)

        hbox_input = QHBoxLayout()
        hbox_input.addStretch(1)
        hbox_input.addWidget(self.leInput1)
        hbox_input.addWidget(self.leInput2)
        hbox_input.addWidget(self.btnInsert)

        vbox = QVBoxLayout()  # 수직 레이아웃 위젯 생성
        vbox.addWidget(QLabel("여러 단어로 조합된 한글단어를 스페이스로 구분해서 입력 후 엔터키를 칩니다.", self))
        vbox.addWidget(self.inputEdit)  # 수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addWidget(QLabel("조회되지 않을때는 입력할 수 있습니다.", self))
        vbox.addLayout(hbox_input)
        vbox.addStretch(1)
        vbox.addStretch(1)
        self.setLayout(vbox)  # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정
        self.setWindowTitle('약어 생성기')  # 윈도우에 포시되는 타이틀 설정
        self.setWindowIcon(QIcon('icon.png'))  # 윈도우 아이콘 추가
        self.resize(420, 300)  # 윈도우 사이즈
        self.show()  # 윈도우 화면이 표시되도록 호출
        self.clearWindow()

    def setDisplay(self):
        self.clearWindow()
        value = self.inputEdit.text()
        lst = list(value.split(" "))
        print(lst)
        value = ''

        for txt in lst:
            found = self.db.find(txt)
            if found == '':
                pass
            else:
                found = found[0].upper() + found[1:].lower()
                value = value + found

        if value is None:
            pass
        elif value == '':
            pass
        else:
            self.le1_L.setText(value[0].lower() + value[1:])
            self.le2_L.setText(value)
            self.le3_L.setText(value.upper())
            self.le1_R.setText("insert" + value)
            self.le2_R.setText("update" + value)
            self.le3_R.setText("delete" + value)
            self.le4_R.setText("select" + value)
            self.le5_R.setText("get" + value)
            self.le6_R.setText("set" + value)

    def clearWindow(self):
        self.le1_L.setText("Case1")
        self.le2_L.setText("Case2")
        self.le3_L.setText("Case3")

        self.le1_R.setText("Insert")
        self.le2_R.setText("Update")
        self.le3_R.setText("Delete")
        self.le4_R.setText("Select")
        self.le5_R.setText("Get")
        self.le6_R.setText("Set")

    def insertData(self):
        self.db.insertData(self.leInput1.text(), self.leInput2.text())
        self.leInput1.clear()
        self.leInput2.clear()
