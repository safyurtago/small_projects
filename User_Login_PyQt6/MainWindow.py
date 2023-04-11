from PyQt6.QtWidgets import *
import sys
from CreateWindow import *
from ShowWindow import *
from SearchWindow import *
from EditWindow import *


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.__main_layout = QHBoxLayout()
        self.__label_layout = QVBoxLayout()
        self.__button_layout = QVBoxLayout()
        self.__l1 = QLabel("1.")
        self.__l2 = QLabel("2.")
        self.__l3 = QLabel("3.")
        self.__l4 = QLabel("4.")
        self.__l5 = QLabel("5.")
        self.__label_layout.addWidget(self.__l1)
        self.__label_layout.addWidget(self.__l2)
        self.__label_layout.addWidget(self.__l3)
        self.__label_layout.addWidget(self.__l4)
        self.__label_layout.addWidget(self.__l5)
        self.__b1 = QPushButton("Create new user")
        self.__b2 = QPushButton("Show all")
        self.__b3 = QPushButton("Edit")
        self.__b4 = QPushButton("Search")
        self.__b5 = QPushButton("Exit")
        self.__button_layout.addWidget(self.__b1)
        self.__button_layout.addWidget(self.__b2)
        self.__button_layout.addWidget(self.__b3)
        self.__button_layout.addWidget(self.__b4)
        self.__button_layout.addWidget(self.__b5)
        self.__main_layout.addLayout(self.__label_layout)
        self.__main_layout.addLayout(self.__button_layout)
        self.__main_layout.addStretch(1)

        self.__b1.clicked.connect(self.go_to_b1)
        self.__b2.clicked.connect(self.go_to_b2)
        self.__b3.clicked.connect(self.go_to_b3)
        self.__b4.clicked.connect(self.go_to_b4)
        self.__b5.clicked.connect(self.go_to_b5)

        self.setLayout(self.__main_layout)

    def go_to_b1(self):
        self.create_win = CreateWindow()
        self.create_win.show()

    def go_to_b2(self):
        self.show_win = Show_allWindow()
        self.show_win.show()
    
    def go_to_b3(self):
        self.eidt_win = EditWindow()
        self.eidt_win.show()

    def go_to_b4(self):
        self.search_win = SearchWindow()
        self.search_win.show()

    def go_to_b5(self):
        sys.exit()

if __name__ == "__main__":
    
    while True:
        app = QApplication([])
        win = MainWindow()
        win.show()
        app.exec()