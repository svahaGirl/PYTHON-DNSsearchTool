#!/usr/bin/python3
# DNS Tool tree view
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.Qt import QStandardItem

from PyQt5.QtGui import QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0,0,0)):
        super().__init__()

        fnt =QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CI2 DNS Search Tool')
        self.resize(500,700)

        treeView = QTreeView(self)
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        '--------------------------------------'

        # DNS Search Tool

        dnsSearch =StandardItem('DNS Search Tools', 16, set_bold=True)

        simpleSearch = StandardItem('Simple Domain Name Search', 14)
        dnsSearch.appendRow(simpleSearch)

        comprehensiveSearch = StandardItem('Comprehensive Domain Name Search', 14)    

        dnsSearch.appendRow(comprehensiveSearch)


        
        rootNode.appendRow(dnsSearch)
        rootNode.appendRow(comprehensiveSearch)

        treeView.setModel(treeModel)
        treeView.expandAll()
        treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())

app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())

