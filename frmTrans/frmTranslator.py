import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import googletrans

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('frmTranslator.ui',self)
        self.AddLanguange()
        self.btnTranslate.clicked.connect(self.Translate)

    def AddLanguange(self):
        for x in googletrans.LANGUAGES.values():
            self.cmbLang1.addItem(x.capitalize())
            self.cmbLang2.addItem(x.capitalize())

    def Translate(self):
        lang1 = self.cmbLang1.currentText()
        lang2 = self.cmbLang2.currentText()
        source = self.txtLang1.toPlainText()

        translator = googletrans.Translator()
        translate = translator.translate(source,lang2,lang1)
        self.txtLang2.setPlainText(translate.text)

#main
app = QApplication(sys.argv)
frmTranslator = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget (frmTranslator)
widget.setFixedHeight(522)
widget.setFixedWidth(662)
widget.show()
sys.exit(app.exec_())