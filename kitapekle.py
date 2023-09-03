import sys
from kitapekle_ui import (Ui_KitapEkleForm)
from PyQt5.QtWidgets import *
import veritabani_06 as baglanti
class KitapEkleEkrani(QWidget, Ui_KitapEkleForm):
    def __init__(self, k_id):
        super().__init__()
        self.k_id = k_id
        self.setupUi(self)
        self.kaydetButton.clicked(self.kitap_ekle)

    def kitap_ekle(self):
        k_adi = self.kitap_Adi.text()
        k_yazari = self.kitap_YazariLineEdit.text()
        k_durumu = self.okunma_DurumuCheckBox.checkState()
        k_begeni = self.begeni_DurumuComboBox.currentText()
        sonuc = baglanti.ekle(self.k_id, k_adi, k_yazari, k_durumu, k_begeni)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = KitapEkleEkrani(1)
    pencere.show()
    sys.exit(app.exec_())
