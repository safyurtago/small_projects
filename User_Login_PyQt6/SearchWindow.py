from PyQt6.QtWidgets import *
import sys
from users_control_database import *


class SearchWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.__main_layout = QVBoxLayout()
        self.__search_edit = QLineEdit()
        self.__search_edit.setPlaceholderText("Enter user's name...")
        self.__main_layout.addWidget(self.__search_edit)
        self.__search_btn = QPushButton("Search")
        self.__main_layout.addWidget(self.__search_btn)
        self.__search_btn.clicked.connect(self.search_name)

        self.setLayout(self.__main_layout)

    def search_name(self):
        a = emp1.search_user(self.__search_edit.text())
        msg = QMessageBox(self)
        msg.setWindowTitle(f"{a[0][1]}'s Info")
        msg.move(500, 500)
        msg.setText(f'''Id |   Fullname         |    Login   |   Password\n
{a[0][0]} |  {a[0][1].capitalize()} {a[0][2].capitalize()}    |   {a[0][3]}     |   {a[0][4]}   
        ''')
        msg.exec()

if __name__ == "__main__":
    app = QApplication([])
    win = SearchWindow()
    win.show()
    sys.exit(app.exec())