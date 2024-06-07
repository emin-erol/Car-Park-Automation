from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from kamera_islemleri import KameraEkle, KameraSil, KameraSecim
from sensor_islemleri import SensorIslemleri, SensorleriGor
from kamera_kaydi import KameraKaydi
from Scripts.Otomasyon.yardimUI import KameralarYardim
import sabitler as sb
import yazdir
import sqlite3

class Kameralar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kameralar")
        self.setGeometry(100, 100, 1400, 900)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\icon.ico"))
        self.initUI()

    def initUI(self):
        self.baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        self.cursor = self.baglanti.cursor()
        self.grid = QGridLayout()

        self.baslik = QLabel("KAMERALAR")
        self.baslik.setStyleSheet("font-size: 24pt; font-weight: bold; padding: 10px;")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.kamera_ekle_buton = QPushButton("Kamera Ekle")
        self.kamera_ekle_buton.setStyleSheet(f"""
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
        self.kamera_ekle_buton.setFixedSize(270, 40)
        self.kamera_ekle_buton.clicked.connect(self.kameraEkle)

        self.kamera_sil_buton = QPushButton("Kamera Sil")
        self.kamera_sil_buton.setStyleSheet(f"""
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
        self.kamera_sil_buton.setFixedSize(270, 40)
        self.kamera_sil_buton.clicked.connect(self.kameraSil)

        self.kamera_ac_buton = QPushButton("Kamerayı Aç")
        self.kamera_ac_buton.setStyleSheet(f"""
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
        self.kamera_ac_buton.setFixedSize(270, 40)
        self.kamera_ac_buton.clicked.connect(self.kameraAc)

        self.yenile_buton = QPushButton("Yenile")
        self.yenile_buton.setStyleSheet(f"""
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
        self.yenile_buton.setFixedSize(270, 40)
        self.yenile_buton.clicked.connect(self.kameralariGoster)

        self.sensor_ekle_buton = QPushButton("Sensörleri Gör")
        self.sensor_ekle_buton.setStyleSheet(f"""
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
        self.sensor_ekle_buton.setFixedSize(270, 40)
        self.sensor_ekle_buton.clicked.connect(self.sensorleriGor)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.kamera_ekle_buton)
        self.hbox.addWidget(self.kamera_sil_buton)
        self.hbox.addWidget(self.kamera_ac_buton)
        self.hbox.addWidget(self.sensor_ekle_buton)
        self.hbox.addWidget(self.yenile_buton)
        self.hbox.addStretch()

        self.menubar = QMenuBar(self)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setFixedWidth(self.width())

        dosya = self.menubar.addMenu('Dosya')
        araclar = self.menubar.addMenu('Araçlar')

        yardim = QAction(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"),
                         'Yardım                   F1', self)
        yardim.triggered.connect(self.yardimPenceresiniAc)

        yenile = QAction(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\refresh.ico"),
                         'Sayfayı Yenile        F5', self)
        yenile.triggered.connect(self.kameralariGoster)

        yazdir = QAction(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\print.ico"),
                         'Verileri Yazdır        Ctrl+P', self)
        yazdir.triggered.connect(self.tablolariYazdir)

        kamera_ac = QAction(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\search-camera.ico"),
                              'Kamera Aç            F2', self)
        kamera_ac.triggered.connect(self.kameraAc)

        kamera_ekle = QAction(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\add-camera.ico"),
                              'Kamera Ekle          F3', self)
        kamera_ekle.triggered.connect(self.kameraEkle)

        kamera_sil = QAction(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\delete-camera.ico"), 'Kamera Sil             F4', self)
        kamera_sil.triggered.connect(self.kameraSil)

        dosya.addAction(yardim)
        dosya.addAction(yenile)
        dosya.addAction(yazdir)

        araclar.addAction(kamera_ac)
        araclar.addAction(kamera_ekle)
        araclar.addAction(kamera_sil)

        anaLayout = QVBoxLayout()
        anaLayout.addStretch()
        anaLayout.addWidget(self.baslik)
        anaLayout.addStretch()
        anaLayout.addLayout(self.grid)
        anaLayout.addStretch()
        anaLayout.addLayout(self.hbox)
        self.setLayout(anaLayout)

        self.kameralariGoster()

    def kameralariGoster(self):
        self.layoutuTemizle(self.grid)

        self.cursor.execute("SELECT * FROM cameras")
        self.veriler = self.cursor.fetchall()

        row = 0
        col = 0
        for index, veri in enumerate(self.veriler):
            vbox = QVBoxLayout()

            pixmap = QPixmap(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\pic.png")
            pixmap = pixmap.scaled(200, 200)
            label = QLabel()
            label.setPixmap(pixmap)
            labelLayout = QHBoxLayout()
            labelLayout.addStretch()
            labelLayout.addWidget(label)
            labelLayout.addStretch()

            self.cameraId = veri[1]
            etiket = QLabel(f"{self.cameraId}")
            etiket.setStyleSheet("font-size: 28pt; font-wight: bold;")
            etiketLayout = QHBoxLayout()
            etiketLayout.addStretch()
            etiketLayout.addWidget(etiket)
            etiketLayout.addStretch()

            vbox.addLayout(labelLayout)
            vbox.addStretch()
            vbox.addLayout(etiketLayout)

            row = index // 5
            col = index % 5

            self.grid.addLayout(vbox, row, col)

    def layoutuTemizle(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    sub_layout = item.layout()
                    if sub_layout is not None:
                        self.layoutuTemizle(sub_layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F5:
            self.kameralariGoster()

        if event.key() == Qt.Key_F4:
            self.kameraSil()

        if event.key() == Qt.Key_F3:
            self.kameraEkle()

        if event.key() == Qt.Key_F2:
            self.kameraAc()

        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniAc()

        if event.key() == Qt.Key_P and event.modifiers() == Qt.ControlModifier:
            self.tablolariYazdir()

    def kameraEkle(self):
        self.kamera_ekle = KameraEkle()
        self.kamera_ekle.show()
        self.kamera_ekle.kamera_eklendi.connect(self.kameralariGoster)

    def kameraSil(self):
        if not self.veriler:
            QMessageBox.information(self, "Uyarı", "Hiçbir Kamera Kaydı Yok!")
        else:
            self.kamera_sil = KameraSil()
            self.kamera_sil.show()
            self.kamera_sil.kamera_silindi.connect(self.kameralariGoster)

    def kameraAc(self):
        self.kayit = KameraSecim()
        self.kayit.show()

    def sensorleriGor(self):
        self.sensorler = SensorleriGor()

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = KameralarYardim()
        self.yardimPenceresi.show()

    def tablolariYazdir(self):
        try:
            self.yazdir = yazdir.tablolariYazdir()
            QMessageBox.information(self, 'Başarılı', f'Excel dosyası başarıyla oluşturuldu ve yazdırıldı.')
        except Exception as e:
            QMessageBox.critical(self, 'Hata', f'Bir hata oluştu: {e}')
