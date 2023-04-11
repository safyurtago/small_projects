from PyQt6.QtWidgets import *
import sys
from users_control_database import *


class EditWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(500, 500, 400, 200)
        self.__main_layout = QVBoxLayout()
        self.lbl = QLabel()
        self.lbl.setText("Enter ID for changing user's info")
        self.__id_edit = QLineEdit()
        self.__id_edit.setPlaceholderText("Enter Id...")
        self.__smain_layout = QHBoxLayout()
        self.__smain_layout.addWidget(self.lbl)
        self.__smain_layout.addWidget(self.__id_edit)
        self.__main_layout.addLayout(self.__smain_layout)
        self.__name_edit = QLineEdit()
        self.__name_edit.setPlaceholderText("Enter first name...")
        self.__lname_edit = QLineEdit()
        self.__lname_edit.setPlaceholderText("Enter last name...")
        self.__login_edit = QLineEdit()
        self.__login_edit.setPlaceholderText("Enter login...")
        self.__password_edit = QLineEdit()
        self.__password_edit.setPlaceholderText("Enter password...")
        self.__save_btn = QPushButton("Change all")
        self.__main_layout.addWidget(self.__name_edit)
        self.__main_layout.addWidget(self.__lname_edit)
        self.__main_layout.addWidget(self.__login_edit)
        self.__main_layout.addWidget(self.__password_edit)
        self.__main_layout.addWidget(self.__save_btn)
        self.__save_btn.clicked.connect(self.__change_all)
        self.setLayout(self.__main_layout)

    def __change_all(self):
        emp1.edit_user(self.__id_edit.text(), self.__name_edit.text(), self.__lname_edit.text(), self.__login_edit.text(), self.__password_edit.text())

if __name__ == "__main__":
    app = QApplication([])
    win = EditWindow()
    win.show()
    sys.exit(app.exec())