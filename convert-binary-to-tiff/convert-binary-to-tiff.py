"""
Binary File Converter
Version: 1.0
Updated: February 2020
Author: Naveen Venkatesan
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import numpy as np
from pathlib import Path
from struct import unpack
from os import path
from tifffile import imsave, imshow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        # Create main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 350)
        
        
        # Populate main window with a central widget object
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        # Program title - Convert Binary to TIFF
        self.Main_Label = QtWidgets.QLabel(self.centralwidget)
        self.Main_Label.setGeometry(QtCore.QRect(10, 10, 580, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Main_Label.setFont(font)
        self.Main_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_Label.setObjectName("Main_Label")
        

        # Label for selected files
        self.SF_Label = QtWidgets.QLabel(self.centralwidget)
        self.SF_Label.setGeometry(QtCore.QRect(10, 60, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SF_Label.setFont(font)
        self.SF_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SF_Label.setObjectName("SF_Label")
        

        # Label for image resolution
        self.IR_Label = QtWidgets.QLabel(self.centralwidget)
        self.IR_Label.setGeometry(QtCore.QRect(10, 100, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IR_Label.setFont(font)
        self.IR_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IR_Label.setObjectName("IR_Label")
        

        # Label for image encoding
        self.IE_Label = QtWidgets.QLabel(self.centralwidget)
        self.IE_Label.setGeometry(QtCore.QRect(10, 140, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IE_Label.setFont(font)
        self.IE_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IE_Label.setObjectName("IE_Label")
        

        # Label for save directory
        self.SD_Label = QtWidgets.QLabel(self.centralwidget)
        self.SD_Label.setGeometry(QtCore.QRect(10, 180, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SD_Label.setFont(font)
        self.SD_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SD_Label.setObjectName("SD_Label")
        

        # Label for progress bar
        self.Prog_Label = QtWidgets.QLabel(self.centralwidget)
        self.Prog_Label.setGeometry(QtCore.QRect(10, 220, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Prog_Label.setFont(font)
        self.Prog_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Prog_Label.setObjectName("Prog_Label")
        

        # Browse button to select files
        self.SF_Browse_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SF_Browse_Button.setGeometry(QtCore.QRect(460, 55, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.SF_Browse_Button.setFont(font)
        self.SF_Browse_Button.setObjectName("SF_Browse_Button")
        self.SF_Browse_Button.clicked.connect(self.SF_Browse)


        # Browse button for save directory
        self.SD_Browse_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SD_Browse_Button.setGeometry(QtCore.QRect(460, 176, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.SD_Browse_Button.setFont(font)
        self.SD_Browse_Button.setObjectName("SD_Browse_Button")
        self.SD_Browse_Button.clicked.connect(self.SD_Browse)


        # Label that indicates the number of binary files selected
        self.SF_Number_Label = QtWidgets.QLabel(self.centralwidget)
        self.SF_Number_Label.setGeometry(QtCore.QRect(160, 60, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.SF_Number_Label.setFont(font)
        self.SF_Number_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.SF_Number_Label.setObjectName("SF_Number_Label")
        

        # Label for image width
        self.Width_Label = QtWidgets.QLabel(self.centralwidget)
        self.Width_Label.setGeometry(QtCore.QRect(170, 100, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Width_Label.setFont(font)
        self.Width_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Width_Label.setObjectName("Width_Label")
        

        # Label for image height
        self.Height_Label = QtWidgets.QLabel(self.centralwidget)
        self.Height_Label.setGeometry(QtCore.QRect(315, 100, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Height_Label.setFont(font)
        self.Height_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Height_Label.setObjectName("Height_Label")
        

        # Line Edit box for image width
        self.Width_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Width_LineEdit.setGeometry(QtCore.QRect(230, 100, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Width_LineEdit.setFont(font)
        self.Width_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Width_LineEdit.setObjectName("Width_LineEdit")
        

        # Line Edit box for image height
        self.Height_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Height_LineEdit.setGeometry(QtCore.QRect(380, 100, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.Height_LineEdit.setFont(font)
        self.Height_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Height_LineEdit.setObjectName("Height_LineEdit")
        

        # Combo Box containing different image encodings
        self.IE_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.IE_ComboBox.setGeometry(QtCore.QRect(170, 140, 291, 30))
        self.IE_ComboBox.addItems(['short', 'unsigned short', 'int', 'unsigned int', 'long', 'unsigned long', 'long long', 'unsigned long long', 'float', 'double'])
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.IE_ComboBox.setFont(font)
        self.IE_ComboBox.setObjectName("IE_ComboBox")
        

        # Line Edit box for save directory
        self.SD_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SD_LineEdit.setGeometry(QtCore.QRect(170, 180, 285, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.SD_LineEdit.setFont(font)
        self.SD_LineEdit.setObjectName("SD_LineEdit")
        

        # Progress Bar for conversion
        self.ProgBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgBar.setGeometry(QtCore.QRect(170, 220, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.ProgBar.setFont(font)
        self.ProgBar.setProperty("value", 0)
        self.ProgBar.setObjectName("ProgBar")
        

        # Button to start the conversion
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 551, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.convertImages)


        # Set main window properties
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Change default labels and values and set the tab order
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.SF_Browse_Button, self.Width_LineEdit)
        MainWindow.setTabOrder(self.Width_LineEdit, self.Height_LineEdit)
        MainWindow.setTabOrder(self.Height_LineEdit, self.IE_ComboBox)
        MainWindow.setTabOrder(self.IE_ComboBox, self.SD_LineEdit)
        MainWindow.setTabOrder(self.SD_LineEdit, self.SD_Browse_Button)
        MainWindow.setTabOrder(self.SD_Browse_Button, self.pushButton)

    
    def retranslateUi(self, MainWindow):
        

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convert Binary to TIFF"))
        self.Main_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">Convert Binary Files to TIFF Images</span></p></body></html>"))
        self.SF_Label.setText(_translate("MainWindow", "Select Files:"))
        self.IR_Label.setText(_translate("MainWindow", "Image Resolution:"))
        self.IE_Label.setText(_translate("MainWindow", "Image Encoding:"))
        self.SD_Label.setText(_translate("MainWindow", "Save Directory:"))
        self.Prog_Label.setText(_translate("MainWindow", "Progress:"))
        self.SF_Browse_Button.setText(_translate("MainWindow", "Browse..."))
        self.SD_Browse_Button.setText(_translate("MainWindow", "Browse..."))
        self.SF_Number_Label.setText(_translate("MainWindow", "0 File(s) Selected"))
        self.Width_Label.setText(_translate("MainWindow", "Width"))
        self.Height_Label.setText(_translate("MainWindow", "Height"))
        self.pushButton.setText(_translate("MainWindow", "Convert Files"))

    

    # Function to browse for binary files
    def SF_Browse(self):

        # Reset the labels
        self.SF_Number_Label.setText('0 File(s) Selected')
        self.SF_Number_Label.repaint()
        

        global file_list
        
        try:
            file_list, _ = QFileDialog.getOpenFileNames(self.centralwidget, 'Please select files you want to convert', './', 'All Files (*.*)')
        except:
            return

        if len(file_list) > 0:
            
            # Update the number of files selected
            self.SF_Number_Label.setText(str(len(file_list)) + ' File(s) Selected')

            # Make default save directory the same as image files if empty
            if self.SD_LineEdit.text() == '':
                self.SD_LineEdit.setText(path.dirname(file_list[0]))
        
        return

    
    # Function to browse for save directory
    def SD_Browse(self):

        try:
            save_dir = QFileDialog.getExistingDirectory(self.centralwidget, 'Select Save Directory')
            self.SD_LineEdit.setText(save_dir)

        except:
            return

    
    # Function to convert binary files to TIFF images
    def convertImages(self):

        try:

            if len(file_list) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error!")
                msg.setInformativeText('No selected files!')
                msg.setWindowTitle("Error!")
                msg.exec_()
                return

            for i in file_list:

                # Set save filename
                saveFileName = Path(i)
                saveFileName = self.SD_LineEdit.text() + '/' + str(saveFileName.stem) + '.tif'

                # Get image width and height
                try:
                    imwidth = int(self.Width_LineEdit.text())
                    imheight = int(self.Height_LineEdit.text())
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error!")
                    msg.setInformativeText('Please enter image height and width!')
                    msg.setWindowTitle("Error!")
                    msg.exec_()
                    return

                # Get image encoding
                encode_str = str(imwidth*imheight)
                encode_type_list = {'short':'h', 'unsigned short':'H', 'int':'i', 'unsigned int':'I', 'long':'l', 'unsigned long':'L', 'long long':'q', 'unsigned long long':'Q', 'float':'f', 'double':'d'}
                encode_type = encode_type_list[self.IE_ComboBox.currentText()]
                encode_str = encode_str + encode_type

                # Unpack binary image
                try:
                    bin_img = Path(i).read_bytes()
                    new_img = unpack(encode_str, bin_img)
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error!")
                    msg.setInformativeText('Unable to unpack binary file! - check if resolution and/or encoding is correct')
                    msg.setWindowTitle("Error!")
                    msg.exec_()
                    return

                # Reshape list of value into image
                try:
                    new_img = np.reshape(new_img, (imheight,-1))
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error!")
                    msg.setInformativeText('Unable to reshape into image!')
                    msg.setWindowTitle("Error!")
                    msg.exec_()
                    return

                # Save image as TIFF file
                try:
                    save_dtype = {'short':np.int16, 'unsigned short':np.uint16, 'int':np.int32, 'unsigned int':np.uint32, 'long':np.int32, 'unsigned long':np.uint32, 'long long':np.int64, 'unsigned long long':np.uint64, 'float':np.float32, 'double':np.float64}
                    new_img = new_img.astype(save_dtype[self.IE_ComboBox.currentText()])
                    imsave(saveFileName, new_img)
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error!")
                    msg.setInformativeText('Unable to save TIFF file!')
                    msg.setWindowTitle("Error!")
                    msg.exec_()
                    return

                # Update progress bar
                self.ProgBar.setValue(self.ProgBar.value() + (100/len(file_list)))
                QtWidgets.QApplication.processEvents()

            # Alert user that conversion is complete
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Success!")
            msg.setInformativeText('Conversion Complete!')
            msg.setWindowTitle("Finished!")
            msg.exec_()

            # Reset progress bar
            self.ProgBar.setValue(0)
            QtWidgets.QApplication.processEvents()

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!")
            msg.setInformativeText('File list empty!')
            msg.setWindowTitle("Error!")
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())