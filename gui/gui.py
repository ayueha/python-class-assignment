import os.path
import sys, codecs
from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text edit application")
        self.setGeometry(450, 450, 450, 450)

        self.textarea = QPlainTextEdit(self)
        self.textarea.move(70, 50)
        self.textarea.resize(300, 300)

        self.button_serch = QPushButton("Search File", self)
        self.button_serch.clicked.connect(self.findexe)
        self.button_serch.move(20, 10)

        self.button_add = QPushButton("save",self)
        self.button_add.clicked.connect(self.write)
        self.button_add.move(20, 400)

        self.button_help = QPushButton("Help",self)
        self.button_help.move(350, 10)
        self.button_help.clicked.connect(self.helpshow)
        self.path = ""

        self.button_close = QPushButton("close",self)
        self.button_close.clicked.connect(self.close)
        self.button_close.move(130, 400)




    def findexe(self):
        path = QFileDialog.getOpenFileName()
        self.path = path[0]
        file_contents = open(self.path, "r")
        for line in file_contents:
            self.textarea.insertPlainText(line)
        file_contents.close()

    def write(self):
        path = QFileDialog.getSaveFileName()
        self.path = path[0]
        f = open(self.path, "w")
        f.write(self.textarea.toPlainText())
        f.close()

    def helpshow(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("Python text Editor")
        msg.setText("Python text editor. Push search and find file." + "\n" + "To save the file, push save" + "\n" + "code:PyQt5")
        msg.exec_()

    def close(self):
        sys.exit()


if __name__ == "__main__":
            app = QApplication(sys.argv)
            ex = App()
            ex.show()
            sys.exit(app.exec_())