import sys
from PyQt5.QtWidgets import *
import requests
import nmap

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title ='hacker tool'
        self.left = 0
        self.top = 0
        self.width = 750
        self.height = 500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.main_contents = MainWidget(self)
        self.setCentralWidget(self.main_contents)
        self.move(300,300)
        self.show()

class MainWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout_req = QVBoxLayout(self)
        self.layout_nmap = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "GET POST request")
        self.tabs.addTab(self.tab2, "NMAP")

        # ---tab 1 ---
        self.tab1.layout = QVBoxLayout(self)
        self.urlLabel = QLabel(self)
        self.urlLabel.setText("Target URL")


        self.select = QComboBox(self)
        self.select.addItem("POST")
        self.select.addItem("GET")

        self.url = QPlainTextEdit(self)
        self.execute_button = QPushButton(self)
        self.execute_button.setText("Retrieve information")
        self.execute_button.clicked.connect(self.retrieve_info)

        self.url_request_result = QLabel(self)
        self.url_cookie_label = QLabel(self)
        self.url_cookie_label.setText("Cookie Info")
        self.url_cookie_result = QPlainTextEdit(self)
        self.url_cookie_result.setReadOnly(True)
        self.url_html_result = QLabel(self)
        self.url_html_result.setText("HTML result")

        self.result = QPlainTextEdit(self)
        self.result.setReadOnly(True)

        self.save_button = QPushButton(self)
        self.save_button.setText("Export in the text")

        self.tab1.layout.addWidget(self.urlLabel)
        self.tab1.layout.addWidget(self.select)
        self.tab1.layout.addWidget(self.url)
        self.tab1.layout.addWidget(self.execute_button)

        self.tab1.layout.addWidget(self.url_request_result)
        self.tab1.layout.addWidget(self.url_cookie_label)
        self.tab1.layout.addWidget(self.url_cookie_result)
        self.tab1.layout.addWidget(self.url_html_result)
        self.tab1.layout.addWidget(self.result)
        self.tab1.layout.addWidget(self.save_button)
        self.tab1.setLayout(self.tab1.layout)

        #add whole
        self.layout_req.addWidget(self.tabs)
        self.setLayout(self.layout_req)

        # tab2
        self.tab2.layout = QVBoxLayout(self)
        self.nmapLabel = QLabel(self)
        self.nmapLabel.setText("Target URL")
        self.nmapurl = QPlainTextEdit(self)

        self.nmap_exe = QPushButton(self)
        self.nmap_exe.setText("Execute Port Scan")
        self.nmap_exe.clicked.connect(self.executeNmap)

        self.nmap_resultLabel = QLabel(self)
        self.nmap_resultLabel.setText("Port Scan results")
        self.nmap_result = QPlainTextEdit(self)
        self.nmap_result.setReadOnly(True)

        self.tab2.layout.addWidget(self.nmapLabel)
        self.tab2.layout.addWidget(self.nmapurl)
        self.tab2.layout.addWidget(self.nmap_exe)
        self.tab2.layout.addWidget(self.nmap_resultLabel)
        self.tab2.layout.addWidget(self.nmap_result)

        self.tab2.setLayout(self.tab2.layout)
        # add whole
        self.layout_nmap.addWidget(self.tabs)
        self.setLayout(self.layout_nmap)

    def retrieve_info(self):
        if str(self.url.toPlainText()) == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle("Info")
            msg.setText("Please fill target URL")
            msg.exec_()
            return

        option = str(self.select.currentText())
        if option == "POST":
            url = self.url.toPlainText()
            r = requests.post(url)
            self.url_request_result.setText("HTTP Status Code : {}".format(r.status_code))
            for info in r.cookies.values():
                self.url_cookie_result.insertPlainText(info)
            self.result.insertPlainText(r.text)

        elif option == "GET":
            url = self.url.toPlainText()
            r = requests.get(url)
            self.url_request_result.setText("HTTP Status Code : {}".format(r.status_code))
            for info in r.cookies.values():
                self.url_cookie_result.insertPlainText(info)
            self.result.insertPlainText(r.text)

    def executeNmap(self):
        if str(self.nmapurl.toPlainText())=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle("Info")
            msg.setText("Please fill target URL")
            msg.exec_()
            return

        nm = nmap.PortScanner()
        nm.scan(self.nmapurl.toPlainText())



if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())