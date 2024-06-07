from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from kameraUI import Kameralar
from Scripts.Otomasyon.yardimUI import NasilKullanilirYardim
import sabitler as sb
import sqlite3
import sys

class ClickableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        self.nasil_kullanilir = NasilKullanilirYardim()
        self.nasil_kullanilir.show()

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Sayfası")
        self.setGeometry(400, 400, 750, 500)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\icon.ico"))
        self.initUI()

    def initUI(self):
        main_bg_color = "#f0f4f7"
        frame_bg_color = "#ffffff"
        border_color = "#cccccc"
        primary_color = "#007BFF"
        button_bg_color = primary_color
        button_hover_color = "#99ccff"
        button_text_color = "#ffffff"
        text_color = "#333333"
        placeholder_color = "#888888"
        footer_text_color = "#555555"

        self.setStyleSheet(f"background-color: {sb.MAIN_BG_COLOR};")

        self.ana_baslik = QLabel("HOŞGELDİNİZ", self)
        self.ana_baslik.setStyleSheet(f"font-size: 22pt; font-weight: bold; padding: 10px; color: {sb.TEXT_COLOR};")
        self.ana_baslik.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        self.baslik = QLabel("GİRİŞ", self)
        self.baslik.setStyleSheet(f"font-size: 20pt; font-weight: bold; padding: 10px; color: {sb.TEXT_COLOR};")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.kullaniciAdiLabel = QLabel("Kullanıcı Adı:", self)
        self.kullaniciAdiLabel.setStyleSheet(f"font-size: 10pt; border: None; color: {sb.TEXT_COLOR};")

        self.sifreLabel = QLabel("Şifre:", self)
        self.sifreLabel.setStyleSheet(f"font-size: 10pt; border: None; color: {sb.TEXT_COLOR};")

        self.kullaniciAdiInput = QLineEdit(self)
        self.kullaniciAdiInput.setPlaceholderText("Kullanıcı Adı")
        self.kullaniciAdiInput.setStyleSheet(f"""
            font-size: 10pt; 
            border: 2px solid {sb.BORDER_COLOR};
            border-radius: 20px; 
            padding-left: 10px; 
            color: {sb.TEXT_COLOR}; 
            background-color: {sb.FRAME_BG_COLOR};
            ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
        """)
        self.kullaniciAdiInput.setFixedSize(270, 40)

        self.sifreInput = QLineEdit(self)
        self.sifreInput.setPlaceholderText("********")
        self.sifreInput.setStyleSheet(f"""
            font-size: 10pt; 
            border: 2px solid {sb.BORDER_COLOR};
            border-radius: 20px; 
            padding-left: 10px; 
            color: {sb.TEXT_COLOR};
            background-color: {sb.FRAME_BG_COLOR};
            ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
        """)
        self.sifreInput.setEchoMode(QLineEdit.Password)
        self.sifreInput.setFixedSize(270, 40)

        self.girisYapButton = QPushButton("Giriş Yap", self)
        self.girisYapButton.setStyleSheet(f"""
                    QPushButton {{
                        font-size: 10pt; 
                        border-radius: 20px; 
                        color: {sb.BUTTON_TEXT_COLOR}; 
                        background-color: {sb.BUTTON_BG_COLOR};
                    }}
                    QPushButton:hover {{
                        background-color: {sb.BUTTON_HOVER_COLOR};
                    }}
                """)
        self.girisYapButton.clicked.connect(self.girisKontrolu)
        self.girisYapButton.setFixedSize(270, 40)

        self.nasilKullanilir = ClickableLabel("Nasıl Kullanılır ?")
        self.nasilKullanilir.setStyleSheet(f"color: {sb.FOOTER_TEXT_COLOR}; text-decoration: underline;")
        self.nasilKullanilir.setAlignment(Qt.AlignCenter)

        self.footer1 = QLabel("Bilgi ve iletişim için erolemin@outlook.com.tr adresinden iletişime geçebilirsiniz.",
                              self)
        self.footer1.setStyleSheet(f"font-size: 9pt; color: {sb.FOOTER_TEXT_COLOR};")
        self.footer1.setAlignment(Qt.AlignCenter)

        self.footer2 = QLabel("Bütün Hakları Saklıdır®.", self)
        self.footer2.setStyleSheet(f"font-size: 9pt; color: {sb.FOOTER_TEXT_COLOR};")
        self.footer2.setAlignment(Qt.AlignCenter)

        containerFrame = QFrame(self)
        containerFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        containerFrame.setLineWidth(2)
        containerFrameLayout = QVBoxLayout(containerFrame)
        containerFrameLayout.addWidget(self.baslik)
        containerFrameLayout.addStretch()
        containerFrameLayout.addWidget(self.kullaniciAdiLabel)
        containerFrameLayout.addWidget(self.kullaniciAdiInput)
        containerFrameLayout.addStretch()
        containerFrameLayout.addWidget(self.sifreLabel)
        containerFrameLayout.addWidget(self.sifreInput)
        containerFrameLayout.addStretch()
        containerFrameLayout.addWidget(self.girisYapButton)
        containerFrame.setStyleSheet(f"""
            QFrame {{
                background-color: {sb.FRAME_BG_COLOR};
                border: 2px solid {sb.BORDER_COLOR};
                border-radius: 10px;
                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.25);
            }}
        """)

        containerFrame.setFixedSize(300, 350)
        mainLayout = QVBoxLayout(self)

        mainLayout.addWidget(self.ana_baslik)
        mainLayout.setAlignment(self.ana_baslik, Qt.AlignTop)

        upperSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(upperSpacer)

        contentLayout = QHBoxLayout()
        contentLayout.addStretch()
        contentLayout.addWidget(containerFrame)
        contentLayout.addStretch()

        footerLayout = QVBoxLayout()
        footerLayout.addWidget(self.nasilKullanilir)
        footerLayout.addWidget(self.footer1)
        footerLayout.addWidget(self.footer2)

        mainLayout.addLayout(contentLayout)
        mainLayout.addStretch()
        mainLayout.addLayout(footerLayout)
        mainLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.girisKontrolu()

    def girisKontrolu(self):
        k_adi = self.kullaniciAdiInput.text()
        sifre = self.sifreInput.text()

        if self.kontrol(k_adi, sifre):
            self.close()
            self.kameralar = Kameralar()
            self.kameralar.show()
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")
            self.kullaniciAdiInput.clear()
            self.sifreInput.clear()

    def kontrol(self, k_adi, sifre):
        baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        cursor = baglanti.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (k_adi, sifre))

        if cursor.fetchone():
            return True
        else:
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())
