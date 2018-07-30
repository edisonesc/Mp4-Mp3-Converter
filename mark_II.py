# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import os
import glob

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 67, 17))
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 40, 256, 501))
        self.listView.setObjectName("listView")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(680, 510, 89, 25))
        self.ok_button.setObjectName("ok_button")
        ########
        self.ok_button.clicked.connect(self.convert_clicked)
        #######

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 70, 411, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.check_path)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 130, 411, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 110, 111, 17))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Mp4 to Mp3", "Mp4 to Mp3"))
        self.label.setText(_translate("Mp4 to Mp3", "Files"))
        self.ok_button.setText(_translate("Mp4 to Mp3", "Convert"))
        self.label_2.setText(_translate("Mp4 to Mp3", "Source"))
        self.label_3.setText(_translate("Mp4 to Mp3", "Destination"))
        self.menuFile.setTitle(_translate("Mp4 to Mp3", "File"))
        self.actionExit.setText(_translate("Mp4 to Mp3", "Exit"))
        self.actionHelp.setText(_translate("Mp4 to Mp3", "Help"))
    def convert_clicked(self):
        source = self.lineEdit.text()
        destination = self.lineEdit_2.text()
        musics = glob.glob(source + "*.mp4")
        print("SRC: " + source)
        print("DSTNN: " + destination)
        if(len(musics) == 0):
            print("error conversion")
        else:
            print("will be converted.")


    def check_path(self):
        path = self.lineEdit.text()
        musics = glob.glob(path + "*.mp4")
        if(len(musics) == 0):
            musics = ["No mp4 found."]
        model = QtGui.QStandardItemModel(self.listView)
        for i in musics:
            item = QtGui.QStandardItem(i.replace(path, "").replace(" ", ""))
            model.appendRow(item)
        self.listView.setModel(model)
        self.listView.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)

    w.setFixedSize(800,600)
    w.show()

    sys.exit(app.exec_())