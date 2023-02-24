import sys
from ui import View  # ui.py의 View 클래스 추가
from ctrl import Control  # ctrl.py의 Control 클래스 추가
from PyQt5.QtWidgets import QApplication
from db import Mariadb


def main():  # 프로그램 식행(Application) 관련 내용 함수화
    app = QApplication(sys.argv)
    db = Mariadb()
    view = View(db=db)
    # Control(view=view)  # Control 인스턴스 선언
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
