# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stringify_desktop_app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Stringify(object):
    def setupUi(self, Stringify):
        if not Stringify.objectName():
            Stringify.setObjectName("Stringify")
        Stringify.resize(800, 600)
        self.centralwidget = QWidget(Stringify)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(110, 30, 561, 121))
        font = QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(40, 250, 281, 211))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setGeometry(QRect(480, 250, 281, 211))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(360, 330, 89, 25))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 390, 89, 25))
        self.delimeter_choice_comboBox = QComboBox(self.centralwidget)
        self.delimeter_choice_comboBox.addItem("")
        self.delimeter_choice_comboBox.addItem("")
        self.delimeter_choice_comboBox.addItem("")
        self.delimeter_choice_comboBox.addItem("")
        self.delimeter_choice_comboBox.addItem("")
        self.delimeter_choice_comboBox.addItem("")
        self.delimeter_choice_comboBox.setObjectName("delimeter_choice_comboBox")
        self.delimeter_choice_comboBox.setGeometry(QRect(370, 270, 71, 25))
        Stringify.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stringify)

        QMetaObject.connectSlotsByName(Stringify)

    # setupUi

    def retranslateUi(self, Stringify):
        Stringify.setWindowTitle(QCoreApplication.translate("Stringify", "MainWindow", None))
        self.label.setText(
            QCoreApplication.translate(
                "Stringify",
                "Convert any collection of objects to strings separated by any delimeter of your choice.",
                None,
            )
        )
        self.textEdit.setPlaceholderText(
            QCoreApplication.translate("Stringify", "Paste or type your raw text here!!", None)
        )
        self.pushButton.setText(QCoreApplication.translate("Stringify", "stringify", None))
        self.pushButton_2.setText(QCoreApplication.translate("Stringify", "reset", None))
        self.delimeter_choice_comboBox.setItemText(
            0, QCoreApplication.translate("Stringify", ",", None)
        )
        self.delimeter_choice_comboBox.setItemText(
            1, QCoreApplication.translate("Stringify", ";", None)
        )
        self.delimeter_choice_comboBox.setItemText(
            2, QCoreApplication.translate("Stringify", ":", None)
        )
        self.delimeter_choice_comboBox.setItemText(
            3, QCoreApplication.translate("Stringify", "|", None)
        )
        self.delimeter_choice_comboBox.setItemText(
            4, QCoreApplication.translate("Stringify", "space", None)
        )
        self.delimeter_choice_comboBox.setItemText(
            5, QCoreApplication.translate("Stringify", "newline", None)
        )

        # if QT_CONFIG(tooltip)
        self.delimeter_choice_comboBox.setToolTip(
            QCoreApplication.translate("Stringify", "choose a delimeter!", None)
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi
