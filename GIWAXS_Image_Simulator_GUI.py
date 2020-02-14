###---------- GIWAXS Image Simulator ---------###
###--------------- Version 1.0 ---------------###
###---------- Updated: February 2020 ---------###
###------ Developed by Naveen Venkatesan -----###

## Import required packages
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import numpy as np
from pathlib import Path
from tifffile import imsave, imshow
import matplotlib.pyplot as plt
import matplotlib as mpl


## Generate program window and associated functions
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        # Create main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        

        # Populate the main window with central widget object
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        # Program title - GIWAXS Image Simulator
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(250, 10, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Title_Label.setFont(font)
        self.Title_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_Label.setObjectName("Title_Label")
        

        # Group box to contain the CIF file section
        self.CF_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.CF_GroupBox.setGeometry(QtCore.QRect(10, 40, 780, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CF_GroupBox.setFont(font)
        self.CF_GroupBox.setObjectName("CF_GroupBox")
        

        # Line Edit box for the CIF file location
        self.CF_LineEdit = QtWidgets.QLineEdit(self.CF_GroupBox)
        self.CF_LineEdit.setGeometry(QtCore.QRect(10, 30, 651, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.CF_LineEdit.setFont(font)
        self.CF_LineEdit.setObjectName("CF_LineEdit")
        

        # Push button to browse for CIF file location
        self.CF_Browse_PushButton = QtWidgets.QPushButton(self.CF_GroupBox)
        self.CF_Browse_PushButton.setGeometry(QtCore.QRect(665, 26, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.CF_Browse_PushButton.setFont(font)
        self.CF_Browse_PushButton.setObjectName("CF_Browse_PushButton")
        self.CF_Browse_PushButton.clicked.connect(self.CF_Browse)
        

        # Group box to contain the structure factor file section
        self.SF_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SF_GroupBox.setGeometry(QtCore.QRect(10, 130, 780, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SF_GroupBox.setFont(font)
        self.SF_GroupBox.setObjectName("SF_GroupBox")
        

        # Line Edit box for the structure factor file location
        self.SF_LineEdit = QtWidgets.QLineEdit(self.SF_GroupBox)
        self.SF_LineEdit.setGeometry(QtCore.QRect(10, 30, 651, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.SF_LineEdit.setFont(font)
        self.SF_LineEdit.setObjectName("SF_LineEdit")
        

        # Push button to browse for the structure factor file location
        self.SF_Browse_PushButton = QtWidgets.QPushButton(self.SF_GroupBox)
        self.SF_Browse_PushButton.setGeometry(QtCore.QRect(665, 26, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.SF_Browse_PushButton.setFont(font)
        self.SF_Browse_PushButton.setObjectName("SF_Browse_PushButton")
        self.SF_Browse_PushButton.clicked.connect(self.SF_Browse)
        

        # Group box to contain simulation parameters
        self.SP_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SP_GroupBox.setGeometry(QtCore.QRect(10, 220, 780, 220))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SP_GroupBox.setFont(font)
        self.SP_GroupBox.setObjectName("SP_GroupBox")
        

        # Frame to contain the lattice parameter section
        self.LP_Frame = QtWidgets.QFrame(self.SP_GroupBox)
        self.LP_Frame.setGeometry(QtCore.QRect(10, 60, 340, 150))
        self.LP_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LP_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LP_Frame.setObjectName("LP_Frame")


        # Label for the lattice parameters section
        self.LP_Label = QtWidgets.QLabel(self.SP_GroupBox)
        self.LP_Label.setGeometry(QtCore.QRect(105, 30, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LP_Label.setFont(font)
        self.LP_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_Label.setObjectName("LP_Label")
        

        # Label for the a lattice parameter
        self.LP_a_Label = QtWidgets.QLabel(self.LP_Frame)
        self.LP_a_Label.setGeometry(QtCore.QRect(10, 20, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.LP_a_Label.setFont(font)
        self.LP_a_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_a_Label.setObjectName("LP_a_Label")


        # Line Edit box for the a lattice parameter
        self.LP_a_LineEdit = QtWidgets.QLineEdit(self.LP_Frame)
        self.LP_a_LineEdit.setGeometry(QtCore.QRect(40, 20, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LP_a_LineEdit.setFont(font)
        self.LP_a_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_a_LineEdit.setObjectName("LP_a_LineEdit")
        

        # Label for the b lattice parameter
        self.LP_b_Label = QtWidgets.QLabel(self.LP_Frame)
        self.LP_b_Label.setGeometry(QtCore.QRect(10, 60, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.LP_b_Label.setFont(font)
        self.LP_b_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_b_Label.setObjectName("LP_b_Label")


        # Line Edit box for the b lattice parameter
        self.LP_b_LineEdit = QtWidgets.QLineEdit(self.LP_Frame)
        self.LP_b_LineEdit.setGeometry(QtCore.QRect(40, 60, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LP_b_LineEdit.setFont(font)
        self.LP_b_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_b_LineEdit.setObjectName("LP_b_LineEdit")
        

        # Label for the c lattice parameter
        self.LP_c_Label = QtWidgets.QLabel(self.LP_Frame)
        self.LP_c_Label.setGeometry(QtCore.QRect(10, 100, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.LP_c_Label.setFont(font)
        self.LP_c_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_c_Label.setObjectName("LP_c_Label")


        # Line Edit box for the c lattice parameter
        self.LP_c_LineEdit = QtWidgets.QLineEdit(self.LP_Frame)
        self.LP_c_LineEdit.setGeometry(QtCore.QRect(40, 100, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LP_c_LineEdit.setFont(font)
        self.LP_c_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_c_LineEdit.setObjectName("LP_c_LineEdit")
        

        # Label for the alpha lattice angle
        self.LP_alpha_Label = QtWidgets.QLabel(self.LP_Frame)
        self.LP_alpha_Label.setGeometry(QtCore.QRect(180, 20, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.LP_alpha_Label.setFont(font)
        self.LP_alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_alpha_Label.setObjectName("LP_alpha_Label")


        # Line Edit box for the alpha lattice angle
        self.LP_alpha_LineEdit = QtWidgets.QLineEdit(self.LP_Frame)
        self.LP_alpha_LineEdit.setGeometry(QtCore.QRect(210, 20, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LP_alpha_LineEdit.setFont(font)
        self.LP_alpha_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_alpha_LineEdit.setObjectName("LP_alpha_LineEdit")
        

        # Label for the beta lattice angle
        self.LP_beta_Label = QtWidgets.QLabel(self.LP_Frame)
        self.LP_beta_Label.setGeometry(QtCore.QRect(180, 60, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.LP_beta_Label.setFont(font)
        self.LP_beta_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_beta_Label.setObjectName("LP_beta_Label")


        # Line Edit box for the beta lattice angle
        self.LP_beta_LineEdit = QtWidgets.QLineEdit(self.LP_Frame)
        self.LP_beta_LineEdit.setGeometry(QtCore.QRect(210, 60, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LP_beta_LineEdit.setFont(font)
        self.LP_beta_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_beta_LineEdit.setObjectName("LP_beta_LineEdit")
        

        # Label for the gamma lattice angle
        self.LP_gamma_Label = QtWidgets.QLabel(self.LP_Frame)
        self.LP_gamma_Label.setGeometry(QtCore.QRect(180, 100, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.LP_gamma_Label.setFont(font)
        self.LP_gamma_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_gamma_Label.setObjectName("LP_gamma_Label")

        
        # Line Edit box for the gamma lattice angle
        self.LP_gamma_LineEdit = QtWidgets.QLineEdit(self.LP_Frame)
        self.LP_gamma_LineEdit.setGeometry(QtCore.QRect(210, 100, 100, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LP_gamma_LineEdit.setFont(font)
        self.LP_gamma_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_gamma_LineEdit.setObjectName("LP_gamma_LineEdit")
        

        # Angstrom unit label for a lattice parameter
        self.Ang_1_Label = QtWidgets.QLabel(self.LP_Frame)
        self.Ang_1_Label.setGeometry(QtCore.QRect(140, 20, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Ang_1_Label.setFont(font)
        self.Ang_1_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ang_1_Label.setObjectName("Ang_1_Label")
        

        # Angstrom unit label for b lattice parameter
        self.Ang_2_Label = QtWidgets.QLabel(self.LP_Frame)
        self.Ang_2_Label.setGeometry(QtCore.QRect(140, 60, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Ang_2_Label.setFont(font)
        self.Ang_2_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ang_2_Label.setObjectName("Ang_2_Label")
        

        # Angstrom unit label for the c lattice parameter
        self.Ang_3_Label = QtWidgets.QLabel(self.LP_Frame)
        self.Ang_3_Label.setGeometry(QtCore.QRect(140, 100, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Ang_3_Label.setFont(font)
        self.Ang_3_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ang_3_Label.setObjectName("Ang_3_Label")
        

        # Degree unit label for the alpha lattice angle
        self.Deg_1_Label = QtWidgets.QLabel(self.LP_Frame)
        self.Deg_1_Label.setGeometry(QtCore.QRect(310, 20, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Deg_1_Label.setFont(font)
        self.Deg_1_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Deg_1_Label.setObjectName("Deg_1_Label")
        

        # Degree unit label for the beta lattice angle
        self.Deg_2_Label = QtWidgets.QLabel(self.LP_Frame)
        self.Deg_2_Label.setGeometry(QtCore.QRect(310, 60, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Deg_2_Label.setFont(font)
        self.Deg_2_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Deg_2_Label.setObjectName("Deg_2_Label")
        

        # Degree unit label for the gamma lattice angle
        self.Deg_3_Label = QtWidgets.QLabel(self.LP_Frame)
        self.Deg_3_Label.setGeometry(QtCore.QRect(310, 100, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Deg_3_Label.setFont(font)
        self.Deg_3_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Deg_3_Label.setObjectName("Deg_3_Label")
        

        # Frame to contain the image resolution section
        self.IR_Frame = QtWidgets.QFrame(self.SP_GroupBox)
        self.IR_Frame.setGeometry(QtCore.QRect(360, 60, 230, 90))
        self.IR_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IR_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IR_Frame.setObjectName("IR_Frame")
        

        # Label for the image resolution section
        self.IR_Label = QtWidgets.QLabel(self.SP_GroupBox)
        self.IR_Label.setGeometry(QtCore.QRect(420, 30, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IR_Label.setFont(font)
        self.IR_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.IR_Label.setObjectName("IR_Label")


        # Label for the maximum Q_xy of the simulated image
        self.Qxy_Max_Label = QtWidgets.QLabel(self.IR_Frame)
        self.Qxy_Max_Label.setGeometry(QtCore.QRect(5, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Qxy_Max_Label.setFont(font)
        self.Qxy_Max_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Qxy_Max_Label.setObjectName("Qxy_Max_Label")
        

        # Line Edit box for the maximum value of Q_xy
        self.Qxy_Max_LineEdit = QtWidgets.QLineEdit(self.IR_Frame)
        self.Qxy_Max_LineEdit.setGeometry(QtCore.QRect(140, 10, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Qxy_Max_LineEdit.setFont(font)
        self.Qxy_Max_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Qxy_Max_LineEdit.setObjectName("Qxy_Max_LineEdit")
        

        # Label for the maximum Q_z of the simulated image
        self.Qz_Max_Label = QtWidgets.QLabel(self.IR_Frame)
        self.Qz_Max_Label.setGeometry(QtCore.QRect(5, 50, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Qz_Max_Label.setFont(font)
        self.Qz_Max_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Qz_Max_Label.setObjectName("Qz_Max_Label")
        

        # Line Edit box for the maximum value of Q_z
        self.Qz_Max_LineEdit = QtWidgets.QLineEdit(self.IR_Frame)
        self.Qz_Max_LineEdit.setGeometry(QtCore.QRect(140, 50, 80, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Qz_Max_LineEdit.setFont(font)
        self.Qz_Max_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Qz_Max_LineEdit.setObjectName("Qz_Max_LineEdit")
        

        # Frame to contain the peak shape section
        self.PS_Frame = QtWidgets.QFrame(self.SP_GroupBox)
        self.PS_Frame.setGeometry(QtCore.QRect(600, 60, 171, 91))
        self.PS_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PS_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PS_Frame.setObjectName("PS_Frame")


        # Label for the peak shape section
        self.PS_Label = QtWidgets.QLabel(self.SP_GroupBox)
        self.PS_Label.setGeometry(QtCore.QRect(630, 30, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PS_Label.setFont(font)
        self.PS_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_Label.setObjectName("PS_Label")
        

        # Label for the FWHM in the x-direction
        self.FWHM_x_Label = QtWidgets.QLabel(self.PS_Frame)
        self.FWHM_x_Label.setGeometry(QtCore.QRect(10, 10, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.FWHM_x_Label.setFont(font)
        self.FWHM_x_Label.setObjectName("FWHM_x_Label")
        

        # Line Edit box for the FWHM in the x-direction
        self.FWHM_x_LineEdit = QtWidgets.QLineEdit(self.PS_Frame)
        self.FWHM_x_LineEdit.setGeometry(QtCore.QRect(100, 10, 60, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.FWHM_x_LineEdit.setFont(font)
        self.FWHM_x_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FWHM_x_LineEdit.setObjectName("FWHM_x_LineEdit")


        # Label for the FWHM in the y-direction
        self.FWHM_y_Label = QtWidgets.QLabel(self.PS_Frame)
        self.FWHM_y_Label.setGeometry(QtCore.QRect(10, 50, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.FWHM_y_Label.setFont(font)
        self.FWHM_y_Label.setObjectName("FWHM_y_Label")
        

        # Line Edit box for the FWHM in the y-direction
        self.FWHM_y_LineEdit = QtWidgets.QLineEdit(self.PS_Frame)
        self.FWHM_y_LineEdit.setGeometry(QtCore.QRect(100, 50, 60, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.FWHM_y_LineEdit.setFont(font)
        self.FWHM_y_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FWHM_y_LineEdit.setObjectName("FWHM_y_LineEdit")
        

        # Frame to contain the preferred orientation section
        self.PO_Frame = QtWidgets.QFrame(self.SP_GroupBox)
        self.PO_Frame.setGeometry(QtCore.QRect(360, 160, 410, 50))
        self.PO_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PO_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PO_Frame.setObjectName("PO_Frame")
        

        # Label for the preferred orientation section
        self.PO_Label = QtWidgets.QLabel(self.PO_Frame)
        self.PO_Label.setGeometry(QtCore.QRect(5, 10, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PO_Label.setFont(font)
        self.PO_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.PO_Label.setObjectName("PO_Label")


        # Spin Box to select h-index of preferred orientation
        self.PO_h_SpinBox = QtWidgets.QSpinBox(self.PO_Frame)
        self.PO_h_SpinBox.setGeometry(QtCore.QRect(230, 10, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.PO_h_SpinBox.setFont(font)
        self.PO_h_SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PO_h_SpinBox.setMinimum(-10)
        self.PO_h_SpinBox.setMaximum(10)
        self.PO_h_SpinBox.setObjectName("PO_h_SpinBox")


        # Spin Box to select k-index of preferred orientation
        self.PO_k_SpinBox = QtWidgets.QSpinBox(self.PO_Frame)
        self.PO_k_SpinBox.setGeometry(QtCore.QRect(290, 10, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.PO_k_SpinBox.setFont(font)
        self.PO_k_SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PO_k_SpinBox.setMinimum(-10)
        self.PO_k_SpinBox.setMaximum(10)
        self.PO_k_SpinBox.setObjectName("PO_k_SpinBox")


        # Spin Box to select the l-index of preferred orientation
        self.PO_l_SpinBox = QtWidgets.QSpinBox(self.PO_Frame)
        self.PO_l_SpinBox.setGeometry(QtCore.QRect(350, 10, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.PO_l_SpinBox.setFont(font)
        self.PO_l_SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PO_l_SpinBox.setMinimum(-10)
        self.PO_l_SpinBox.setMaximum(10)
        self.PO_l_SpinBox.setObjectName("PO_l_SpinBox")
        
        
        # Push button to start GIWAXS simulation
        self.Simulate_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Simulate_PushButton.setGeometry(QtCore.QRect(10, 460, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Simulate_PushButton.setFont(font)
        self.Simulate_PushButton.setObjectName("Simulate_PushButton")
        self.Simulate_PushButton.clicked.connect(self.SimImage)
        

        # Progress bar for GIWAXS simulation
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(280, 460, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        

        # Set the central widget inside the main window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Call function to change the texts and titles of labels
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    ## Set the text in all the labels and the default parameters
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GIWAXS Image Simulator"))
        self.Title_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">GIWAXS Image Simulator</span></p></body></html>"))
        self.CF_GroupBox.setTitle(_translate("MainWindow", "CIF File"))
        self.CF_Browse_PushButton.setText(_translate("MainWindow", "Browse..."))
        self.SF_GroupBox.setTitle(_translate("MainWindow", "Structure Factor File"))
        self.SF_Browse_PushButton.setText(_translate("MainWindow", "Browse..."))
        self.SP_GroupBox.setTitle(_translate("MainWindow", "Simulation Parameters"))
        self.LP_a_Label.setText(_translate("MainWindow", "a:"))
        self.LP_b_Label.setText(_translate("MainWindow", "b:"))
        self.LP_c_Label.setText(_translate("MainWindow", "c:"))
        self.LP_alpha_Label.setText(_translate("MainWindow", "α:"))
        self.LP_beta_Label.setText(_translate("MainWindow", "β:"))
        self.LP_gamma_Label.setText(_translate("MainWindow", "γ:"))
        self.Ang_1_Label.setText(_translate("MainWindow", "Å"))
        self.Ang_2_Label.setText(_translate("MainWindow", "Å"))
        self.Ang_3_Label.setText(_translate("MainWindow", "Å"))
        self.Deg_1_Label.setText(_translate("MainWindow", "˚"))
        self.Deg_2_Label.setText(_translate("MainWindow", "˚"))
        self.Deg_3_Label.setText(_translate("MainWindow", "˚"))
        self.LP_Label.setText(_translate("MainWindow", "Lattice Parameters"))
        self.Qxy_Max_Label.setText(_translate("MainWindow", "Max Q_xy (1/Å):"))
        self.Qz_Max_Label.setText(_translate("MainWindow", "Max Q_z (1/A):"))
        self.IR_Label.setText(_translate("MainWindow", "Image Range"))
        self.FWHM_x_Label.setText(_translate("MainWindow", "FWHM (x):"))
        self.FWHM_y_Label.setText(_translate("MainWindow", "FWHM (y):"))
        self.PS_Label.setText(_translate("MainWindow", "Peak Shape"))
        self.PO_Label.setText(_translate("MainWindow", "Preferred Orientation (hkl):"))
        self.Simulate_PushButton.setText(_translate("MainWindow", "Simulate GIWAXS Pattern"))


    ## Function that handles the browsing for the CIF file
    def CF_Browse(self):

        # Open CIF file and set path
        fname, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open file', './','CIF files (*.cif)')
        self.CF_LineEdit.setText(fname)
        cif_file = Path(fname)
        

        # Extract lattice parameters and angles from CIF file
        try:
            with open(cif_file) as cif_data:
                
                # Iterate through lines in file
                for line in cif_data:

                    # Unit cell parameters
                    if '_cell_length_a' in line:
                        a = float(line.replace('_cell_length_a', '').replace(' ', '').replace('(', '').replace(')', ''))
                        self.LP_a_LineEdit.setText(str(a))
                    if '_cell_length_b' in line:
                        b = float(line.replace('_cell_length_b', '').replace(' ', '').replace('(', '').replace(')', ''))
                        self.LP_b_LineEdit.setText(str(b))
                    if '_cell_length_c' in line:
                        c = float(line.replace('_cell_length_c', '').replace(' ', '').replace('(', '').replace(')', ''))
                        self.LP_c_LineEdit.setText(str(c))

                    # Unit cell angles
                    if '_cell_angle_alpha' in line:
                        alpha = float(line.replace('_cell_angle_alpha', '').replace(' ', '').replace('(', '').replace(')', ''))
                        self.LP_alpha_LineEdit.setText(str(alpha))
                    if '_cell_angle_beta' in line:
                        beta = float(line.replace('_cell_angle_beta', '').replace(' ', '').replace('(', '').replace(')', ''))
                        self.LP_beta_LineEdit.setText(str(beta))
                    if '_cell_angle_gamma' in line:
                        gamma = float(line.replace('_cell_angle_gamma', '').replace(' ', '').replace('(', '').replace(')', ''))
                        self.LP_gamma_LineEdit.setText(str(gamma))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Invalid CIF file!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return


    ## Function that handles browsing for the structure factor file
    def SF_Browse(self):

        # Set SF file path
        fname, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open file', './','Text files (*.txt)')
        self.SF_LineEdit.setText(fname)


    def SimImage(self):
        
        # Convert lattice angles to radians
        try:
            alpha = float(self.LP_alpha_LineEdit.text())*np.pi/180
            beta = float(self.LP_beta_LineEdit.text())*np.pi/180
            gamma = float(self.LP_gamma_LineEdit.text())*np.pi/180
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Check lattice angles!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return 

        # Get lattice parameters
        try:
            a = float(self.LP_a_LineEdit.text())
            b = float(self.LP_b_LineEdit.text())
            c = float(self.LP_c_LineEdit.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Check lattice parameters!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Calculate reciprocal lattice parameters
        V = (a*b*c)*np.sqrt(1 - (np.cos(alpha))**2 - (np.cos(beta))**2 - (np.cos(gamma))**2 + 2*np.cos(alpha)*np.cos(beta)*np.cos(gamma))
        a_r = (b*c*np.sin(alpha))/V
        b_r = (c*a*np.sin(beta))/V
        c_r = (a*b*np.sin(gamma))/V

        # Calculate reciprocal lattice angles
        alpha_r = np.arccos((np.cos(beta)*np.cos(gamma) - np.cos(alpha))/(np.sin(beta)*np.sin(gamma)))
        beta_r = np.arccos((np.cos(alpha)*np.cos(gamma) - np.cos(beta))/(np.sin(alpha)*np.sin(gamma)))
        gamma_r = np.arccos((np.cos(alpha)*np.cos(beta) - np.cos(gamma))/(np.sin(alpha)*np.sin(beta)))

        # Get preferred orientation direction
        h_pref = float(self.PO_h_SpinBox.value())
        k_pref = float(self.PO_k_SpinBox.value())
        l_pref = float(self.PO_l_SpinBox.value())
        pref_orientation = str(int(h_pref)) + str(int(k_pref)) + str(int(l_pref))

        # Make sure direction is not 000 -- will cause divide by zero error
        if h_pref == 0 and k_pref == 0 and l_pref == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Set a preferred orientation direction!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Calculate d-spacing of the preferred orientation plane
        d_pref = 1/(np.sqrt((h_pref*a_r)**2 + (k_pref*b_r)**2 + (l_pref*c_r)**2 + 2*k_pref*l_pref*b_r*c_r*np.cos(alpha_r)
                           + 2*l_pref*h_pref*c_r*a_r*np.cos(beta_r) + 2*h_pref*k_pref*a_r*b_r*np.cos(gamma_r)))

        # Get range of Q values for GIXRD simulation
        try:
            q_xy_max = float(self.Qxy_Max_LineEdit.text())
            q_z_max = float(self.Qz_Max_LineEdit.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Check Q range values!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Get peak widths
        try:
            fwhm_x = float(self.FWHM_x_LineEdit.text())
            fwhm_y = float(self.FWHM_y_LineEdit.text())
            sigma_x = fwhm_x/2.355
            sigma_y = fwhm_y/2.355
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Check FWHM values!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Import structure factor data
        try:
            sf_filename = Path(self.SF_LineEdit.text())
            h, k, l, d, I = np.loadtxt(sf_filename, unpack=True, usecols=(0, 1, 2, 3, 6), skiprows=1) 
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('Invalid structure factor file!')
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

        # Intensity is given by the square of the structure factor
        I = np.multiply(I,I)

        # Sort reflections based on intensity
        h = [x for (y,x) in sorted(zip(I,h), reverse=True)]
        k = [x for (y,x) in sorted(zip(I,k), reverse=True)]
        l = [x for (y,x) in sorted(zip(I,l), reverse=True)]
        d = [x for (y,x) in sorted(zip(I,d), reverse=True)]
        I = sorted(I, reverse=True)

        # Calculate momentum transfer vector values (q)
        q = (2*np.pi)/np.array(d)

        # Calculate angles between lattice planes and preferred orientation direction
        # Initialize array of zeros
        phi = np.zeros(len(q))

        # Iterate through lattice planes and calculate angle between planes
        for i in range(0, len(q)):
            phi[i] = (d_pref*d[i])*(h[i]*h_pref*(a_r**2) + k[i]*k_pref*(b_r**2) + l[i]*l_pref*(c_r**2) + 
                                   (k[i]*l_pref + l[i]*k_pref)*b_r*c_r*np.cos(alpha_r) + 
                                   (h[i]*l_pref + l[i]*h_pref)*a_r*c_r*np.cos(beta_r) + 
                                   (h[i]*k_pref + k[i]*h_pref)*a_r*b_r*np.cos(gamma_r))
            
            # Make sure input to arccos is between 0 and 1
            if phi[i] > 1:
                phi[i] = 1
            elif phi[i] < 0:
                phi[i] = 0
            
            phi[i] = np.arccos(phi[i])

        # Calculate components of q-vector in-plane and out-of-plane
        q_xy = np.multiply(q, np.sin(phi))
        q_z = np.multiply(q, np.cos(phi))

        # Save list of reflections and q-vector components
        cif_filename = self.CF_LineEdit.text()
        refl_filename = cif_filename.replace('.cif', '_') + pref_orientation + '_reflections.csv'
        head = 'h, k, l, Q_xy (1/A), Q_z (1/A)'
        np.savetxt(refl_filename, np.c_[h, k, l, q_xy, q_z], fmt=['%i', '%i', '%i', '%.3f', '%.3f'], delimiter=',', comments='', header=head)

        # Only use reflections that are in the set q limits
        q_xy_GIWAXS = np.array([])
        q_z_GIWAXS = np.array([])
        I_GIWAXS = np.array([])

        for i in range(0, len(q_xy)):
          if q_xy[i] <= q_xy_max and q_z[i] <= q_z_max:
            q_xy_GIWAXS = np.append(q_xy_GIWAXS, q_xy[i])
            q_z_GIWAXS = np.append(q_z_GIWAXS, q_z[i])
            I_GIWAXS = np.append(I_GIWAXS, I[i])

        # Create meshgrid for GIWAXS plot
        q_xy_points = int(1000*(q_xy_max/2.5))
        q_z_points = int(1000*(q_z_max/2.5))
        X, Y = np.meshgrid(np.linspace(0, q_xy_max, q_xy_points), np.linspace(0, q_z_max, q_z_points))

        # Calculate Gaussian peaks for Bragg reflections
        Z = np.ones([np.size(X, 0), np.size(X, 1)])

        for i in range(len(q_xy_GIWAXS)):

            # Update progress bar
            self.progressBar.setValue((100*i)/(len(q_xy_GIWAXS) - 1))
            QtWidgets.QApplication.processEvents()
            
            # Calculate angle of diffraction spot
            if q_xy_GIWAXS[i] == 0:
                ang = np.pi/2
            elif q_z_GIWAXS[i] == 0:
                ang = 0
            else:
                ang = np.arctan(q_z_GIWAXS[i]/q_xy_GIWAXS[i])

            # Calculate constants for elliptical gaussian
            a = (np.cos(ang)**2)/(2*sigma_x**2) + (np.sin(ang)**2)/(2*sigma_y**2)
            b = -(np.sin(2*ang))/(4*sigma_x**2) + (np.sin(2*ang))/(4*sigma_y**2)
            c = (np.sin(ang)**2)/(2*sigma_x**2) + (np.cos(ang)**2)/(2*sigma_y**2)

            # Calculate gaussian and add to meshgrid
            Z = Z + I_GIWAXS[i]*np.exp(-(a*(X - q_xy_GIWAXS[i])**2 - 2*b*(X - q_xy_GIWAXS[i])*(Y - q_z_GIWAXS[i]) + c*(Y - q_z_GIWAXS[i])**2))

        # Save GIXRD image
        gixrd_filename = refl_filename.replace('_reflections.csv', '') + '_qxy_' + str(q_xy_max) + '_qz_' + str(q_z_max) + '_GIXRD.tif'
        imsave(gixrd_filename, np.flipud(Z))

        # Show image
        plt.ion()

        # In case of different aspect ratios
        ratio = (q_xy_max)/(q_z_max)

        # Generate figure and subplot
        mpl.rcParams['font.family'] = 'Arial'
        plt.rcParams['axes.linewidth'] = 1.5

        fig = plt.figure(figsize=(ratio*3,3), tight_layout=True, dpi=300)
        ax = plt.subplot(111)
        ax.imshow(np.flipud(Z), cmap='RdBu_r', extent=(0, q_xy_max, 0, q_z_max))

        # Set axis labels
        ax.set_xlabel(u'$\mathregular{q_{xy}}$ (\u00c5$\mathregular{^{-1}}$)')
        ax.set_ylabel(u'$\mathregular{q_{z}}$ (\u00c5$\mathregular{^{-1}}$)')

        plt.tight_layout()
        plt.show()


## Open the main window when the program is run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
