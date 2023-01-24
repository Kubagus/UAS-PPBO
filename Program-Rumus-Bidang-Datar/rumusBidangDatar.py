from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sys
import math

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('formMenu.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnPersegi.clicked.connect(self.persegi)
        self.btnPersegiPanjang.clicked.connect(self.persegiPanjang)
        self.btnJajarGenjang.clicked.connect(self.jajarGenjang)
        self.btnSegiTiga.clicked.connect(self.segiTiga)
        self.btnBelahKetupat.clicked.connect(self.belahKetupat)
        self.btnLayangLayang.clicked.connect(self.layangLayang)
        self.btnLingkaran.clicked.connect(self.lingkaran)
        self.btnTrapesium.clicked.connect(self.trapesium)
    
    def persegi(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
    def persegiPanjang(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
    def jajarGenjang(self):
        widget.setCurrentIndex(widget.currentIndex()+3)
    def segiTiga(self):
        widget.setCurrentIndex(widget.currentIndex()+4)
    def belahKetupat(self):
        widget.setCurrentIndex(widget.currentIndex()+5)
    def layangLayang(self):
        widget.setCurrentIndex(widget.currentIndex()+6)
    def lingkaran(self):
        widget.setCurrentIndex(widget.currentIndex()+7)
    def trapesium(self):
        widget.setCurrentIndex(widget.currentIndex()+8)
  
        
class Persegi(QDialog):
    def __init__(self):
        super(Persegi, self).__init__()
        loadUi('rumusPersegi.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasPersegi.clicked.connect(self.luasPersegi)
        
    def luasPersegi(self):
        panjangSisi = float(self.txtSisi.text())
        hasil = panjangSisi * panjangSisi
        self.txtLuasPersegi.setText(f"{hasil:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
 
       
class PersegiPanjang(QDialog):
    def __init__(self):
        super(PersegiPanjang, self).__init__()
        loadUi('rumusPersegiPanjang.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasPersegiPanjang.clicked.connect(self.luasPersegiPanjang)
        
    def luasPersegiPanjang(self):
        panjang = float(self.txtPanjang.text())
        lebar = float(self.txtLebar.text())
        luas = panjang * lebar
        self.txtLuasPersegiPanjang.setText(f"{luas:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

       
class JajarGenjang(QDialog):
    def __init__(self):
        super(JajarGenjang, self).__init__()
        loadUi('rumusJajarGenjang.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasJajarGenjang.clicked.connect(self.luasJajarGenjang)
        
    def luasJajarGenjang(self):
        alas = float(self.txtAlas.text())
        tinggi = float(self.txtTinggi.text())
        luas = alas * tinggi
        self.txtLuasJajarGenjang.setText(f"{luas:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-3)
       
       
class SegiTiga(QDialog):
    def __init__(self):
        super(SegiTiga, self).__init__()
        loadUi('rumusSegiTiga.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasSegiTiga.clicked.connect(self.luasSegiTiga)
        
    def luasSegiTiga(self):
        alas = int(self.txtAlasSegiTiga.text())
        tinggi = int(self.txtTinggiSegiTIga.text())
        luas = alas * tinggi / 2
        self.txtLuasSegiTiga.setText(str(luas))
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-4)
       
       
class BelahKetupat(QDialog):
    def __init__(self):
        super(BelahKetupat, self).__init__()
        loadUi('rumusBelahKetupat.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasBelahKetupat.clicked.connect(self.luasBelahKetupat)
        
    def luasBelahKetupat(self):
        diagonal1 = float(self.txtDiagonal1.text())
        diagonal2 = float(self.txtDiagonal2.text())
        luas = diagonal1 * diagonal2 / 2
        self.txtLuasBelahKetupat.setText(f"{luas:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-5)
       
       
class LayangLayang(QDialog):
    def __init__(self):
        super(LayangLayang, self).__init__()
        loadUi('rumusLayangLayang.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasLayangLayang.clicked.connect(self.luasLayangLayang)
        
    def luasLayangLayang(self):
        diagonal1 = float(self.txtDiagonal1.text())
        diagonal2 = float(self.txtDiagonal2.text())
        luas = diagonal1 * diagonal2 / 2
        self.txtLuasLayangLayang.setText(f"{luas:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-6)
       
       
class Lingkaran(QDialog):
    def __init__(self):
        super(Lingkaran, self).__init__()
        loadUi('rumusLingkaran.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasLingkaran.clicked.connect(self.luasLingkaran)
        
    def luasLingkaran(self):
        jariJari = float(self.txtLingkaran.text())
        luas = math.pi * jariJari**2
        self.txtLuasLingkaran.setText(f"{luas:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-7)
       
       
class Trapesium(QDialog):
    def __init__(self):
        super(Trapesium, self).__init__()
        loadUi('rumusTrapesium.ui', self)
        self.EventHandler()
        
    def EventHandler(self):
        self.btnBack.clicked.connect(self.menu)
        self.btnHitungLuasTrapesium.clicked.connect(self.luasTrapesium)
        
    def luasTrapesium(self):
        sisiAtas = float(self.txtSisiAtas.text())
        sisiBawah = float(self.txtSisiBawah.text())
        TinggiTrapesium = float(self.txtTinggiTrapesium.text())
        luas = (sisiAtas + sisiBawah) * TinggiTrapesium / 2
        self.txtLuasTrapesium.setText(f"{luas:.2f}")
    
    def menu(self):
        widget.setCurrentIndex(widget.currentIndex()-8)
       

# Main
app = QApplication(sys.argv)
mainwindow = MainWindow()
formPersegi = Persegi()
formPersegiPanjang = PersegiPanjang()
formJajarGenjang = JajarGenjang()
formSegiTiga = SegiTiga()
formBelahKetupat = BelahKetupat()
formLayangLayang = LayangLayang()
formLingkaran = Lingkaran()
formTrapesium = Trapesium()

widgetForm = [mainwindow, formPersegi, formPersegiPanjang, formJajarGenjang, formSegiTiga, formBelahKetupat, formLayangLayang, formLingkaran, formTrapesium]
widget = QtWidgets.QStackedWidget()

for w in widgetForm:
    widget.addWidget(w)
    
widget.setFixedHeight(500)
widget.setFixedWidth(650)
widget.show()

try:
    sys.exit(app.exec_())
    
except:
    print('Exiting')
