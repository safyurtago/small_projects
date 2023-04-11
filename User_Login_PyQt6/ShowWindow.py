from PyQt6.QtWidgets import *
import sys
from users_control_database import *

class Show_allWindow(QWidget):
    def __init__(self, ) -> None:
        super().__init__()

        self.__list_all_users = emp1.list_all_users()

        self.setGeometry(500, 500, 400, 400)
        self.__main_layout = QVBoxLayout()
        x = 0
        while len(self.__list_all_users) > x:
            l = QLabel()
            l.setText(f"{x+1}. {self.__list_all_users[x][1].capitalize()} {self.__list_all_users[x][2].capitalize()}")
            self.__main_layout.addWidget(l)
            x += 1
        self.setLayout(self.__main_layout)

if __name__ == "__main__":
    app = QApplication([])
    win = Show_allWindow()
    win.show()
    sys.exit(app.exec())

