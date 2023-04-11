from PyQt6.QtWidgets import *
import sys
from users_control_database import *
from MainWindow import *

class CreateWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        print(1)
        self.setGeometry(500, 500, 400, 200)
        self.__main_layout = QVBoxLayout()
        self.__name_edit = QLineEdit()
        self.__name_edit.setPlaceholderText("Enter first name...")
        self.__lname_edit = QLineEdit()
        self.__lname_edit.setPlaceholderText("Enter last name...")
        self.__login_edit = QLineEdit()
        self.__login_edit.setPlaceholderText("Enter login...")
        self.__password_edit = QLineEdit()
        self.__password_edit.setPlaceholderText("Enter password...")
        self.__save_btn = QPushButton("Save all")
        self.__main_layout.addWidget(self.__name_edit)
        self.__main_layout.addWidget(self.__lname_edit)
        self.__main_layout.addWidget(self.__login_edit)
        self.__main_layout.addWidget(self.__password_edit)
        self.__main_layout.addWidget(self.__save_btn)
        self.__save_btn.clicked.connect(self.__save_all)
        self.setLayout(self.__main_layout)

    def __save_all(self):
        emp1.create_user(self.__name_edit.text().capitalize(), self.__lname_edit.text().capitalize(), self.__login_edit.text().lower(), self.__password_edit.text())
        

if __name__ == "__main__":
    app = QApplication([])
    win = CreateWindow()
    win.show()
    sys.exit(app.exec())