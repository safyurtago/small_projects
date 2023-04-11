from PyQt6.QtWidgets import *
import sys
from sql_base import *

class MainWidwow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.list_words = d1.show_all()

        self.main_layout = QVBoxLayout()
        self.edit_layout = QHBoxLayout()
        self.edit_uzbek = QLineEdit()
        self.edit_uzbek.setPlaceholderText("Uzbek...")
        self.edit_english = QLineEdit()
        self.edit_english.setPlaceholderText("English...")
        self.add_btn = QPushButton("➕")
        self.edit_layout.addWidget(self.edit_uzbek)
        self.edit_layout.addWidget(self.edit_english)
        self.edit_layout.addWidget(self.add_btn)
        self.add_btn.clicked.connect(self.add_word)

        self.main_layout.addLayout(self.edit_layout)
        self.text_list = QListWidget()
        self.set_words()
        self.main_layout.addWidget(self.text_list)

        self.search_layout = QHBoxLayout()
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Enter word...")
        self.search_btn = QPushButton("Search")
        self.search_layout.addWidget(self.search_edit)
        self.search_layout.addWidget(self.search_btn)
        self.main_layout.addLayout(self.search_layout)
        self.search_edit.textChanged.connect(self.search_word)

        self.setLayout(self.main_layout)

    def set_words(self):
        for lst in self.list_words:
            self.text_list.addItem(f"{lst[0]}. {lst[1]} - {lst[2]}")

    def add_word(self):
        d1.add_word(self.edit_uzbek.text(), self.edit_english.text())
        self.edit_uzbek.clear()
        self.edit_english.clear()
        self.list_words = d1.show_all()
        self.text_list.clear()
        self.set_words()

    def search_word(self):
        temp = d1.search_word(self.search_edit.text())
        self.list_words = d1.show_all()
        self.text_list.clear()
        for lst in temp:
            self.text_list.addItem(f"{lst[0]}. {lst[1]} - {lst[2]}")

if __name__ == "__main__":
    app = QApplication([])
    win = MainWidwow()
    win.show()
    sys.exit(app.exec())