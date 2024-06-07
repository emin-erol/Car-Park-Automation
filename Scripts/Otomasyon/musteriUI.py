from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore
from yardimUI import AnasayfaYardim
import numpy as np
import sqlite3

class MusteriPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Otopark Otomasyonu")
        self.setGeometry(100, 100, 1400, 900)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\icon.ico"))

        self.baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")

        self.cursor = self.baglanti.cursor()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.initUI)
        self.timer.start(100)

        self.initUI()

    def initUI(self):
        layout = self.layout()
        if layout:
            for i in reversed(range(layout.count())):
                silinecekWidget = layout.itemAt(i).widget()
                if silinecekWidget is not None:
                    silinecekWidget.setParent(None)
        else:
            layout = QGridLayout()
            self.setLayout(layout)

        self.cursor.execute("SELECT * FROM sensors WHERE situation=?", (0,))
        sensorler = self.cursor.fetchall()
        satir_sayisi = len(sensorler)

        baslik = QLabel("BOŞ PARK ALANLARI")
        baslik.setStyleSheet("font-size: 32pt; font-weight: bold; padding: 50px;")
        baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(baslik, 0, 0, 1, 3)

        for i in range(satir_sayisi):
            tuval = np.zeros((150, 150, 3), np.uint8)

            if sensorler[i][-1] == 0:
                tuval[:, :, 1] = 255

                widget = QWidget()
                widget_layout = QVBoxLayout()
                widget.setLayout(widget_layout)

                qimage = QPixmap(150, 150)
                qimage.fill(QColor(tuval[0, 0, 0], tuval[0, 0, 1], tuval[0, 0, 2]))
                label = QLabel()
                label.setPixmap(qimage)
                label.setAlignment(Qt.AlignCenter)
                widget_layout.addWidget(label)

                camera_no = QLabel(f"{sensorler[i][1]}")
                camera_no.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                camera_no.setStyleSheet("font-size: 28pt; font-wight: bold;")

                sensor_no = QLabel(f"Park No: {sensorler[i][0]}")
                sensor_no.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                sensor_no.setStyleSheet("font-size: 24pt; font-wight: bold;")

                widget_layout.addWidget(camera_no)
                widget_layout.addWidget(sensor_no)
                widget_layout.addStretch()

                layout.addWidget(widget, i // 3 + 1, i % 3)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniGoster()

    def yardimPenceresiniGoster(self):
        self.yardim_penceresi = AnasayfaYardim()
        self.yardim_penceresi.show()
