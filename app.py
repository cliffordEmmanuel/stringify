from PyQt5 import QtCore, QtGui, QtWidgets
from detect_delimiter import detect


class Ui_Stringify(object):
    def __init__(self) -> None:
        self._raw_text = None
        self._processed_text = None
        self._separator = ","

    def setupUi(self, Stringify):
        Stringify.setObjectName("Stringify")
        Stringify.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        Stringify.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Stringify)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 561, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        # input text field
        self.input_text_field = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text_field.setGeometry(QtCore.QRect(40, 250, 281, 211))
        self.input_text_field.setObjectName("input_text_field")

        # output text field
        self.output_text_field = QtWidgets.QTextEdit(self.centralwidget)
        self.output_text_field.setGeometry(QtCore.QRect(480, 250, 281, 211))
        self.output_text_field.setObjectName("output_text_field")

        # stringify button
        self.stringify_button = QtWidgets.QPushButton(self.centralwidget)
        self.stringify_button.setGeometry(QtCore.QRect(360, 320, 89, 25))
        self.stringify_button.setObjectName("stringify_button")

        self.stringify_button.clicked.connect(self.stringify_clicked)

        # delimit button
        self.delimit_button = QtWidgets.QPushButton(self.centralwidget)
        self.delimit_button.setGeometry(QtCore.QRect(360, 360, 89, 25))
        self.delimit_button.setObjectName("delimit_button")

        self.delimit_button.clicked.connect(self.delimit_clicked)

        # reset button
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(360, 400, 89, 25))
        self.reset_button.setObjectName("reset_button")

        self.reset_button.clicked.connect(self._reset)

        self.delimeter_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.delimeter_comboBox.setGeometry(QtCore.QRect(370, 270, 71, 25))
        self.delimeter_comboBox.setObjectName("delimeter_comboBox")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")
        self.delimeter_comboBox.addItem("")

        Stringify.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stringify)
        QtCore.QMetaObject.connectSlotsByName(Stringify)

    def stringify(self, raw_text: str, separator: str = ",") -> str:
        """Converts a raw list of objects into their string versions.

        Args:
            raw (str): assumes that the input is a big string of the objects combined.
            separator (str, optional): the character to be used as a delimeter. Defaults to ','.

        Returns:
            str: a 'stringified' version of the delimited objects.
        """

        if separator == "newline":
            separator = "\n"
        elif separator == "space":
            separator = " "

        # detecting the delimiter used in the raw text provided
        delimiter = detect(raw_text, whitelist=[" ", ",", "|", ";", "\t", "\n"])
        # count how many times a delimiter occurs rank by frequency and return the one that occurs the most.
        # perhaps i can re-write this instead of importing a library...

        splitted = raw_text.split(delimiter)
        # the str.split function always returns a list of string versions.
        string_version = str(splitted).replace("[", "").replace("]", "")

        processed_text = string_version.replace(", ", separator)

        return processed_text

    def delimit(self, raw_text: str, separator: str = ",") -> str:
        """Separates a list of objects by a specifc delimiter.

        Args:
            raw (str): assumes that the input is a big string of the objects combined.
            separator (str, optional): the character to be used as a delimeter. Defaults to ','.

        Returns:
            str: the delimited objects.
        """

        if separator == "newline":
            separator = "\n"
        elif separator == "space":
            separator = " "

        # detecting the delimiter used in the raw text provided
        delimiter = detect(raw_text, whitelist=[" ", ",", "|", ";", "\t", "\n"])

        splitted = raw_text.split(delimiter)
        processed_text = separator.join(splitted)

        return processed_text

    def stringify_clicked(self) -> None:
        """Calls the stringify function when the stringify button is clicked"""

        # get the raw text entered
        self._raw_text = self.input_text_field.toPlainText()
        print(f"raw_text: {self._raw_text}")
        # get the separator
        self._separator = self.delimeter_comboBox.currentText()
        # compute the stringified version
        self._processed_text = self.stringify(self._raw_text, self._separator)
        print(f"processed_text: {self._processed_text}")
        # output to the output text field
        self.output_text_field.clear()
        self.output_text_field.insertPlainText(self._processed_text)

        return None

    def delimit_clicked(self) -> None:
        """Calls the delimit function when the delimit button is clicked"""

        # get the raw text entered
        self._raw_text = self.input_text_field.toPlainText()
        print(f"raw_text: {self._raw_text}")
        # get the separator
        self._separator = self.delimeter_comboBox.currentText()
        # compute the stringified version
        self._processed_text = self.delimit(self._raw_text, self._separator)
        print(f"processed_text: {self._processed_text}")
        # output to the output text field
        self.output_text_field.clear()
        self.output_text_field.insertPlainText(self._processed_text)

        return None

    def _reset(self):
        """Resets all the input and output elements to their default"""
        self.input_text_field.clear()
        self.output_text_field.clear()
        self.delimeter_comboBox.setCurrentText(",")
        # TODO: add a message box to display info.
        print("All fields have been reset back to defaults")

    def retranslateUi(self, Stringify):
        _translate = QtCore.QCoreApplication.translate
        Stringify.setWindowTitle(_translate("Stringify", "Stringify desktop"))
        self.label.setText(
            _translate(
                "Stringify",
                "Convert any collection of objects to strings separated by any delimeter of your choice.",
            )
        )
        self.input_text_field.setPlaceholderText(
            _translate("Stringify", "Paste or type your raw text here!!")
        )
        self.stringify_button.setText(_translate("Stringify", "stringify"))
        self.delimit_button.setText(_translate("Stringify", "delimit"))
        self.reset_button.setText(_translate("Stringify", "reset"))
        self.delimeter_comboBox.setToolTip(_translate("Stringify", "choose a delimeter!"))
        self.delimeter_comboBox.setItemText(0, _translate("Stringify", ","))
        self.delimeter_comboBox.setItemText(1, _translate("Stringify", ";"))
        self.delimeter_comboBox.setItemText(2, _translate("Stringify", ":"))
        self.delimeter_comboBox.setItemText(3, _translate("Stringify", "|"))
        self.delimeter_comboBox.setItemText(4, _translate("Stringify", "space"))
        self.delimeter_comboBox.setItemText(5, _translate("Stringify", "newline"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Stringify = QtWidgets.QMainWindow()
    ui = Ui_Stringify()
    ui.setupUi(Stringify)
    Stringify.show()
    sys.exit(app.exec_())
