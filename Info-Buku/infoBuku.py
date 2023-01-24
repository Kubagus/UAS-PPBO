from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

import sqlite3
import sys
import os 
os.system('python Connection.py')

# conn = sqlite3.connect("D:\Materi & Tugas Kuliah\Semester 3\PBO\SqLite\dbToko.db")
# curr = conn.cursor()

class MainWindow(QDialog):
    isEdit = False
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('InfoBuku.ui', self)
        self.loadData()
        self.EventHandler()
        
    def EventHandler(self):
        self.btnSaveData.clicked.connect(self.SimpanData)
        self.btnEditData.clicked.connect(self.editData)
        self.btnDeleteData.clicked.connect(self.deleteData)
        self.btnSearch.clicked.connect(self.cariData)
        self.tblBuku.clicked.connect(self.getItem)
        self.ActiveText(False)
        
    def SimpanData(self):
        conn = sqlite3.connect("dbBuku.db")
        curr = conn.cursor()
        cb = self.btnSaveData.text()
        print(cb)
        if cb == 'New':
            self.ActiveText(True)
            self.clearForm()
            self.btnSaveData.setText('Save')
            self.btnEditData.setText('Cancel')
            
        elif cb == 'Save':
            if self.isEdit == False:
                self.btnSaveData.setText('New')    
                noIsbn = self.txtnoIsbn.text()
                judulBuku = self.txtJudulBuku.text()
                penulis = self.txtPenulis.text()
                penerbit = self.txtPenerbit.text()
                tahunTerbit = self.txtTahunTerbit.text()
                harga = self.txtPrice.text()
                
                query = "INSERT or IGNORE INTO tb_buku (no_isbn, judul_buku, penulis, penerbit, tahun_terbit, harga) VALUES (?, ?, ?, ?, ?, ?)"
                curr.execute(query,(noIsbn,judulBuku,penulis,penerbit, tahunTerbit, harga))
                conn.commit()
                print("Simpan Berhasil")
               
            elif self.isEdit == True:
                noIsbn = self.txtnoIsbn.text()
                judulBuku = self.txtJudulBuku.text()
                penulis = self.txtPenulis.text()
                penerbit = self.txtPenerbit.text()
                tahunTerbit = self.txtTahunTerbit.text()
                harga = self.txtPrice.text()            
                query = "UPDATE tb_buku SET no_isbn = ?, judul_buku = ?, penulis = ?, penerbit = ?, tahun_terbit = ?, harga = ? WHERE no_isbn = ?"
                curr.execute(query,(noIsbn, judulBuku,penulis,penerbit,tahunTerbit,harga, noIsbn))
                conn.commit()
                print("Edit Berhasil")
            curr.close()
            conn.close()
            self.loadData()
            self.ActiveText(False)
            self.clearForm()
            self.btnSaveData.setText('New')
            self.btnEditData.setText('Edit')
        return
    def editData(self):
            if self.btnEditData.text() == 'Edit':
                self.btnEditData.setText('Cancel')
                self.btnSaveData.setText('Save')
                self.ActiveText(True)
                self.isEdit = True
                
            elif self.btnEditData.text() == 'Cancel':
                self.btnEditData.setText('Edit')
                self.btnSaveData.setText('New')
                self.ActiveText(False)
                self.clearForm()

    def deleteData(self):
        conn = sqlite3.connect("dbBuku.db")
        curr = conn.cursor()
        query = "DELETE FROM tb_buku WHERE no_isbn = ?"
        noIsbn = self.txtnoIsbn.text()
        curr.execute(query,(noIsbn,))
        conn.commit()
        print("Hapus Berhasil")
        curr.close()
        conn.close()
        self.loadData()
        self.clearForm()
        return
        
        
    def getItem(self):
        row = self.tblBuku.currentRow()
        noIsbn = self.tblBuku.item(row, 0).text()
        judulBuku = self.tblBuku.item(row, 1).text()
        penulis = self.tblBuku.item(row, 2).text()
        penerbit = self.tblBuku.item(row, 3).text()
        tahunTerbit = self.tblBuku.item(row, 4).text()
        harga = self.tblBuku.item(row, 5).text()
        
        self.txtnoIsbn.setText(noIsbn)
        self.txtJudulBuku.setText(judulBuku)
        self.txtPenulis.setText(penulis)
        self.txtPenerbit.setText(penerbit)
        self.txtTahunTerbit.setText(tahunTerbit)
        self.txtPrice.setText(harga)
        return
        
        
    def clearForm(self):
        self.txtnoIsbn.setText("")
        self.txtJudulBuku.setText("")
        self.txtPenulis.setText("")
        self.txtPenerbit.setText("")
        self.txtTahunTerbit.setText("")
        self.txtPrice.setText("")
        return
    
    def ActiveText(self, bool):
        self.txtnoIsbn.setEnabled(bool)
        self.txtJudulBuku.setEnabled(bool)
        self.txtPenulis.setEnabled(bool)
        self.txtPenerbit.setEnabled(bool)
        self.txtTahunTerbit.setEnabled(bool)
        self.txtPrice.setEnabled(bool)
        return
        
    def loadData(self):
        conn = sqlite3.connect("dbBuku.db")
        curr = conn.cursor()
        query = f"SELECT * FROM tb_buku WHERE judul_buku LIKE '%{ self.txtSearch.text()}%' OR penulis LIKE '%{ self.txtSearch.text()}%' OR penerbit LIKE '%{ self.txtSearch.text()}%' OR tahun_terbit LIKE '%{ self.txtSearch.text()}%' OR harga LIKE '%{ self.txtSearch.text()}%' ORDER BY judul_buku ASC"
        curr.execute(query)
        result = curr.fetchall()
        conn.commit()
        self.tblBuku.setRowCount(len(result))
        tableRow = 0

        for row in result:
            self.tblBuku.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tblBuku.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tblBuku.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tblBuku.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tblBuku.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tblBuku.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tblBuku.setItem(tableRow, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            tableRow +=1
        curr.close()
        conn.close()
        return

    def cariData(self):
        self.loadData()
        
        
# Main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(700)
widget.setFixedWidth(750)
widget.show()

try:
    sys.exit(app.exec_())
    
except:
    print('Exiting')

