# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stringify_desktop_appnphiXL.ui'
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
        font = QFont()
        font.setFamily("Ubuntu")
        Stringify.setFont(font)
        self.centralwidget = QWidget(Stringify)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(110, 30, 561, 121))
        font1 = QFont()
        font1.setFamily("Ubuntu")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.input_text_field = QTextEdit(self.centralwidget)
        self.input_text_field.setObjectName("input_text_field")
        self.input_text_field.setGeometry(QRect(40, 250, 281, 211))
        self.output_text_field = QTextEdit(self.centralwidget)
        self.output_text_field.setObjectName("output_text_field")
        self.output_text_field.setGeometry(QRect(480, 250, 281, 211))
        self.stringify_button = QPushButton(self.centralwidget)
        self.stringify_button.setObjectName("stringify_button")
        self.stringify_button.setGeometry(QRect(360, 330, 89, 25))
        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setGeometry(QRect(360, 390, 89, 25))
        self.delimeter_comboBox = QComboBox(self.centralwidget)
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.setObjectName("delimeter_comboBox")
        self.delimeter_comboBox.setGeometry(QRect(370, 270, 71, 25))
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
        self.input_text_field.setPlaceholderText(
            QCoreApplication.translate("Stringify", "Paste or type your raw text here!!", None)
        )
        self.stringify_button.setText(QCoreApplication.translate("Stringify", "stringify", None))
        self.reset_button.setText(QCoreApplication.translate("Stringify", "reset", None))
        self.delimeter_comboBox.setItemText(0, QCoreApplication.translate("Stringify", ",", None))
        self.delimeter_comboBox.setItemText(1, QCoreApplication.translate("Stringify", ";", None))
        self.delimeter_comboBox.setItemText(2, QCoreApplication.translate("Stringify", ":", None))
        self.delimeter_comboBox.setItemText(3, QCoreApplication.translate("Stringify", "|", None))
        self.delimeter_comboBox.setItemText(
            4, QCoreApplication.translate("Stringify", "space", None)
        )
        self.delimeter_comboBox.setItemText(
            5, QCoreApplication.translate("Stringify", "newline", None)
        )

        # if QT_CONFIG(tooltip)
        self.delimeter_comboBox.setToolTip(
            QCoreApplication.translate("Stringify", "choose a delimeter!", None)
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi
