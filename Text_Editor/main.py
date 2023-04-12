import sys
from PyQt6.QtWidgets import *

class EditEmptyError(Exception):
    pass

def make_str(lst):
    str_text = ""
    for i in lst:
        str_text = str_text[0:] + i
    return str_text

class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.textBox = QPlainTextEdit()
        self.main_layout.addWidget(self.textBox)
        self.name_edit = QLineEdit()
        self.main_layout.addWidget(self.name_edit)

        self.btns_layout = QHBoxLayout()
        self.open_btn = QPushButton("Open...")
        self.btns_layout.addWidget(self.open_btn)
        self.open_btn.clicked.connect(self.open_file)
        self.save_btn = QPushButton("Save")
        self.btns_layout.addWidget(self.save_btn)
        self.save_btn.clicked.connect(self.save_file)
        self.clear_btn = QPushButton("Clear window")
        self.btns_layout.addWidget(self.clear_btn)
        self.main_layout.addLayout(self.btns_layout)
        self.clear_btn.clicked.connect(self.clear_window)
        
        self.setLayout(self.main_layout)

    def open_file(self):
        if self.name_edit.text() == "":
            file_dialog = QFileDialog()
            fname = file_dialog.getOpenFileName()
            temp = fname[0].split("/")
            with open(f"{temp[-1]}", "r") as file:
                lst = file.readlines()                    
                self.textBox.setPlainText(make_str(lst))
                file.close()
        else:
            with open(f"{self.name_edit.text()}", "r+") as file:
                lst = file.readlines()                    
                self.textBox.setPlainText(make_str(lst))
                file.close()
    
    def save_file(self):
        try:
            if self.name_edit.text() == "":
                raise EditEmptyError

            with open(f"{self.name_edit.text()}", "w") as file:
                temp_str = self.textBox.toPlainText()
                file.write(temp_str)
                file.close()

        except EditEmptyError:
            msg = QMessageBox()
            msg.setText("File name must be written!")
            msg.setWindowTitle("MessageBox demo")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()

    def clear_window(self):
        self.textBox.clear()
        self.name_edit.clear()


if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec())