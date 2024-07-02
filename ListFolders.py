# -------------------------------------------------------------------------------
# Name:             ListFolders.py
# Purpose:          Select a folder and list the Subfolders of that folder
#
# Author:           Jeffreaux
#
# Created:          19June24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLabel, QPlainTextEdit
from PyQt5 import uic
import sys
from fileModule import *


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("ListFolders_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.actExit = self.findChild(QAction, "actExit")
        self.btnChooseRoot = self.findChild(QPushButton, "btnChooseRoot")
        self.lblFolderPath = self.findChild(QLabel, "lblFolderPath")
        self.btnListFolders = self.findChild(QPushButton, "btnListFolders")
        self.ptxtResultList = self.findChild(QPlainTextEdit, "ptxtResultList")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)
        self.btnChooseRoot.clicked.connect(self.getSource)
        self.btnListFolders.clicked.connect(self.getFolderList)

        # Show the app
        self.show()

    def getSource(self):
        global homePath
        print("getting source folder")
        homePath = getPath(self)
        self.lblFolderPath.setText(homePath)
        print(homePath)

    def getFolderList(self):
        print("Getting Folder list")
        flist = subCountCurrent(self,homePath)
        print(flist)
        for sub in flist: # looping through list for each result
            print(sub)
            self.ptxtResultList.appendPlainText(sub) #Write results to PlainTextEdit

    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
