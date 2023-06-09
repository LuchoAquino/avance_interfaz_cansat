# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diseñochvre.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1572, 974)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.interfaz_general = QtWidgets.QFrame(self.centralwidget)
        self.interfaz_general.setStyleSheet("QFrame{\n"
"background-color:rgb(36,0,70);\n"
"}")
        self.interfaz_general.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.interfaz_general.setFrameShadow(QtWidgets.QFrame.Raised)
        self.interfaz_general.setObjectName("interfaz_general")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.interfaz_general)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fr_izq = QtWidgets.QFrame(self.interfaz_general)
        self.fr_izq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_izq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_izq.setObjectName("fr_izq")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fr_izq)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fr_izq_sup = QtWidgets.QFrame(self.fr_izq)
        self.fr_izq_sup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_izq_sup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_izq_sup.setObjectName("fr_izq_sup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_izq_sup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hatun_mayu = QtWidgets.QFrame(self.fr_izq_sup)
        self.hatun_mayu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hatun_mayu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hatun_mayu.setObjectName("hatun_mayu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.hatun_mayu)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_hm = QtWidgets.QFrame(self.hatun_mayu)
        self.logo_hm.setMinimumSize(QtCore.QSize(148, 159))
        self.logo_hm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_hm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_hm.setObjectName("logo_hm")
        self.label = QtWidgets.QLabel(self.logo_hm)
        self.label.setGeometry(QtCore.QRect(-10, 0, 161, 159))
        self.label.setMinimumSize(QtCore.QSize(148, 159))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Proyecto Cansat/HM/logocansat.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.logo_hm)
        self.text_hm = QtWidgets.QFrame(self.hatun_mayu)
        self.text_hm.setMinimumSize(QtCore.QSize(301, 51))
        self.text_hm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text_hm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text_hm.setObjectName("text_hm")
        self.label_2 = QtWidgets.QLabel(self.text_hm)
        self.label_2.setGeometry(QtCore.QRect(-10, 50, 301, 51))
        self.label_2.setMinimumSize(QtCore.QSize(301, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.text_hm)
        self.horizontalLayout_3.setStretch(0, 148)
        self.horizontalLayout_3.setStretch(1, 279)
        self.horizontalLayout_2.addWidget(self.hatun_mayu)
        self.cm_serial = QtWidgets.QFrame(self.fr_izq_sup)
        self.cm_serial.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.cm_serial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cm_serial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cm_serial.setObjectName("cm_serial")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.cm_serial)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.cm_serial)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.cm_serial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(95, 33))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.cm_serial)
        self.comboBox.setMinimumSize(QtCore.QSize(186, 22))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.cm_serial)
        self.label_5.setMinimumSize(QtCore.QSize(95, 33))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.cm_serial)
        self.comboBox_2.setMinimumSize(QtCore.QSize(186, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bt_conectar = QtWidgets.QPushButton(self.cm_serial)
        self.bt_conectar.setMinimumSize(QtCore.QSize(122, 21))
        self.bt_conectar.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color : rgb(208,216,191);\n"
"font: 10pt ;\n"
"color: rgb(36,0,70);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 5px;\n"
"background-color : rgb(36,0,70);\n"
"font: 10pt ;\n"
"color: rgb(208,216,191);\n"
"\n"
"}")
        self.bt_conectar.setObjectName("bt_conectar")
        self.horizontalLayout_6.addWidget(self.bt_conectar)
        self.bt_actualizar = QtWidgets.QPushButton(self.cm_serial)
        self.bt_actualizar.setMinimumSize(QtCore.QSize(122, 21))
        self.bt_actualizar.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color : rgb(208,216,191);\n"
"font: 10pt ;\n"
"color: rgb(36,0,70);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 5px;\n"
"background-color : rgb(36,0,70);\n"
"font: 10pt ;\n"
"color: rgb(208,216,191);\n"
"\n"
"}")
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.horizontalLayout_6.addWidget(self.bt_actualizar)
        self.bt_desconectar = QtWidgets.QPushButton(self.cm_serial)
        self.bt_desconectar.setMinimumSize(QtCore.QSize(122, 21))
        self.bt_desconectar.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color : rgb(208,216,191);\n"
"font: 10pt ;\n"
"color: rgb(36,0,70);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 5px;\n"
"background-color : rgb(36,0,70);\n"
"font: 10pt ;\n"
"color: rgb(208,216,191);\n"
"\n"
"}")
        self.bt_desconectar.setObjectName("bt_desconectar")
        self.horizontalLayout_6.addWidget(self.bt_desconectar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addWidget(self.cm_serial)
        self.horizontalLayout_2.setStretch(0, 466)
        self.horizontalLayout_2.setStretch(1, 375)
        self.verticalLayout_2.addWidget(self.fr_izq_sup)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.fr_izq_med = QtWidgets.QFrame(self.fr_izq)
        self.fr_izq_med.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.fr_izq_med.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_izq_med.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_izq_med.setLineWidth(1)
        self.fr_izq_med.setMidLineWidth(1)
        self.fr_izq_med.setObjectName("fr_izq_med")
        self.label_6 = QtWidgets.QLabel(self.fr_izq_med)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 221, 41))
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(self.fr_izq_med)
        self.widget.setGeometry(QtCore.QRect(81, 50, 251, 151))
        self.widget.setObjectName("widget")
        self.gp_temp_hm = QtWidgets.QVBoxLayout(self.widget)
        self.gp_temp_hm.setContentsMargins(0, 0, 0, 0)
        self.gp_temp_hm.setObjectName("gp_temp_hm")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setStyleSheet("\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gp_temp_hm.addWidget(self.label_11)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gp_temp_hm.addLayout(self.verticalLayout_5)
        self.gp_temp_hm.setStretch(0, 1)
        self.gp_temp_hm.setStretch(1, 25)
        self.widget1 = QtWidgets.QWidget(self.fr_izq_med)
        self.widget1.setGeometry(QtCore.QRect(343, 50, 241, 151))
        self.widget1.setObjectName("widget1")
        self.gp_alt_hm = QtWidgets.QVBoxLayout(self.widget1)
        self.gp_alt_hm.setContentsMargins(0, 0, 0, 0)
        self.gp_alt_hm.setObjectName("gp_alt_hm")
        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gp_alt_hm.addWidget(self.label_12)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gp_alt_hm.addLayout(self.verticalLayout_6)
        self.gp_alt_hm.setStretch(0, 1)
        self.gp_alt_hm.setStretch(1, 25)
        self.widget2 = QtWidgets.QWidget(self.fr_izq_med)
        self.widget2.setGeometry(QtCore.QRect(605, 50, 231, 151))
        self.widget2.setObjectName("widget2")
        self.gp_gps_hm = QtWidgets.QVBoxLayout(self.widget2)
        self.gp_gps_hm.setContentsMargins(0, 0, 0, 0)
        self.gp_gps_hm.setObjectName("gp_gps_hm")
        self.label_13 = QtWidgets.QLabel(self.widget2)
        self.label_13.setStyleSheet("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gp_gps_hm.addWidget(self.label_13)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gp_gps_hm.addLayout(self.verticalLayout_7)
        self.gp_gps_hm.setStretch(0, 1)
        self.gp_gps_hm.setStretch(1, 25)
        self.verticalLayout_2.addWidget(self.fr_izq_med)
        spacerItem1 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.fr_izq_inf = QtWidgets.QFrame(self.fr_izq)
        self.fr_izq_inf.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.fr_izq_inf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_izq_inf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_izq_inf.setObjectName("fr_izq_inf")
        self.label_7 = QtWidgets.QLabel(self.fr_izq_inf)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 231, 41))
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self.fr_izq_inf)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 60, 251, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gp_temp_ext = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.gp_temp_ext.setContentsMargins(0, 0, 0, 0)
        self.gp_temp_ext.setObjectName("gp_temp_ext")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gp_temp_ext.addWidget(self.label_14)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gp_temp_ext.addLayout(self.verticalLayout_12)
        self.gp_temp_ext.setStretch(0, 1)
        self.gp_temp_ext.setStretch(1, 25)
        self.layoutWidget_2 = QtWidgets.QWidget(self.fr_izq_inf)
        self.layoutWidget_2.setGeometry(QtCore.QRect(80, 230, 251, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gp_presion_ext = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.gp_presion_ext.setContentsMargins(0, 0, 0, 0)
        self.gp_presion_ext.setObjectName("gp_presion_ext")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gp_presion_ext.addWidget(self.label_15)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.gp_presion_ext.addLayout(self.verticalLayout_14)
        self.gp_presion_ext.setStretch(0, 1)
        self.gp_presion_ext.setStretch(1, 25)
        self.layoutWidget_3 = QtWidgets.QWidget(self.fr_izq_inf)
        self.layoutWidget_3.setGeometry(QtCore.QRect(360, 60, 251, 151))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gp_girosc_ext = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.gp_girosc_ext.setContentsMargins(0, 0, 0, 0)
        self.gp_girosc_ext.setObjectName("gp_girosc_ext")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gp_girosc_ext.addWidget(self.label_16)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.gp_girosc_ext.addLayout(self.verticalLayout_16)
        self.gp_girosc_ext.setStretch(0, 1)
        self.gp_girosc_ext.setStretch(1, 25)
        self.layoutWidget_4 = QtWidgets.QWidget(self.fr_izq_inf)
        self.layoutWidget_4.setGeometry(QtCore.QRect(360, 230, 251, 151))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gp_humedad_ext = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.gp_humedad_ext.setContentsMargins(0, 0, 0, 0)
        self.gp_humedad_ext.setObjectName("gp_humedad_ext")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gp_humedad_ext.addWidget(self.label_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.gp_humedad_ext.addLayout(self.verticalLayout_18)
        self.gp_humedad_ext.setStretch(0, 1)
        self.gp_humedad_ext.setStretch(1, 25)
        self.layoutWidget_5 = QtWidgets.QWidget(self.fr_izq_inf)
        self.layoutWidget_5.setGeometry(QtCore.QRect(640, 60, 241, 151))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gp_acel_ext = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.gp_acel_ext.setContentsMargins(0, 0, 0, 0)
        self.gp_acel_ext.setObjectName("gp_acel_ext")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gp_acel_ext.addWidget(self.label_18)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.gp_acel_ext.addLayout(self.verticalLayout_20)
        self.gp_acel_ext.setStretch(0, 1)
        self.gp_acel_ext.setStretch(1, 25)
        self.verticalLayout_2.addWidget(self.fr_izq_inf)
        self.verticalLayout_2.setStretch(2, 249)
        self.verticalLayout_2.setStretch(4, 415)
        self.horizontalLayout.addWidget(self.fr_izq)
        self.fr_der = QtWidgets.QFrame(self.interfaz_general)
        self.fr_der.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_der.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_der.setObjectName("fr_der")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fr_der)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.fr_der)
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_9.addLayout(self.verticalLayout_21)
        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(1, 10)
        self.verticalLayout_3.addWidget(self.frame_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.frame_6 = QtWidgets.QFrame(self.fr_der)
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    width:80px;\n"
"    height:80px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    image: url(\"C:/Users/Luis/Downloads/copiaseguridad/bt_on1.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(\"C:/Users/Luis/Downloads/copiaseguridad/bt_off.png\");\n"
"}")
        self.checkBox.setText("")
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_8.addWidget(self.checkBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_10.addWidget(self.tableWidget)
        self.verticalLayout_3.addWidget(self.frame_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.frame_7 = QtWidgets.QFrame(self.fr_der)
        self.frame_7.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("border-radius: 5px;\n"
"color: rgb(36,0,70);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setKeyboardTracking(True)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_7.addWidget(self.timeEdit)
        self.verticalLayout_3.addWidget(self.frame_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.frame_8 = QtWidgets.QFrame(self.fr_der)
        self.frame_8.setStyleSheet("QFrame{\n"
"background-color:rgb(94,96,206);\n"
"border-radius: 20px;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.frame_8)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19)
        self.progressBar = QtWidgets.QProgressBar(self.frame_8)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_8.addWidget(self.progressBar)
        self.label_20 = QtWidgets.QLabel(self.frame_8)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.label_20)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(2, 2)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_3.setStretch(0, 364)
        self.verticalLayout_3.setStretch(2, 283)
        self.verticalLayout_3.setStretch(4, 82)
        self.verticalLayout_3.setStretch(6, 142)
        self.horizontalLayout.addWidget(self.fr_der)
        self.horizontalLayout.setStretch(0, 885)
        self.horizontalLayout.setStretch(1, 513)
        self.verticalLayout.addWidget(self.interfaz_general)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">HATUN MAYU</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Conexión Serial</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Puerto:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">BaudRate:</span></p></body></html>"))
        self.bt_conectar.setText(_translate("MainWindow", "Conectar"))
        self.bt_actualizar.setText(_translate("MainWindow", "Actualizar"))
        self.bt_desconectar.setText(_translate("MainWindow", "Desconectar"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Estado del Cansat</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Temperatura</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Altitud</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">GPS</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Exterior del Cansat</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Temperatura</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Presión relativa</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Giroscopio</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Humedad Relativa</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#240046;\">Aceleración</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Ubicación (GPS)</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Control de Telemetría</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Tiempo de Vuelo</span></p></body></html>"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Batería</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#240046;\">100%</span></p></body></html>"))
