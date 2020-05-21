"""
X-Ray Scattering Analyzer
Version 1.0
Updated: February 2020
Author: Naveen Venkatesan
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path
from os import path
from tifffile import imread, imshow


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 670)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.Main_Label = QtWidgets.QLabel(self.centralwidget)
        self.Main_Label.setGeometry(QtCore.QRect(250, 0, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Main_Label.setFont(font)
        self.Main_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_Label.setObjectName("Main_Label")


        self.Calibration_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Calibration_GroupBox.setGeometry(QtCore.QRect(10, 40, 780, 240))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Calibration_GroupBox.setFont(font)
        self.Calibration_GroupBox.setObjectName("Calibration_GroupBox")


        self.CF_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.CF_Label.setGeometry(QtCore.QRect(0, 30, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CF_Label.setFont(font)
        self.CF_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CF_Label.setObjectName("CF_Label")


        self.Calibrant_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.Calibrant_Label.setGeometry(QtCore.QRect(0, 80, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Calibrant_Label.setFont(font)
        self.Calibrant_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Calibrant_Label.setObjectName("Calibrant_Label")


        self.AgBe_RadioButton = QtWidgets.QRadioButton(self.Calibration_GroupBox)
        self.AgBe_RadioButton.setGeometry(QtCore.QRect(100, 80, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.AgBe_RadioButton.setFont(font)
        self.AgBe_RadioButton.setChecked(True)


        self.AgBe_RadioButton.setObjectName("AgBe_RadioButton")
        self.LaB6_RadioButton = QtWidgets.QRadioButton(self.Calibration_GroupBox)
        self.LaB6_RadioButton.setGeometry(QtCore.QRect(170, 80, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LaB6_RadioButton.setFont(font)
        self.LaB6_RadioButton.setChecked(False)
        self.LaB6_RadioButton.setObjectName("LaB6_RadioButton")


        self.Energy_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.Energy_Label.setGeometry(QtCore.QRect(265, 80, 115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Energy_Label.setFont(font)
        self.Energy_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Energy_Label.setObjectName("Energy_Label")


        self.Energy_LineEdit = QtWidgets.QLineEdit(self.Calibration_GroupBox)
        self.Energy_LineEdit.setGeometry(QtCore.QRect(390, 80, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Energy_LineEdit.setFont(font)
        self.Energy_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Energy_LineEdit.setObjectName("Energy_LineEdit")


        self.PS_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.PS_Label.setGeometry(QtCore.QRect(505, 80, 135, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PS_Label.setFont(font)
        self.PS_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PS_Label.setObjectName("PS_Label")


        self.PS_LineEdit = QtWidgets.QLineEdit(self.Calibration_GroupBox)
        self.PS_LineEdit.setGeometry(QtCore.QRect(650, 80, 90, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.PS_LineEdit.setFont(font)
        self.PS_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_LineEdit.setObjectName("PS_LineEdit")


        self.CF_Browse_PushButton = QtWidgets.QPushButton(self.Calibration_GroupBox)
        self.CF_Browse_PushButton.setGeometry(QtCore.QRect(685, 30, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        self.CF_Browse_PushButton.setFont(font)
        self.CF_Browse_PushButton.setObjectName("CF_Browse_PushButton")
        self.CF_Browse_PushButton.clicked.connect(self.CF_Browse)


        self.CF_LineEdit = QtWidgets.QLineEdit(self.Calibration_GroupBox)
        self.CF_LineEdit.setGeometry(QtCore.QRect(100, 30, 580, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.CF_LineEdit.setFont(font)
        self.CF_LineEdit.setObjectName("CF_LineEdit")


        self.Resolution_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.Resolution_Label.setGeometry(QtCore.QRect(50, 130, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Resolution_Label.setFont(font)
        self.Resolution_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Resolution_Label.setObjectName("Resolution_Label")


        self.Width_LineEdit = QtWidgets.QLineEdit(self.Calibration_GroupBox)
        self.Width_LineEdit.setGeometry(QtCore.QRect(210, 130, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Width_LineEdit.setFont(font)
        self.Width_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Width_LineEdit.setObjectName("Width_LineEdit")


        self.Width_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.Width_Label.setGeometry(QtCore.QRect(290, 130, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Width_Label.setFont(font)
        self.Width_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Width_Label.setObjectName("Width_Label")


        self.Height_LineEdit = QtWidgets.QLineEdit(self.Calibration_GroupBox)
        self.Height_LineEdit.setGeometry(QtCore.QRect(360, 130, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Height_LineEdit.setFont(font)
        self.Height_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Height_LineEdit.setObjectName("Height_LineEdit")


        self.Height_Label = QtWidgets.QLabel(self.Calibration_GroupBox)
        self.Height_Label.setGeometry(QtCore.QRect(440, 130, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Height_Label.setFont(font)
        self.Height_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Height_Label.setObjectName("Height_Label")


        self.Calibration_PushButton = QtWidgets.QPushButton(self.Calibration_GroupBox)
        self.Calibration_PushButton.setGeometry(QtCore.QRect(520, 127, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Calibration_PushButton.setFont(font)
        self.Calibration_PushButton.setObjectName("Calibration_PushButton")
        self.Calibration_PushButton.clicked.connect(self.calcSDD)


        self.Calibration_Frame = QtWidgets.QFrame(self.Calibration_GroupBox)
        self.Calibration_Frame.setGeometry(QtCore.QRect(10, 180, 760, 50))
        self.Calibration_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Calibration_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Calibration_Frame.setLineWidth(2)
        self.Calibration_Frame.setObjectName("Calibration_Frame")


        self.BeamCenter_Label = QtWidgets.QLabel(self.Calibration_Frame)
        self.BeamCenter_Label.setGeometry(QtCore.QRect(5, 10, 115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BeamCenter_Label.setFont(font)
        self.BeamCenter_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BeamCenter_Label.setObjectName("BeamCenter_Label")


        self.BC_x_LineEdit = QtWidgets.QLineEdit(self.Calibration_Frame)
        self.BC_x_LineEdit.setGeometry(QtCore.QRect(130, 10, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BC_x_LineEdit.setFont(font)
        self.BC_x_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.BC_x_LineEdit.setObjectName("BC_x_LineEdit")


        self.BC_x_Label = QtWidgets.QLabel(self.Calibration_Frame)
        self.BC_x_Label.setGeometry(QtCore.QRect(210, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BC_x_Label.setFont(font)
        self.BC_x_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.BC_x_Label.setObjectName("BC_x_Label")


        self.BC_y_LineEdit = QtWidgets.QLineEdit(self.Calibration_Frame)
        self.BC_y_LineEdit.setGeometry(QtCore.QRect(280, 10, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BC_y_LineEdit.setFont(font)
        self.BC_y_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.BC_y_LineEdit.setObjectName("BC_y_LineEdit")


        self.BC_y_Label = QtWidgets.QLabel(self.Calibration_Frame)
        self.BC_y_Label.setGeometry(QtCore.QRect(360, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BC_y_Label.setFont(font)
        self.BC_y_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.BC_y_Label.setObjectName("BC_y_Label")


        self.SDD_Label = QtWidgets.QLabel(self.Calibration_Frame)
        self.SDD_Label.setGeometry(QtCore.QRect(440, 10, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SDD_Label.setFont(font)
        self.SDD_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SDD_Label.setObjectName("SDD_Label")


        self.SDD_LineEdit = QtWidgets.QLineEdit(self.Calibration_Frame)
        self.SDD_LineEdit.setGeometry(QtCore.QRect(560, 10, 181, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.SDD_LineEdit.setFont(font)
        self.SDD_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SDD_LineEdit.setObjectName("SDD_LineEdit")


        self.Analysis_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Analysis_GroupBox.setGeometry(QtCore.QRect(10, 290, 780, 321))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Analysis_GroupBox.setFont(font)
        self.Analysis_GroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Analysis_GroupBox.setObjectName("Analysis_GroupBox")


        self.IF_Label = QtWidgets.QLabel(self.Analysis_GroupBox)
        self.IF_Label.setGeometry(QtCore.QRect(0, 30, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IF_Label.setFont(font)
        self.IF_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IF_Label.setObjectName("IF_Label")


        self.IF_LineEdit = QtWidgets.QLineEdit(self.Analysis_GroupBox)
        self.IF_LineEdit.setGeometry(QtCore.QRect(100, 30, 580, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.IF_LineEdit.setFont(font)
        self.IF_LineEdit.setObjectName("IF_LineEdit")


        self.IF_Browse_PushButton = QtWidgets.QPushButton(self.Analysis_GroupBox)
        self.IF_Browse_PushButton.setGeometry(QtCore.QRect(685, 30, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        self.IF_Browse_PushButton.setFont(font)
        self.IF_Browse_PushButton.setObjectName("IF_Browse_PushButton")
        self.IF_Browse_PushButton.clicked.connect(self.IF_Browse)


        self.IA_Label = QtWidgets.QLabel(self.Analysis_GroupBox)
        self.IA_Label.setGeometry(QtCore.QRect(10, 80, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.IA_Label.setFont(font)
        self.IA_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IA_Label.setObjectName("IA_Label")


        self.IA_LineEdit = QtWidgets.QLineEdit(self.Analysis_GroupBox)
        self.IA_LineEdit.setGeometry(QtCore.QRect(170, 80, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.IA_LineEdit.setFont(font)
        self.IA_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.IA_LineEdit.setObjectName("IA_LineEdit")


        self.CA_PushButton = QtWidgets.QPushButton(self.Analysis_GroupBox)
        self.CA_PushButton.setGeometry(QtCore.QRect(260, 76, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        self.CA_PushButton.setFont(font)
        self.CA_PushButton.setObjectName("CA_PushButton")
        self.CA_PushButton.clicked.connect(self.calcCA)


        self.GIXS_PushButton = QtWidgets.QPushButton(self.Analysis_GroupBox)
        self.GIXS_PushButton.setGeometry(QtCore.QRect(410, 76, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        self.GIXS_PushButton.setFont(font)
        self.GIXS_PushButton.setObjectName("GIXS_PushButton")
        self.GIXS_PushButton.clicked.connect(self.calcGIXS)


        self.IP_PushButton = QtWidgets.QPushButton(self.Analysis_GroupBox)
        self.IP_PushButton.setGeometry(QtCore.QRect(530, 76, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        self.IP_PushButton.setFont(font)
        self.IP_PushButton.setObjectName("IP_PushButton")
        self.IP_PushButton.clicked.connect(self.calcIP)


        self.OOP_PushButton = QtWidgets.QPushButton(self.Analysis_GroupBox)
        self.OOP_PushButton.setGeometry(QtCore.QRect(650, 76, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(15)
        self.OOP_PushButton.setFont(font)
        self.OOP_PushButton.setObjectName("OOP_PushButton")
        self.OOP_PushButton.clicked.connect(self.calcOOP)


        self.GIXS_Params_Label = QtWidgets.QLabel(self.Analysis_GroupBox)
        self.GIXS_Params_Label.setGeometry(QtCore.QRect(285, 120, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.GIXS_Params_Label.setFont(font)
        self.GIXS_Params_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GIXS_Params_Label.setObjectName("GIXS_Params_Label")


        self.MinMax_Frame = QtWidgets.QFrame(self.Analysis_GroupBox)
        self.MinMax_Frame.setGeometry(QtCore.QRect(10, 160, 370, 151))
        self.MinMax_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MinMax_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MinMax_Frame.setLineWidth(2)
        self.MinMax_Frame.setObjectName("MinMax_Frame")


        self.Int_Label = QtWidgets.QLabel(self.MinMax_Frame)
        self.Int_Label.setGeometry(QtCore.QRect(260, 10, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Int_Label.setFont(font)
        self.Int_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Int_Label.setObjectName("Int_Label")


        self.Int_Min_LineEdit = QtWidgets.QLineEdit(self.MinMax_Frame)
        self.Int_Min_LineEdit.setGeometry(QtCore.QRect(260, 50, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Int_Min_LineEdit.setFont(font)
        self.Int_Min_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Int_Min_LineEdit.setObjectName("Int_Min_LineEdit")


        self.Qz_Label = QtWidgets.QLabel(self.MinMax_Frame)
        self.Qz_Label.setGeometry(QtCore.QRect(160, 10, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Qz_Label.setFont(font)
        self.Qz_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Qz_Label.setObjectName("Qz_Label")


        self.Qz_Min_LineEdit = QtWidgets.QLineEdit(self.MinMax_Frame)
        self.Qz_Min_LineEdit.setGeometry(QtCore.QRect(160, 50, 70, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Qz_Min_LineEdit.setFont(font)
        self.Qz_Min_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Qz_Min_LineEdit.setObjectName("Qz_Min_LineEdit")


        self.Qxy_Label = QtWidgets.QLabel(self.MinMax_Frame)
        self.Qxy_Label.setGeometry(QtCore.QRect(60, 10, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Qxy_Label.setFont(font)
        self.Qxy_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Qxy_Label.setObjectName("Qxy_Label")


        self.Qxy_Min_LineEdit = QtWidgets.QLineEdit(self.MinMax_Frame)
        self.Qxy_Min_LineEdit.setGeometry(QtCore.QRect(60, 50, 70, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Qxy_Min_LineEdit.setFont(font)
        self.Qxy_Min_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Qxy_Min_LineEdit.setObjectName("Qxy_Min_LineEdit")


        self.Min_Label = QtWidgets.QLabel(self.MinMax_Frame)
        self.Min_Label.setGeometry(QtCore.QRect(0, 50, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Min_Label.setFont(font)
        self.Min_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Min_Label.setObjectName("Min_Label")


        self.Int_Max_LineEdit = QtWidgets.QLineEdit(self.MinMax_Frame)
        self.Int_Max_LineEdit.setGeometry(QtCore.QRect(260, 100, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Int_Max_LineEdit.setFont(font)
        self.Int_Max_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Int_Max_LineEdit.setObjectName("Int_Max_LineEdit")


        self.Qz_Max_LineEdit = QtWidgets.QLineEdit(self.MinMax_Frame)
        self.Qz_Max_LineEdit.setGeometry(QtCore.QRect(160, 100, 70, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Qz_Max_LineEdit.setFont(font)
        self.Qz_Max_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Qz_Max_LineEdit.setObjectName("Qz_Max_LineEdit")


        self.Qxy_Max_LineEdit = QtWidgets.QLineEdit(self.MinMax_Frame)
        self.Qxy_Max_LineEdit.setGeometry(QtCore.QRect(60, 100, 70, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Qxy_Max_LineEdit.setFont(font)
        self.Qxy_Max_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Qxy_Max_LineEdit.setObjectName("Qxy_Max_LineEdit")


        self.Max_Label = QtWidgets.QLabel(self.MinMax_Frame)
        self.Max_Label.setGeometry(QtCore.QRect(0, 100, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Max_Label.setFont(font)
        self.Max_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Max_Label.setObjectName("Max_Label")


        self.Appearance_Frame = QtWidgets.QFrame(self.Analysis_GroupBox)
        self.Appearance_Frame.setGeometry(QtCore.QRect(400, 160, 370, 151))
        self.Appearance_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Appearance_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Appearance_Frame.setObjectName("Appearance_Frame")


        self.Log_CheckBox = QtWidgets.QCheckBox(self.Appearance_Frame)
        self.Log_CheckBox.setGeometry(QtCore.QRect(230, 70, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Log_CheckBox.setFont(font)
        self.Log_CheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Log_CheckBox.setObjectName("Log_CheckBox")


        self.Font_ComboBox = QtWidgets.QFontComboBox(self.Appearance_Frame)
        self.Font_ComboBox.setGeometry(QtCore.QRect(10, 40, 130, 30))
        font = QtGui.QFont()
        font.setPixelSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Font_ComboBox.setFont(font)
        self.Font_ComboBox.setObjectName("Font_ComboBox")


        self.CM_ComboBox = QtWidgets.QComboBox(self.Appearance_Frame)
        self.CM_ComboBox.setGeometry(QtCore.QRect(220, 40, 140, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.CM_ComboBox.setFont(font)
        self.CM_ComboBox.setObjectName("CM_ComboBox")
        self.CM_ComboBox.addItems(plt.colormaps())


        self.FS_LineEdit = QtWidgets.QLineEdit(self.Appearance_Frame)
        self.FS_LineEdit.setGeometry(QtCore.QRect(140, 40, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.FS_LineEdit.setFont(font)
        self.FS_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FS_LineEdit.setObjectName("FS_LineEdit")


        self.Font_Label = QtWidgets.QLabel(self.Appearance_Frame)
        self.Font_Label.setGeometry(QtCore.QRect(80, 10, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Font_Label.setFont(font)
        self.Font_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Font_Label.setObjectName("Font_Label")


        self.CM_Label = QtWidgets.QLabel(self.Appearance_Frame)
        self.CM_Label.setGeometry(QtCore.QRect(240, 10, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CM_Label.setFont(font)
        self.CM_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.CM_Label.setObjectName("CM_Label")


        self.AI_Label = QtWidgets.QLabel(self.Appearance_Frame)
        self.AI_Label.setGeometry(QtCore.QRect(10, 110, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AI_Label.setFont(font)
        self.AI_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.AI_Label.setObjectName("AI_Label")


        self.Major_Label = QtWidgets.QLabel(self.Appearance_Frame)
        self.Major_Label.setGeometry(QtCore.QRect(100, 110, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Major_Label.setFont(font)
        self.Major_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Major_Label.setObjectName("Major_Label")


        self.Minor_Label = QtWidgets.QLabel(self.Appearance_Frame)
        self.Minor_Label.setGeometry(QtCore.QRect(240, 110, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Minor_Label.setFont(font)
        self.Minor_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Minor_Label.setObjectName("Minor_Label")


        self.Major_LineEdit = QtWidgets.QLineEdit(self.Appearance_Frame)
        self.Major_LineEdit.setGeometry(QtCore.QRect(160, 110, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Major_LineEdit.setFont(font)
        self.Major_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Major_LineEdit.setObjectName("Major_LineEdit")


        self.Minor_LineEdit = QtWidgets.QLineEdit(self.Appearance_Frame)
        self.Minor_LineEdit.setGeometry(QtCore.QRect(300, 110, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Minor_LineEdit.setFont(font)
        self.Minor_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Minor_LineEdit.setObjectName("Minor_LineEdit")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.CF_LineEdit, self.CF_Browse_PushButton)
        MainWindow.setTabOrder(self.CF_Browse_PushButton, self.AgBe_RadioButton)
        MainWindow.setTabOrder(self.AgBe_RadioButton, self.LaB6_RadioButton)
        MainWindow.setTabOrder(self.LaB6_RadioButton, self.Energy_LineEdit)
        MainWindow.setTabOrder(self.Energy_LineEdit, self.PS_LineEdit)
        MainWindow.setTabOrder(self.PS_LineEdit, self.Width_LineEdit)
        MainWindow.setTabOrder(self.Width_LineEdit, self.Height_LineEdit)
        MainWindow.setTabOrder(self.Height_LineEdit, self.Calibration_PushButton)
        MainWindow.setTabOrder(self.Calibration_PushButton, self.BC_x_LineEdit)
        MainWindow.setTabOrder(self.BC_x_LineEdit, self.BC_y_LineEdit)
        MainWindow.setTabOrder(self.BC_y_LineEdit, self.SDD_LineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "X-Ray Scattring Analyzer"))
        self.Main_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">X-Ray Scattering Analyzer</span></p></body></html>"))
        self.Calibration_GroupBox.setTitle(_translate("MainWindow", "Calibration"))
        self.CF_Label.setText(_translate("MainWindow", "File:"))
        self.Calibrant_Label.setText(_translate("MainWindow", "Calibrant:"))
        self.AgBe_RadioButton.setText(_translate("MainWindow", "AgBe"))
        self.LaB6_RadioButton.setText(_translate("MainWindow", "LaB6"))
        self.Energy_Label.setText(_translate("MainWindow", "Energy (keV):"))
        self.PS_Label.setText(_translate("MainWindow", "Pixel Size (mm):"))
        self.CF_Browse_PushButton.setText(_translate("MainWindow", "Browse..."))
        self.Resolution_Label.setText(_translate("MainWindow", "Image Resolution:"))
        self.Width_Label.setText(_translate("MainWindow", "Width"))
        self.Height_Label.setText(_translate("MainWindow", "Height"))
        self.Calibration_PushButton.setText(_translate("MainWindow", "Calibrate"))
        self.BeamCenter_Label.setText(_translate("MainWindow", "Beam Center:"))
        self.BC_x_Label.setText(_translate("MainWindow", "x-pixel"))
        self.BC_y_Label.setText(_translate("MainWindow", "y-pixel"))
        self.SDD_Label.setText(_translate("MainWindow", "SDD (mm):"))
        self.Analysis_GroupBox.setTitle(_translate("MainWindow", "Analysis"))
        self.IF_Label.setText(_translate("MainWindow", "File:"))
        self.IF_Browse_PushButton.setText(_translate("MainWindow", "Browse..."))
        self.IA_Label.setText(_translate("MainWindow", "Incident Angle (˚):"))
        self.CA_PushButton.setText(_translate("MainWindow", "Circular Average"))
        self.GIXS_PushButton.setText(_translate("MainWindow", "GIXS Image"))
        self.IP_PushButton.setText(_translate("MainWindow", "IP Linecut"))
        self.OOP_PushButton.setText(_translate("MainWindow", "OOP Linecut"))
        self.GIXS_Params_Label.setText(_translate("MainWindow", "GIXS Image Parameters"))
        self.Int_Label.setText(_translate("MainWindow", "Intensity"))
        self.Qz_Label.setText(_translate("MainWindow", "Qz (1/A)"))
        self.Qz_Min_LineEdit.setText(_translate("MainWindow", "0"))
        self.Qxy_Label.setText(_translate("MainWindow", "Qxy (1/A)"))
        self.Qxy_Min_LineEdit.setText(_translate("MainWindow", "0"))
        self.Min_Label.setText(_translate("MainWindow", "Min:"))
        self.Qz_Max_LineEdit.setText(_translate("MainWindow", "2.5"))
        self.Qxy_Max_LineEdit.setText(_translate("MainWindow", "2.5"))
        self.Max_Label.setText(_translate("MainWindow", "Max:"))
        self.Log_CheckBox.setText(_translate("MainWindow", "Log Image?"))
        self.FS_LineEdit.setText(_translate("MainWindow", "16"))
        self.Font_Label.setText(_translate("MainWindow", "Font"))
        self.CM_Label.setText(_translate("MainWindow", "Colormap"))
        self.AI_Label.setText(_translate("MainWindow", "Ticks:"))
        self.Major_Label.setText(_translate("MainWindow", "Major"))
        self.Minor_Label.setText(_translate("MainWindow", "Minor"))
        self.Major_LineEdit.setText(_translate("MainWindow", "1.0"))
        self.Minor_LineEdit.setText(_translate("MainWindow", "0.5"))


    def CF_Browse(self):

        # Try to load the selected image file
        try:
            calibFile, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Please select a calibration image file', './', 'TIFF Files (*.tif)')
        except:
            return

        self.CF_LineEdit.setText(calibFile)


        # Get the image resolution and fill in the height and width
        try:
            img = imread(calibFile)
            img_size = img.shape
            self.Height_LineEdit.setText(str(img_size[0]))
            self.Width_LineEdit.setText(str(img_size[1]))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Invalid image file!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

    def calcSDD(self):

        # Load calibration image
        try:
            img_filename = self.CF_LineEdit.text()
            img = imread(img_filename)
        
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Invalid image file!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return


        # Get X-Ray Wavelength and Pixel Size
        try:
            xlam = 12.3984/float(self.Energy_LineEdit.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Please enter a valid X-ray energy!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return


        # Get detector pixel size
        try:
            pix_size = float(self.PS_LineEdit.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Please enter a valid pixel size!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return


        # Create figure for calibration
        plt.ion()
        imshow(np.ma.log(img), cmap='RdBu_r')


        # Set d-spacing based on selected calibrant
        if self.AgBe_RadioButton.isChecked():
            d_spacing = 58.378/3
            plt.title('Select points on 3rd diffraction ring', size=20)
        else:
            d_spacing = 4.159/np.sqrt(2)
            plt.title('Select points on the 2nd diffraction ring', size=20)


        # Get points around the calibration image and fit to circle
        coords = plt.ginput(30, timeout=0)
        coords = np.transpose([list(i) for i in coords])
        par = self.circleFit(coords)


        # Plot calibrated ring
        theta = np.linspace(0, 2*np.pi, 1000)
        plt.plot(par[2]*np.sin(theta) + par[0], par[2]*np.cos(theta) + par[1], color='black', linewidth=4)
        plt.scatter(par[0], par[1], s=50, color='yellow')
        plt.draw()


        # Calculate the SDD
        r = par[2]*pix_size
        theta = np.arcsin(xlam/(2*d_spacing))
        sdd = np.round(r/np.tan(2*theta), 3)

        # Update beam center and SDD
        self.BC_x_LineEdit.setText(str(int(par[0])))
        self.BC_y_LineEdit.setText(str(int(par[1])))
        self.SDD_LineEdit.setText(str(sdd))



    ## Function to fit list of points to circle using the Newton-Taubin method ##

    def circleFit(self, coords):

        # Initial variables
        n = coords.shape[1]
        centroid = [np.mean(i) for i in coords]

        # Initialize moments
        Mxx = 0
        Myy = 0
        Mxy = 0
        Mxz = 0
        Myz = 0
        Mzz = 0

        for i in range(n):
            Xi = coords[0][i] - centroid[0]
            Yi = coords[1][i] - centroid[1]
            Zi = Xi*Xi + Yi*Yi
            Mxy = Mxy + Xi*Yi
            Mxx = Mxx + Xi*Xi
            Myy = Myy + Yi*Yi
            Mxz = Mxz + Xi*Zi
            Myz = Myz + Yi*Zi
            Mzz = Mzz + Zi*Zi

        Mxx = Mxx/n
        Myy = Myy/n
        Mxy = Mxy/n
        Mxz = Mxz/n
        Myz = Myz/n
        Mzz = Mzz/n

        # Compute coefficients of characteristic polynomial
        Mz = Mxx + Myy
        Cov_xy = Mxx*Myy - Mxy*Mxy
        Mxz2 = Mxz*Mxz
        Myz2 = Myz*Myz
        A3 = 4*Mz
        A2 = 4*Cov_xy - 3*Mz*Mz - Mzz
        A1 = Mzz*Mz + 4*Cov_xy*Mz - Mxz2 - Myz2 - Mz*Mz*Mz
        A0 = Mxz*Mxz*Myy + Myz*Myz*Mxx - Mzz*Cov_xy - 2*Mxz*Myz*Mxy + Mz*Mz*Cov_xy
        A22 = A2 + A2
        A33 = A3 + A3 + A3
        
        xnew = 0;
        ynew = 1e+20
        epsilon = 1e-12
        IterMax = 20
        
        # Newton's method starting at x=0
        for iter in range(IterMax):
            yold = ynew
            ynew = A0 + xnew*(A1 + xnew*(A2 + xnew*A3))
            if np.abs(ynew) > np.abs(yold):
                print('Newton-Taubin goes wrong direction: |ynew| > |yold|')
                xnew = 0
                break
            Dy = A1 + xnew*(A22 + xnew*A33)
            xold = xnew
            xnew = xold - ynew/Dy
            if np.abs((xnew - xold)/xnew) < epsilon:
                break
            if iter >= IterMax:
                print('Newton-Taubin will not converge')
                xnew = 0
            if xnew < 0:
                print('Newton-Taubin negative root')
                xnew = 0
        
        # Compute circle parameters
        DET = xnew*xnew - xnew*Mz + Cov_xy
        Center = [Mxz*(Myy - xnew) - Myz*Mxy, Myz*(Mxx - xnew) - Mxz*Mxy]/DET/2 
        par = np.append(Center + centroid, np.sqrt(np.dot(Center, Center) + Mz))

        return par


    def IF_Browse(self):

        # Try to load the selected image file
        try:
            calibFile, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Please select a calibration image file', './', 'TIFF Files (*.tif)')
        except:
            return

        self.IF_LineEdit.setText(calibFile)


        # Get the image intensities min/max and fill them in
        try:
            img = imread(calibFile)
            self.Int_Min_LineEdit.setText(str(img.min()))
            self.Int_Max_LineEdit.setText(str(img.max()))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Invalid image file!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return


    def calcCA(self):

        # Get calibration values
        try:
            cen_x = float(self.BC_x_LineEdit.text())
            cen_y = float(self.BC_y_LineEdit.text())
            sdd = float(self.SDD_LineEdit.text())
            xlam = 12.3984/float(self.Energy_LineEdit.text())
            pix_size = float(self.PS_LineEdit.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Make sure you have done calibration!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Load image file
        try:
            img_filename = self.IF_LineEdit.text()
            img = imread(img_filename)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Invalid image file!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Get image parameters
        a = img.shape[0]
        b = img.shape[1]

        [X, Y] = np.meshgrid(np.arange(b) - cen_x, np.arange(a) - cen_y)
        R = np.sqrt(np.square(X) + np.square(Y))

        rad = np.arange(1, np.max(R), 1)
        intensity = np.zeros(len(rad))
        counter = 0

        for i in rad:
            mask = (np.greater(R, i - 1) & np.less(R, i + 1))
            values = img[mask]
            intensity[counter] = np.median(values)
            counter += 1
            
            # Update the progress bar on the screen based on the iteration of the loop
            QtWidgets.QApplication.processEvents()

        # Calculate scattering vector values at each radius
        q = (4*np.pi/xlam)*np.sin(np.arctan((rad*pix_size)/sdd)/2)

        # Save Averaging Data
        saveFileName = Path(img_filename)
        saveFileName = str(saveFileName.parent) + '/' + str(saveFileName.stem) + '_CircAvg.csv'
        np.savetxt(saveFileName, np.c_[q, intensity], delimiter=',', header='q (1/A), Intensity', comments='')

        # Show plot
        plt.ion()
        plt.plot(q, intensity)

        # Axis labels
        plt.xlabel('q (1/A)', labelpad=10)
        plt.ylabel('Intensity', labelpad=10)
        
        plt.show()


    def calcGIXS(self):

        cen_x = float(self.BC_x_LineEdit.text())
        cen_y = float(self.BC_y_LineEdit.text())
        sdd = float(self.SDD_LineEdit.text())
        xlam = 12.3984/float(self.Energy_LineEdit.text())
        pix_size = float(self.PS_LineEdit.text())
        inc_ang = (np.pi/180)*float(self.IA_LineEdit.text())
        k = 2*np.pi/xlam

        # Get image filename
        img_filename = self.IF_LineEdit.text()
        img = imread(img_filename)

        # Get image parameters
        a = img.shape[0]
        b = img.shape[1]

        # Create new image
        img2 = np.concatenate((img[:, 0:int(cen_x + 1)], np.full((a, 1), 0), img[:, int(cen_x):]), axis=1)

        # Create meshgrids for X and Z pixels
        X, Z = np.meshgrid(np.arange(b + 3) - int(cen_x + 1), np.arange(a + 1) - int(cen_y))
        X[:,int(cen_x + 2):] -= 1

        # Calculate angles for q-maps
        L = np.sqrt(np.square(pix_size*X) + sdd**2)
        theta = np.arctan(pix_size*np.divide(Z, L))
        phi = np.arctan(pix_size*X/sdd)

        # Calculate q-maps
        q_x = k*np.multiply(np.cos(theta), np.sin(phi))
        q_y = k*np.multiply(np.cos(theta), np.cos(phi)) - k*np.cos(inc_ang)
        q_z = -k*np.sin(theta) + k*np.sin(inc_ang)

        # Calculate q_r
        q_r = np.sqrt(np.square(q_x) + np.square(q_y))
        q_r[:, 0:int(cen_x + 2)] = -1*q_r[:, 0:int(cen_x + 2)]

        # Get plot parameters
        qxy_min = float(self.Qxy_Min_LineEdit.text())
        qxy_max = float(self.Qxy_Max_LineEdit.text())
        qz_min = float(self.Qz_Min_LineEdit.text())
        qz_max = float(self.Qz_Max_LineEdit.text())
        int_min = float(self.Int_Min_LineEdit.text())
        int_max = float(self.Int_Max_LineEdit.text())
        font_name = str(self.Font_ComboBox.currentFont().family())
        font_size = int(self.FS_LineEdit.text())
        log_color = self.Log_CheckBox.isChecked()
        colormap = self.CM_ComboBox.currentText()
        tick_major = float(self.Major_LineEdit.text())
        tick_minor = float(self.Minor_LineEdit.text())

        if log_color:
            img2 = np.ma.log(img2)
            
            if int_min != 0:
                int_min = np.log(int_min)

            if int_max != 0:
                int_max = np.log(int_max)


        # Create figures
        mpl.rcParams['font.family'] = font_name
        plt.rcParams['axes.linewidth'] = 1.5
        plt.rcParams['font.size'] = font_size

        # In case of different aspect ratios
        ratio = (qxy_max - qxy_min)/(qz_max - qz_min)

        # Generate figure and subplot
        plt.ion()
        fig = plt.figure(figsize=(ratio*3, 3), tight_layout=True, dpi=300)
        ax = plt.subplot(111)

        # Set tick parameters
        ax.xaxis.set_tick_params(size=7, width=1.5, direction='out')
        ax.xaxis.set_tick_params(which='minor', size=5, width=1.5, direction='out')
        ax.yaxis.set_tick_params(size=7, width=1.5, direction='out')
        ax.yaxis.set_tick_params(which='minor', size=5, width=1.5, direction='out')

        ax.pcolormesh(q_r, q_z, img2, vmin=int_min, vmax=int_max, cmap=colormap, shading='flat')

        ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(tick_major))
        ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(tick_major))
        ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(tick_minor))
        ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(tick_minor))

        ax.set_xlabel(u'q$\mathregular{_{xy}}$ (\u00c5$\mathregular{^{-1}}$)')
        ax.set_ylabel(u'q$\mathregular{_{z}}$ (\u00c5$\mathregular{^{-1}}$)')

        ax.set_xlim(qxy_min, qxy_max)
        ax.set_ylim(qz_min, qz_max)

        saveFileName = Path(img_filename)
        saveFileName = str(saveFileName.parent) + '/' + str(saveFileName.stem) + '_GIXS.png'

        plt.savefig(saveFileName)
        plt.show()


    def calcIP(self):

        cen_x = float(self.BC_x_LineEdit.text())
        cen_y = float(self.BC_y_LineEdit.text())
        sdd = float(self.SDD_LineEdit.text())
        xlam = 12.3984/float(self.Energy_LineEdit.text())
        pix_size = float(self.PS_LineEdit.text())
        inc_ang = (np.pi/180)*float(self.IA_LineEdit.text())
        k = 2*np.pi/xlam

        # Get image filename
        img_filename = self.IF_LineEdit.text()
        img = imread(img_filename)

        # Get image parameters
        a = img.shape[0]
        b = img.shape[1]

        # Create meshgrids for X and Z pixels
        X, Z = np.meshgrid(np.arange(b) - int(cen_x), np.arange(a) - int(cen_y))

        # Calculate angles for q-maps
        L = np.sqrt(np.square(pix_size*X) + sdd**2)
        theta = np.arctan(pix_size*np.divide(Z, L))
        phi = np.arctan(pix_size*X/sdd)

        # Calculate q-maps
        q_x = k*np.multiply(np.cos(theta), np.sin(phi))
        q_y = k*np.multiply(np.cos(theta), np.cos(phi)) - k*np.cos(inc_ang)
        q_z = -k*np.sin(theta) + k*np.sin(inc_ang)

        # Calculate q_r
        q_r = np.sqrt(np.square(q_x) + np.square(q_y))
        q_r[:, 0:int(cen_x)] *= -1

        # Get in-plane q vector
        q_ip = q_r[int(cen_y)]

        # Get intensity from image (use 15 pixel average)
        int_ip = np.mean([img[int(cen_y - 14), :], img[int(cen_y - 13), :], img[int(cen_y - 12), :], img[int(cen_y - 11), :], img[int(cen_y - 10), :], img[int(cen_y - 9), :], img[int(cen_y - 8), :], img[int(cen_y - 7), :], img[int(cen_y - 6), :], img[int(cen_y - 5), :], img[int(cen_y - 4), :], img[int(cen_y - 3), :], img[int(cen_y - 2), :], img[int(cen_y - 1), :], img[int(cen_y), :]], axis=0)
        print(len(int_ip))

        # Make sure data is sorted
        int_ip = [x for (y,x) in sorted(zip(q_ip, int_ip))]
        q_ip = sorted(q_ip)
        
        # Save linecut data
        saveFileName = Path(img_filename)
        saveFileName = str(saveFileName.parent) + '/' + str(saveFileName.stem) + '_IP_Linecut.csv'
        np.savetxt(saveFileName, np.c_[q_ip, int_ip], delimiter=',', header='q_xy (1/A), Intensity', comments='')

        # Plot in-plane linecut
        plt.ion()
        plt.plot(q_ip, int_ip)

        # Axis labels
        plt.xlabel('q_xy (1/A)', labelpad=10)
        plt.ylabel('Intensity', labelpad=10)

        # Show plot
        plt.show()


    def calcOOP(self):

        cen_x = float(self.BC_x_LineEdit.text())
        cen_y = float(self.BC_y_LineEdit.text())
        sdd = float(self.SDD_LineEdit.text())
        xlam = 12.3984/float(self.Energy_LineEdit.text())
        pix_size = float(self.PS_LineEdit.text())
        inc_ang = (np.pi/180)*float(self.IA_LineEdit.text())
        k = 2*np.pi/xlam

        # Get image filename
        img_filename = self.IF_LineEdit.text()
        img = imread(img_filename)

        # Get image parameters
        a = img.shape[0]
        b = img.shape[1]

        # Create meshgrids for X and Z pixels
        X, Z = np.meshgrid(np.arange(b) - int(cen_x), np.arange(a) - int(cen_y))

        # Calculate angles for q-maps
        L = np.sqrt(np.square(pix_size*X) + sdd**2)
        theta = np.arctan(pix_size*np.divide(Z, L))
        phi = np.arctan(pix_size*X/sdd)

        # Calculate q-maps
        q_x = k*np.multiply(np.cos(theta), np.sin(phi))
        q_y = k*np.multiply(np.cos(theta), np.cos(phi)) - k*np.cos(inc_ang)
        q_z = -k*np.sin(theta) + k*np.sin(inc_ang)

        # Calculate q_r
        q = np.transpose(np.sqrt(np.square(q_x) + np.square(q_y) + np.square(q_z)))
        q[:, int(cen_y):] *= -1

        q_oop = q[int(cen_x)]

        img = np.transpose(img)

        # Get intensity from image (use 11 pixel average)
        int_oop = (1/11)*(img[int(cen_x - 5), :] + img[int(cen_x - 4), :] + img[int(cen_x - 3), :] + img[int(cen_x - 2), :] + img[int(cen_x - 1), :] + img[int(cen_x), :] + img[int(cen_x + 1), :] + img[int(cen_x + 2), :] + img[int(cen_x + 3), :] + img[int(cen_x + 4), :] + img[int(cen_x + 5), :])
        
        # Make sure the data is sorted
        int_oop = [x for (y,x) in sorted(zip(q_oop, int_oop))]
        q_oop = sorted(q_oop)

        # Save linecut data
        saveFileName = Path(img_filename)
        saveFileName = str(saveFileName.parent) + '/' + str(saveFileName.stem) + '_OOP_Linecut.csv'
        np.savetxt(saveFileName, np.c_[q_oop, int_oop], delimiter=',', header='q (1/A), Intensity', comments='')

        # Plot out-of-plane linecut
        plt.ion()
        plt.plot(q_oop, int_oop)

        # Axis labels
        plt.xlabel('q (1/A)', labelpad=10)
        plt.ylabel('Intensity', labelpad=10)

        # Show plot
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())