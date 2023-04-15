from PyQt6.QtWidgets import *
import sys
from main import *

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setGeometry(500,500,700,200)
        self.main_layout = QVBoxLayout()
        self.edit_layout = QHBoxLayout()
        self.edit_line = QLineEdit()
        self.edit_line.setPlaceholderText("Enter the list items...")
        self.edit_layout.addWidget(self.edit_line)
        self.sort_btn = QPushButton("SortAll")
        self.sort_btn.clicked.connect(self.sort_all)
        self.edit_layout.addWidget(self.sort_btn)
        self.main_layout.addLayout(self.edit_layout)
        self.list_items = QListWidget()
        self.main_layout.addWidget(self.list_items)

        self.setLayout(self.main_layout)

    def sort_all(self):
        self.list_items.addItem(sorting(self.edit_line.text()))
        self.edit_line.clear()

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())