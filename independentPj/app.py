import sys
from PyQt5.QtWidgets import *
import requests
import nmap
from scapy.all import *


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
        self.layout_packet = QVBoxLayout(self)
        self.layout_help = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tabs.setGeometry(0, 0, 670, 450)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.tabs.addTab(self.tab1, "GET POST request")
        self.tabs.addTab(self.tab2, "NMAP")
        self.tabs.addTab(self.tab3, "Send Packet")
        self.tabs.addTab(self.tab4, "HELP")

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


        self.save_button = QPushButton(self)
        self.save_button.setText("Export in the text")
        self.save_button.clicked.connect(self.export)

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

        self.port_start_lb = QLabel(self)
        self.port_start_lb.setText("start port")
        self.port_start = QPlainTextEdit(self)
        self.port_end_lb = QLabel(self)
        self.port_end_lb.setText("end port")
        self.port_end = QPlainTextEdit(self)

        self.nmap_resultLabel = QLabel(self)
        self.nmap_resultLabel.setText("Port Scan results")
        self.nmap_result = QPlainTextEdit(self)

        self.tab2.layout.addWidget(self.nmapLabel)
        self.tab2.layout.addWidget(self.nmapurl)

        self.tab2.layout.addWidget(self.port_start_lb)
        self.tab2.layout.addWidget(self.port_start)
        self.tab2.layout.addWidget(self.port_end_lb)
        self.tab2.layout.addWidget(self.port_end)

        self.tab2.layout.addWidget(self.nmap_exe)
        self.tab2.layout.addWidget(self.nmap_resultLabel)
        self.tab2.layout.addWidget(self.nmap_result)

        # add whole
        self.tab2.setLayout(self.tab2.layout)
        self.layout_nmap.addWidget(self.tabs)
        self.setLayout(self.layout_nmap)

        #Add packet sending
        self.tab3.layout = QVBoxLayout(self)
        self.select_protocol = QComboBox(self)
        self.select_protocol.addItem("ICMAP")
        self.select_protocol.addItem("ICMAPv6")
        self.select_protocol.addItem("ARP")
        self.select_protocol.addItem("NDS")
        self.select_protocol.addItem("DHCP")

        self.packet_url = QPlainTextEdit(self)
        self.labelpacket_url = QLabel(self)
        self.labelpacket_url.setText("Packet URL")
        self.prtcol_button = QPushButton(self)
        self.prtcol_button.setText("Execute packet sending")
        self.prtcol_button.clicked.connect(self.execute_protocol)
        self.prtocol_resul = QPlainTextEdit(self)


        self.tab3.layout.addWidget(self.select_protocol)
        self.tab3.layout.addWidget(self.labelpacket_url)
        self.tab3.layout.addWidget(self.packet_url)
        self.tab3.layout.addWidget(self.prtcol_button)
        self.tab3.layout.addWidget(self.prtocol_resul)
        self.tab3.setLayout(self.tab3.layout)
        self.layout_packet.addWidget(self.tabs)
        self.setLayout(self.layout_packet)

        #help captions
        self.tab4.layout = QVBoxLayout(self)

        self.caption = QLabel(self)
        self.caption.setText("This is a easy hacker tool \n"
                             + "Prerequisite of NMAP: install NMAP & set path \n"
                             + "nmap.org : https://nmap.org/\n\n"
                             + "Prerequisite of Scapy\n"
                             + "pip3 install scapy-python3"
                             )

        self.tab4.layout.addWidget(self.caption)

        self.tab4.setLayout(self.tab4.layout)
        self.layout_help.addWidget(self.tabs)
        self.setLayout(self.layout_help)


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
        start_port = str(self.port_start.toPlainText())
        end_port = str(self.port_end.toPlainText())
        port_range = str(start_port + "-" + end_port)
        target_host = str(self.nmapurl.toPlainText())
        nm.scan(target_host, port_range)
        self.nmap_result.clear()

        for host in nm.all_hosts():
            for protocol in nm[host].all_protocols():
                self.nmap_result.insertPlainText('Protocol : %s' % protocol)
                if 'tcp' == protocol:
                    lport = list(nm[host]['tcp'].keys())
                    lport.sort()
                    for port in lport:
                            self.nmap_result.insertPlainText('port : %s\tstate : %s' % (port, nm[host]['tcp'][port]['state']) + "\n")
                if 'udp' == protocol:
                    lport = list(nm[host]['udp'].keys())
                    lport.sort()
                    for port in lport:
                        self.nmap_result.insertPlainText('port : %s\tstate : %s' % (port, nm[host]['udp'][port]['state'])+ "\n")
    def export(self):
        path = QFileDialog.getSaveFileName()
        self.path =path[0]
        f = open(self.path, "w")
        f.write(self.result.toPlainText())
        f.close()

    def execute_protocol(self):
        option = str(self.select_protocol.currentText())
        url = str(self.packet_url.toPlainText())
        #p = IP(dst=url)/ICMP()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())