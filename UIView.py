# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UIView(object):
    def setupUi(self, UIView):
        if not UIView.objectName():
            UIView.setObjectName(u"UIView")
        UIView.resize(551, 391)
        UIView.setContextMenuPolicy(Qt.PreventContextMenu)
        icon = QIcon()
        icon.addFile(u"games.ico", QSize(), QIcon.Normal, QIcon.Off)
        UIView.setWindowIcon(icon)
        self.centralwidget = QWidget(UIView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 241, 371))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(self.groupBox_2)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaxLength(10)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)

        self.lineEdit_0 = QLineEdit(self.groupBox_2)
        self.lineEdit_0.setObjectName(u"lineEdit_0")
        self.lineEdit_0.setMaxLength(6)

        self.gridLayout.addWidget(self.lineEdit_0, 8, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(260, 280, 281, 101))
        self.choice_theme = QComboBox(self.groupBox_7)
        self.choice_theme.setObjectName(u"choice_theme")
        self.choice_theme.setGeometry(QRect(20, 40, 241, 41))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 10, 281, 261))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaxLength(6)

        self.gridLayout_3.addWidget(self.lineEdit_9, 0, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_14, 3, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaxLength(6)

        self.gridLayout_3.addWidget(self.lineEdit_10, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 4, 0, 1, 4)

        self.doubleSpinBox_1 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_1.setObjectName(u"doubleSpinBox_1")
        self.doubleSpinBox_1.setMinimum(-1.000000000000000)
        self.doubleSpinBox_1.setMaximum(1.000000000000000)
        self.doubleSpinBox_1.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_1, 1, 1, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimum(-1.000000000000000)
        self.doubleSpinBox_3.setMaximum(1.000000000000000)
        self.doubleSpinBox_3.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMinimum(-1.000000000000000)
        self.doubleSpinBox_4.setMaximum(1.000000000000000)
        self.doubleSpinBox_4.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_4, 3, 3, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimum(-1.000000000000000)
        self.doubleSpinBox_2.setMaximum(1.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_2, 1, 3, 1, 1)

        self.gridLayout_3.setColumnMinimumWidth(1, 100)
        self.gridLayout_3.setColumnMinimumWidth(3, 100)
        UIView.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.lineEdit_0)
        QWidget.setTabOrder(self.lineEdit_0, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.doubleSpinBox_1)
        QWidget.setTabOrder(self.doubleSpinBox_1, self.doubleSpinBox_2)
        QWidget.setTabOrder(self.doubleSpinBox_2, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.doubleSpinBox_3)
        QWidget.setTabOrder(self.doubleSpinBox_3, self.doubleSpinBox_4)
        QWidget.setTabOrder(self.doubleSpinBox_4, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.choice_theme)

        self.retranslateUi(UIView)

        QMetaObject.connectSlotsByName(UIView)
    # setupUi

    def retranslateUi(self, UIView):
        UIView.setWindowTitle(QCoreApplication.translate("UIView", u"Keyboard", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("UIView", u"\u952e\u4f4d/Key map", None))
        self.label_8.setText(QCoreApplication.translate("UIView", u"\u8868\u60c5/Emote", None))
        self.label_4.setText(QCoreApplication.translate("UIView", u"\u5411\u5de6/Left", None))
        self.pushButton.setText(QCoreApplication.translate("UIView", u"\u5e94\u7528/Apply", None))
        self.label_6.setText(QCoreApplication.translate("UIView", u"\u64cd\u4f5c/Operate", None))
        self.label_7.setText(QCoreApplication.translate("UIView", u"\u62ff\u653e/Pick up", None))
        self.label.setText(QCoreApplication.translate("UIView", u"\u5411\u4e0a/Up", None))
        self.label_2.setText(QCoreApplication.translate("UIView", u"\u5411\u4e0b/Down", None))
        self.label_3.setText(QCoreApplication.translate("UIView", u"\u52a0\u901f/Dash", None))
        self.label_5.setText(QCoreApplication.translate("UIView", u"\u5411\u53f3/Right", None))
        self.label_15.setText(QCoreApplication.translate("UIView", u"\u6362\u4eba/Switch", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("UIView", u"\u4e3b\u9898/Theme", None))
        self.groupBox.setTitle(QCoreApplication.translate("UIView", u"\u5c0f\u89d2\u5ea6/Arbitrary angle", None))
        self.label_9.setText(QCoreApplication.translate("UIView", u"\u952e1/Key1", None))
        self.label_11.setText(QCoreApplication.translate("UIView", u"Y", None))
        self.label_13.setText(QCoreApplication.translate("UIView", u"X", None))
        self.label_10.setText(QCoreApplication.translate("UIView", u"X", None))
        self.label_14.setText(QCoreApplication.translate("UIView", u"Y", None))
        self.label_12.setText(QCoreApplication.translate("UIView", u"\u952e2/Key1", None))
        self.pushButton_2.setText(QCoreApplication.translate("UIView", u"\u5e94\u7528/Apply", None))
    # retranslateUi

