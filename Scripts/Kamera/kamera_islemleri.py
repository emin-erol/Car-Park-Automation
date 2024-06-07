from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRegExp, Qt, QSize, pyqtSignal
from PyQt5.QtGui import QRegExpValidator, QIcon
from Scripts.Otomasyon.yardimUI import KameraEkleYardim, KameraSilYardim, KameraAcYardim
from kamera_kaydi import KameraKaydi
import sabitler as sb
import sqlite3

class KameraEkle(QMainWindow):
    kamera_eklendi = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Ekle")
        self.setGeometry(250, 250, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\add-camera.ico"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.baslik = QLabel("Kamera Ekle", self)
        self.baslik.setStyleSheet("font-size: 12pt;")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.idLabel = QLabel("Kamera ID:", self)
        self.idLabel.setStyleSheet("font-size: 10pt;")

        self.portLabel = QLabel("Port:", self)
        self.portLabel.setStyleSheet("font-size: 10pt;")

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Kamera Id Giriniz")
        self.idInput.setStyleSheet(f"""
                                    font-size: 10pt;
                                    border: 2px solid {sb.BORDER_COLOR};
                                    border-radius: 20px;
                                    padding-left: 10px;
                                    color: {sb.TEXT_COLOR};
                                    background-color: {sb.FRAME_BG_COLOR};
                                    ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
                                """)
        self.idInput.setFixedSize(270, 40)
        regex = QRegExp(r"[^*?&%+!\\''.:;(){}½$#£><|=,]+")
        validator = QRegExpValidator(regex)
        self.idInput.setValidator(validator)

        self.portInput = QLineEdit(self)
        self.portInput.setPlaceholderText("Port Giriniz")
        self.portInput.setStyleSheet(f"""
                                    font-size: 10pt;
                                    border: 2px solid {sb.BORDER_COLOR};
                                    border-radius: 20px;
                                    padding-left: 10px;
                                    color: {sb.TEXT_COLOR};
                                    background-color: {sb.FRAME_BG_COLOR};
                                    ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
                                """)
        self.portInput.setFixedSize(270, 40)

        self.kameraEkle = QPushButton("Kamera Ekle", self)
        self.kameraEkle.setStyleSheet(f"""
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
        self.kameraEkle.setFixedSize(270, 40)
        self.kameraEkle.clicked.connect(self.yeniKameraEkle)

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        formLayout = QVBoxLayout()
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)
        formLayout.addWidget(self.portLabel)
        formLayout.addWidget(self.portInput)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(formLayout)
        hbox.addStretch()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.kameraEkle)
        buttonLayout.addStretch()

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.baslik)
        verticalLayout.addStretch()
        verticalLayout.addLayout(hbox)
        verticalLayout.addStretch()
        verticalLayout.addLayout(buttonLayout)
        verticalLayout.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addLayout(verticalLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.yardimButonu, 0, 1, Qt.AlignRight | Qt.AlignTop)

        central_widget.setLayout(mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.yeniKameraEkle()

        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniAc()

    def yeniKameraEkle(self):
        baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        cursor = baglanti.cursor()

        camera_id = self.idInput.text()
        port = self.portInput.text()

        if camera_id and port:
            cursor.execute('''INSERT INTO cameras (camera_id, port)
                                          VALUES (?, ?)''', (camera_id, port))
            baglanti.commit()
            baglanti.close()
            onay_mesaji = "Kamera başarıyla eklendi."
            self.idInput.clear()
            self.portInput.clear()
            self.mesajKutusu(onay_mesaji)
            self.kamera_eklendi.emit()
        else:
            hata_mesaji = "Lütfen Kamera Adı ve Port bilgilerini giriniz."
            self.mesajKutusu(hata_mesaji)
            self.idInput.clear()
            self.portInput.clear()

    def mesajKutusu(self, mesaj):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Bilgi')
        msg_box.setText(f"{mesaj}")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = KameraEkleYardim()
        self.yardimPenceresi.show()


class KameraSil(QMainWindow):
    kamera_silindi = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Sil")
        self.setGeometry(250, 250, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\delete-camera.ico"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.baslik = QLabel("Kamera Sil", self)
        self.baslik.setStyleSheet("font-size: 12pt; padding: 10px;")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.idLabel = QLabel("Kamera ID:", self)
        self.idLabel.setStyleSheet("font-size: 10pt;")

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Kamera Id Giriniz")
        self.idInput.setStyleSheet(f"""
                            font-size: 10pt; 
                            border: 2px solid {sb.BORDER_COLOR};
                            border-radius: 20px; 
                            padding-left: 10px; 
                            color: {sb.TEXT_COLOR}; 
                            background-color: {sb.FRAME_BG_COLOR};
                            ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
                        """)
        self.idInput.setFixedSize(270, 40)

        self.kameraSil = QPushButton("Kamera Sil", self)
        self.kameraSil.setStyleSheet(f"""
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
        self.kameraSil.setFixedSize(270, 40)
        self.kameraSil.clicked.connect(self.kamerayiSil)

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        formLayout = QVBoxLayout()
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(formLayout)
        hbox.addStretch()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.kameraSil)
        buttonLayout.addStretch()

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.baslik)
        verticalLayout.addStretch()
        verticalLayout.addLayout(hbox)
        verticalLayout.addStretch()
        verticalLayout.addLayout(buttonLayout)
        verticalLayout.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addLayout(verticalLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.yardimButonu, 0, 1, Qt.AlignRight | Qt.AlignTop)

        central_widget.setLayout(mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.kamerayiSil()

        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniAc()

    def kamerayiSil(self):
        baglanti = None
        cursor = None
        try:
            baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
            cursor = baglanti.cursor()
            camera_id = self.idInput.text()

            if camera_id:
                cursor.execute("SELECT * FROM cameras WHERE camera_id=?", (camera_id,))
                sonuc = cursor.fetchone()

                if sonuc:
                    cursor.execute("SELECT * FROM sensors WHERE cameraId=?", (camera_id,))
                    hata_mesaji = "Kamera başarıyla kaldırıldı."
                    cursor.execute("DELETE FROM cameras WHERE camera_id=?", (camera_id,))
                    cursor.execute("DELETE FROM sensors WHERE cameraId=?", (camera_id,))
                    baglanti.commit()
                    onay_mesaji = "Kamera kaydı başarıyla silindi."
                    self.idInput.clear()
                    self.mesajKutusu(onay_mesaji)
                    self.kamera_silindi.emit()
                else:
                    hata_mesaji = "Kamera bulunamadı!"
                    self.idInput.clear()
                    self.mesajKutusu(hata_mesaji)
            else:
                hata_mesaji = "Lütfen bir kamera id'si giriniz."
                self.mesajKutusu(hata_mesaji)
        except Exception as e:
            hata_mesaji = "Bir hata oluştu, Hata Kodu: " + e
            self.mesajKutusu(hata_mesaji)
        finally:
            if cursor:
                cursor.close()
            if baglanti:
                baglanti.close()

    def mesajKutusu(self, mesaj):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Bilgi')
        msg_box.setText(f'{mesaj}')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = KameraSilYardim()
        self.yardimPenceresi.show()


class KameraSecim(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Kaydını Aç")
        self.setGeometry(250, 250, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\search-camera.ico"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.baslik = QLabel("Kamera Kaydını Aç", self)
        self.baslik.setStyleSheet("font-size: 12pt; padding: 10px;")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.idLabel = QLabel("Kamera ID:", self)
        self.idLabel.setStyleSheet("font-size: 10pt;")

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Kamera Id Giriniz")
        self.idInput.setStyleSheet(f"""
                    font-size: 10pt; 
                    border: 2px solid {sb.BORDER_COLOR};
                    border-radius: 20px; 
                    padding-left: 10px; 
                    color: {sb.TEXT_COLOR}; 
                    background-color: {sb.FRAME_BG_COLOR};
                    ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
                """)
        self.idInput.setFixedSize(270, 40)

        self.kaydi_goster = QPushButton("Kaydı Göster", self)
        self.kaydi_goster.setStyleSheet(f"""
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
        self.kaydi_goster.setFixedSize(270, 40)
        self.kaydi_goster.clicked.connect(self.kameraAc)

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        formLayout = QVBoxLayout()
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(formLayout)
        hbox.addStretch()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.kaydi_goster)
        buttonLayout.addStretch()

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.baslik)
        verticalLayout.addStretch()
        verticalLayout.addLayout(hbox)
        verticalLayout.addStretch()
        verticalLayout.addLayout(buttonLayout)
        verticalLayout.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addLayout(verticalLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.yardimButonu, 0, 1, Qt.AlignRight | Qt.AlignTop)

        central_widget.setLayout(mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.kameraAc()

        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniAc()

    def kameraAc(self):
        baglanti = None
        cursor = None
        try:
            baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
            cursor = baglanti.cursor()
            camera_id = self.idInput.text()

            if camera_id:
                cursor.execute("SELECT * FROM cameras WHERE camera_id=?", (camera_id,))
                sonuc = cursor.fetchone()

                if sonuc:
                    self.close()
                    self.kayit = KameraKaydi(camera_id)
                    self.kayit.show()
                else:
                    hata_mesaji = "Kamera kaydı bulunamadı!"
                    self.idInput.clear()
                    self.mesajKutusu(hata_mesaji)

            else:
                hata_mesaji = "Lütfen bir kamera id'si giriniz."
                self.mesajKutusu(hata_mesaji)

        except Exception as e:
            hata_mesaji = "Bir hata oluştu, Hata Kodu: " + e
            self.mesajKutusu(hata_mesaji)
        finally:
            if cursor:
                cursor.close()
            if baglanti:
                baglanti.close()

    def mesajKutusu(self, hata_mesaji):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Hata')
        msg_box.setText(f'{hata_mesaji}')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = KameraAcYardim()
        self.yardimPenceresi.show()
