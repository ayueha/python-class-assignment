import sys, time, os
from PyQt5.QtWidgets import *
from websocket import create_connection


class ChatForm(QWidget):

    def __init__(self):
        super().__init__()
        self.ws = create_connection("ws://127.0.0.1:8080")
        self.setWindowTitle("Python Chat Application")
        self.setGeometry(450, 450, 450, 450)

        self.name = QPlainTextEdit(self)
        self.name.move(200, 10)
        self.name.resize(150, 30)

        self.label = QLabel(self)
        self.label.move(100, 10)
        self.label.setText('Your Name');

        self.textarea = QPlainTextEdit(self)
        self.textarea.move(70, 50)
        self.textarea.resize(300, 50)

        self.sendButton = QPushButton("Send", self)
        self.sendButton.move(70, 100)
        self.sendButton.resize(300, 35)
        self.sendButton.clicked.connect(self.sendmessage)

        self.textinfo = QPlainTextEdit(self)
        self.textinfo.move(70, 150)
        self.textinfo.resize(300, 200)



    def sendmessage(self):
        if self.name.toPlainText() == "":
            name = "anonymous"
        else:
            name = self.name.toPlainText()
        chat_str = name + ":" + self.textarea.toPlainText() + "\n"
        self.ws.send(chat_str.encode(encoding='UTF-8', errors='can not encode in UTF-8'))
        result = self.ws.recv()
        self.textinfo.insertPlainText(result)

    def closeEvent(self, QCloseEvent):
        self.ws.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wmain = ChatForm()
    wmain.show()
    sys.exit(app.exec_())
