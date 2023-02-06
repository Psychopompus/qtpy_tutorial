import sys
from PyQt5.QtWidgets import QApplication, QWidget   # 애플리케이션 핸들러와 빈 GUI 위젯

class Calculator(QWidget): # QWidget 클래스를 상속받아서 클래스를 정의
    def __init__(self):
        super().__init__()  # 부모 클래스 QWidget을 초기화
        self.initUI()       # 나머지 초기화는 initUI함수에 정의

    def initUI(self):
        self.setWindowTitle('Calculator')   # 윈도우에 포시되는 타이틀 설정
        self.resize(256,256)                # 윈도우 사이즈
        self.show()                         # 윈도우 화면이 표시되도록 호출

if __name__=='__main__':            # pyqt는 애플리케이션 당 1개의 QApplication이 필요함
    app = QApplication(sys.argv)    # QApplication 인스턴스 생성
    view = Calculator()             # Calculator 위도우 인스턴스 생성
    sys.exit(app.exec_())           # 애플리케이션이 이벤트 처리를 하도록 루프 구동
    