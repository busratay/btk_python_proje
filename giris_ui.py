import sys
from PyQt5.QtWidgets import *
from giris import Ui_Form
from anaekran import Anaekran
import veritabani_06 as baglanti

class GirisPenceresi(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sifreText.setEchoMode(QLineEdit.Password)
        self.girisButton.clicked.connect(self.fGirisKontrol)

    def fGirisKontrol(self):
        self.mesajLabel.setText("Giriş Butonu Tıklandı")
        eposta = self.epostaText.text()
        sifre = self.sifreText.text()
        k_id = baglanti.k_giris(eposta, sifre)
        if k_id == 0:
            self.mesajLabel.setText("Hatalı Giriş Yapıldı")

        else:
            self.mesajLabel.setText("Giriş Onaylandı")
            self.close()
            self.ype = Anaekran(k_id)
            self.ype.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = GirisPenceresi()
    pencere.show()
    sys.exit(app.exec_())
