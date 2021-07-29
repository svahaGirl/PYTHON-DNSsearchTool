    # -*- coding: utf-8 -*-

    # Form implementation generated from reading ui file 'useruserInputSim.ui'
    #
    # Created by: PyQt5 UI code generator 5.15.0
    #
    # WARNING: Any manual changes made to this file will be lost when pyuic5 is
    # run again.  Do not edit this file unless you know what you are doing.


    from PyQt5 import QtCore, QtGui, QtWidgets
    import dns as dns
    import dns.resolver 
    import subprocess

    class Ui_userInputSim(object):

        #def handleTxt(self):
        #    hTxt = userInput
        #    result_show(hTxt)

        #def add_entry(self):
        #    userInput = self.userInput.text()
        #    add_entry()
        

        def setupUi(self, userInputSim):
            userInputSim.setObjectName("User Input Simple DNS Search")
            userInputSim.resize(800, 600)
            self.centralwidget = QtWidgets.QWidget(userInputSim)
            self.centralwidget.setObjectName("centralwidget")
            self.userInput = QtWidgets.QLineEdit(self.centralwidget)
            self.userInput.setGeometry(QtCore.QRect(280, 100, 221, 41))

            self.userInput.setObjectName("userInput")

            # donot know to get value of input use GUI action


            self.webAddress_label = QtWidgets.QLabel(self.centralwidget)
            self.webAddress_label.setGeometry(QtCore.QRect(100, 100, 111, 31))
            self.webAddress_label.setObjectName("webAddress_label")
            self.sim_search_btn = QtWidgets.QPushButton(self.centralwidget)
            self.sim_search_btn.setGeometry(QtCore.QRect(360, 190, 75, 23))

            self.sim_search_btn.setObjectName("sim_search_btn")
        # self.sim_search_btn.clicked.connect(self.print_sth)


            self.IP_label = QtWidgets.QLabel(self.centralwidget)
            self.IP_label.setGeometry(QtCore.QRect(100, 260, 101, 20))
            self.IP_label.setObjectName("IP_label")
            self.ipResult = QtWidgets.QLineEdit(self.centralwidget)
            self.ipResult.setGeometry(QtCore.QRect(290, 250, 221, 41))
            self.ipResult.setObjectName("ipResult")
            self.saveIP_btn = QtWidgets.QPushButton(self.centralwidget)
            self.saveIP_btn.setGeometry(QtCore.QRect(360, 370, 91, 23))
            
            self.saveIP_btn.setObjectName("saveIP_btn")

            #self.saveIP_btn.clicked.connect(self.result_show)
            # Do not know how to save the result and out put


            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(180, 30, 281, 41))
            self.label.setObjectName("label")
            userInputSim.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(userInputSim)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
            self.menubar.setObjectName("menubar")
            userInputSim.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(userInputSim)
            self.statusbar.setObjectName("statusbar")
            userInputSim.setStatusBar(self.statusbar)

            self.retranslateUi(userInputSim)
            QtCore.QMetaObject.connectSlotsByName(userInputSim)

        def retranslateUi(self, userInputSim):
            _translate = QtCore.QCoreApplication.translate
            userInputSim.setWindowTitle(_translate("MainWindow", "User Input Simple DNS Search"))
            self.webAddress_label.setText(_translate("MainWindow", "Website Address"))
            self.sim_search_btn.setText(_translate("MainWindow", "Search"))
            self.IP_label.setText(_translate("MainWindow", "IP Address Result"))
            self.saveIP_btn.setText(_translate("MainWindow", "Save "))
            self.label.setText(_translate("MainWindow", "Simple DNS search User Input"))

        # class Window(object):
            #    def __init__(self):
            #        super(Window, self).__init__()
            #       self.setGeometry(50, 50, 500, 300)
            #       self.setWindowTitle("TEMP FILE")

            #      self.home()

            # def home (self):
            #       btn_run = sim_search_btn("Run", self)
            #       btn_run.clicked.connect(self.execute)

            #        self.show()

            #    def execute(self):
            #        subprocess.Popen('getIpValue.py', shell=True)
            #       subprocess.call(["python", "getIpValue.py"])
                    
                
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        userInputSim = QtWidgets.QMainWindow()
        ui = Ui_userInputSim()
        ui.setupUi(userInputSim)
        userInputSim.show()

        sys.exit(app.exec_())