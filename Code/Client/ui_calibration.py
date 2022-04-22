# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Freenove\Desktop\树莓派六足机器人\界面UI\calibration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calibration(object):
    def setupUi(self, calibration):
        calibration.setObjectName("calibration")
        calibration.resize(1080, 570)
        font = QtGui.QFont()
        font.setFamily("Arial")
        calibration.setFont(font)
        calibration.setStyleSheet(
            "QWidget{ background:#e9e9e9 }"

            "QAbstractButton{ border-style:outset; border-radius:5px; border-color: #d3d3d3; padding:5px; color:#1a1a1a; background:#fafafa }"
            "QAbstractButton:hover{ color:#1a1a1a; background-color:#e8e8e8 }"
            "QAbstractButton:pressed{ color:#dcdcdc; background-color:#8a6353 }"
            
            "QLabel{ color:#1a1a1a }"
            "QLabel:focus{ border:1px solid #8a6353 }"

            "QLineEdit{ border:1px solid #d3d3d3; border-radius:5px; padding:2px; background:none; selection-background-color:#8a6353; selection-color:#dcdcdc }"
            "QLineEdit:focus,QLineEdit:hover{ border:1px solid #d3d3d3 }"
            "QLineEdit{ lineedit-password-character:9679 }")

        font = QtGui.QFont()
        font.setFamily("Arial")           

        self.radioButton_one = QtWidgets.QRadioButton(calibration)
        self.radioButton_one.setGeometry(QtCore.QRect(30, 90, 120, 30))
        self.radioButton_one.setFont(font)
        self.radioButton_one.setObjectName("radioButton_one")

        self.radioButton_two = QtWidgets.QRadioButton(calibration)
        self.radioButton_two.setGeometry(QtCore.QRect(30, 150, 120, 30))
        self.radioButton_two.setFont(font)
        self.radioButton_two.setObjectName("radioButton_two")

        self.radioButton_three = QtWidgets.QRadioButton(calibration)
        self.radioButton_three.setGeometry(QtCore.QRect(30, 210, 120, 30))
        self.radioButton_three.setFont(font)
        self.radioButton_three.setObjectName("radioButton_three")

        self.radioButton_four = QtWidgets.QRadioButton(calibration)
        self.radioButton_four.setGeometry(QtCore.QRect(30, 270, 120, 30))
        self.radioButton_four.setFont(font)
        self.radioButton_four.setObjectName("radioButton_four")

        self.radioButton_five = QtWidgets.QRadioButton(calibration)
        self.radioButton_five.setGeometry(QtCore.QRect(30, 330, 120, 30))
        self.radioButton_five.setFont(font)
        self.radioButton_five.setObjectName("radioButton_five")

        self.radioButton_six = QtWidgets.QRadioButton(calibration)
        self.radioButton_six.setGeometry(QtCore.QRect(30, 390, 120, 30))
        self.radioButton_six.setFont(font)
        self.radioButton_six.setObjectName("radioButton_six")

        self.label_X = QtWidgets.QLabel(calibration)
        self.label_X.setGeometry(QtCore.QRect(210, 30, 90, 30))
        self.label_X.setFont(font)
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")

        self.label_Y = QtWidgets.QLabel(calibration)
        self.label_Y.setGeometry(QtCore.QRect(360, 30, 90, 30))
        self.label_Y.setFont(font)
        self.label_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y.setObjectName("label_Y") 
 
        self.label_Z = QtWidgets.QLabel(calibration)
        self.label_Z.setGeometry(QtCore.QRect(510, 30, 90, 30))
        self.label_Z.setFont(font)
        self.label_Z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z.setObjectName("label_Z")

        self.one_x = QtWidgets.QLineEdit(calibration)
        self.one_x.setGeometry(QtCore.QRect(210, 90, 90, 30))
        self.one_x.setFont(font)
        self.one_x.setAlignment(QtCore.Qt.AlignCenter)
        self.one_x.setObjectName("one_x")

        self.one_y = QtWidgets.QLineEdit(calibration)
        self.one_y.setGeometry(QtCore.QRect(360, 90, 90, 30))
        self.one_y.setFont(font)
        self.one_y.setAlignment(QtCore.Qt.AlignCenter)
        self.one_y.setObjectName("one_y")

        self.one_z = QtWidgets.QLineEdit(calibration)
        self.one_z.setGeometry(QtCore.QRect(510, 90, 90, 30))
        self.one_z.setFont(font)
        self.one_z.setAlignment(QtCore.Qt.AlignCenter)
        self.one_z.setObjectName("one_z")

        self.two_x = QtWidgets.QLineEdit(calibration)
        self.two_x.setGeometry(QtCore.QRect(210, 159, 90, 30))
        self.two_x.setFont(font)
        self.two_x.setAlignment(QtCore.Qt.AlignCenter)
        self.two_x.setObjectName("two_x")

        self.two_y = QtWidgets.QLineEdit(calibration)
        self.two_y.setGeometry(QtCore.QRect(360, 150, 90, 30))
        self.two_y.setFont(font)
        self.two_y.setAlignment(QtCore.Qt.AlignCenter)
        self.two_y.setObjectName("two_y")

        self.two_z = QtWidgets.QLineEdit(calibration)
        self.two_z.setGeometry(QtCore.QRect(510, 150, 90, 30))
        self.two_z.setFont(font)
        self.two_z.setAlignment(QtCore.Qt.AlignCenter)
        self.two_z.setObjectName("two_z")

        self.three_x = QtWidgets.QLineEdit(calibration)
        self.three_x.setGeometry(QtCore.QRect(210, 210, 90, 30))
        self.three_x.setFont(font)
        self.three_x.setAlignment(QtCore.Qt.AlignCenter)
        self.three_x.setObjectName("three_x")

        self.three_y = QtWidgets.QLineEdit(calibration)
        self.three_y.setGeometry(QtCore.QRect(360, 210, 90, 30))
        self.three_y.setFont(font)
        self.three_y.setAlignment(QtCore.Qt.AlignCenter)
        self.three_y.setObjectName("three_y")
 
        self.three_z = QtWidgets.QLineEdit(calibration)
        self.three_z.setGeometry(QtCore.QRect(510, 210, 90, 30))
        self.three_z.setFont(font)
        self.three_z.setAlignment(QtCore.Qt.AlignCenter)
        self.three_z.setObjectName("three_z")

        self.four_x = QtWidgets.QLineEdit(calibration)
        self.four_x.setGeometry(QtCore.QRect(210, 270, 90, 30))
        self.four_x.setFont(font)
        self.four_x.setAlignment(QtCore.Qt.AlignCenter)
        self.four_x.setObjectName("four_x")

        self.four_y = QtWidgets.QLineEdit(calibration)
        self.four_y.setGeometry(QtCore.QRect(360, 270, 90, 30))
        self.four_y.setFont(font)
        self.four_y.setAlignment(QtCore.Qt.AlignCenter)
        self.four_y.setObjectName("four_y")

        self.four_z = QtWidgets.QLineEdit(calibration)
        self.four_z.setGeometry(QtCore.QRect(510, 270, 90, 30))
        self.four_z.setFont(font)
        self.four_z.setAlignment(QtCore.Qt.AlignCenter)
        self.four_z.setObjectName("four_z")

        self.five_x = QtWidgets.QLineEdit(calibration)
        self.five_x.setGeometry(QtCore.QRect(210, 330, 90, 30))
        self.five_x.setFont(font)
        self.five_x.setAlignment(QtCore.Qt.AlignCenter)
        self.five_x.setObjectName("five_x")

        self.five_y = QtWidgets.QLineEdit(calibration)
        self.five_y.setGeometry(QtCore.QRect(360, 330, 90, 30))
        self.five_y.setFont(font)
        self.five_y.setAlignment(QtCore.Qt.AlignCenter)
        self.five_y.setObjectName("five_y")

        self.five_z = QtWidgets.QLineEdit(calibration)
        self.five_z.setGeometry(QtCore.QRect(510, 330, 90, 30))
        self.five_z.setFont(font)
        self.five_z.setAlignment(QtCore.Qt.AlignCenter)
        self.five_z.setObjectName("five_z")

        self.six_x = QtWidgets.QLineEdit(calibration)
        self.six_x.setGeometry(QtCore.QRect(210, 390, 90, 30))
        self.six_x.setFont(font)
        self.six_x.setAlignment(QtCore.Qt.AlignCenter)
        self.six_x.setObjectName("six_x")

        self.six_y = QtWidgets.QLineEdit(calibration)
        self.six_y.setGeometry(QtCore.QRect(360, 390, 90, 30))
        self.six_y.setFont(font)
        self.six_y.setAlignment(QtCore.Qt.AlignCenter)
        self.six_y.setObjectName("six_y")

        self.six_z = QtWidgets.QLineEdit(calibration)
        self.six_z.setGeometry(QtCore.QRect(510, 390, 90, 30))
        self.six_z.setFont(font)
        self.six_z.setAlignment(QtCore.Qt.AlignCenter)
        self.six_z.setObjectName("six_z")

        self.Button_X1 = QtWidgets.QPushButton(calibration)
        self.Button_X1.setGeometry(QtCore.QRect(210, 465, 90, 30))
        self.Button_X1.setFont(font)
        self.Button_X1.setObjectName("Button_X1")

        self.Button_X2 = QtWidgets.QPushButton(calibration)
        self.Button_X2.setGeometry(QtCore.QRect(210, 510, 90, 30))
        self.Button_X2.setFont(font)
        self.Button_X2.setObjectName("Button_X2")

        self.Button_Y1 = QtWidgets.QPushButton(calibration)
        self.Button_Y1.setGeometry(QtCore.QRect(360, 465, 90, 30))
        self.Button_Y1.setFont(font)
        self.Button_Y1.setObjectName("Button_Y1")

        self.Button_Y2 = QtWidgets.QPushButton(calibration)
        self.Button_Y2.setGeometry(QtCore.QRect(360, 510, 90, 30))
        self.Button_Y2.setFont(font)
        self.Button_Y2.setObjectName("Button_Y2")

        self.Button_Z1 = QtWidgets.QPushButton(calibration)
        self.Button_Z1.setGeometry(QtCore.QRect(510, 465, 90, 30))
        self.Button_Z1.setFont(font)
        self.Button_Z1.setObjectName("Button_Z1")

        self.Button_Z2 = QtWidgets.QPushButton(calibration)
        self.Button_Z2.setGeometry(QtCore.QRect(510, 510, 90, 30))
        self.Button_Z2.setFont(font)
        self.Button_Z2.setObjectName("Button_Z2")

        self.Button_Save = QtWidgets.QPushButton(calibration)
        self.Button_Save.setGeometry(QtCore.QRect(30, 510, 120, 30))
        self.Button_Save.setFont(font)
        self.Button_Save.setObjectName("Button_Save")

        self.label_picture = QtWidgets.QLabel(calibration)
        self.label_picture.setGeometry(QtCore.QRect(660, 90, 390, 390))
        self.label_picture.setFont(font)
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")

        self.retranslateUi(calibration)
        QtCore.QMetaObject.connectSlotsByName(calibration)

    def retranslateUi(self, calibration):
        _translate = QtCore.QCoreApplication.translate
        calibration.setWindowTitle(_translate("calibration", "Calibration"))

        self.radioButton_one.setText(_translate("calibration", "One"))
        self.radioButton_two.setText(_translate("calibration", "Two"))
        self.radioButton_three.setText(_translate("calibration", "Three"))
        self.radioButton_four.setText(_translate("calibration", "Four"))
        self.radioButton_five.setText(_translate("calibration", "Five"))
        self.radioButton_six.setText(_translate("calibration", "Six"))

        self.label_X.setText(_translate("calibration", "X"))
        self.label_Y.setText(_translate("calibration", "Y"))
        self.label_Z.setText(_translate("calibration", "Z"))

        self.one_x.setText(_translate("calibration", "0"))
        self.one_y.setText(_translate("calibration", "72"))
        self.one_z.setText(_translate("calibration", "0"))

        self.two_y.setText(_translate("calibration", "72"))
        self.two_x.setText(_translate("calibration", "0"))
        self.two_z.setText(_translate("calibration", "0"))

        self.three_y.setText(_translate("calibration", "72"))
        self.three_x.setText(_translate("calibration", "0"))
        self.three_z.setText(_translate("calibration", "0"))

        self.four_x.setText(_translate("calibration", "0"))
        self.four_y.setText(_translate("calibration", "72"))
        self.four_z.setText(_translate("calibration", "0"))

        self.five_x.setText(_translate("calibration", "0"))
        self.five_y.setText(_translate("calibration", "72"))
        self.five_z.setText(_translate("calibration", "0"))

        self.six_x.setText(_translate("calibration", "0"))
        self.six_z.setText(_translate("calibration", "0"))
        self.six_y.setText(_translate("calibration", "72"))


        self.Button_X1.setText(_translate("calibration", "X+"))
        self.Button_X2.setText(_translate("calibration", "X-"))
        self.Button_Y1.setText(_translate("calibration", "Y+"))
        self.Button_Y2.setText(_translate("calibration", "Y-"))
        self.Button_Z1.setText(_translate("calibration", "Z+"))
        self.Button_Z2.setText(_translate("calibration", "Z-"))

        self.Button_Save.setText(_translate("calibration", "Save"))




