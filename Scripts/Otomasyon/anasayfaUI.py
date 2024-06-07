from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore
from yardimUI import AnasayfaYardim
from musteriUI import MusteriPanel
import numpy as np
import sqlite3
import threading

class Anasayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Otopark Otomasyonu")
        self.setGeometry(100, 100, 1400, 900)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\icon.ico"))
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.anasayfayiGuncelle)
        self.timer.start(100)

    def initUI(self):
        self.baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        self.cursor = self.baglanti.cursor()

        menubar = QMenuBar(self)
        menubar.setNativeMenuBar(False)
        menubar.setFixedWidth(self.width())

        secenekler = menubar.addMenu('Seçenekler')

        yardim = QAction(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"), 'Yardım       F1', self)
        yardim.triggered.connect(self.yardimPenceresiniGoster)

        musteri_paneli = QAction(QIcon("../../Images/sensor.ico"), 'Müşteri Paneli  F3', self)
        musteri_paneli.triggered.connect(self.musteriPaneliniAc)

        secenekler.addAction(yardim)
        secenekler.addAction(musteri_paneli)

        self.anasayfayiGuncelle()

    def anasayfayiGuncelle(self):
        layout = self.layout()
        if layout:
            for i in reversed(range(layout.count())):
                silinecekWidget = layout.itemAt(i).widget()
                if silinecekWidget is not None:
                    silinecekWidget.setParent(None)
        else:
            layout = QGridLayout()
            self.setLayout(layout)

        self.cursor.execute("SELECT * FROM sensors")
        sensorler = self.cursor.fetchall()
        satir_sayisi = len(sensorler)

        baslik = QLabel("PARK ALANLARI")
        baslik.setStyleSheet("font-size: 18pt; font-weight: bold; padding: 10px;")
        baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(baslik, 0, 0, 1, 3)

        for i in range(satir_sayisi):
            tuval = np.zeros((150, 150, 3), np.uint8)

            if sensorler[i][-1] == 0:
                tuval[:, :, 1] = 255
            else:
                tuval[:, :, 0] = 255

            widget = QWidget()
            widget_layout = QVBoxLayout()
            widget.setLayout(widget_layout)

            qimage = QPixmap(150, 150)
            qimage.fill(QColor(tuval[0, 0, 0], tuval[0, 0, 1], tuval[0, 0, 2]))
            label = QLabel()
            label.setPixmap(qimage)
            label.setAlignment(Qt.AlignCenter)
            widget_layout.addWidget(label)

            id_etiketi = QLabel(f"Park No: {sensorler[i][0]}")
            id_etiketi.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
            widget_layout.addWidget(id_etiketi)

            layout.addWidget(widget, i // 3 + 1, i % 3)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniGoster()

    def yardimPenceresiniGoster(self):
        self.yardim_penceresi = AnasayfaYardim()
        self.yardim_penceresi.show()

    def musteriPaneliniAc(self):
        self.panel = MusteriPanel()
        self.panel.show()
